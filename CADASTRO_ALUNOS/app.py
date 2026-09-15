from flask import Flask, render_template, request

app = Flask(__name__)

# Alunos já cadastrados no sistema
alunos = [
    {
        "nome": "João Silva",
        "idade": 20,
        "curso": "Sistemas de Informação"
    },
    {
        "nome": "Maria Santos",
        "idade": 21,
        "curso": "Administração"
    },
    {
        "nome": "Pedro Oliveira",
        "idade": 19,
        "curso": "Engenharia de Software"
    },
    {
        "nome": "Ana Costa",
        "idade": 22,
        "curso": "Pedagogia"
    }
]


# Rota 1 - Página inicial
@app.route("/")
def inicio():
    return render_template("index.html", alunos=alunos)


# Rota 2 - Cadastrar novo aluno
@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    nome = request.form["nome"]
    idade = request.form["idade"]
    curso = request.form["curso"]

    # Adiciona o novo aluno à lista
    alunos.append({
        "nome": nome,
        "idade": idade,
        "curso": curso
    })

    return render_template("index.html", alunos=alunos)


# Iniciar o sistema
if __name__ == "__main__":
    app.run(debug=True)
