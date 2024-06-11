import pandas as pd
import plotly.graph_objects as go

def get_group_data(x, y=None):
    if y:
        if type(y) == str:
            data = df[df['DT_ATEND'].str.contains(y)].groupby(x).size().reset_index(name='count')
        else:
            regex = '|'.join(y)
            data = df[df['DT_ATEND'].str.contains(regex)].groupby(x).size().reset_index(name='count')
    else:
        data = df.groupby(x).size().reset_index(name='count')
    
    return data

def plot_bar(x, y=None):
    data = get_group_data(x, y)
    fig = go.Figure(data=[go.Bar(x=data.iloc[:,0], y=data.iloc[:,1])])
    return fig

def plot_line(x, y=None):
    data = get_group_data(x, y)
    fig = go.Figure(data=[go.Scatter(x=data.iloc[:,0], y=data.iloc[:,1])])
    return fig

def plot_pie(x, y=None):
    data = get_group_data(x, y)
    fig = go.Figure(data=[go.Pie(labels=data.iloc[:,0], values=data.iloc[:,1])])
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