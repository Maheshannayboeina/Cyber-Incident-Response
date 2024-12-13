# Cyber Incident Response Website

This is a website built using Flask and Machine Learning, designed to help users identify the type of cyber incident they are facing and provide recommendations for post-attack actions and relevant helpline information.

## Features

- **Incident Reporting:** A user-friendly form where individuals can describe their cyber incident.
- **Automated Analysis:** Uses a machine learning model to predict the type of attack.
- **Post-Attack Steps:** Provides a list of recommended actions to take after an incident.
- **Helpline Information:** Displays contact details for relevant authorities and support organizations.
- **About Us** Page with project details.
- **Contact** Page with contact form
- **Analytics** page that will contain details about incidents reported.

## Tech Stack

-   **Frontend:** HTML, CSS, JavaScript, Bootstrap
-   **Backend:** Python, Flask
-   **Machine Learning:** scikit-learn (for text classification), gensim (for word embeddings)
-   **Text Preprocessing:** NLTK or SpaCy for text pre-processing
-   **Database:** (Optional, but you can add one to store data for analysis)

## Setup Instructions

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2.  Navigate to the project directory:
    ```bash
    cd incident_response_site
    ```
3.  Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate      # On Windows
    ```
4.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5.  Run the Flask app:
    ```bash
    python app.py
    ```
6. Access the website on http://127.0.0.1:5000

## Usage

-   Navigate to the website's homepage.
-   Enter a description of your cyber incident in the text area.
-   Click "Analyze Incident" to submit the description.
-   Review the results, which will display the predicted attack type, related information, and steps for post-attack actions.

## Contributing

We welcome contributions! If you have ideas for new features or find bugs, please open an issue or submit a pull request.

## Disclaimer

This website provides analysis for informational purposes only. It should not be considered a substitute for professional incident response services.

## License

(license information will be added soon..)
