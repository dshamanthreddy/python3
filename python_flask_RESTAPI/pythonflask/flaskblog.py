
from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
	{
		'author' : 'shamanth',
		'title' : 'boddjdjd',
		'content' : 'first post',         
		'date'	: 'December 20,2019'
	},
	{
		'author' : '11shamanth',
		'title' : 'bol111gpost',
		'content' : 'firs11t post',  
		'date'	: 'December 19,2019'
	},
	
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',r=posts)

@app.route("/about")
def about():
    return render_template('about.html',title = 'about')


if __name__ == '__main__':
    app.run(debug=True)
