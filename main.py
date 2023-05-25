from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/game_info')
def game_info():
    return render_template('game_info.html')

@app.route('/characters')
def characters():
    return render_template('characters.html')

@app.route('/characters/kumira')
def kumira():
    return render_template('/Characters/kumira.html')

@app.route('/weapon_skills')
def weapon_skills():
    return render_template('weapon_skills.html')

@app.route('/passive_skills')
def passive_skills():
    return render_template('passive_skills.html')

@app.route('/stages')
def stages():
    return render_template('stages.html')

if __name__ == '__main__':
    app.run(debug=True)