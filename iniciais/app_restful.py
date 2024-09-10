from flask import Flask, request, json
from flask_restful import Resource, Api
from iniciais.habilidades import Habilidades, ListaHabilidades
app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': '0',
        'nome': 'Renan',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id': '1',
        'nome': 'Aline',
        'habilidades': ['Vendadora', 'Gerente']
    }
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'error', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador'
            response = {'status': 'error', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return ({'status': 'sucesso', 'mensagem': 'Registro excluido'})


class ListaDesenvolvedores(Resource):
    def post(self, id):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return (desenvolvedores[posicao])

    def get(self):
        return (desenvolvedores)


api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/<int:id>')
api.add_resource(ListaHabilidades, '/habilidades/')

if __name__ == '__main__':
    app.run()
