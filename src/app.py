from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
  return render_template("index.html")

@app.route("/quem-somos")
def quem():
  return render_template("quem-somos.html")

@app.route("/contatos")
def contatos():
  return render_template("contatos.html")

if __name__ == "__main__":
  app.run(debug=True)
