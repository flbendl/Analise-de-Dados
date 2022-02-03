# MONTAR UMA LISTA SOMENTE COM QUANTIDADES DE BENEFÍCIOS PAGOS POR CIDADE

#Importar bibliotecas
import csv
import time

print('=============================')
print('Aguarde o processamento ...')
print('=============================')
print('')

hora_ini=time.time()
#201401_BolsaFamilia_Pagamentos
#2014_SAL_FAM

cidades_uf={}   
    
with open('201401_BolsaFamilia_Pagamentos.csv','r') as csv_arquivo:
    leitura=csv.reader(csv_arquivo,delimiter=';')    
# Pular primeira linha do cabeçalho
    next(leitura)
# Converte arquivo CSV para LISTA        
    for item in leitura:
        if item[4] in cidades_uf:
            cidades_uf[item[4]]+=1
        else:
            cidades_uf[item[4]]=1
#Classifica o dicionário por ordem alfebética de UD
for key, value in sorted(cidades_uf.items()):
    print('{} : {}'.format(key,value))
    
hora_fim=time.time()
print('TEMPO DE EXECUÇÃO : {}'.format(hora_fim-hora_ini))


