from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def hello():
	return render_template("hello.html")

@app.route("/<name>")
def hello_someone(name):
	return render_template("hello.html", name=name.title())

def something_went_wrong():
	print "oops"

@app.route("/signup", methods=["POST"])
def sign_up():
	form_data = request.form

	email = form_data["email"]


	#


	if not form_data["vehicle1"]:
		vehicle1 = ''
	else:
		vehicle1 = form_data["vehicle1"]

	if not form_data["vehicle2"]:
		vehicle2 = ''
	else:
		vehicle2 = form_data["vehicle2"]

	vehicles = "{} {}".format(vehicle1, vehicle2)

	if request.method == 'POST':
		return render_template("form_submission.html", email=email, vehicles=vehicles)
	else:
		something_went_wrong()

@app.route("/hi")
def hi():
	return "Hi"

@app.route("/bye")
def bye():
	return "Bye"


app.run(debug=True)
