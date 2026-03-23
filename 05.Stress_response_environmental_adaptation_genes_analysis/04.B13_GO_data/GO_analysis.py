import pandas as pd
import requests
import time
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import argparse
import os
import re

# GO groups for analysis
roots = {
    'General Stress': 'GO:0006950', 'Oxidative Stress': 'GO:0042742',
    'Heat Cold Stress': 'GO:0009408', 'Antibiotic Response': 'GO:0046677',
    'Starvation Response': 'GO:0009267', 'DNA Repair Stress': 'GO:0006281',
    'Osmotic pH Stress': 'GO:0006970', 'Protein Protection': 'GO:0006457',
    'Toxin Antitoxin': 'GO:0033013', 'Stringent Response': 'GO:0019217',
    'Chemotaxis Locomotion': 'GO:0006935', 'Biofilm Formation': 'GO:0042710',
    'Two Component System': 'GO:0000160', 'Quorum Sensing': 'GO:0009372',
    'Metal Ion Adaptation': 'GO:0046688', 'Efflux Pumps': 'GO:0006855',
    'Horizontal Gene Transfer': 'GO:0009296', 'Oxygen Adaptation': 'GO:0071453',
    'Secretion Systems': 'GO:0030254'
}

def get_go_details(go_id):
    base_url = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms"
    headers = {"Accept": "application/json"}
    try:
        res_desc = requests.get(f"{base_url}/{go_id}/descendants?relations=is_a", headers=headers, timeout=10)
        desc_data = res_desc.json()['results'][0].get('descendants', [])
        descendants = {d if isinstance(d, str) else d.get('id') for d in desc_data}
        descendants.add(go_id)

        res_info = requests.get(f"{base_url}/{go_id}", headers=headers, timeout=10)
        name = res_info.json()['results'][0]['name']
        return name, descendants
    except:
        return go_id, {go_id}

