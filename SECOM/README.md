<h1 align="center">Segmentação de Dados</h1>

<img src="https://img.shields.io/static/v1?label=Blog&message=Flávio Bendl&color=0dbe98&style=for-the-badge&logo=ghost"/>
<h2>✨ Funcionalidades</h2>
<p align="left">Programas desenvolvidos em linguagem PYTHON com funcionalidade de reduzir o tamanho do arquivo do Auxílio Emergência (Programa de Assistência Social do Governo Federal). Esta redução possibilita manipular o arquivo em editores de código como por exemplo o Jupyter Notebook.
O programa possibilita selecionar quais colunas devem ser gravadas no arquivo de saída.
Em média os arquivos possuem 8GB de tamanho e 48 milhões de linhas.
</p>

<h3>📂 Arquivos</h3>
<p align="left">Os arquivos de entrada estão disponíveis em [Arquivos do Auxílio Emergêncial](https://www.portaltransparencia.gov.br/download-de-dados/auxilio-emergencial), no formato CSV (comma-separated values).
</p>

<h3>⚙️ Descrição de cada programa</h3>

```bash

# Gerar novo arquivo CSV somente com as colunas selecionadas.
$ STACK102-auxilioemergencial_v2CSV.py

# Gerar novo arquivo CSV somente com Estados (UF) selecionados.
$ STACK102-auxilioemergencialESTADOCSV.py

# Gerar multiplos arquivos de tamanhos fixos (chunk).
$ STACK102-auxilioemergencialMULTIPLOSCSV.py

```

<h3>🔨 Uso</h3>

```bash

# Esta lista pode ser alterada em reduzir o número de colunas.
# Exemplo: foi retirado as colunas NIS e NOME BENEFICIARIO
lista=['UF','NOME MUNICÍPIO','VALOR BENEFÍCIO']
```

<h3>🛠 Tecnologias</h3>

```bash

# Python version 3.8
# Editor para trabalhar com o código como: VSCode , IDLE Python ou PyCharm.

```