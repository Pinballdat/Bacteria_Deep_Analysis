import pandas as pd
import argparse
import os

def Convert_jsonl_to_tsv(input, output):
    if not os.path.exists(input):
        print(f"Error: File {input} is not found!!")
        return
    
    print(f"File {input} is found. Processing!!!")

    # Read and normalize jsonl file
    df = pd.read_json(jsonl_path, lines=True)
    df = pd.json_normalize(df.to_dict(orient="records"))

    # Save tsv file
    df.to_csv(output, sep="\t", index=False)

if __name__ == "__main__":
    # Setting params for cmd
    parser = argparse.ArgumentParser(description="Convert JSONL to TSV")
    
    parser.add_argument("-i", "--input", required=True, help="Input path")
    parser.add_argument("-o", "--output", required=True, help="Output path")
    
    args = parser.parse_args()
    
    Convert_jsonl_to_tsv(args.input, args.output)