from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
LINKS_FILE = 'links.json'

def carregar_links():
    if not os.path.exists(LINKS_FILE):
        return []
    with open(LINKS_FILE, 'r') as f:
        return json.load(f)

def salvar_links(links):
    with open(LINKS_FILE, 'w') as f:
        json.dump(links, f, indent=4)

@app.route('/')
def index():
    links = carregar_links()
    return render_template('index.html', links=links)

@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        nome = request.form['nome']
        url = request.form['url']
        links = carregar_links()
        links.append({'nome': nome, 'url': url})
        salvar_links(links)
        return redirect(url_for('index'))
    return render_template('setup.html')

if __name__ == '__main__':
    app.run(debug=True)
