from flask import Flask, render_template

from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    return str(search4letters('life, universe and everything', 'eiru,l'))    

@app.route('/entry')
def entry_page():
    return render_template('entry.html', 
                           the_title='Welcome to search4letter on the web!')

app.run(debug=True)