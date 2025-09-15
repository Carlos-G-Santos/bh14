import pandas as pd
import numpy as np


#print("Iniciando execução do script...")
#import os
#print("Diretório atual:", os.getcwd())
#print("Arquivos no diretório:", os.listdir())
#try:
df = pd.read_csv('flux_516', sep='\s+')
#    print(df.head())
#except FileNotFoundError:
#    print("Arquivo não encontrado")
#except pd.errors.EmptyDataError:
#    print("Arquivo vazio")
#except Exception as e:
#    print("Erro ao ler o arquivo:", e)

print(df.head())
