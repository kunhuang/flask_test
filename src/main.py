from flask import Flask
from auth import requires_auth
main = Flask(__name__)

@main.route("/")
def hello():
    return "Hello World!"

@main.route("/auth_test")
@requires_auth
def auth_test():
    return "Passed the authentication!"

if __name__ == "__main__":
    main.run()