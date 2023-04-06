from flask import Flask

application = Flask(__name__)


@application.route("/")
def hello_world():
    return "Hello, World!"


@application.route("/dojo")
def enter_the_dojo():
    return "Dojo!"


@application.route("/say/<string:input>")
def say_something(input):
    return f"Hi, {input.capitalize()}!"


@application.route("/repeat/<int:count>/<string:input>")
def repeat_something(count, input):
    string = ""
    for i in range(count):
        string += f"{input} \n"
    return string


@application.route("/<invalid_url>")
def invalid_route(invalid_url):
    return "Sorry! No response. Try again."


if __name__ == "__main__":
    application.run(debug=True)
