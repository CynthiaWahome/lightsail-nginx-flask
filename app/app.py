from flask import Flask, render_template_string
from datetime import datetime

app = Flask("app")

def gethtml():
    html_content = '''
    <html>
        <body>
            <h1>Hey there! I'm a Python Flask web app!</h1>
            <div>Current time: {{ current_time }}</div>
            <div>🎉Surprise!🎉 You just got served🛎... by an Nginx reverse proxy🔀, not the Flask app directly😁</div>
        </body>
    </html>
    '''
    return render_template_string(html_content, current_time=datetime.now())

@app.route("/")
def index():
    return gethtml()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)