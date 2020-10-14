from flask import Flask
app = Flask(__name__)
@app.route("/")

def hello():
	html = "<h1>Hello {name}!</h1>".format(name="Jenny")
	return html

if __name__ == "__main__":
	app.run(hosst='0,0,0,0'. port=80)

