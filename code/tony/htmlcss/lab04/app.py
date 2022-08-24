from crypt import methods
import enum
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    s = '\n'.join([f'<p>{k}: <strong>{v}</strong></p>' for k, v in request.values.items()])
    if request.values:
        return render_template('success.html', request=s)
    else:
        return render_template('index.html')

app.run(debug=True)