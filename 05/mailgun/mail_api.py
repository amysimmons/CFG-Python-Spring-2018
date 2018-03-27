from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

def send_simple_message(name, email):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxffcad52fe3544aca85d70e97c8c31cf5.mailgun.org/messages",
        auth=("api", "key-94a0d7d05b2209e3774d3535eb26c601"),
        data={"from": "Excited User <mailgun@sandboxffcad52fe3544aca85d70e97c8c31cf5.mailgun.org>",
              "to": [email, "YOU@sandboxffcad52fe3544aca85d70e97c8c31cf5.mailgun.org"],
              "subject": "Hello {}".format(name),
              "text": "Testing some Mailgun awesomness!"})

@app.route("/")
def home():
	return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def sign_up():
	form_data = request.form
	name = form_data["name"]
	email = form_data["email"]
	send_simple_message(name, email)
	return "OK"

app.run(debug=True)
