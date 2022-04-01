import json
from flask import Flask, jsonify, request, render_template, after_this_request
app = Flask(__name__)

@app.route('/')
def home_page():
    example_embed='This string is from python'
    return render_template('index.html', embed=example_embed)

middle_point = [None, None]
@app.route('/coordinates', methods=['GET', 'POST'])
def coordinates():
    # @after_this_request
    # def add_header(response):
    #     response.headers.add('Access-Control-Allow-Origin', '*')
    #     return response
    if request.method == 'GET':
        if middle_point:
            jsonResp = {
                'x': middle_point[0], 
                'y': middle_point[1]
                }
        else:
            jsonResp = {
                'Error': "No middlepoint found!"
            }

        print(jsonResp)
        return jsonify(jsonResp)

    if request.method == 'POST':
        content = jsonify(request.form).json
        middle_point[0] = content['x']
        middle_point[1] = content['y']
        print(content)
        return "OK"

if __name__ == '__main__':
    app.run(debug=True)