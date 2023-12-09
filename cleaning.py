import pandas as pd

df = pd.read_csv('amazon_200k_asin_a_vscode.csv')
# df = df[~df['Brand'].astype(str).str.contains(r'\$', regex=True)]
df = df[df['Title'] != 'Title']
df.to_csv('amazon_200k_asin_a_vscode.csv')