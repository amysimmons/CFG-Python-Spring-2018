from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

def send_simple_message(name, email):
    return requests.post(
        "https://api.mailgun.net/v3//messages",
        auth=("api", ""),
        data={"from": "Excited User <mailgun@>",
              "to": [email, "YOU@"],
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
