from flask import Flask, request
import pandas as pd

app = Flask(__name__)

df = pd.DataFrame()

@app.route('/json', methods=['POST'])
def handle_request():
    if request.headers['Content-Type'] == 'application/json':
        json_data = request.json
        print(json_data)
        # Use json_normalize() to convert the JSON data to a dataframe
        new_data = pd.json_normalize(json_data)

        # Append the new data to the existing dataframe
        global df
        df = df.append(new_data, ignore_index=True)
        print(df)
        return 'JSON posted'
    else:
        return 'Unsupported Media Type', 415

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
