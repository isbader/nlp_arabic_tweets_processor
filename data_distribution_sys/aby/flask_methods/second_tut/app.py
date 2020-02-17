from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')

def index():
    name = request.args.get('name','world')
    return render_template('index.html',name=name)

@app.route('/register',methods=['POST'])
def register():
    name = request.form.get('name')
    student_id = request.form.get('student_id')
    tweet_num = request.form.get('tweet_num')

    if not name or not student_id:
        return 'failed'
    render_template('success.html')


