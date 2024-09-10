from flask_restful import Resource, request

import json

lista_habilidades= [
    {'id':'', 'linguagem':'Pyhon'},
    {'id':'', 'linguagem':'JavaScript'},
    {'id':'', 'linguagem':'Flask'},
    {'id':'', 'linguagem':'PHP'},
    {'id':'', 'linguagem':'Ruby'}   
]

for i, habilidade in enumerate(lista_habilidades, start=0):
    habilidade['id'] = str(i)
    
class Habilidades(Resource):
    def get(self, id):
        return lista_habilidades[id]

    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados

    def delete(self, id):
        lista_habilidades.pop(id)
        return ({'status': 'sucesso', 'mensagem': 'Registro excluido'})
    
class ListaHabilidades(Resource):
    def post(self):
        dados = json.loads(request.data)
        # Atribui o próximo ID disponível
        novo_id = str(int(max([hab['id'] for hab in lista_habilidades])) + 1)
        dados['id'] = novo_id
        lista_habilidades.append(dados)
        return dados

    def get(self):
        return lista_habilidades
    