from flask import Flask, render_template, request, redirect
import json
app = Flask('__name__')

# @app.route('/', methods=['GET','POST'])
# def index():
#     if request.method == 'POST':
#         color = request.form['color']
#         brightness = request.form['brightness']
#         print(color + ' ' + brightness)
#         return redirect('/')
#     return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html', contents=contents)

@app.route('/submit-form/', methods=['POST'])
def submit_form():
    color = request.form['color']
    brightness = request.form['brightness']
    print(color + ' ' + brightness)

    new_color = {
        'color': color,
        'brightness': brightness,
    }

    contents['colors_list'].append(new_color)
    with open('data.json', 'w') as f:
        f.write(json.dumps(contents, indent=4))

    return redirect('/')

with open('data.json', 'r') as f:
    contents = json.load(f)



app.run(debug=True)