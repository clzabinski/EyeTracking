from crypt import methods
import json
from flask import Flask, jsonify, request, render_template, after_this_request
app = Flask(__name__)

@app.route('/')
def home_page():
    example_embed='This string is from python'
    return render_template('index.html', embed=example_embed)

@app.route('/coordinates', methods=['GET'])
def get_coordinates():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
    jsonResp = {
        'x':50, 
        'y':50
        }
    print(jsonResp)
    return jsonify(jsonResp)

if __name__ == '__main__':
    app.run(debug=True)