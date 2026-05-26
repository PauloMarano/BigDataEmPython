import pandas as pd

dfArr = pd.read_csv(R'Tabelas/FevereiroEMarço - Use Cases - T.csv', encoding='latin-1', sep=',');
dfArr['Arr'] = pd.to_numeric(dfArr['Arr'], errors='coerce');
dfArr['Arr'] = dfArr['Arr'].fillna(0);
soma_total = dfArr['Arr'].sum();

dfArr['Valor_Total_Geral'] = "";
dfArr.at[0, 'ValorTotal'] = soma_total;


coluna_Final = dfArr[['Arr', 'ValorTotal']];

coluna_Final.to_csv(R'Tabela1.csv', index=False, sep=';', decimal=',');

print(coluna_Final);