import os

# Define project structure
folders = ["static", "templates"]
files = {
    "app.py": """from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
""",
    "templates/index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lance's Portfolio</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <h1>Lance's Portfolio</h1>
        <p>IT Student | Python Developer | OpenCV Enthusiast</p>
    </header>

    <section id="about">
        <h2>About Me</h2>
        <p>Hello! I'm Lance, an aspiring IT professional passionate about coding and technology.</p>
    </section>

    <section id="projects">
        <h2>Projects</h2>
        <ul>
            <li>OpenCV Object Detection</li>
            <li>MQTT Location Data Processing</li>
            <li>Flask Web App</li>
        </ul>
    </section>

    <section id="contact">
        <h2>Contact</h2>
        <p>Email: your.email@example.com</p>
        <p>GitHub: <a href="https://github.com/yourgithub" target="_blank">github.com/yourgithub</a></p>
    </section>
</body>
</html>
""",
    "static/style.css": """body {
    font-family: Arial, sans-serif;
    text-align: center;
    background-color: #f4f4f4;
    color: #333;
}

header {
    background: #007bff;
    color: white;
    padding: 20px;
}

section {
    margin: 20px;
    padding: 20px;
    background: white;
    border-radius: 10px;
}
""",
    "requirements.txt": "flask"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with content
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("✅ Flask portfolio project created successfully!")
print("👉 Now run: `pip install -r requirements.txt`")
print("👉 Then start the server: `python app.py`")
