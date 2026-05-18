import pandas as pd

dfSeg = pd.read_csv(R'FevereiroEMarço - Use Cases - T.csv', encoding='latin-1', sep=',');
dfSeg = dfSeg.dropna(subset=['pipe_taxonomy_l3']);
dfSeg['Segmento'] = dfSeg['pipe_taxonomy_l3'].astype(str).str.strip();

ranking = dfSeg['Segmento'].value_counts().head(3).reset_index();
ranking.columns = ['Segmento', 'Quantidade'];

ranking.to_csv(R'Tabela3.csv', index=False, sep=';', encoding='latin-1');

print(ranking);