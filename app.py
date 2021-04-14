from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api/apa/getFirst', methods=['GET'])
def get_first():
    test = "First_get"
    return test

@app.route('/api/apa/getSecond', methods=['GET'])
def get_second():
    test = "second_get"
    return test

@app.route('/api/apa/', methods=['POST'])
def post():     
    
    test = request.form['0']
    print(test)

    return jsonify(test)
    

if __name__ == "__main__":
    app.run(debug=False)
