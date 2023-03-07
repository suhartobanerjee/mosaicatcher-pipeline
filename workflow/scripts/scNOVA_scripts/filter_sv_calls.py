import pandas as pd

df = pd.read_csv(snakemake.input[0], sep="\t")
df.loc[df["chrom"] != "chrY"].to_csv(snakemake.output[0], sep="\t", index=False)