import pandas as pd

df = pd.read_csv(R'Portfólio - 3 month.csv', encoding='latin-1', sep=',')

df['Overusage'] = df['Overusage'].astype(str).str.strip()


tabela6 = df['Overusage'].value_counts().reset_index()
tabela6.columns = ['Overusage', 'Quantidade']

tabela6.to_csv(R'TabelaQuantidadeOverusage.csv', index=False, sep=';', encoding='latin-1')