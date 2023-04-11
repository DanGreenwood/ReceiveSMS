from flask import Flask, request

app = Flask(__name__)

@app.route('/json', methods=['POST'])
def handle_request():
    if request.headers['Content-Type'] == 'application/json':
        json_data = request.json
        print(json_data)
        return 'JSON posted'
    else:
        return 'Unsupported Media Type', 415

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
