from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Aline',idade=29)
    print(pessoa)
    pessoa.save()
    
def consulta_pessoa():
    pessoas = Pessoas.query.all()
    #pessoa = Pessoas.query.filter_by(nome='Aline').first()
    print(pessoas)
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Aline').first()
    pessoa.nome = 'Joana'
    pessoa.save()
    
def deleta_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Joana').first()
    pessoa.delete()
    
if __name__ == '__main__':
    #insere_pessoas()
    consulta_pessoa()
    #altera_pessoa()
    #deleta_pessoa()