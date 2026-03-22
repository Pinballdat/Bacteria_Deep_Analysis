# Phân tích CRISPR–Cas system trên hệ gene vi khuẩn

## Mục tiêu

### Phân tích CRISPR–Cas nhằm trả lời các câu hỏi sinh học sau:

- Vi khuẩn có hay không hệ thống CRISPR–Cas?

- Nếu có thì thuộc Class / Type / Subtype nào? Cấu trúc locus CRISPR ra sao (repeat–spacer–repeat)? Có đầy đủ gene cas cốt lõi không (cas1, cas2, cas3, cas9, cas10…)?

- Spacer có nguồn gốc từ đâu? (Phage, Plasmid, Mobile genetic elements)

- Vai trò tiềm năng: Miễn dịch chống phage; ổn định hệ gen, ảnh hưởng đến tiếp nhận gen ngoại lai (HGT)

### Dữ liệu đầu vào

|Loại dữ liệu|Định dạng|
|------------|---------|
|Hệ gene|FASTA/FNA|
|Chú giải|GFF/GenBank|
|Protein sequences|FASTA/FAA|

Nếu chưa annotate thì chạy Prokka/Funannotate trước để xác định CAS genes.

### Lý thuyết

1. CRISPR–Cas system là gì?

- Clustered Regularly Interspaced Short Palindromic Repeats – CRISPR-associated proteins
- Là hệ miễn dịch thích nghi (adaptive immunity) của vi khuẩn/vi khuẩn cổ
- Cho phép tế bào ghi nhớ các tác nhân xâm nhập (phage, plasmid); nhận diện chính xác trình tự ngoại lai; cắt và loại bỏ DNA/RNA của tác nhân xâm nhập trong lần nhiễm sau
- Là hệ miễn dịch di truyền duy nhất được biết đến ngoài động vật bậc cao

2. Cấu trúc cơ bản của hệ thống CRISPR–Cas

a/ CRISPR array

- CRISPR array là vùng DNA gồm: ```Leader – Repeat – Spacer – Repeat – Spacer – … – Repeat```

|Thành phần|Đặc điểm|
|----------|--------|
|Leader|Vùng giàu AT, chứa promoter, định hướng phiên mã|
|Repeat|Trình tự lặp lại, ngắn (24–48 bp), bán đối xứng|
|Spacer|Trình tự ngoại lai (20–40 bp), nguồn từ phage/plasmid, là ký ức miễn dịch của vi khuẩn|

b/ Cas genes

- Cas genes mã hóa protein Cas – máy móc phân tử của hệ CRISPR.

|Gene|Chức năng|
|----|---------|
|cas1|Thu nhận spacer (bắt buộc)|
|cas2|Hỗ trợ cas1|
|cas3|Helicase + nuclease (Type I)|
|cas9|Endonuclease (Type II)|
|cas10|DNase/RNase (Type III)|
|cas12/13|Nhận diện DNA/RNA|

- cas1 + cas2 là dấu hiệu xác định hệ CRISPR hoạt động

3. Ba giai đoạn hoạt động của CRISPR–Cas

a/ Thu nhận spacer

- Khi phage xâm nhập, một đoạn DNA ngoại lai được Cas1-2 cắt và gắn vào đầu leader-proximal của CRISPR array
- Spacer mới luôn nằm gần leader nhất
- Thứ tự spacer phản ánh lịch sử nhiễm phage

b/ Biểu hiện

- CRISPR array được phiên mã thành pre-crRNA
- pre-crRNA được cắt thành crRNA riêng lẻ
- crRNA mang trình tự spacer làm dẫn đường

c/ Can thiệp

- crRNA + Cas protein tạo phức hợp
- Nhận diện trình tự ngoại lai bổ sung
- Cắt DNA/RNA của phage/plasmid
- Nhận diện cần PAM (Protospacer Adjacent Motif) để tránh tự cắt DNA của chính mình

4. Phân loại CRISPR–Cas system

a/ Tổng quát

