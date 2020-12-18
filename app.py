from flask import Flask, render_template, request, send_file

from barcode import create_barcodes

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

        create_barcodes(barcode)
        return send_file(barcode + '.pdf', as_attachment=True)


if __name__ == '__main__':
    app.run()
