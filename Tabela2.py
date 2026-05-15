import pandas as pd

dfMedia = pd.read_csv(R'Portfólio - 3 month(Portfólio - 3 month).csv', encoding='latin-1');
dfMedia['Satisfacao Media'] = pd.to_numeric(dfMedia['Satisfacao_CSAT'], errors='coerce');
dfMedia = dfMedia.dropna(subset=['Satisfacao Media']);

dfMedia['Data'] = pd.to_datetime(dfMedia['Data']);
dfMedia['Mes'] = dfMedia['Data'].dt.month_name();
dfMedia['Mes'] = dfMedia['Mes'].replace({'February': 'Fevereiro', 'March': 'Março', 'April': 'Abril'});

tabela_final = dfMedia.groupby('Mes')['Satisfacao Media'].mean().round(2).reset_index();

tabela_final.to_csv(R'Tabela2.csv', index=False, sep=',', decimal='.');

print(tabela_final);