from flask import Flask, request, render_template
import logging
import os
from models.model import load_model, train_model
from utils.attack_details import attack_details


app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


# Load the model
model = load_model()
if not model:
     logging.info('Starting model training ...')
     model = train_model() # if loading the model fails, train a new model

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
     return render_template('contact.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return render_template('predict.html', error="Model not available.")

    if 'description' not in request.form or not request.form['description']:
         return render_template('predict.html', error="Please provide a description")

    description = request.form['description']
    try:
        prediction = model.predict([description])[0]
    except Exception as e:
         logging.error(f"Model prediction error: {e}")
         return render_template('predict.html', error="Prediction Error.")

    # Normalize the prediction to match the dictionary keys
    normalized_prediction = prediction.strip().lower()
    details = attack_details.get(normalized_prediction, {
        "info": "Information not available.",
        "post_attack_steps": ["N/A"],
        "helplines": {"N/A": "N/A"}
    })

    return render_template('predict.html',
                           prediction=prediction,
                           info=details['info'],
                           steps=details['post_attack_steps'],
                           helplines=details['helplines'])

@app.errorhandler(500)
def internal_error(error):
    logging.error(f"Internal server error: {error}")
    return render_template('error.html', error="An unexpected error occurred."), 500

if __name__ == '__main__':
    app.run(debug=True)