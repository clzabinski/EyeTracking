from crypt import methods
import json
from flask import Flask, jsonify, request, render_template, after_this_request
app = Flask(__name__)

middle_point = None

@app.route('/')
def home_page():
    example_embed='This string is from python'
    return render_template('index.html', embed=example_embed)

@app.route('/coordinates', methods=['GET'])
def get_coordinates():
    # @after_this_request
    # def add_header(response):
    #     response.headers.add('Access-Control-Allow-Origin', '*')
    #     return response
    if middle_point:
        jsonResp = {
            'x': middle_point[0], 
            'y':middle_point[1]
            }
    else:
        jsonResp = {
            'Error': "No middlepoint found!"
        }

    print(jsonResp)
    return jsonify(jsonResp)

def pass_coordinates(middle_coords):
    middle_point = middle_coords

if __name__ == '__main__':
    app.run(debug=True)