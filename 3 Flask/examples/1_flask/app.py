from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = 'Cesar'
    location = 'Tampa'
    fav_color = 'green'
    fav_num = 18
    important_nums = [73, 29, 12]
    return render_template('index.html', name1=name, location=location, fav_color=fav_color, fav_num=fav_num, nums=important_nums)

@app.route('/aboutme/')
def about_me():
    return 'My name is Matt and I am a TA for Class Orchid.'

@app.route('/student/<string:student_name>')
def student_page(student_name):
    return f'{student_name.title()} is a student in Class Orchid.'

@app.route('/post/<int:post_id>')
def post(post_id):
    post_id += 1000
    return f'This is post number {post_id}!'

app.run(debug=True)