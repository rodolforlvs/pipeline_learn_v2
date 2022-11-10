import os
import datetime as dt

import pandas as pd 
from acesso_credito.tasks.utils import (
    data_lake, 
    path_bronze, 
    path_silver, 
    dados
)

def move_silver():

    df_silver = pd.DataFrame([])

    list_files = os.listdir(path_bronze)
    if len(list_files):
        for file_nome in list_files:
            path_file = os.path.join(path_bronze, file_nome)
            df_aux = pd.read_parquet(path_file)

            code_base = file_nome.replace('.parquet', '')
            indicador_base = dados.get(code_base)

            df_aux['NOME_INDICADOR'] = indicador_base

            df_silver = pd.concat([df_silver, df_aux], axis=0)

        df_silver = df_silver.rename(
            columns={
                'DATA': 'DT_LANCAMENTO',
                'NOME_INDICADOR': 'NM_INDICADOR',
                'VALOR': 'VL_INDICADOR'
            }
        )

        df_silver['DT_LANCAMENTO'] = pd.to_datetime(df_silver['DT_LANCAMENTO'], format='%d/%m/%Y')
        df_silver['NR_ANO'] = df_silver['DT_LANCAMENTO'].dt.year
        df_silver['NR_MES'] = df_silver['DT_LANCAMENTO'].dt.month

        # df_silver = df_silver.convert_dtypes().dtypes
        df_silver['NM_INDICADOR'] = df_silver['NM_INDICADOR'].astype('string')
        
        path_output = os.path.join(path_silver, 'indicadores.parquet')
        df_silver.to_parquet(path_output, index=False)
        # df_silver.to_csv(path_output, index=False)

    else:
        raise Exception('Não há arquivo para processamento!!')
