import pandas as pd

df = pd.read_json("organizations.json")
df.to_csv("organizations.csv", index=False)