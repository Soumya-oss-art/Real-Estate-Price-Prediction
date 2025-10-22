from flask import Flask, request, jsonify, send_from_directory
import util
import os

# Create Flask app first
app = Flask(__name__)

# Serve frontend
@app.route('/')
def serve_homepage():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    return send_from_directory(os.path.join(base_dir, 'UI'), 'app.html')

# --- Route 1: Get all location names ---
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# --- Route 2: Predict home price ---
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
    except (KeyError, ValueError):
        return jsonify({'error': 'Invalid input data'}), 400

    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    response = jsonify({
        'estimated_price': estimated_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
