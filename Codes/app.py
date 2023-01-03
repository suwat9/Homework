# an object of WSGI application
from flask import Flask	
app = Flask(__name__) # Flask constructor

# A decorator used to tell the application
# which URL is associated function
@app.route('/')	
def hello():
	return 'Mr.Suwat Tachaphetpibon'

@app.route('/address')
def address():
    return 'Phetchaburi Province'

@app.route('/university')
def university():
    return 'Phetchaburi Rajabhat University'

@app.route('/student')
def student():
    return '6542-72001 Suwat Tachaphetpiboon'

if __name__=='__main__':
    app.run()
