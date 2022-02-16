from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/proyecto")
def proyecto():
	return render_template("proyecto.html")

@app.route("/faqs")
def faqs():
	return render_template("faqs.html")

@app.route("/conclusiones")
def conclusiones():
	return render_template("conclusiones.html")

@app.route("/thanks")
def agradecimiento():
	return render_template("thanks.html")

@app.route("/pagina")
def pagina():
	return render_template("pagina.html")

@app.route("/hardware")
def hardware():
	return render_template("hardware.html")

if __name__ == '__main__':
	app.run(debug=True)