import os
import datetime as dt

import pandas as pd 
from acesso_credito.tasks.utils import (
    data_lake, 
    path_silver, 
    path_gold, 
    dados
)

def move_gold():

    list_files = os.listdir(path_silver)
    if len(list_files):
        path_file = os.path.join(path_silver, list_files[0])
        df_gold = pd.read_parquet(path_file)

        df_gold.loc[df_gold['NR_MES'] == 1, 'NM_TRIMESTRE'] = 'segundo'
        df_gold.loc[df_gold['NR_MES'] == 4, 'NM_TRIMESTRE'] = 'terceiro'
        df_gold.loc[df_gold['NR_MES'] == 7, 'NM_TRIMESTRE'] = 'quarto'
        df_gold.loc[df_gold['NR_MES'] == 10, 'NM_TRIMESTRE'] = 'primeiro'

        df_gold['NM_TRIMESTRE'] = df_gold['NM_TRIMESTRE'].astype('string')

        path_output = os.path.join(path_gold, 'indicadores.parquet')
        df_gold.to_parquet(path_output, index=False)
        # df_silver.to_csv(path_output, index=False)

        # df_gold[['NR_ANO', 'NM_INDICADOR', 'VL_INDICADOR']].groupby(['NR_ANO', 'NM_INDICADOR']).agg('sum')


# result = df_gold[df_gold.columns.tolist()].groupby('NR_ANO', 'NM_INDICADOR').aggregate('sum')
# result = df_gold.groupby(['NR_ANO', 'NM_INDICADOR']).aggregate('sum')
    else:
        raise Exception('Não há arquivo para processamento!!')


#pendencias
    # criar coluna com soma de valores por ano e indicador_base
    # criar coluna com media "" ""
    # criar coluna com valor minimo "" ""
    # criar coluna com valor maximo "" ""

#tentar colocar as tarefas no airflow
# subir o airflow no dockercompose
# subir container com sql server
# salvar os dados no sql server
