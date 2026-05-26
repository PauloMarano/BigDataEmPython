import pandas as pd

dfIa = pd.read_csv(R'Portfólio - 3 month.csv', encoding='latin-1', sep=',');
dfIa = dfIa.dropna(subset=['Status_Uso_IA']);
dfIa['UsoIa'] = dfIa['Status_Uso_IA'].astype(str).str.strip();

tabelaIa = dfIa['UsoIa'].value_counts().reset_index();
tabelaIa.columns = ['StatusIA', 'Quantidade'];

totalGeral = tabelaIa['Quantidade'].sum();

colunaTotal = pd.DataFrame([['Total Geral', totalGeral]], columns=['StatusIA', 'Quantidade']);
tabelaFinal = pd.concat([tabelaIa, colunaTotal], ignore_index=True);

tabelaFinal.to_csv(R'TabelaUsoIa.csv', index=False, sep=';', encoding='latin-1');