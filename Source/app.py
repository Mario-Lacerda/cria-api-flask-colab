from flask import Flask
from developers import developers

app = Flask(__name__)
app.register_blueprint(developers)

@app.route('/')
def index():
    return 'Index Page'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
