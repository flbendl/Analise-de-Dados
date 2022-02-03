import csv
import time

print('INICIO DO PROCESSAMENTO...')
t_ini=time.time()
cont=0

with open('202004_AuxilioEmergencial.csv','r',encoding='ISO-8859-1') as arq:
    csv_leitura=csv.DictReader(arq,delimiter=';')

    with open('202004_AuxilioEmergencial_NOVOLIMITADO.csv','w',encoding='ISO-8859-1') as grava:
        lista=['UF','NOME MUNICÍPIO','CPF BENEFICIÁRIO','NIS BENEFICIÁRIO','NOME BENEFICIÁRIO',
               'PARCELA','VALOR BENEFÍCIO']

        csv_grava = csv.DictWriter(grava, fieldnames=lista, delimiter=';',extrasaction='ignore')
        csv_grava.writeheader()
        for item in csv_leitura:
            if cont==8000000:
                break
            csv_grava.writerow(item)
            cont+=1
t_fim=time.time()
print()
print(f'TOTAL DE REGISTROS ... {cont}')
print()
print(f'DURAÇÃO DO PROCESSAMENTO (Minutos) : {round(((t_fim-t_ini)/60),1)}')
