
# Canvas AI Backend

Canvas AI Backend is a FastAPI application designed to process images with mathematical expressions, leveraging artificial intelligence to generate solutions and insights.

## Table of Contents
- [Technologies](#technologies)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Deployment](#deployment)
- [Contributing](#contributing)


## Technologies
This project utilizes the following technologies:
- **FastAPI**: A modern web framework for building APIs with Python.
- **Pillow**: A Python Imaging Library (PIL) fork for image processing.
- **Google Generative AI**: For AI-driven content generation and analysis.
- **Uvicorn**: A lightning-fast ASGI server for serving FastAPI applications.

## Features
- Image processing for mathematical expressions and graphical problems.
- Integration with Google Generative AI to analyze images and return solutions.
- RESTful API endpoints for easy interaction with frontend applications.
- CORS support for cross-origin requests.

## Installation
To get started with the Canvas AI backend application, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/karthikrk0180/canvas-ai-backend.git
   cd canvas-ai-backend
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the application locally, use the following command:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
Open your browser and navigate to `http://localhost:8000` to view the API documentation (Swagger UI).

## API Endpoints

### Health Check
- **GET /**  
  - Response: 
    ```json
    {
      "message": "server is running"
    }
    ```

## Deployment
The application can be deployed on platforms like Render. Ensure that all necessary environment variables are configured correctly in the deployment settings.

1. To deploy, simply push your code to your chosen platform, following their specific deployment instructions.

2. Note: I pushed to Render.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or create an issue for any bugs or enhancements.


Feel free to modify any section as needed!
