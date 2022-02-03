import pandas as pd
import time

print('INICIO DO PROCESSAMENTO...')
t_ini=time.time()
cont=0

chunk_size=4000000
batch_no=1

for chunk in pd.read_csv(r'C:\Users\FBENDL\Documents\TAREFAS\202004_AuxilioEmergencial_NOVO.csv',sep=';',encoding='ISO-8859-1',chunksize=chunk_size):
    chunk.to_csv('AuxilioEmergencial' + str(batch_no) + '.csv',index=False)
    batch_no +=1

t_fim=time.time()
print()
print(f'TOTAL DE ARQUIVOS.... {batch_no}')
print()
print(f'DURAÇÃO DO PROCESSAMENTO (Minutos) : {round(((t_fim-t_ini)/60),1)}')
