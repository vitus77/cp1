import flask, ocr
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        file = request.files['file']
        file.save("./static/" + secure_filename('test.jpg'))

    result = ocr.plate()
    return render_template('index.html', result = result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 5432)