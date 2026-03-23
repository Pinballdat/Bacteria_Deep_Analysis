import pandas as pd
import re
import argparse

def parse_gff(gff_file):
    """
    Hàm phân tích file GFF để lấy thông tin vị trí của các locus_tag.
    """
    gff_data = {}
    with open(gff_file, 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            
            parts = line.split('\t')
            if len(parts) < 9:
                continue
            
            chrom = parts[0]
            start = parts[3]
            end = parts[4]
            attributes = parts[8]
            
            # Tìm ID hoặc locus_tag trong phần attributes
            locus_tag_match = re.search(r'ID=([^;]+)', attributes)
            if not locus_tag_match:
                locus_tag_match = re.search(r'locus_tag=([^;]+)', attributes)
                
            if locus_tag_match:
                locus_tag = locus_tag_match.group(1).strip()
                # Lưu vị trí theo định dạng Chrom: Start-End
                gff_data[locus_tag] = f"{chrom}: {start}-{end}"
                
    return gff_data

def process_files(vf_file, gff_file, output_file):
    # 1. Đọc file VF kết quả (xử lý như CSV theo yêu cầu)
    # Lưu ý: File đính kèm của bạn dùng dấu phẩy (,) làm phân cách
    df = pd.read_csv(vf_file)
    
    # 2. Parse thông tin từ file GFF
    print(f"Đang đọc file GFF: {gff_file}...")
    gff_map = parse_gff(gff_file)
    
    # 3. Ánh xạ thông tin vào cột Position
    # Key là cột 'B13 (Prediction)' chứa locus_tag
    print("Đang ánh xạ vị trí...")
    
    def get_position(locus_tag):
        if pd.isna(locus_tag) or locus_tag == '-':
            return '-'
        return gff_map.get(locus_tag, '-')

    df['Position'] = df['B13 (Prediction)'].apply(get_position)
    
    # 4. Xuất kết quả ra file CSV mới
    df.to_csv(output_file, index=False)
    print(f"Hoàn thành! Kết quả đã được lưu tại: {output_file}")

if __name__ == "__main__":
    # Bạn có thể thay đổi tên file trực tiếp ở đây hoặc dùng tham số dòng lệnh
    parser = argparse.ArgumentParser(description='Nối vị trí từ file GFF vào file kết quả VF.')
    parser.add_argument('--vf', default='VF_results.tsv', help='Đường dẫn file VF đầu vào (CSV format)')
    parser.add_argument('--gff', required=True, help='Đường dẫn file GFF từ Prokka')
    parser.add_argument('--out', default='VF_results_extended.csv', help='Tên file đầu ra')

    args = parser.parse_args()
    
    try:
        process_files(args.vf, args.gff, args.out)
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")