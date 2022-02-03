#       ANÁLISE DE DADOS --- BOLSA FAMÍLIA
#=====================================================
# TOTALIZAR BENEFÍCIOS PAGOS POR UNIDADE FEDERATIVA
#           (VALORES MONETÁRIOS)

#Importar os módulos ncessários
import csv
import time

print('================================')
print('Aguarde processamento...        ')
print('================================')
print('')

hora_ini=time.time()
valor_total=0
#Definir um dicionário para armazenar o resultado
total_uf={}
#201401_BolsaFamilia_Pagamentos
#2014_SAL_FAM
#Abrir e carrager o arquivo CSV
with open('201401_BolsaFamilia_Pagamentos.csv','r') as csv_arquivo:
    leitura=csv.reader(csv_arquivo,delimiter=';')
#Pular linha de cabeçalho
    next(leitura)    
#Preencher o dicionário com total de benefícios pagos por UF
    for item in leitura:
        if item[2] not in total_uf:
            total_uf[item[2]]=round(int(float(item[7].replace(',','.'))))         
        else:
            total_uf[item[2]]=round(int(float(item[7].replace(',','.'))))+total_uf[item[2]]
                        
#Classifica o dicionário por ordem alfebética de UD
for key, value in sorted(total_uf.items()):
    valor_total=value+valor_total
#    print('{} : {}'.format(key,value))
    print(f'{key:>10} : {value:<10}')

hora_fim=time.time()
print('')
print('TEMPO DE EXECUÇÃO : {}'.format(hora_fim-hora_ini))
print('')
# Imprime maiores municípios por total de pagamentos
n=10
maiores={key: total_uf[key] for key in
         sorted(total_uf, key=total_uf.get, reverse=True)[:n]}
print('===============================================')
print(' Maiores Estados com Benefícios Pagos em R$    ')
print('===============================================')
print('')
for key,value in maiores.items():    
#    print('{} : {}.00'.format(key,value))
    print(f'{key:>10} : {value:.>20}.00')
print('')
print('Total Pago de Benefícios : R$ {0:.2f}'.format(valor_total))
            
 
            
           
