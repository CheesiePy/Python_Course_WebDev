# main flask app

from flask import Flask
from flask import render_template # import render_template function - this is used to render html files

app = Flask(__name__, template_folder='templates') # create an instance of the Flask class

@app.route('/') # route decorator - this is used to define the route for the home page
def home(): # function to render the home page
    return render_template('home.html')

def main():
    app.run(debug=True) # run the app

main()