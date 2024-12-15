# Cyber Incident Response and Reporting Platform

A comprehensive web application designed to empower individuals and communities by enabling them to effectively understand, report, and respond to both cyber and physical security incidents. The platform features a user-friendly interface, an advanced machine learning model, educational resources, and real-time analytics, providing a holistic incident management system.

## Key Features

### **Incident Analysis:**
- **Incident Input:** Users can input descriptions of incidents for automated analysis.
- **Machine Learning Prediction:** Utilizes a machine learning model to predict the type of cyberattack based on the provided description.
- **Guidance:** Tailored recommendations and next steps are provided based on the predicted attack type.

### **Incident Reporting:**
- **Reporting Form:** Users can report incidents with detailed forms that allow for both anonymous and detailed submissions.
- **Structured Data:** Collects relevant data such as location, date, and a detailed description of the incident.

### **Cyber Awareness and Education:**
- **Learning Resources:** A dedicated "Learn" page provides valuable information on crime reporting, types of crimes, and user rights.
- **Awareness Videos:** Includes a carousel of educational videos focused on enhancing cyber awareness.

### **Real-time Analytics:**
- **Dynamic Statistics:** Visualizes cybercrime trends and statistics in real-time using interactive charts and tables.
- **Geographic Distribution:** Provides insights into the geographic distribution of cybercrimes through interactive maps.

### **Post-Attack Guidance:**
- **Actionable Steps:** Offers post-incident steps to mitigate further damage.
- **Helpline Contacts:** Provides contact information for relevant support organizations and helplines.

### **Team and Project Information:**
- **About Us Page:** Displays background information on the project’s mission, vision, and key team members.
- **Contact Us Page:** Includes contact details for users seeking further information or assistance.

## Tech Stack

### **Frontend:**
- **HTML & CSS:** For structuring and styling the web content. Bootstrap is used for responsiveness.
- **JavaScript:** For dynamic behavior and interactivity, along with libraries like Chart.js and Leaflet.js.

### **Backend:**
- **Python:** The main programming language for backend development.
- **Flask:** A lightweight web framework for building the application.

### **Machine Learning & Data Processing:**
- **scikit-learn:** For text classification and developing machine learning models.
- **pandas:** Used for handling and manipulating tabular data.
- **joblib:** For saving and loading machine learning models.

### **Charting & Mapping:**
- **Chart.js:** For creating interactive charts to visualize data.
- **Leaflet.js:** For embedding interactive maps to display crime distribution.

## Setup Instructions

1. **Navigate to the Project Directory:**
    ```bash
    cd <your_project_directory>
    ```

2. **Clone the Repository:**
    ```bash
    git clone https://github.com/Maheshannayboeina/Cyber-Incident-Response.git
    ```

3. **Create a Virtual Environment and Activate It:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
    ```

4. **Install Required Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask App:**
    ```bash
    python app.py
    ```

6. **Access the Website:** Open a browser and visit `http://127.0.0.1:5000` to view the app.

## Usage

1. **Incident Analysis:** On the homepage, input a cyber incident description in the text box. The system will predict the attack type and suggest steps based on the prediction.
2. **Incident Reporting:** Navigate to the "Report" page to submit a new report (anonymous or with your details).
3. **Cyber Awareness:** Visit the "Learn" page to explore crime types, user rights, and safety tips. Watch educational videos to stay informed.
4. **Analytics:** Visit the "Analytics" page to view real-time data visualizations of cybercrime trends.

**Note:** The Analytics page currently uses dummy data. To use real data, modify the `app.py` file to implement proper data-fetching and aggregation.

## Contributing

We welcome contributions! If you have ideas for enhancements, new features, or have found any bugs, please open an issue or submit a pull request. Ensure your changes are well-tested before submission.

## Disclaimer

This platform aims to provide information and guidance on cyber security incidents. Although we strive for accuracy, it should not be considered a substitute for professional advice or incident response services. The machine learning analysis and guidance are based on the available data and model capabilities, and should not be treated as definitive conclusions. For any legal or security-related concerns, always seek professional assistance.

## License

(license information will be added soon…)

---