from flask import Flask, jsonify

app = Flask (__name__)

@app.route('/<int:id>')
def pessoa(id):
    return jsonify({'id':id,'nome':'Renan','profissao':'programador'})

if __name__ == '__main__':
    app.run(debug=True)