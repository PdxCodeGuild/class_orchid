from flask import Flask, render_template, redirect, request
import json
app = Flask('__name__')

@app.route('/')
def index():
    name = contents.get('name')
    age = contents.get('age')
    location = contents.get('location')
    quote = contents.get('quote')
    places_lived = contents.get('places_lived')
    occupation = contents.get('occupation')
    photos = contents.get('photos')
    bio = contents.get('bio')
    return render_template('index.html',name=name,age=age,location=location,quote=quote,places_lived=places_lived,occupation=occupation,photos=photos,bio=bio)

@app.route('/submit-form/', methods=['POST'])
def submit_form():
    place = request.form['place']
    contents['places_lived'].append(place)
    with open('data.json','w') as f:
        f.write(json.dumps(contents,indent=4))
    return redirect('/')

with open('data.json','r') as f:
    contents = json.load(f)

app.run(debug=True)