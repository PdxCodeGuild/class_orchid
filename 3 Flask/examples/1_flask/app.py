# import Flask and any necessary components
from flask import Flask, render_template
# instantiate a Flask object and assign it to the "app" variable
app = Flask(__name__)

# @app.route('/path/') tells Flask to run this function when /path/ is requested by your browser
@app.route('/')
def index():
    # variables can be assigned and later passed to the template renderer where they will be replaced with their values
    name = 'Cesar'
    location = 'Tampa'
    fav_color = 'green'
    fav_num = 18
    important_nums = [73, 29, 12]
    
    # this could be a dictionary instead - if a dictionary is used, this syntax is used on your template: {{ dictionary_name.key_name }}
    # contents = {
    #     'name': 'Cesar',
    #     'location': 'Tampa',
    #     'fav_color': 'green',
    #     'fav_num': 18,
    #     'important_nums': [73, 29, 12]
    # }

    # call the render_template method and pass it arguments
    # the first argument is the filename of your template file as a string, in this case 'index.html'
    # remaining arguments in this example are all data that are passed to the renderer
    return render_template('index.html', name1=name, location=location, fav_color=fav_color, fav_num=fav_num, nums=important_nums)
    
    # if the commented-out dictionary was used, this is what the return would look like:
    # return render_template('index.html',contents=contents)

# you can map as many routes/paths as you want by adding new functions preceded by the @app.route('/path/') decorator
@app.route('/aboutme/')
def about_me():
    # you can return something without a template, but nothing else (not even an <html> tag) will be rendered in your browser
    # returning information this way results in a plain page with text
    return 'My name is Matt and I am a TA for Class Orchid.'

# paths can be dynamic - in this case a string is passed
@app.route('/student/<string:student_name>')
# Flask takes that string as an argument for the function
def student_page(student_name):
    return f'{student_name.title()} is a student in Class Orchid.'

# ints can also be used in a path
@app.route('/post/<int:post_id>')
def post(post_id):
    # any variable within the scope of the function can be manipulated like you would with any other Python file
    post_id += 1000
    return f'This is post number {post_id}!'

# at the end of your app.py file, you have to run the app
# debug mode is enabled for verbose error messages - this should be turned off in a production environment
app.run(debug=True)