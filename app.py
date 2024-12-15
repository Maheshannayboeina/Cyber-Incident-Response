from flask import Flask, request, render_template, jsonify
import logging
import os
from models.model import load_model, train_model
from utils.attack_details import attack_details, load_attack_details
import traceback
import random
from datetime import datetime, timedelta
from collections import defaultdict

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

# Function to generate dummy data for visualization (replace this with your actual database or data source logic)
def generate_dummy_reports(num_reports=100):
    states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
              "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
              "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
              "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
    attacks = list(attack_details.keys())
    reports = []
    for i in range(num_reports):
        report_date = datetime.now() - timedelta(days=random.randint(0, 30))
        reports.append({
            "date": report_date.strftime('%Y-%m-%d'),
            "attack_type": random.choice(attacks),
            "state": random.choice(states)
         })
    return reports
#API endpoint to get incident counts
@app.route('/api/incident-counts')
def get_incident_counts():
    # Replace this with your logic to fetch incident counts from your data source
    analysed_incidents = random.randint(100,500)
    reported_incidents = random.randint(500,1000)
    solved_incidents = random.randint(50, 100)

    return jsonify({
        'analysed_incidents': analysed_incidents,
        'reported_incidents': reported_incidents,
        'solved_incidents': solved_incidents
    })


# API endpoint for total reports
@app.route('/api/total-reports')
def get_total_reports():
    reports = generate_dummy_reports()
    total_reports = len(reports)
    return jsonify(total_reports)


# API endpoint for bar chart
@app.route('/api/attack-types-data')
def get_attack_types_data():
    reports = generate_dummy_reports()
    attack_counts = defaultdict(int)
    for report in reports:
        attack_counts[report['attack_type']] += 1
    return jsonify(dict(attack_counts))

# API endpoint for pie chart
@app.route('/api/incident-locations-data')
def get_incident_locations_data():
    reports = generate_dummy_reports()
    state_counts = defaultdict(int)
    for report in reports:
        state_counts[report['state']] += 1
    return jsonify(dict(state_counts))


# API endpoint for time series chart
@app.route('/api/time-series-data')
def get_time_series_data():
    reports = generate_dummy_reports()
    date_counts = defaultdict(int)
    for report in reports:
        date_counts[report['date']] += 1

    # Convert date counts to a sorted list
    sorted_dates = sorted(date_counts.items(), key=lambda item: item[0])

    # Return list of data
    return jsonify(sorted_dates)

# API endpoint for Stacked Bar Chart
@app.route('/api/stacked-bar-data')
def get_stacked_bar_data():
     reports = generate_dummy_reports()
     location_attacks = defaultdict(lambda: defaultdict(int))
     for report in reports:
         location_attacks[report['state']][report['attack_type']] += 1
     return jsonify(dict(location_attacks))

# API endpoint for recent reports
@app.route('/api/recent-reports')
def get_recent_reports():
    reports = generate_dummy_reports()
    recent_reports = sorted(reports, key=lambda x: x['date'], reverse=True)[:10]
    # Anonymize the state before passing
    for report in recent_reports:
      report['state'] = report['state'][:3] + '...'
    return jsonify(recent_reports)


@app.errorhandler(500)
def internal_error(error):
    logging.error(f"Internal server error: {error}, traceback: {traceback.format_exc()}")
    return render_template('error.html', error="An unexpected error occurred."), 500


if __name__ == '__main__':
    app.run(debug=True)