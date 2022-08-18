from flask import Flask, render_template, request, redirect
import json
app = Flask('__name__')

# you can use a conditional to handle form submission in the same view as you render the page

# @app.route('/', methods=['GET','POST'])
# def index():
#     # if the request made by your browser is a "post" request, grab the information from the form and save it to variables
#     if request.method == 'POST':
#         # in the following lines we're grabbing keys from the request.form dictionary
#         # those keys are set with the "name" attribute in the html form
#         color = request.form['color']
#         brightness = request.form['brightness']
#         # here we print the form data to show it's being received
#         print(color + ' ' + brightness)
#         # after handling the form data, we redirect to the main page
#         return redirect('/')
#     # if the request is not a "post" request, just render the page
#     return render_template('index.html')

# you can also split the rendering and form handling into separate views with separate paths
# this function just renders the page like normal
@app.route('/')
def index():
    return render_template('index.html', contents=contents)

# this function handles the form submission only
@app.route('/submit-form/', methods=['POST'])
def submit_form():
    color = request.form['color']
    brightness = request.form['brightness']
    print(color + ' ' + brightness)
    # here we're adding a new color dictionary, which we then append to our list of colors in the contents dictionary
    new_color = {
        'color': color,
        'brightness': brightness,
    }
    contents['colors_list'].append(new_color)
    # then we write the contents back to the json file
    with open('data.json', 'w') as f:
        f.write(json.dumps(contents, indent=4))
    # finally, we redirect to a different page - in this case it's the index (via the '/' path) where the form is
    return redirect('/')

# we're saving data externally in a json file, so the first thing we need to do after declaring our functions is load that data and save it to a variable
with open('data.json', 'r') as f:
    contents = json.load(f)

# as always, we have to tell the app to run itself at the end of the file
app.run(debug=True)