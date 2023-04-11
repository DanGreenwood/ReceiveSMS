from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def receive_data():
    try:
        data = request.get_json(force=True)
        # Do something with the JSON data here
        print(data)
        return jsonify({'success': True}), 200
    except:
        # Handle JSON decoding errors here
        return jsonify({'error': 'JSON decoding error'}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)