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
                    // Install Python dependencies
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
                    // Archive coverage report
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

