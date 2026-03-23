import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import os
import re

# KEGG pathway
pathway_config = {
    'map02030': 'Bacterial chemotaxis', 'map02040': 'Flagellar assembly',
    'map02024': 'Quorum sensing', 'map02020': 'Two-component system',
    'map02025': 'ROS pathway - prokaryotes', 'map02026': 'Biofilm formation - E. coli',
    'map05111': 'Biofilm formation - Vibrio',
    'map02010': 'ABC transporters', 'map03060': 'Protein export',
    'map00480': 'Glutathione metabolism', 'map03410': 'Base excision repair',
    'map03420': 'Nucleotide excision repair', 'map03430': 'Mismatch repair',
    'map03440': 'Homologous recombination', 'map03018': 'RNA degradation',
    'map00440': 'Phosphonate/phosphinate metabolism', 'map00710': 'Carbon fixation in prokaryotes'
}

env_set = {'map02030', 'map02040', 'map02024', 'map02020', 'map02025', 'map02026', 'map05111'}
stress_set = set(pathway_config.keys()) - env_set

# Read Eggnog file
def main(input, output):
    # Kiểm tra file đầu vào
    if not os.path.exists(input):
        print(f"Lỗi: Không tìm thấy file {input}")
        return
    
    # Read Eggnog results
    header_idx = 0
    with open(input, 'r') as f:
        for i, line in enumerate(f):
            if line.startswith('#query'):
                header_idx = i
                break

    df = pd.read_csv(input, sep='\t', skiprows=header_idx)
    df.columns = [c.replace('#', '').strip() for c in df.columns]

    # Processing
    plot_data = []
    csv_results = []

    for _, row in df.iterrows():
        gene = row['query']
        kegg_raw = str(row.get('KEGG_Pathway', '-'))
        if kegg_raw == '-' or pd.isna(kegg_raw): continue
        
        gene_maps = set([m.replace('ko', 'map') for m in kegg_raw.split(',')])
        
        has_stress = not gene_maps.isdisjoint(stress_set)
        has_env = not gene_maps.isdisjoint(env_set)
        
        # CASE 1: BOTH
        if has_stress and has_env:
            main_label = "Both"
            sub_label = "Both (Cross-functional)"
            csv_results.append({'Gene_Name': gene, 'KEGG_Pathways': kegg_raw, 'Classification': main_label})
            plot_data.append({'Sub_Category': sub_label, 'Main_Group': main_label})
            
        # CASE 2 & 3: Only one pathway type
        elif has_stress or has_env:
            main_label = "Stress Response" if has_stress else "Environmental Adaptation"
            csv_results.append({'Gene_Name': gene, 'KEGG_Pathways': kegg_raw, 'Classification': main_label})
            
            matched_maps = gene_maps.intersection(pathway_config.keys())
            for m in matched_maps:
                plot_data.append({'Sub_Category': pathway_config[m], 'Main_Group': main_label})

    # Draw bar chart
    pd.DataFrame(csv_results).to_csv('kegg_exclusive_classification.csv', index=False)

    df_plot = pd.DataFrame(plot_data)
    counts = df_plot.groupby(['Sub_Category', 'Main_Group']).size().reset_index(name='Count')

    # Priority: Both (0), Stress (1), Adaptation (2)
    priority = {'Both': 2, 'Stress Response': 0, 'Environmental Adaptation': 1}
    counts['Priority'] = counts['Main_Group'].map(priority)
    counts = counts.sort_values(by=['Priority', 'Count'], ascending=[True, False])

    plt.figure(figsize=(14, 11))
    sns.set_theme(style="white")

    palette = {'Stress Response': '#e74c3c', 'Environmental Adaptation': '#3498db', 'Both': '#9b59b6'}

    ax = sns.barplot(
        data=counts, y='Sub_Category', x='Count', hue='Main_Group', 
        palette=palette, dodge=False, edgecolor='black', order=counts['Sub_Category']
    )

    # Add number of genes
    for p in ax.patches:
        val = p.get_width()
        if not np.isnan(val) and val > 0:
            ax.text(val + 0.5, p.get_y() + p.get_height()/2, f'{int(val)}', 
                    va='center', fontsize=11, fontweight='bold')

    plt.title('Gene Distribution by KEGG Pathway', fontsize=16, fontweight='bold', pad=25)
    plt.xlabel('Number of Genes', fontsize=13, fontweight='bold')
    plt.ylabel('')
    plt.legend(title='Main Groups', loc='lower right', frameon=True, edgecolor='black')

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_edgecolor('black')

    plt.tight_layout()
    plt.savefig('KEEGG_barchart.png', dpi=300)

    # Create table
    print("Đang tổng hợp bảng dữ liệu KEGG...")

    preferred_col = next((c for c in df.columns if 'Preferred_Name' in c or 'Preferred name' in c), None)

    table_dict = {}

    both_protein_entries = []

    for _, row in df.iterrows():
        gene_id = row['query']
        kegg_raw = str(row.get('KEGG_Pathway', '-'))
        if kegg_raw == '-' or pd.isna(kegg_raw): continue
        
        gene_maps = set([m.replace('ko', 'map') for m in kegg_raw.split(',')])
        
        # p_name = "Uncharacterized"
        # if preferred_col and pd.notna(row[preferred_col]) and row[preferred_col] != '-':
        #     p_name = row[preferred_col]
        display_str = f"{gene_id}"

        has_stress = not gene_maps.isdisjoint(stress_set)
        has_env = not gene_maps.isdisjoint(env_set)

        if has_stress and has_env:
            both_protein_entries.append(display_str)
        else:
            f_group = "Stress response" if has_stress else "Environmental adaptation"
            
            matched_maps = gene_maps.intersection(pathway_config.keys())
            for m in matched_maps:
                pathway_name = f"{pathway_config[m]} ({m})"
                if pathway_name not in table_dict:
                    table_dict[pathway_name] = {'group': f_group, 'proteins': []}
                table_dict[pathway_name]['proteins'].append(display_str)

    final_report_list = []

    if both_protein_entries:
        unique_both = sorted(list(set(both_protein_entries)))
        final_report_list.append({
            'Annotation source': 'KEGG',
            'Category/term pathway': 'Both (Cross-functional)',
            'Functional group': 'Both',
            'Gene count': len(unique_both),
            'Representative genes/proteins in B13': '; '.join(unique_both)
        })

    for path_name, data in table_dict.items():
        unique_prots = sorted(list(set(data['proteins'])))
        final_report_list.append({
            'Annotation source': 'KEGG',
            'Category/term pathway': path_name,
            'Functional group': data['group'],
            'Gene count': len(unique_prots),
            'Representative genes/proteins in B13': '; '.join(unique_prots)
        })

    # Create dataframe and reorder
    report_df = pd.DataFrame(final_report_list)

    priority_map = {'Both': 0, 'Stress response': 1, 'Environmental adaptation': 2}
    report_df['Priority'] = report_df['Functional group'].map(priority_map)
    report_df = report_df.sort_values(['Priority', 'Gene count'], ascending=[True, False]).drop(columns=['Priority'])

    # Save csv and xlsx file
    report_df.to_excel('KEGG_Functional_Table.xlsx', index=False)
    report_df.to_csv('KEGG_Functional_Table.csv', index=False, encoding='utf-8-sig')

    print("Done!!!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="KEGG analysis")
    parser.add_argument("-i", "--input", required=True, help="Input path")
    parser.add_argument("-o", "--output", required=True, help="Output path")

    args = parser.parse_args()
    main(args.input, args.output)