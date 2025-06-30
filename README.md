# Otimização de Rotas com Algoritmo Genético

Este projeto implementa uma solução para o Problema de Roteamento de Veículos (PRV), modelado como uma variação do Problema do Caixeiro Viajante (TSP), utilizando um Algoritmo Genético simples. O objetivo é encontrar a menor rota possível que percorra um conjunto de pontos de coleta em um grid bidimensional.

---

## 🎯 Objetivo
- Gerar um conjunto de pontos aleatórios no plano 2D.
- Criar uma população inicial de rotas (permutações dos pontos de coleta).
- Avaliar as rotas com base na distância total percorrida.
- Visualizar as melhores rotas obtidas.
- Executar múltiplas simulações com diferentes seeds.
- Comparar duas abordagens: Algorítimo de População Inicial Aleatória `(APIA)` e Algoritmo Genético Evolutivo `(AGE)`.
- Salvar os resultados (imagens e CSV) para análise posterior.
- Permitir reprodutibilidade via entrada de `seed`.

---

## 📁 Estrutura do Projeto
```bash
├── src/                    # Diretório de arquivos fonte do projeto.
│   ├── config.py               # Parâmetros principais de execução.
│   ├── execute_experiments.py      # Execução automatizada com múltiplas seeds aleatórias.
│   ├── file_handling.py        # Manipulação de arquivos (imagens, CSV).
│   ├── genetic_evolution.py    # Implementação do algoritmo genético evolutivo.
│   ├── main.py                 # Execução padrão com entrada de seed manual.
│   ├── plotting.py             # Geração de figuras com o módulo MatPlotLib.
│   ├── routing.py              # Geração de grid, população e avaliação de rotas.
│   └── utils.py                # Coleção de funções utilitárias compartilhadas.
├── output/                 # Diretório de resultados gerados (.png, .csv).
│   ├── experiments.csv         # Resultado compilado de todas as melhores rotas obtidas em execução automatizada.
│   └── route_seed_*.png        # Arquivos de imagens das melhores rotas obtidas em execução automatizada.
├── config.ini              # Parâmetros principais de execução.
├── requirements.txt        # Dependências do projeto.
├── README.md               # Arquivo de documentação do projeto.
└── LICENSE                 # Licença para utilização do projeto, uso livre com base na licença MIT.
```

---

## ⚙️ Parâmetros Configuráveis (`config.INI`)
```
[PARAMETERS]
Number_of_Points = Número de pontos de coleta a serem gerados no plano 2D.
Grid_Size = Dimensão máxima do plano em que os pontos são distribuídos (ex.: 1000 significa uma área 1000x1000).
Population_Size = Número de rotas diferentes geradas aleatoriamente para formar a população inicial.
Number_of_Generations = Número de gerações para o algoritmo evolutivo.

[OUTPUT]
Folder_Name = Nome do diretório onde os arquivos de saída serão salvos (imagens e CSV).
CSV_File_Name = Nome do arquivo onde os resultados das simulações serão armazenados.
Image_File_Name = Prefixo utilizado para nomear os arquivos de imagem com as melhores rotas encontradas.
Number_of_Seeds = Número de execuções com diferentes valores de seed (controle de aleatoriedade).
```

---

## ▶️ Execução

### Execução padrão com entrada manual de seed:
```bash
python .\src\main.py
```

### Execução automatizada com várias seeds:
```bash
python .\execute_experiments.py
```

Os resultados serão salvos no diretório definido em `config.INI` (por padrão é `'.\output\'`).

---

## 📊 Resultados

- Cada execução gera duas imagens `.PNG` de rota: uma para o `APIA` e outra para `AGE`.
- O arquivo experiments.csv inclui:
  - Seed
  - Distância, tempo e rota para APIA
  - Distância, tempo e rota para AGE
- As imagens seguem o padrão: route_seed_{seed}_RIPA.png e route_seed_{seed}_EA.png respectivamente para APIA e AGE.

---

## 🧩 Dependências

Instale as bibliotecas necessárias com:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Autor

Fábio Gandini  
Junho de 2025
