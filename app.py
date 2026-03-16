from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():

    usuario = request.form.get("usuario")
    contraseña = request.form.get("contraseña")

    if usuario == "admin" and contraseña == "1234":
        return render_template("success.html", usuario=usuario)
    elif usuario == "mayu" and contraseña == "esunaloca":
        return render_template("success.html", usuario=usuario)

    else:
        return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)
