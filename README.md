# Location-Based Redirect Service

This project is a simple Flask web service that displays a message to users, attempts to retrieve their location, and redirects them to a specified URL. If location permissions are denied, it still redirects the user to the URL.

The project is designed to be deployed on Google Cloud Run, making it easily accessible and scalable.

## Features

- Displays a message ("Mira lo que salió en las noticias...") to users upon visiting the page.
- Attempts to obtain the user's latitude and longitude.
- Sends location data to the Flask backend.
- Redirects users to [Debate.com.mx](https://www.debate.com.mx/) regardless of location access permissions.

## Prerequisites

- Python 3.8 or higher
- Google Cloud SDK
- A Google Cloud project with billing enabled
- Flask and Gunicorn (for production deployment)

## Setup

1. Clone the repository and navigate to the project directory:

    ```bash
    git clone https://github.com/yourusername/location-redirect-service.git
    cd location-redirect-service
    ```

2. Install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the Flask development server:

    ```bash
    flask run
    ```

   By default, this will run on `http://127.0.0.1:80`. Open this URL in your browser to test locally.

## Project Structure

```plaintext
.
├── app.py               # Main Flask application file
├── templates
│   └── index.html       # HTML file containing the front-end script and layout
├── requirements.txt     # Python dependencies for the project
└── Dockerfile           # Dockerfile for deploying to Google Cloud Run
