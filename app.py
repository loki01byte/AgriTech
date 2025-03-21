from flask import Flask
from flask import redirect,render_template,request

app=Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')

@app.route('/crop-info')
def cropinfo():
    return render_template('crop-info.html')

@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/forum')
def forum():
    return render_template('forum.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__=='__main__':
    app.run(debug=True)