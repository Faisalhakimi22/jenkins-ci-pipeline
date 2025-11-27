pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                script {
                    bat '''
                        python -m pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building application...'
                script {
                    bat '''
                        echo Build successful - Dependencies installed
                        python -c "import flask; print('Flask version:', flask.__version__)"
                    '''
                }
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                script {
                    bat '''
                        set PYTHONPATH=%CD%
                        pytest tests/ -v --junitxml=test-results.xml --cov=app --cov-report=html --cov-report=term
                    '''
                }
            }
            post {
                always {
                    // Publish test results
                    junit 'test-results.xml'
                    
                    // Archive coverage HTML report
                    archiveArtifacts artifacts: 'htmlcov/**', allowEmptyArchive: true
                }
            }
        }
        
        stage('Report') {
            steps {
                echo 'Generating test reports...'
                script {
                    bat '''
                        echo === Test Summary === > test-summary.txt
                        echo Tests completed successfully >> test-summary.txt
                        echo Coverage report generated in htmlcov/ >> test-summary.txt
                        type test-summary.txt
                    '''
                }
                archiveArtifacts artifacts: 'test-summary.txt', allowEmptyArchive: true
                
                // Publish HTML coverage report in Jenkins
                publishHTML(target: [
                    reportDir: 'htmlcov',
                    reportFiles: 'index.html',
                    reportName: 'Coverage Report'
                ])
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying to local server...'
                script {
                    bat '''
                        echo Stopping any existing instance on port 5000...
                        for /f "tokens=5" %%a in ('netstat -aon ^| find ":5000" ^| find "LISTENING"') do taskkill /f /pid %%a || echo No process found on port 5000
                        
                        echo Starting application...
                        start /B python app.py > app.log 2>&1
                        
                        echo Waiting for application to start...
                        ping 127.0.0.1 -n 10 >nul
                        
                        echo Verifying deployment...
                        python -c "import urllib.request; print('Health Check Status:', urllib.request.urlopen('http://localhost:5000/').getcode())"
                    '''
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed'
        }
        success {
            echo 'Pipeline succeeded! ✓'
        }
        failure {
            echo 'Pipeline failed! ✗'
        }
    }
}
