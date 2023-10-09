from flask import Flask, request, jsonify

app = Flask(__name__)

correct_date = "29/03/2023"

@app.route('/')
def index():
    return open("index.html").read()

@app.route('/verificar_data', methods=['POST'])
def verificar_data():
    data_input = request.form['data']
    if data_input == correct_date:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

if __name__ == '__main__':
    app.run()