|Cấp|Phân loại|
|---|---------|
|Class 1|Phức hợp đa protein|
|Class 2|1 protein hiệu ứng chính|

b/ Các Type chính

|Class|Type|Protein hiệu ứng|
|-----|----|----------------|
|Class 1|I|Cas3|
|Class 1|III|Cas10|
|Class 2|II|Cas9|
|Class 2|V|Cas12|
|Class 2|VI|Cas13|

- Type II (Cas9) là nền tảng cho công nghệ chỉnh sửa gene.

### Quy trình phân tích 

#### Bước 1 – Phát hiện CRISPR array (Repeat–Spacer)

1. Công cụ: CRISPRCasFinder

2. Kết quả:

- Vị trí CRISPR array (start–end)
- Repeat consensus
- Danh sách spacer
- CRISPR evidence level (1–4)

Chỉ giữ array evidence ≥ 3 cho phân tích nghiêm túc.

3. Kết quả thực tế mẫu B13

a/ Bảng tóm tắt CRISPR arrays
_
|Trường|Ý nghĩa|Array 1|Array 2|
|------|-------|-------|-------|
|CRISPR ID|Mã định danh array|NODE_1_length_1303931_cov_187_300689_1|NODE_5_length_298854_cov_229_536410_1|
|Start – End|Vị trí trên genome|941687-941766|290127-290232|
|Length|Độ dài array|79 bp|105 bp|
|Direction|Hướng trên bộ gene|-|ND|
|Potential Orientation (AT%)|Hướng sinh học|+|+|
|Nb repeats|Số repeat|1|1|
|DR Consensus|Trình tự repeat đại diện|TATCAAGTTTTTATGTTGCTTGCCAAC|AGAAAACAAAACCAACAATCAGCTG|
|DR Length|Độ dài repeat|27 bp|25 bp|
|Conservation DR|Độ bảo tồn giữa các DR|96,3%|96%|
|Nb spacers|Số spacer|1|1|
|Spacer sequence|Trình tự DNA ngoại lai|GTCCGGCTCTCGTAGTCCGGAAAATG|CTGGTCAAGGTCAATTTGGCACTGAATTTGCTAGCGAAACAAACGCTCAGCAAGTC|
|Spacer Length|Độ dài spacer|26 bp|56 bp|
|Conservation Spacer|Độ bảo tồn của Spacer|100%|100%|
|Evidence level|Độ tin cậy (1–4)|1|1|


#### Bước 2 – Phát hiện và phân loại Cas genes

|Class|Gene đặc trưng|
|-----|--------------|
|Class 1|cas3, cas5, cas6, cas7|
|Class 2|cas9, cas12, cas13|
|Adaptation|cas1, cas2 (bắt buộc)|

Công cụ: CRISPRCasFinder, MacSyFinder + CasFinder

#### Bước 3 – Phân loại CRISPR–Cas System

|Cấp|Ví dụ|
|--|------|
|Class|Class 1 / Class 2|
|Type|I, II, III, IV, V, VI|
|Subtype|I-E, I-F, II-A, II-C, III-B|

- Điều kiện một hệ CRISPR hợp lệ: Có cas1 + cas2; Cas genes nằm gần CRISPR array (thường < 10 kb)

#### Bước 4 – Phân tích Spacer (Quan trọng)

- Xác định nguồn gốc spacer
- Dự đoán phage/plasmid đã từng xâm nhập
- Cách thực hiện: Trích spacer sequences (FASTA) BLASTn với PHASTER phage DB, RefSeq Virus, Plasmid DB
- Lọc: Identity ≥ 90%, Coverage ≥ 80%
- Kết quả:

|Spacer|Target|Loại|
|----|------|------|
|S12|Phage XYZ|Phage|
|S21|Plasmid ABC|Plasmid|

### Kết quả

- Hai array đượcc phát hiện bằng CRISPRCasFinder chỉ là CRISPR-like motifs mức thấp, không đủ tiêu chuẩn sinh học để coi là CRISPR array hay CRISPR–Cas system.
- Macsyfinder với database là CasFinder không phát hiện được hệ thống nào.