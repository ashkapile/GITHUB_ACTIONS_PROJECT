from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Optional: API route
@app.route('/api/hello')
def hello_api():
    return {'message': 'Hello from Flask!'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
