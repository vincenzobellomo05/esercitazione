
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <title>La mia prima pagina web</title>
    </head>
    <body>
        <h1>Ciao, mondo!</h1>
        <p>Questa pagina è servita da Python.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
