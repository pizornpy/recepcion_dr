from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def receive_webhook():
    data = request.json  # Assuming the request payload is in JSON format
    # Process the data as needed
    print("Received POST request:", data)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)

