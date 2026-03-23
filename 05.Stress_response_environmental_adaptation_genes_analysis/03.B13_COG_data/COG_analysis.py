import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import os

# COG groups for analysis
target_cogs = {
    'O': 'Post-translational modification, protein turnover, chaperones',
    'P': 'Inorganic ion transport and metabolism',
    'T': 'Signal transduction mechanisms',
    'V': 'Defense mechanisms'
}

def main(input, output):
    # Check input file
    if not os.path.exists(input):
        print(f"File {input} is not found!!!")
        return
    
    # Read Eggnog results
    header_idx = 0
    try:
        with open(input_file, 'r') as f:
            for i, line in enumerate(f):
                if line.startswith('#query'):
                    header_idx = i
                    break
        df = pd.read_csv(input_file, sep='\t', skiprows=header_idx)
        df.columns = [c.replace('#', '').strip() for c in df.columns]
    except Exception as e:
        print(f"Error when reading files: {e}")
        return

    # Classification analysis
    processed_data = []
    for _, row in df.iterrows():
        cog_raw = str(row.get('COG_category', '-')).strip()
        if cog_raw == '-' or pd.isna(cog_raw) or cog_raw == '':
            continue
            
        found_targets = [char for char in cog_raw if char in target_cogs]
        
        if len(found_targets) > 1:
            processed_data.append("Multiple COG")
        elif len(found_targets) == 1:
            code = found_targets[0]
            processed_data.append(f"[{code}] {target_cogs[code]}")

    if not processed_data:
        print("Can not find the suitable data")
        return

    df_counts = pd.DataFrame(processed_data, columns=['Category'])
    counts = df_counts['Category'].value_counts().reset_index()
    counts.columns = ['Category', 'Count']
    counts = counts.sort_values(by='Count', ascending=False)

    # Draw bar chart
    plt.figure(figsize=(12, 8))
    sns.set_theme(style="ticks")
    
    ax = sns.barplot(
        data=counts, 
        x='Count', 
        y='Category', 
        palette='rocket', 
        edgecolor='black',
        linewidth=1.5
    )

    # Set border for bar chart
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_edgecolor('black')
        spine.set_linewidth(2)

    # Add numbers of genes
    for p in ax.patches:
        width = p.get_width()
        ax.text(width + (counts['Count'].max() * 0.01), 
                p.get_y() + p.get_height()/2, 
                f'{int(width)}', 
                va='center', fontsize=12, fontweight='bold')

    # Set title, labels
    plt.title('Functional Distribution: O, P, T, V & Multiple COG', 
              fontsize=16, fontweight='bold', pad=25)
    plt.xlabel('Number of Genes', fontsize=12, fontweight='bold')
    plt.ylabel('')
    
    plt.tight_layout()
    # Save file PNG
    plt.savefig('COG_barchart.png', dpi=300)

    # Save file CSV + XLSX
    print("Table is processing !!!")
    
    preferred_col = next((c for c in df.columns if 'Preferred_Name' in c or 'Preferred name' in c), None)
    
    cog_table_data = {f"[{code}] {desc}": [] for code, desc in target_cogs.items()}
    cog_table_data["Multiple COG"] = []

    for _, row in df.iterrows():
        cog_raw = str(row.get('COG_category', '-')).strip()
        if cog_raw == '-' or pd.isna(cog_raw) or cog_raw == '':
            continue
            
        p_name = row[preferred_col] if preferred_col and pd.notna(row[preferred_col]) and row[preferred_col] != '-' else "Uncharacterized"
        display_str = f"{row['query']} ({p_name})"
        
        found_targets = [char for char in cog_raw if char in target_cogs]
        
        if len(found_targets) > 1:
            cog_table_data["Multiple COG"].append(display_str)
        elif len(found_targets) == 1:
            code = found_targets[0]
            category_name = f"[{code}] {target_cogs[code]}"
            cog_table_data[category_name].append(display_str)

    final_report_list = []
    for category, proteins in cog_table_data.items():
        unique_prots = sorted(list(set(proteins)))
        
        final_report_list.append({
            'Annotation source': 'COG',
            'Category/term pathway': category,
            'Functional group': 'Functional mechanisms',
            'Gene count': len(unique_prots),
            'Representative genes/proteins in B13': '; '.join(unique_prots) if unique_prots else "None"
        })

    report_df = pd.DataFrame(final_report_list)
    
    # Reoreder COG groups
    report_df['Sort_Order'] = report_df['Category/term pathway'].apply(lambda x: 0 if x == "Multiple COG" else 1)
    report_df = report_df.sort_values(['Sort_Order', 'Gene count'], ascending=[True, False]).drop(columns=['Sort_Order'])

    report_df.to_csv('COG_Functional_Table.csv', index=False)
    report_df.to_excel('COG_Functional_Table.xlsx', index=False)
    # print("---")
    print(f"Done! Number of Multiple COG: {len(cog_table_data['Multiple COG'])}")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analysis and visualize COG classification")
    
    parser.add_argument("-i", "--input", required=True, help="Input path")
    parser.add_argument("-n", "--name", required=True, help="Output path")
    
    args = parser.parse_args()
    main(args.input, args.name)