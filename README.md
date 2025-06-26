# Otimização de Rotas com Algoritmo Genético
Este projeto implementa uma solução para o Problema de Roteamento de Veículos (PRV), modelado como uma variação do Problema do Caixeiro Viajante (TSP), utilizando um Algoritmo Genético simples. O objetivo é encontrar a menor rota possível que percorra um conjunto de pontos de coleta em um grid bidimensional.


## 🎯 Objetivo
- Gerar um conjunto de pontos aleatórios no plano 2D.
- Criar uma população inicial de rotas (permutações dos pontos).
- Avaliar as rotas com base na distância total percorrida.
- Visualizar a melhor rota obtida.
- Permitir reprodutibilidade via entrada de `seed`.


## 📁 Estrutura do Projeto
```
├── main.py               # Arquivo principal de execução
├── config.ini            # Arquivo de configuração com parâmetros principais
├── config.py             # Leitura e validação do arquivo config.ini
├── routing.py       	  # Geração de grid, rotas e avaliação
├── plotting.py           # Função para visualização de rotas
├── utils.py              # Entrada de seed com tratamento de erros
└── requirements.txt      # Dependências do projeto
```


## ⚙️ Parâmetros Configuráveis (`config.ini`)
```ini
[PARAMETERS]
Number_of_Points = 10
Grid_Size = 100
Population_Size = 100
```


## ▶️ Execução
```bash
python main.py
```
Durante a execução, o programa solicitará que você informe uma **seed numérica**. Caso digite `0` ou algo inválido, o algoritmo executará com comportamento aleatório.


## 📊 Resultados
- A melhor rota da população inicial será impressa no console.
- Um gráfico com a rota será exibido utilizando `matplotlib`.


## 🧩 Dependências
Instale as bibliotecas necessárias com:
```bash
pip install -r requirements.txt
```


## 👨‍💻 Autor
Fábio Gandini  
Junho de 2025
