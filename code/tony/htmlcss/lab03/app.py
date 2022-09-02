import json, sys
from flask import Flask, render_template, redirect
app = Flask(__name__)

with open(f'{sys.path[0]}/data/posts.json', 'r') as f:
    post_content = json.loads(f.read())

for post in post_content:
    post['excerpt'] = post['body'][0:500]

@app.route('/')
def index():
    return redirect('0', code=302)

@app.route('/<int:offset>')
def posts(offset):
    page_next = len(post_content) - offset >= 10 and str(offset + 10) or None
    page_previous = offset >= 10 and str(offset - 10) or None
    return render_template('posts.html', page_next=page_next, page_previous=page_previous, posts=post_content[offset:offset+10])

app.run(debug=True)