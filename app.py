
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Vercel!"
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/periode1')
def periode1():
    return render_template('periode1.html', 
                         title="L'hégémonie imposée (1945-1960)")

@app.route('/periode2') 
def periode2():
    return render_template('periode2.html',
                         title="L'hégémonie autoritaire (1960-1987)")

@app.route('/periode3')
def periode3():
    return render_template('periode3.html',
                         title="L'hégémonie démocratique (1987-2000)")

@app.route('/periode4')
def periode4():
    return render_template('periode4.html',
                         title="L'hégémonie négociée (2000-2020)")

@app.route('/ressources')
def ressources():
    return render_template('ressources.html',
                         title="Sources et ressources")

if __name__ == '__main__':
    app.run(debug=True)