from flask import Flask, request, jsonify
import pickle
import os

# 1. The Pickle Class Fix: Define the structure so Pickle can reconstruct it
class DeliveryModel:
    def predict(self, distance, weight):
        # Time = 0.5 + (Distance * 0.2) + (Weight * 0.1)
        return 0.5 + (distance * 0.2) + (weight * 0.1)

app = Flask(__name__)

# 2. Load the model from the .pkl file
MODEL_PATH = 'delivery_model.pkl'
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from JSON request
        data = request.get_json()
        
        # Extract values
        dist = data.get('distance')
        wgt = data.get('weight')
        
        # Validation
        if dist is None or wgt is None:
            return jsonify({"error": "Please provide both distance and weight"}), 400
        
        # Calculate prediction
        prediction = model.predict(dist, wgt)
        
        return jsonify({
            "distance": dist,
            "weight": wgt,
            "estimated_delivery_time_hours": round(prediction, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Use port assigned by Render or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)