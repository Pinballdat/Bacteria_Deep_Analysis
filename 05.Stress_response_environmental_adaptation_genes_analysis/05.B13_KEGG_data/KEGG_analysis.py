import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. CẤU HÌNH (Giữ nguyên danh sách Pathway của bạn) ---
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

# --- 2. ĐỌC FILE EGGNOG ---
input_file = 'B13_eggnog.emapper.annotations'
header_idx = 0
with open(input_file, 'r') as f:
    for i, line in enumerate(f):
        if line.startswith('#query'):
            header_idx = i
            break

df = pd.read_csv(input_file, sep='\t', skiprows=header_idx)
df.columns = [c.replace('#', '').strip() for c in df.columns]

# --- 3. XỬ LÝ LOGIC LOẠI TRỪ (MUTUAL EXCLUSION) ---
plot_data = []
csv_results = []

for _, row in df.iterrows():
    gene = row['query']
    kegg_raw = str(row.get('KEGG_Pathway', '-'))
    if kegg_raw == '-' or pd.isna(kegg_raw): continue
    
    gene_maps = set([m.replace('ko', 'map') for m in kegg_raw.split(',')])
    
    has_stress = not gene_maps.isdisjoint(stress_set)
    has_env = not gene_maps.isdisjoint(env_set)
    
    # CASE 1: Gene thuộc cả 2 nhóm lớn -> Xếp vào "Both" và DỪNG LẠI
    if has_stress and has_env:
        main_label = "Both"
        sub_label = "Both (Cross-functional)"
        csv_results.append({'Gene_Name': gene, 'KEGG_Pathways': kegg_raw, 'Classification': main_label})
        plot_data.append({'Sub_Category': sub_label, 'Main_Group': main_label})
        
    # CASE 2 & 3: Chỉ thuộc 1 nhóm -> Liệt kê vào các Sub-Pathway cụ thể
    elif has_stress or has_env:
        main_label = "Stress Response" if has_stress else "Environmental Adaptation"
        csv_results.append({'Gene_Name': gene, 'KEGG_Pathways': kegg_raw, 'Classification': main_label})
        
        # Tìm các mã map cụ thể trong whitelist để vẽ đồ thị
        matched_maps = gene_maps.intersection(pathway_config.keys())
        for m in matched_maps:
            plot_data.append({'Sub_Category': pathway_config[m], 'Main_Group': main_label})

# --- 4. VẼ ĐỒ THỊ VÀ XUẤT FILE ---
pd.DataFrame(csv_results).to_csv('kegg_exclusive_classification.csv', index=False)

df_plot = pd.DataFrame(plot_data)
counts = df_plot.groupby(['Sub_Category', 'Main_Group']).size().reset_index(name='Count')

# Sắp xếp theo Priority: Both (tím) lên đầu, rồi tới Stress, Adaptation
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

# Thêm số lượng gene in đậm
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
plt.savefig('kegg_exclusive_distribution.png', dpi=300)
print("Hoàn thành! Kết quả đã được tách biệt hoàn toàn.")

# --- 5. TẠO BẢNG CHI TIẾT THEO CẤU TRÚC KEGG (MUTUAL EXCLUSION) ---
print("Đang tổng hợp bảng dữ liệu KEGG...")
import re

# 1. Tìm tên cột Preferred_Name an toàn
preferred_col = next((c for c in df.columns if 'Preferred_Name' in c or 'Preferred name' in c), None)

# Dictionary lưu trữ kết quả cuối cùng cho bảng
# Cấu trúc: { 'Pathway Name': { 'Functional group': '...', 'Proteins': [] } }
table_dict = {}

# Tập hợp các protein thuộc nhóm "Both" để tránh lặp lại ở các dòng dưới
both_protein_entries = []

for _, row in df.iterrows():
    gene_id = row['query']
    kegg_raw = str(row.get('KEGG_Pathway', '-'))
    if kegg_raw == '-' or pd.isna(kegg_raw): continue
    
    gene_maps = set([m.replace('ko', 'map') for m in kegg_raw.split(',')])
    
    # Lấy tên hiển thị protein
    p_name = "Uncharacterized"
    if preferred_col and pd.notna(row[preferred_col]) and row[preferred_col] != '-':
        p_name = row[preferred_col]
    display_str = f"{gene_id} ({p_name})"

    has_stress = not gene_maps.isdisjoint(stress_set)
    has_env = not gene_maps.isdisjoint(env_set)

    # LOGIC LOẠI TRỪ:
    if has_stress and has_env:
        # Nếu thuộc cả 2, chỉ cho vào nhóm Both
        both_protein_entries.append(display_str)
    else:
        # Nếu chỉ thuộc 1 nhóm, liệt kê vào các Pathway con tương ứng
        f_group = "Stress response" if has_stress else "Environmental adaptation"
        
        # Chỉ lấy những map nằm trong cấu hình whitelist của bạn
        matched_maps = gene_maps.intersection(pathway_config.keys())
        for m in matched_maps:
            pathway_name = f"{pathway_config[m]} ({m})"
            if pathway_name not in table_dict:
                table_dict[pathway_name] = {'group': f_group, 'proteins': []}
            table_dict[pathway_name]['proteins'].append(display_str)

# 2. Xây dựng danh sách dòng cho DataFrame
final_report_list = []

# Thêm dòng "Both" lên đầu nếu có
if both_protein_entries:
    unique_both = sorted(list(set(both_protein_entries)))
    final_report_list.append({
        'Annotation source': 'KEGG',
        'Category/term pathway': 'Both (Cross-functional)',
        'Functional group': 'Both',
        'Gene count': len(unique_both),
        'Representative genes/proteins in B13': '; '.join(unique_both)
    })

# Thêm các dòng Pathway con
for path_name, data in table_dict.items():
    unique_prots = sorted(list(set(data['proteins'])))
    final_report_list.append({
        'Annotation source': 'KEGG',
        'Category/term pathway': path_name,
        'Functional group': data['group'],
        'Gene count': len(unique_prots),
        'Representative genes/proteins in B13': '; '.join(unique_prots)
    })

# 3. Tạo DataFrame và Sắp xếp
report_df = pd.DataFrame(final_report_list)

# Thứ tự ưu tiên: Both -> Stress -> Env
priority_map = {'Both': 0, 'Stress response': 1, 'Environmental adaptation': 2}
report_df['Priority'] = report_df['Functional group'].map(priority_map)
report_df = report_df.sort_values(['Priority', 'Gene count'], ascending=[True, False]).drop(columns=['Priority'])

# 4. Xuất file
report_df.to_excel('B13_KEGG_Functional_Table.xlsx', index=False)
report_df.to_csv('B13_KEGG_Functional_Table.csv', index=False, encoding='utf-8-sig')

print("---")
print(f"Xử lý thành công! Đã tách biệt {len(set(both_protein_entries))} gene vào nhóm Both.")
print("File kết quả: B13_KEGG_Functional_Table.xlsx")