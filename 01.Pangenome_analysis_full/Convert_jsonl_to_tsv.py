import pandas as pd

jsonl_path = "/home/datnguyen/Downloads/B13_KimCo_24012026/New_pangenome/Bs_meta.jsonl"

df = pd.read_json(jsonl_path, lines=True)
df = pd.json_normalize(df.to_dict(orient="records"))

df.to_csv("metadata.tsv", sep="\t")