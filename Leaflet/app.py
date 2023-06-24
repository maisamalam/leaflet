from flask import Flask, render_template, jsonify
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    # Renders the index.html template when the root URL is accessed
    return render_template('index.html')

@app.route('/part1')
def part1():
    # This function gets called when the Part 1 button is clicked
    # Replace the return statement with your code
    return jsonify({'message': 'Part 1 button clicked'})

@app.route('/logic.js', methods=['GET'])
def serve_logic():
    # This function is called when '/logic.js' is accessed,
    # and sends the file 'logic.js' from the directory 'static/js'
    return send_from_directory('static/js', 'logic.js')

@app.route('/logic_2.js', methods=['GET', 'POST'])
def serve_logic_2():
    # This function is called when '/logic_2.js' is accessed,
    # and sends the file 'logic_2.js' from the directory 'static/js'
    return render_template('part2.html')

if __name__ == "__main__":
    app.run(debug=True)
    