# Algoritmo de Caminho Mais Curto com Abordagem Gulosa

Este projeto implementa um algoritmo para encontrar o caminho mais curto entre duas cidades utilizando uma abordagem **gulosa**. O grafo das cidades e as distâncias entre elas são carregados de um arquivo JSON. O algoritmo busca o caminho de menor distância, escolhendo sempre a cidade mais próxima.

## Funcionalidades

### 🔗 Adicionar Arestas
O grafo é criado e as arestas entre as cidades são inseridas com base nos dados de distâncias contidas em um arquivo JSON. Cada cidade está conectada às outras com uma distância específica.

### 🧭 Busca Gulosa
O algoritmo percorre as cidades e, a cada passo, escolhe a cidade mais próxima, sem considerar o caminho global mais curto, mas apenas a proximidade imediata.

### 🌍 Visualização de Caminho
O programa exibe o caminho encontrado entre a cidade de origem e a cidade de destino, juntamente com a distância total percorrida.

## Como Usar

### 1. Preparação do Ambiente

Certifique-se de ter o arquivo `cidades2.json` no mesmo diretório do código.

Execute o script Python:
python mapa.py

O programa pedirá para você inserir a cidade de origem e a cidade de destino:
Digite a cidade de origem: CidadeA
Digite a cidade de destino: CidadeC
