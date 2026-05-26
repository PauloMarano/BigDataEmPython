import pandas as pd

dfArr = pd.read_csv(R'Tabelas/FevereiroEMarço - Use Cases - T.csv', encoding='latin-1', sep=',');
dfArr['Arr'] = pd.to_numeric(dfArr['Arr'], errors='coerce');
dfArr['Arr'] = dfArr['Arr'].fillna(0);
somaTotal = dfArr['Arr'].sum();

dfArr['Valor_Total_Geral'] = "";
dfArr.at[0, 'ValorTotal'] = somaTotal;


colunaFinal = dfArr[['Arr', 'ValorTotal']];

colunaFinal.to_csv(R'TabelaCalculoFaturamento.csv', index=False, sep=';', decimal=',');
