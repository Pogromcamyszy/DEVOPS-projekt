from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route 
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the app on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)