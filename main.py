from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/authorization", methods=['POST'])
def 

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('user-signup.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()