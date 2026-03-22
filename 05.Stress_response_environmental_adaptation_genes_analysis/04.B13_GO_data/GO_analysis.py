import pandas as pd
import requests
import time
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- 1. CẤU HÌNH GỐC ---
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

def main(input_file):
    go_metadata = {}
    stress_all = set()
    env_all = set()

    print("Đang đồng bộ hóa dữ liệu từ QuickGO API...")
    for label, go_id in roots.items():
        name, descendants = get_go_details(go_id)
        display_name = f"{name} ({go_id})" 
        go_metadata[display_name] = descendants
        
        # Phân loại dựa trên root để check nhóm "Both"
        if go_id in ['GO:0006950', 'GO:0042742', 'GO:0009408', 'GO:0046677', 'GO:0009267', 
                     'GO:0006281', 'GO:0006970', 'GO:0006457', 'GO:0033013', 'GO:0019217']:
            stress_all.update(descendants)
        else:
            env_all.update(descendants)
        time.sleep(0.4)

    # Đọc file eggNOG
    header_idx = 0
    with open(input_file, 'r') as f:
        for i, line in enumerate(f):
            if line.startswith('#query'):
                header_idx = i
                break
    
    df = pd.read_csv(input_file, sep='\t', skiprows=header_idx)
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

    # --- 3. VẼ ĐỒ THỊ ---
    df_plot = pd.DataFrame(plot_data)
    if df_plot.empty:
        print("Không tìm thấy gene nào khớp với các mã GO mục tiêu.")
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
    plt.savefig('detailed_go_analysis.png', dpi=300)
    print("Hoàn thành! Các nhãn trục Y đã được viết hoa chữ cái đầu.")
    
    # --- 4. TẠO BẢNG CHI TIẾT THEO ĐỊNH DẠNG CHUẨN (BAO GỒM NHÓM BOTH) ---
    print("Đang tạo bảng báo cáo chi tiết...")
    import re

    # Tìm tên cột chính xác cho Preferred_Name
    preferred_col = next((c for c in df.columns if 'Preferred_Name' in c or 'Preferred name' in c), None)
    
    go_to_proteins = {}
    gene_classification_map = {}
    gene_to_display = {} # Lưu mapping: GeneID -> "GeneID (PreferredName)"

    for _, row in df.iterrows():
        gene_id = row['query']
        if pd.isna(row['GOs']) or row['GOs'] == '-': continue
        current_gos = set(row['GOs'].split(','))
        
        # Lấy tên protein hiển thị
        p_name = "Uncharacterized"
        if preferred_col and pd.notna(row[preferred_col]) and row[preferred_col] != '-':
            p_name = row[preferred_col]
        display_str = f"{gene_id} ({p_name})"
        gene_to_display[gene_id] = display_str

        # Xác định phân loại gene (Giống logic barplot)
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
    
    # 1. Tìm các gene thuộc cả 2 nhóm (Both) trước
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

    # 2. Thêm các dòng GO chi tiết
    for display_name, gene_ids in go_to_proteins.items():
        unique_gene_ids = sorted(list(set(gene_ids)))
        protein_entries = [gene_to_display[gid] for gid in unique_gene_ids]
        
        go_match = re.search(r'GO:\d+', display_name)
        go_id = go_match.group(0) if go_match else ""
        
        # Xác định nhóm cho dòng dựa trên mã GO
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

    # --- TẠO DATAFRAME VÀ SẮP XẾP ---
    report_df = pd.DataFrame(report_list)
    if not report_df.empty:
        # Sắp xếp ưu tiên: Both (0) -> Stress (1) -> Env (2)
        priority_map = {'Both': 0, 'Stress response': 1, 'Environmental adaptation': 2}
        report_df['Sort_Priority'] = report_df['Functional group'].map(priority_map)
        report_df = report_df.sort_values(['Sort_Priority', 'Gene count'], ascending=[True, False]).drop(columns=['Sort_Priority'])
        
        # Xuất file
        report_df.to_excel('B13_Functional_Table_Final.xlsx', index=False)
        report_df.to_csv('B13_Functional_Table_Final.csv', index=False, encoding='utf-8-sig')
        print("---")
        print(f"Thành công! Đã tìm thấy {len(both_gene_ids)} gene thuộc cả 2 nhóm.")
        print("File xuất: B13_Functional_Table_Final.xlsx")
    else:
        print("Không tìm thấy dữ liệu phù hợp để xuất bảng.")
    
if __name__ == "__main__":
    main('B13_eggnog.emapper.annotations')