import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def get_group_data(x, anos, sexos, estab, mode):
    df_group = df.copy()

    if mode == 'sum':
        if anos:
            df_group = df_group[df_group['DT_ATEND'].str[:4].isin(anos)]
        if sexos:
            df_group = df_group[df_group['SEXOPAC'].isin(sexos)]
        if estab:
            df_group = df_group[df_group['CNES_EXEC'].isin(estab)]
        return df_group.groupby(x).size().reset_index(name='count')
    
    if mode == 'compare':
        if anos:
            df_group = df_group[df_group['DT_ATEND'].isin(anos)]
        if sexos:
            df_group = df_group[df_group['SEXOPAC'].isin(sexos)]
        if estab:
            df_group = df_group[df_group['CNES_EXEC'].isin(estab)]

        match x:
            case 'CNES_EXEC':
                return df_group.groupby([x, 'DT_ATEND', 'SEXOPAC']).size().reset_index(name='count')
            
            case 'SEXOPAC':
                return df_group.groupby([x, 'DT_ATEND', 'CNES_EXEC']).size().reset_index(name='count')
            
            case _:
                return df_group.groupby([x, 'DT_ATEND', 'SEXOPAC', 'CNES_EXEC']).size().reset_index(name='count')

def fig_layout(fig, x):
    fig.update_layout(
        font=dict(
            family="Poppins, sans-serif",
            size=16,
            color="#526174"
        ),
        bargap=0 if x == 'IDADEPAC' else 0.1,
        width=1500,
        height=645
    )
    fig.update_traces(
        marker=dict(
            line=dict(
                width=0.5,
                color='#526174'
            )
        ),
        hoverlabel=dict(
            bgcolor='white',
            font_size=16,
            font_family="Poppins, sans-serif"
        )
    )
    return fig

def plot_bar_sum(x, anos, sexos, estab):
    data = get_group_data(x, anos, sexos, estab, mode='sum')
    fig = px.bar(data, x=x, y='count',
                 labels=labels, width=1500, height=645)
    fig = fig_layout(fig, x)
    return fig

def plot_bar_compare(x, anos, sexos, estab):
    data = get_group_data(x, anos, sexos, estab, mode='compare')

    match x:
        case 'CNES_EXEC':
            fig = px.bar(data, x=x, y='count', color='DT_ATEND', facet_row='SEXOPAC',
                         labels=labels)
        case 'SEXOPAC':
            fig = px.bar(data, x=x, y='count', color='DT_ATEND', facet_col='CNES_EXEC',
                         labels=labels)            
        case _:
            fig = px.bar(data, x=x, y='count', color='DT_ATEND', facet_row='SEXOPAC', facet_col='CNES_EXEC',
                         labels=labels)
    
    fig = fig_layout(fig, x)
    return fig

def plot_pie(x, anos, sexos, estab):
    data = get_group_data(x, anos, sexos, estab, mode='sum')
    fig = go.Figure(data=[go.Pie(labels=data[x], values=data['count'], insidetextorientation='radial')])
    fig = fig_layout(fig, x)
    return fig

cnes = pd.read_csv('data/cnes.csv', encoding='ISO-8859-1', dtype=str)
cnes.set_index('CNES', inplace=True)
cid = pd.read_csv('data/cid.csv', encoding='ISO-8859-1', dtype=str)
cid.set_index('CD_COD', inplace=True)
droga = pd.read_csv('data/droga.csv', encoding='ISO-8859-1', dtype=str)
droga.set_index('COD_DROGA', inplace=True)
local = pd.read_csv('data/local.csv', encoding='ISO-8859-1', dtype=str)
local.set_index('COD_LOC', inplace=True)
municipio = pd.read_csv('data/municipio.csv', encoding='ISO-8859-1', dtype=str)
municipio.set_index('CO_MUNICIP', inplace=True)
proc = pd.read_csv('data/proc.csv', encoding='ISO-8859-1', dtype=str)
proc.set_index('IP_COD', inplace=True)
raca = pd.read_csv('data/raca.csv', encoding='ISO-8859-1', dtype=str)
raca.set_index('COD_RACACOR', inplace=True)
sexo = pd.read_csv('data/sexo.csv', encoding='ISO-8859-1', dtype=str)
sexo.set_index('COD_SEXO', inplace=True)
simnao = pd.read_csv('data/simnao.csv', encoding='ISO-8859-1', dtype=str)
simnao.set_index('COD_SIMNAO', inplace=True)
idade = pd.read_csv('data/idade.csv', encoding='ISO-8859-1', dtype=str)
idade.set_index('IDADE', inplace=True)

df = pd.read_csv("data/PS_Ijui_2014-2023_filter.csv", encoding='ISO-8859-1', dtype=str)

df['CNES_EXEC'] = df['CNES_EXEC'].map(cnes['FANTASIA'])
df['UFMUN'] = df['UFMUN'].map(municipio['DS_NOME'])
df['SEXOPAC'] = df['SEXOPAC'].map(sexo['NOME_SEXO'])
df['RACACOR'] = df['RACACOR'].map(raca['NOME_RACACOR'])
df['MUNPAC'] = df['MUNPAC'].map(municipio['DS_NOME'])
df['CIDPRI'] = df['CIDPRI'].map(cid['CD_DESCR'])
df['COB_ESF'] = df['COB_ESF'].map(simnao['NOME_SIMNAO'])
df['PA_PROC_ID'] = df['PA_PROC_ID'].map(proc['IP_DSCR'])
df['SIT_RUA'] = df['SIT_RUA'].map(simnao['NOME_SIMNAO'])
df['TP_DROGA'] = df['TP_DROGA'].map(droga['NOME_DROGA'])
df['LOC_REALIZ'] = df['LOC_REALIZ'].map(local['NOME_LOC'])
df['IDADEPAC'] = df['IDADEPAC'].map(idade['GRUPO_IDADE'])
df['DT_ATEND'] = df['DT_ATEND'].str[:4]

labels = {
    'CNES_EXEC': 'Estabelecimento',
    'UFMUN': 'Município',
    'SEXOPAC': 'Sexo',
    'RACACOR': 'Raça/Cor',
    'MUNPAC': 'Município',
    'CIDPRI': 'CID',
    'COB_ESF': 'Cobertura ESF',
    'PA_PROC_ID': 'Procedimento',
    'SIT_RUA': 'Situação de Rua',
    'TP_DROGA': 'Droga',
    'LOC_REALIZ': 'Local',
    'IDADEPAC': 'Idade',
    'DT_ATEND': 'Ano',
    'count': 'Quantidade'
}