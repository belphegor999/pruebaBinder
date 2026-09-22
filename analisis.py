import pandas as pd

df = pd.read_csv("temperaturas.csv")

print("Resumen estadístico:")
print(df.describe())

print("\nTemperatura media:", df["temperatura"].mean())
