from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello YOU</h1>'
@app.route('/hi')
def hell():
    return '<h1>BYE</h1>'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
