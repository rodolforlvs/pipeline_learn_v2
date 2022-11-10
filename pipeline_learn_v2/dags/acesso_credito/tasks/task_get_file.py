import os

import requests

from acesso_credito.tasks.utils import data_lake, dados, create_path


def baixar_csv(url, path_output):
    retorno = requests.get(url)
    if retorno.status_code == requests.codes.OK:
        with open(path_output, 'wb') as f:
            f.write(retorno.content)

        print(f"Download finalizado. Arquivo salvo em: {path_output}")

    else:
        retorno.raise_for_status()


def get_files():
    url_base = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=csv'

    data_lake_tmp = os.path.join(data_lake, 'tmp')
    create_path(data_lake_tmp)

    for valor in dados.keys():
        nome_arquivo = os.path.join(data_lake_tmp, f'dados_BC_{valor}.csv')

        baixar_csv(url_base.format(valor), nome_arquivo)





