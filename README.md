# Cyber Incident Response and Reporting Platform

A comprehensive web application designed to empower individuals and communities to understand, report, and respond effectively to cyber and physical security incidents. This platform integrates a user-friendly interface, a machine learning model, educational resources, and real-time analytics to provide a holistic incident management system.

## Key Features

-   **Incident Analysis:**
    -   Allows users to input incident descriptions for automated analysis.
    -   Utilizes a machine learning model to predict the type of cyberattack.
    -   Provides tailored guidance based on the predicted attack type.
-   **Incident Reporting:**
    -   Offers a detailed form for reporting incidents, with options for anonymous or detailed reports.
    -   Collects structured data such as location, date, and incident description.
-   **Cyber Awareness and Education:**
    -   A dedicated "Learn" page with resources about crime reporting, different types of crimes, and user rights.
    -   Includes a carousel of cyber awareness videos to help in educating the users.
-   **Real-time Analytics:**
    -   Displays dynamic cybercrime statistics and trends through interactive charts and tables.
    -    Provides insights into the distribution of crimes geographically.
-   **Post-Attack Guidance:**
    -   Provides specific post-attack steps and recommendations.
    -   Offers contact details for relevant helplines and support organizations.
-   **Team and Project Information:**
    -   An "About Us" page provides background information on the project's mission, vision, and team members.
    -   A "Contact Us" page provides necessary information for people who want to reach out to the organization.

## Tech Stack

-   **Frontend:**
    -   HTML: For structuring web content.
    -   CSS: For styling and layout, using Bootstrap for responsiveness.
    -   JavaScript: For dynamic behavior and interactivity of the webpage, along with using libraries such as Chart.js and Leaflet.js.
-   **Backend:**
    -   Python: The primary programming language.
    -   Flask: A micro web framework for creating the web application.
-   **Machine Learning & Data:**
    -   scikit-learn: For text classification and machine learning model development.
    -   pandas: For handling and manipulating tabular data and for reading csv files.
    -   joblib: For saving and loading the trained machine learning model.
-   **Charting & Mapping:**
    -    Chart.js: For creating various types of interactive charts.
    -    Leaflet.js: For creating interactive maps to show cyber crime data.

## Setup Instructions

1.  **Navigate to the Project Directory:**
    ```bash    cd <your_project_directory>    ```
2.  **Clone the Repository:**
    ```bash    git clone https://github.com/Maheshannayboeina/Cyber-Incident-Response.git    ```
3.  **Create a Virtual Environment and Activate It:**
    ```bash    python -m venv venv    source venv/bin/activate  # On macOS/Linux    venv\Scripts\activate      # On Windows    ```
4.  **Install the Required Dependencies:**
    ```bash    pip install -r requirements.txt    ```
5.  **Run the Flask App:**
    ```bash    python app.py    ```
6.  **Access the Website:** Open your web browser and go to `http://127.0.0.1:5000` to view the application.

## Usage

1.  **Incident Analysis:** On the home page, enter a description of a cyber incident in the text box and submit it. The system will predict the attack type and provide guidance.
2.  **Incident Reporting:** Go to the "Report" page to submit a new report. You can choose to submit it anonymously or with your details.
3.   **Cyber Awareness:** Visit the "Learn" page for insights into different types of crimes, reporting rights, and safety tips, and watch the cyber awareness videos.
4.  **View Analytics:** Check the "Analytics" page for real-time cyber crime data visualized using charts and tables.

**Note:** The analytics page currently uses dummy data. To connect to your actual data source, replace the dummy data generation logic in `app.py` with the appropriate data-fetching and aggregation logic.

## Contributing

Contributions are highly encouraged! If you have ideas for improvements, new features, or find any bugs, please open an issue or submit a pull request. Please make sure to test your changes thoroughly before submitting them.

## Disclaimer

This website is intended to provide information and guidance on cyber security incidents. While we strive to provide accurate and up-to-date information, this application should not be considered a substitute for professional advice or incident response services. The analysis and guidance provided are based on the capabilities of the machine learning model and the data available, and should not be taken as a legal or definitive judgment about the nature or cause of a specific incident. For any security or legal related concerns, seek professional advice.

## License

(license information will be added soon..)