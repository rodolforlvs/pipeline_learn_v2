import os

import pandas as pd 

from acesso_credito.tasks.utils import (
    data_lake, 
    path_tmp, 
    path_bronze, 
    dados
)

def move_bronze():

    list_files = os.listdir(path_tmp)
    if len(list_files):
        for file_nome in list_files:
            path_file = os.path.join(path_tmp, file_nome)
            df_bronze = pd.read_csv(path_file, sep=';', decimal=',')

            code_base = file_nome.split('dados_BC_')[1].replace('.csv', '')

            df_bronze = df_bronze.rename(
                columns={
                    'data': 'DATA', 
                    'valor': 'VALOR',
                }
            )

            path_output = os.path.join(path_bronze, code_base+'.parquet')
            df_bronze.to_parquet(path_output, index=False)
            # df_bronze.to_csv(path_output, index=False)

    else:
        raise Exception('Não há arquivo para processamento!!')
