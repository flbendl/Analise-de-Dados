import pandas as pd
import time

print('INICIO DO PROCESSAMENTO...')
t_ini=time.time()
cont=0

uf=['RO','AC','AM','RR','PA','AP','TO','MA','PI','CE','RN','PB','PE','AL','SE','BA','MG','RJ','SP','PR','SC','RS','MS','MT','GO','ES','DF']
uf_ordenadas=sorted(uf)


for item in pd.read_csv('C:/Users/FBENDL/Documents/TAREFAS/202004_AuxilioEmergencial.csv',sep=';',encoding='ISO-8859-1'):
    for uf in uf_ordenadas:
        caminho_do_arquivo='C:/Users/FBENDL/Documents/TAREFAS/202004_AuxilioEmergencial_{}.csv'.format(uf)
        df[df['UF']==uf].to_csv(caminho_do_aruivo,sep=';',encoding='ISO-8859-1')


t_fim=time.time()
print()
print(f'TOTAL DE ARQUIVOS.... {batch_no}')
print()
print(f'DURAÇÃO DO PROCESSAMENTO (Minutos) : {round(((t_fim-t_ini)/60),1)}')
