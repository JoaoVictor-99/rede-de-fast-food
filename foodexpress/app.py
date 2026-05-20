from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cardapio")
def cardapio():
    return render_template("cardápio.html")

@app.route("/lanche/<nome>")
def lanche(nome):
    mensagens = {
        "pizza": "Pizza quentinha e deliciosa!",
        "hamburguer": "Hambúrguer suculento e saboroso!",
        "batata": "Batata frita crocante!",
        "milkshake": "Milkshake gelado e cremoso!"
    }

    if nome.lower() in mensagens:
        mensagem = mensagens[nome.lower()]
    else:
        mensagem = "Lanche não encontrado."

    return render_template(
        "lanche.html",
        nome=nome,
        mensagem=mensagem
    )

@app.route("/pedidos")
def pedidos():
    return render_template("pedidos.html")

@app.route("/cliente/<nome>/<cidade>")
def cliente(nome, cidade):
    if cidade.lower() == "natal":
        entrega = "Entrega disponível"
    else:
        entrega = "Entrega indisponível."

    return render_template(
        "cliente.html",
        nome=nome,
        cidade=cidade,
        entrega=entrega
    )

@app.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)
