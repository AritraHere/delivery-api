# delivery-api
# Eco-Formula Delivery Estimator

A lightweight Flask API that predicts delivery times for bike couriers based on distance and package weight. This project utilizes a custom "Eco-Formula" to ensure couriers are not overworked by providing realistic delivery estimates.

## 🔗 Live Deployment
**Base URL:** `https://delivery-api-go4n.onrender.com`  
*Note: The root URL displays a status message. Use the `/predict` endpoint for calculations.*

---

## Formula
The system calculates delivery time (in hours) using the following linear equation:

$$Time = 0.5 + (Distance \times 0.2) + (Weight \times 0.1)$$

- **Base Time:** 0.5 hours (Buffer for pickup/drop-off)
- **Distance:** 0.2 hours per kilometer/unit
- **Weight:** 0.1 hours per kilogram/unit

---

## Tech Stack
- **Language:** Python 3.x
- **Framework:** Flask (Serving)
- **Serialization:** Pickle (Model Storage)
- **Deployment:** Render (PaaS)
- **Production Server:** Gunicorn
