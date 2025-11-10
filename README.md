# Calculator API - CI/CD Pipeline Project

A simple RESTful Calculator API built with Flask, configured with Jenkins CI/CD pipeline.

## Project Overview

This project demonstrates a complete CI/CD setup using Jenkins. The application provides basic mathematical operations through a REST API.

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

