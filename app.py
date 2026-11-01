from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the model from a .pkl file
try:
    model = joblib.load("place_model.pkl")
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            # Get form data
            gender = int(request.form.get("gender"))
            ssc_p = float(request.form.get("ssc_p"))
            ssc_b = int(request.form.get("ssc_b"))
            hsc_p = float(request.form.get("hsc_p"))
            hsc_b = int(request.form.get("hsc_b"))
            hsc_s = int(request.form.get("hsc_s"))
            degree_p = float(request.form.get("degree_p"))
            degree_t = int(request.form.get("degree_t"))
            workex = int(request.form.get("workex"))
            etest_p = float(request.form.get("etest_p"))
            specialisation = int(request.form.get("specialisation"))
            mba_p = float(request.form.get("mba_p"))

            # Prepare input data
            input_data = np.array([[gender, ssc_p, ssc_b, hsc_p, hsc_b, hsc_s, degree_p, degree_t, workex, etest_p, specialisation, mba_p]])

            # Make prediction
            prediction = model.predict(input_data)

            # Map prediction to result
            result = "Placed" if prediction[0] == 1 else "Not Placed"
        except Exception as e:
            result = f"Error: {str(e)}"
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)