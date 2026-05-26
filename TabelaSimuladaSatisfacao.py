import pandas as pd

df = pd.read_csv(R'Portfólio - 3 month.csv', encoding='latin-1', sep=',')
df['Qtd_Reunioes_Estrategicas'] = pd.to_numeric(df['Qtd_Reunioes_Estrategicas'], errors='coerce')
df['Satisfacao_CSAT'] = pd.to_numeric(df['Satisfacao_CSAT'], errors='coerce')
df = df.dropna(subset=['Qtd_Reunioes_Estrategicas', 'Satisfacao_CSAT'])

mediaComReuniao = df[df['Qtd_Reunioes_Estrategicas'] >= 1]['Satisfacao_CSAT'].mean()
mediaSemReuniao = df[df['Qtd_Reunioes_Estrategicas'] == 0]['Satisfacao_CSAT'].mean()

bonusReuniao = mediaComReuniao - mediaSemReuniao

df['CSAT_Previsto'] = df.apply( lambda row: row['Satisfacao_CSAT'] + bonusReuniao if row['Qtd_Reunioes_Estrategicas'] == 0 else row['Satisfacao_CSAT'], axis=1 )

MediaAtual = df['Satisfacao_CSAT'].mean()
MediaSimulada = df['CSAT_Previsto'].mean()

tabela5 = pd.DataFrame([{
    'Métrica': 'Média Geral',
    'Cenário Atual': round(MediaAtual, 2),
    'Cenário Simulado': round(MediaSimulada, 2),
    'Ganho Estimado': round(MediaSimulada - MediaAtual, 2)
}]) 

tabela5.to_csv(R'TabelaSimuladaSatisfacao.csv', index=False, sep=';', encoding='latin-1')