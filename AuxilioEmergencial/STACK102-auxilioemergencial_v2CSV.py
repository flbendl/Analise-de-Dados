import csv
import time

print('INICIO DO PROCESSAMENTO...')
t_ini=time.time()
cont=0

with open('AuxilioEmergencial_NOVOLIMITADO_curto.csv','r',encoding='ISO-8859-1') as arq:
    csv_leitura=csv.DictReader(arq,delimiter=';')

    with open('AuxilioEmergencial_NOVOLIMITADO_curtov2.csv','w',encoding='ISO-8859-1') as grava:
        lista=['UF','NOME MUNICÍPIO','NIS BENEFICIÁRIO','VALOR BENEFÍCIO']

        csv_grava = csv.DictWriter(grava, fieldnames=lista, delimiter=';',extrasaction='ignore')
        csv_grava.writeheader()
        for item in csv_leitura:            
            csv_grava.writerow(item)
            cont+=1
t_fim=time.time()
print()
print(f'TOTAL DE REGISTROS ... {cont}')
print()
print(f'DURAÇÃO DO PROCESSAMENTO (Minutos) : {round(((t_fim-t_ini)/60),1)}')
