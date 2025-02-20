from flask import Flask, render_template, jsonify, redirect, url_for
import random

app = Flask(__name__)

ttrpg_quotes = [
    "The dice are cast, and fate unfolds.",
    "In the dungeon's depths, heroes are forged.",
    "Roll for initiative—adventure awaits!"
]

@app.route('/')
def home():
    quote = random.choice(ttrpg_quotes)
    return render_template('index.html', quote=quote)

@app.route('/ttrpg')
def ttrpg_page():
    # Redirect to your FoundryVTT server
    return redirect('https://ttrpg.devopsfables.net', code=302)

@app.route('/roll/<int:sides>', methods=['GET'])
def roll_die(sides):
    result = random.randint(1, sides)
    return jsonify({'result': result, 'sides': sides})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)