from flask import Flask, request

app = Flask(__name__)




@app.route("/windows", methods=["POST"])
def save_windwos():
    data = request.json
    print(data)

    return {"mensagem": "Solicitação recebida com sucesso", "data": data}


if __name__ == "__main__":
    app.run()
