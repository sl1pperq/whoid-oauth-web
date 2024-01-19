from flask import *
import uuid

app = Flask(__name__)

@app.route('/')
def main_page():
    token = str(uuid.uuid4())
    return render_template('main.html', token=token)

@app.route('/log')
def log_page():
    status = request.args.get('status')
    mail = request.args.get('mail')
    if status == 'Success':
        return render_template('welcome.html')
    else:
        token = str(uuid.uuid4())
        return render_template('error.html', token=token)

app.run(port=5000)