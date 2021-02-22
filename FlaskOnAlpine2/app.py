from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def welcomemsg():
    return "Welcome to the world of the container"

@app.route("/welcome")
def home():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4500,debug=True)
