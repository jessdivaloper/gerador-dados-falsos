from flask import Flask, jsonify, request
import random
from datetime import datetime, timedelta

app = Flask(__name__)

def gerar_dados_sinteticos():
    dados = []
    alunos = [f"A{100+i}" for i in range(100)]
    hoje = datetime.today()
    for aluno_id in alunos:
        for dias_atras in range(5):
            data = (hoje - timedelta(days=dias_atras)).strftime("%Y-%m-%d")
            tempo_uso = random.randint(30, 180)
            dados.append({
                "aluno_id": aluno_id,
                "data": data,
                "tempo_uso_minutos": tempo_uso
            })
    return dados

dados_uso = gerar_dados_sinteticos()

@app.route('/api/tempo-uso', methods=['GET'])
def tempo_uso():
    aluno_id = request.args.get('aluno_id')
    data = request.args.get('data')

    resultado = dados_uso
    if aluno_id:
        resultado = [d for d in resultado if d["aluno_id"] == aluno_id]
    if data:
        resultado = [d for d in resultado if d["data"] == data]

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)




# python api_tempo_uso.py

'''
http://localhost:5000/api/tempo-uso → retorna todos os registros

http://localhost:5000/api/tempo-uso?aluno_id=A101 → filtra por aluno

http://localhost:5000/api/tempo-uso?data=2025-06-05 → filtra por data

'''