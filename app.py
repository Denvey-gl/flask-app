from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)


@app.route('/')
@app.route('/tovar')
def tovar():
    return render_template('tovar.html')

@app.route('/izbr')
def izbr():
    return render_template('izbr.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/friend')
def friend():
    return render_template('friend.html')

@app.route('/tovar/<int:tovar_id>')
def tovar_detail(tovar_id):
    return render_template('tovar_detail.html',tovar_id=tovar_id)

