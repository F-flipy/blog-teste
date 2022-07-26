from flask import Flask, render_template     #A partir da biblioteca flask importo a Classe Flask

app = Flask("hello")        #criação do aplicativo aapp recebe classe Flask com nome hello

@app.route("/")              # criação de rota
@app.route("/hello")
def hello():                #define função
    return "Hello World"    

@app.route("/meucontato")
def meuContato():
    return render_template("index.html")
	