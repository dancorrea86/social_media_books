from app import app

@app.route("/")
@app.route("/home")
def index():
    return "Bem Vindo ao Projeto"