def main(input, output):
    go_metadata = {}
    stress_all = set()
    env_all = set()

    print("Take processed data from QuickGO API")
    for label, go_id in roots.items():
        name, descendants = get_go_details(go_id)
        display_name = f"{name} ({go_id})" 
        go_metadata[display_name] = descendants
        
        if go_id in ['GO:0006950', 'GO:0042742', 'GO:0009408', 'GO:0046677', 'GO:0009267', 
                     'GO:0006281', 'GO:0006970', 'GO:0006457', 'GO:0033013', 'GO:0019217']:
            stress_all.update(descendants)
        else:
            env_all.update(descendants)
        time.sleep(0.4)

    # Read Eggnog results
    header_idx = 0
    with open(input, 'r') as f:
        for i, line in enumerate(f):
            if line.startswith('#query'):
                header_idx = i
                break
    
    df = pd.read_csv(input, sep='\t', skiprows=header_idx)
    df.columns = [c.replace('#', '').strip() for c in df.columns]

    plot_data = []
    final_csv = []

    for _, row in df.iterrows():
        gene = row['query']
        if pd.isna(row['GOs']) or row['GOs'] == '-': continue
        current_gos = set(row['GOs'].split(','))
        
        is_stress = not current_gos.isdisjoint(stress_all)
        is_env = not current_gos.isdisjoint(env_all)
        
        if is_stress and is_env:
            main_grp = "Both"
            plot_data.append({'Sub_Category': 'Both (Cross-functional)', 'Main_Group': 'Both'})
            final_csv.append({'Gene_Name': gene, 'GO_Terms': row['GOs'], 'Classification': 'Both'})
        elif is_stress:
            main_grp = "Stress Response"
            final_csv.append({'Gene_Name': gene, 'GO_Terms': row['GOs'], 'Classification': main_grp})
            for display_name, whitelist in go_metadata.items():
                if not current_gos.isdisjoint(whitelist) and "GO:00" in display_name: # Lọc đúng nhóm con
                    plot_data.append({'Sub_Category': display_name, 'Main_Group': main_grp})
        elif is_env:
            main_grp = "Environmental Adaptation"
            final_csv.append({'Gene_Name': gene, 'GO_Terms': row['GOs'], 'Classification': main_grp})
            for display_name, whitelist in go_metadata.items():
                if not current_gos.isdisjoint(whitelist) and "GO:00" in display_name:
                    plot_data.append({'Sub_Category': display_name, 'Main_Group': main_grp})

    # Draw bar chart
    df_plot = pd.DataFrame(plot_data)
    if df_plot.empty:
        print("Can not find target genes")
        return

    counts = df_plot.groupby(['Sub_Category', 'Main_Group']).size().reset_index(name='Count')
    
    # --- SỬA TẠI ĐÂY: VIẾT HOA CHỮ CÁI ĐẦU ---
    # Cách 1: Chỉ viết hoa chữ đầu tiên của chuỗi (nhanh nhất)
    counts['Sub_Category'] = counts['Sub_Category'].apply(lambda x: x[0].upper() + x[1:] if len(x) > 0 else x)
    
    # Sắp xếp theo Priority: Both -> Stress -> Adaptation
    priority = {'Both': 2, 'Stress Response': 0, 'Environmental Adaptation': 1}
    counts['Priority'] = counts['Main_Group'].map(priority)
    counts = counts.sort_values(by=['Priority', 'Count'], ascending=[True, False])

    plt.figure(figsize=(14, 12))
    sns.set_theme(style="white")
    
    palette = {'Stress Response': '#e74c3c', 'Environmental Adaptation': '#3498db', 'Both': '#9b59b6'}
    
    # Sử dụng order=counts['Sub_Category'] để đảm bảo thứ tự đã sắp xếp
    ax = sns.barplot(data=counts, y='Sub_Category', x='Count', hue='Main_Group', 
                    palette=palette, dodge=False, edgecolor='black', order=counts['Sub_Category'])

    # Thêm số lượng gene
    for p in ax.patches:
        val = p.get_width()
        if not np.isnan(val) and val > 0:
            ax.annotate(f'{int(val)}', 
                        (val + 0.3, p.get_y() + p.get_height()/2),
                        va='center', fontsize=11, fontweight='bold')

    # Thiết kế khung viền (Border) bao quanh
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_edgecolor('black')
        spine.set_linewidth(1.5)

    plt.title('Gene Distribution by Gene Ontology', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Number of Genes', fontsize=13, fontweight='bold')
    plt.ylabel('')
    plt.legend(title='Main Group', frameon=True, loc='lower right', edgecolor='black')
    
    plt.tight_layout()
    plt.savefig('GO_barchart.png', dpi=300)
    
    # Save CSV + XLSX format
    preferred_col = next((c for c in df.columns if 'Preferred_Name' in c or 'Preferred name' in c), None)
    
    go_to_proteins = {}
    gene_classification_map = {}
    gene_to_display = {}

    for _, row in df.iterrows():
        gene_id = row['query']
        if pd.isna(row['GOs']) or row['GOs'] == '-': continue
        current_gos = set(row['GOs'].split(','))
        
        # if preferred_col and pd.notna(row[preferred_col]) and row[preferred_col] != '-':
        #     p_name = row[preferred_col]
        display_str = f"{gene_id}"
        gene_to_display[gene_id] = display_str

        is_stress = not current_gos.isdisjoint(stress_all)
        is_env = not current_gos.isdisjoint(env_all)
        
        if is_stress and is_env:
            grp = "Both"
        elif is_stress:
            grp = "Stress response"
        elif is_env:
            grp = "Environmental adaptation"
        else:
            continue
            
        gene_classification_map[gene_id] = grp

        # Phân bổ vào từng Category GO
        for display_name, whitelist in go_metadata.items():
            if not current_gos.isdisjoint(whitelist):
                if display_name not in go_to_proteins:
                    go_to_proteins[display_name] = []
                go_to_proteins[display_name].append(gene_id)

    report_list = []
    
    report_list = []
    
    # Find genes in Both group
    both_gene_ids = [gid for gid, grp in gene_classification_map.items() if grp == "Both"]
    
    if both_gene_ids:
        both_entries = sorted([gene_to_display[gid] for gid in both_gene_ids])
        report_list.append({
            'Annotation source': 'GO',
            'Category/term pathway': 'Both (Cross-functional)',
            'Functional group': 'Both',
            'Gene count': len(both_gene_ids),
            'Representative genes/proteins in B13': '; '.join(both_entries)
        })

    # Add GO classification
    for display_name, gene_ids in go_to_proteins.items():
        unique_gene_ids = sorted(list(set(gene_ids)))
        protein_entries = [gene_to_display[gid] for gid in unique_gene_ids]
        
        go_match = re.search(r'GO:\d+', display_name)
        go_id = go_match.group(0) if go_match else ""
        
        if go_id in stress_all:
            f_group = "Stress response"
        else:
            f_group = "Environmental adaptation"

        report_list.append({
            'Annotation source': 'GO',
            'Category/term pathway': display_name,
            'Functional group': f_group,
            'Gene count': len(unique_gene_ids),
            'Representative genes/proteins in B13': '; '.join(protein_entries)
        })

    # Create dataframe and reorder
    report_df = pd.DataFrame(report_list)
    if not report_df.empty:
        # Priority: Both (0) -> Stress (1) -> Env (2)
        priority_map = {'Both': 0, 'Stress response': 1, 'Environmental adaptation': 2}
        report_df['Sort_Priority'] = report_df['Functional group'].map(priority_map)
        report_df = report_df.sort_values(['Sort_Priority', 'Gene count'], ascending=[True, False]).drop(columns=['Sort_Priority'])
        
        # Save file
        report_df.to_excel('Functional_Table_Final.xlsx', index=False)
        report_df.to_csv('Functional_Table_Final.csv', index=False, encoding='utf-8-sig')
        # print("---")
        # print(f"Thành công! Đã tìm thấy {len(both_gene_ids)} gene thuộc cả 2 nhóm.")
        print("Done!")
    else:
        print("Can not find data for creating table")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GO analysis")
    parser.add_argument("-i", "--input", required=True, help="Input path")
    parser.add_argument("-n", "--name", reaqiured=True, help="Output path")

    args = parser.parse_args()
    main(args.input, args.name)