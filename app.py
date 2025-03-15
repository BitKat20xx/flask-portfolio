from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')  # New page
def projects():
    return render_template('projects.html')  # Make sure you create this file

if __name__ == '__main__':
    app.run(debug=True)
