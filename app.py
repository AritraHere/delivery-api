import pickle
from flask import Flask, request, jsonify
import os

# CRITICAL: The class MUST be defined in the same file where you load the pickle
class DeliveryModel:
    def predict(self, distance, weight):
        return 0.5 + (distance * 0.2) + (weight * 0.1)

app = Flask(__name__)

# Load the model
MODEL_PATH = 'delivery_model.pkl'

# Check if file exists to avoid crash
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
else:
    # Fallback in case the file didn't upload
    model = DeliveryModel()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    dist = data.get('distance')
    wgt = data.get('weight')
    
    if dist is None or wgt is None:
        return jsonify({"error": "Missing data"}), 400
        
    prediction = model.predict(float(dist), float(wgt))
    return jsonify({"estimated_delivery_time_hours": round(prediction, 2)})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
