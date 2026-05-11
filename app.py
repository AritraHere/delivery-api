import pickle
from flask import Flask, request, jsonify
import os
import sys

# --- THE PICKLE FIX ---
# 1. Define the class exactly as it was in train.py
class DeliveryModel:
    def predict(self, distance, weight):
        # Time = 0.5 + (Distance * 0.2) + (Weight * 0.1)
        return 0.5 + (distance * 0.2) + (weight * 0.1)

# 2. Tell Python that 'train.DeliveryModel' is the same as this local class
# This prevents the AttributeError: module '__main__' has no attribute 'DeliveryModel'
import __main__
__main__.DeliveryModel = DeliveryModel

app = Flask(__name__)

# --- MODEL LOADING ---
MODEL_PATH = 'delivery_model.pkl'

# Try to load the saved model, otherwise use a fresh instance
if os.path.exists(MODEL_PATH):
    try:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
    except Exception:
        model = DeliveryModel()
else:
    model = DeliveryModel()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        
        # Convert inputs to floats to be safe
        dist = float(data.get('distance', 0))
        wgt = float(data.get('weight', 0))
        
        prediction = model.predict(dist, wgt)
        
        return jsonify({
            "distance": dist,
            "weight": wgt,
            "estimated_delivery_time_hours": round(prediction, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "Delivery API is Live! Use /predict for estimations."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
