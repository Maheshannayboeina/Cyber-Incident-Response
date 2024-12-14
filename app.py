from flask import Flask, request, render_template
import logging
import os
from models.model import load_model, train_model
from utils.attack_details import attack_details, load_attack_details # also import load_attack_details
import traceback

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


# Load the model
model = load_model()
if not model:
    logging.info('Starting model training ...')
    model = train_model()  # if loading the model fails, train a new model
    if not model: # stop the program if model training failed as well
      logging.error("Model could not be loaded or trained. Stopping.")
      exit()

# load attack_details
attack_details = load_attack_details()
if not attack_details: # Stop if attack details could not be loaded
      logging.error("Could not load attack details. Stopping.")
      exit()

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

@app.route('/learn')
def learn():
    return render_template('learn.html')


@app.route('/predict', methods=['POST'])
def predict():
    logging.info('predict endpoint called')
    if not model:
         logging.error("Model is not available. Check model loading error.")
         return render_template('predict.html', error="Model not available at the moment. Please try later")

    if 'description' not in request.form or not request.form['description']:
        logging.error(f'no description provided in form : {request.form}')
        return render_template('predict.html', error="Please provide a description")

    description = request.form['description']
    try:
        prediction = model.predict([description])[0]
        logging.info(f"Model prediction is: {prediction}")  # logging the prediction
    except Exception as e:
        logging.error(f"Model prediction error: {e}, traceback: {traceback.format_exc()}")
        return render_template('predict.html', error="Prediction Error.")


    # Normalize the prediction to match the dictionary keys
    normalized_prediction = prediction.strip().lower()

    # Normalize keys in attack_details dictionary
    normalized_attack_details = {key.strip().lower(): value for key, value in attack_details.items()}

    details = normalized_attack_details.get(normalized_prediction, {
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
    logging.error(f"Internal server error: {error}, traceback: {traceback.format_exc()}")
    return render_template('error.html', error="An unexpected error occurred."), 500


if __name__ == '__main__':
    app.run(debug=True)