import pickle

print("Trying to load model...")

try:
    with open("artifacts/bangalore_home_prices_model.pickle", "rb") as f:
        model = pickle.load(f)
    print("✅ Model loaded successfully!")
except Exception as e:
    print("❌ Error loading model:")
    print(e)
