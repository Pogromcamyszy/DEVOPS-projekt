from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a routes for application
@app.route('/')
def hello_world():
    return 'Hello, World!'

# added rout for testing python CI 
@app.route('/python')
def python():
    return 'Python CI is very cool'

#added rout for testin docker CI
@app.route('/docker')
def docker():
    return 'Docker Ci is super cool'

#last update testing CD process
@app.route('/deploy')
def deploy():
   return 'I hope i will get 5 for this funny project'

# Run the app on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)