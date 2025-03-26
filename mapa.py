import json

class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_aresta(self, origem, destino, dist):
        if origem not in self.grafo:
            self.grafo[origem] = {}
        if destino not in self.grafo:
            self.grafo[destino] = {}
        self.grafo[origem][destino] = dist
        self.grafo[destino][origem] = dist

    def percorrer_cidades_guloso(self, cidade_inicial, cidade_destino):
        visitado = set([cidade_inicial])
        caminho = [cidade_inicial]
        distancia_total = 0
        cidade_atual = cidade_inicial

        while cidade_atual != cidade_destino:
            vizinhos = self.grafo.get(cidade_atual, {})
            candidatos = [(vizinhos[vizinho], vizinho) for vizinho in vizinhos if vizinho not in visitado]

            if not candidatos:
                print("Não foi possível encontrar um caminho para a cidade de destino.")
                return [], 0

            menor_distancia, proxima_cidade = min(candidatos)
            visitado.add(proxima_cidade)
            distancia_total += menor_distancia
            caminho.append(proxima_cidade)
            cidade_atual = proxima_cidade

        return caminho, distancia_total

try:
    with open('cidades2.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except UnicodeDecodeError:
    print("Erro ao decodificar usando UTF-8, tentando outra codificação...")
    with open('cidades2.json', 'r', encoding='latin-1') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Erro: Arquivo 'cidades2.json' não encontrado.")
    exit(1)
except json.JSONDecodeError:
    print("Erro: Não foi possível ler o arquivo JSON. Verifique a formatação.")
    exit(1)

grafo = Grafo()

for origem, destinos in data.items():
    for destino, dist in destinos.items():
        grafo.adicionar_aresta(origem, destino, dist)

cidade_inicial = input("Digite a cidade de origem: ")
cidade_destino = input("Digite a cidade de destino: ")

if cidade_inicial not in grafo.grafo or cidade_destino not in grafo.grafo:
    print("Erro: Uma das cidades informadas não está no grafo.")
else:
    caminho, distancia_total = grafo.percorrer_cidades_guloso(cidade_inicial, cidade_destino)
    
    if caminho:
        print("\nO caminho encontrado é:")
        for i in range(len(caminho) - 1):
            print(f"{caminho[i]} -> {caminho[i+1]} ({grafo.grafo[caminho[i]][caminho[i+1]]} km)")
        print(f"\nA distância total percorrida é: {distancia_total} km")
