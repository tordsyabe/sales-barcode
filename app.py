from flask import Flask, render_template, request, send_file, request, jsonify

from barcode import create_barcodes
from name_tag import create_name_tag

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def generate():
    if request.method == 'POST':
        barcode = request.form['barcode']
        if barcode == '':
            return render_template('index.html', message='Please enter required fields')

        stripped_barcode = barcode.strip()

        create_barcodes(stripped_barcode)
        return send_file(stripped_barcode + '.pdf', as_attachment=True)


@app.route('/name-tag', methods=['POST'])
def name_tag():
    content = request.json
    print(content['name'])
    print(content['position'])
    create_name_tag(content['name'], content['position'])

    return jsonify({"uuid": "hello"})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.debug(True)
