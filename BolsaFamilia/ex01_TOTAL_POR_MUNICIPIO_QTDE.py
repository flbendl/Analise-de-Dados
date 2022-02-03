#       ANÁLISE DE DADOS --- BOLSA FAMÍLIA
#========================================================
# TOTALIZAR QUANTIDADES DE BENEFÍCIOS PAGOS POR MUNICÍPIO
#           (VALORES QUANTIDADE)

# MONTAR UMA LISTA SOMENTE COM 

#Importar bibliotecas
import csv
import time

# FUNÇÃO para imprrimir mensagens de tela
def mensagem(texto):
     print('*'*51)
     print(texto)
     print('*'*51)
     print('')
       
mensagem('           Aguarde processamento...  '.upper())

# Inicializa variáveis
valor_total=0
#Defini hora inicial do processamento
hora_ini=time.time()

#201401_BolsaFamilia_Pagamentos
#2014_SAL_FAM

# Gravação de um dicionário com todos os municipios do Brasil
municipios_fora={}
contador=0
with open('MUNICIPIOS.csv','r') as csv_arquivo:
    leitura=csv.reader(csv_arquivo,delimiter=';')
    next(leitura)
    for item in leitura:         
         municipios_fora[item[1].upper()]=item[0]         
    else:       
        municipios_fora[item[1].upper()]=item[0]         
        

# Gravação do dicionário com quantidade total de pagamento por município
cidades_uf={}   
    
with open('2014_SAL_FAM.csv','r') as csv_arquivo:
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
    valor_total=value+valor_total
    #print('{} : {}'.format(key,value))

# Imprime maiores municípios por quantidade total de pagamentos
n=10
maiores={key: cidades_uf[key] for key in
         sorted(cidades_uf, key=cidades_uf.get, reverse=True)[:n]}
        
mensagem(' Maiores Estados com Benefícios Pagos em Quantidade')

for key,value in maiores.items():    
    print('{} : {}'.format(key,value))
print('')
print('Quantidade total de Benefícios : {}'.format(valor_total))
print('')
# Elemento principal de comparação é o nome do Município que é chave do dicionário
# de todos os Municipios do Brasil.
# Esta chave será comparada com o dicionário dos municipios do processamento do
# mês que foi processado.
d3 = {key:municipios_fora[key] for key in municipios_fora if key not in cidades_uf}

mensagem('   Municipios que estão fora do Bolsa Familia      ')

#Classifica o dicionário por ordem alfebética de UD
contador=0
for key, value in sorted(d3.items()):
    contador=contador+1
    #print('{} : {}'.format(key,value)) 
print('  Total de Municípios fora do Balsa Família:',contador)
print('')

# Defini hora final do processamento    
hora_fim=time.time()
mensagem('         F I M  D O  P R O C E S S A M E N T O      ')
print('TEMPO DE EXECUÇÃO : {:.2f}'.format(hora_fim-hora_ini))
