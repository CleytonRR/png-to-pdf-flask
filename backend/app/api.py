from flask import Flask, request
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = os.path.abspath("")
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/v1/image/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'image' not in request.files:
            response = {"Error": 'Erro1'}
            return response, 400
        file = request.files['image']
        if file.filename == '':
            response = {"Error": 'Erro2'}
            return response, 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return {'Message': 'Tudo okay'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')