from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores =[
    {'nome':'Renan',
    'habilidades':['Python','Flask']
    },
    {'nome':'Aline',
     'habilidades':['Vendadora','Gerente']
     }
]
#devolve um desenvolvedor pelo ID, deleta e altera
@app.route('/dev/<int:id>/', methods =['GET','PUT', 'DELETE'])

def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'error', 'mensagem' :mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador'
            response = {'status':'error', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluido'})
    

    
if __name__ == '__main__':
    app.run()