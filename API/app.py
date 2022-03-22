from crypt import methods
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    example_embed='This string is from python'
    return render_template('index.html', embed=example_embed)

@app.route('/coordinates', methods=['GET'])
def get_coordinates():
    coordinates = {
        'x':50, 
        'y':50
        }
    return jsonify(coordinates)

app.run(debug=True)