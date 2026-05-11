import pickle

# The Pickle Class Fix: Define the logic structure
class DeliveryModel:
    def predict(self, distance, weight):
        # Time = 0.5 + (Distance * 0.2) + (Weight * 0.1)
        return 0.5 + (distance * 0.2) + (weight * 0.1)

# 1. Create an instance of the model
model = DeliveryModel()

# 2. Save (pickle) the model into a file
filename = 'delivery_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(model, file)

print(f"Success! {filename} has been created.")