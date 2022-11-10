import os


data_lake = os.path.join(os.path.abspath('.'), 'datalake')
path_tmp = os.path.join(data_lake, 'tmp')
path_bronze = os.path.join(data_lake, 'bronze')
path_silver = os.path.join(data_lake, 'silver')
path_gold = os.path.join(data_lake, 'gold')

dados = {
    "25741": "Taxa de juros de pessoa jurídica - pequeno porte - recursos livres",
    "25742": "Taxa de juros de pessoa jurídica  micro empresa - recursos livres",
    "25743": "Saldo de crédito pessoa jurídica por região - pequeno porte - Sul",
    "25744": "Saldo de crédito pessoa jurídica por região - pequeno porte - Sudeste",
    "25745": "Saldo de crédito pessoa jurídica por região - pequeno porte - Norte",
    "25746": "Saldo de crédito pessoa jurídica por região - pequeno porte - Nordeste",
    "26536": "Saldo de crédito pessoa jurídica por região - pequeno porte - Centro-Oeste",
    "26440": "Saldo de crédito pessoa jurídica por região - microempresa - Sul"
}

def create_path(path_):
    if not os.path.isdir(path_):
        print(f'Diretorio não existe. Criando diretório: {path_}!!')
        os.makedirs(path_)

# df.head() todas as colunas
# pd.pandas.set_option('display.max_columns', None)