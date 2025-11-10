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
                    sh '''
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
                    sh '''
                        echo "Build successful - Dependencies installed"
                        python -c "import flask; print('Flask version:', flask.__version__)"
                    '''
                }
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                script {
                    sh '''
                        pytest tests/ -v --junitxml=test-results.xml --cov=app --cov-report=html --cov-report=term
                    '''
                }
            }
            post {
                always {
                    // Publish test results
                    junit 'test-results.xml'
                    // Publish coverage report
                    publishHTML([
                        reportDir: 'htmlcov',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                }
            }
        }
        
        stage('Report') {
            steps {
                echo 'Generating test reports...'
                script {
                    sh '''
                        echo "=== Test Summary ===" > test-summary.txt
                        echo "Tests completed successfully" >> test-summary.txt
                        echo "Coverage report generated in htmlcov/" >> test-summary.txt
                        cat test-summary.txt
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

