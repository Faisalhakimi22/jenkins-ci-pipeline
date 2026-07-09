# Jenkins CI/CD Pipeline Demo

**What this demonstrates:** a working Jenkins pipeline (checkout → install → build → test → coverage report) wired up end-to-end against a real Flask app. The app itself (a calculator REST API) is intentionally minimal — it's the pipeline configuration, not the API, that's the point of this repo.

## Project Overview

This project demonstrates a complete CI/CD setup using Jenkins: automated checkout, dependency install, build verification, unit testing with pytest, and coverage reporting on every change. The application provides basic mathematical operations through a REST API as a deliberately simple target to build the pipeline around.

## Features

- RESTful API endpoints for basic operations (add, subtract, multiply, divide)
- Unit tests with pytest
- Code coverage reporting
- Jenkins pipeline automation

## API Endpoints

- `GET /` - API information
- `POST /add` - Add two numbers
- `POST /subtract` - Subtract two numbers
- `POST /multiply` - Multiply two numbers
- `POST /divide` - Divide two numbers

## Example Usage

```bash
# Start the application
python app.py

# Test addition
curl -X POST http://localhost:5000/add -H "Content-Type: application/json" -d '{"a": 10, "b": 5}'
```

## Jenkins Pipeline

The Jenkinsfile includes:
1. **Checkout** - Source code checkout
2. **Setup Environment** - Install dependencies
3. **Build** - Build verification
4. **Test** - Run unit tests with coverage
5. **Report** - Generate test reports

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run tests:
   ```bash
   pytest tests/ -v
   ```

3. Run application:
   ```bash
   python app.py
   ```

## Jenkins Configuration

1. Create a new Pipeline job in Jenkins
2. Point to the Jenkinsfile in this repository
3. Run the pipeline to see automated build, test, and reporting

