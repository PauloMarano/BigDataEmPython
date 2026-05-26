import pandas as pd

dfMedia = pd.read_csv(R'Portfólio - 3 month.csv', encoding='latin-1');
dfMedia['Satisfacao Media'] = pd.to_numeric(dfMedia['Satisfacao_CSAT'], errors='coerce');
dfMedia = dfMedia.dropna(subset=['Satisfacao Media']);

dfMedia['Data'] = pd.to_datetime(dfMedia['Data']);
dfMedia['Mes'] = dfMedia['Data'].dt.month_name();
dfMedia['Mes'] = dfMedia['Mes'].replace({'February': 'Fevereiro', 'March': 'Março', 'April': 'Abril'});

tabelaFinal = dfMedia.groupby('Mes')['Satisfacao Media'].mean().round(2).reset_index();

tabelaFinal.to_csv(R'TabelaMediaSatisfacao.csv', index=False, sep=';', decimal=',');