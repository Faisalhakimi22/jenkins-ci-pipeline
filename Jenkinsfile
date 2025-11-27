pipeline {
    agent any
    
    environment {
        PYTHONPATH = "${WORKSPACE}"
        PYTHON_VERSION = '3.10'
        APP_PORT = '5000'
    }
    
    stages {
        stage('Validate Environment') {
            steps {
                echo 'Validating build environment...'
                bat '''
                    python --version
                    pip --version
                    echo Workspace: %CD%
                '''
            }
        }
        
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
                        pip install -r requirements.txt --cache-dir .pip-cache
                    '''
                }
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building application...'
                script {
                    bat '''
                        echo Build started at %DATE% %TIME%
                        echo Build successful - Dependencies installed
                        python -c "import importlib.metadata; print('Flask version:', importlib.metadata.version('flask'))"
                        
                        REM Generate build version
                        echo %BUILD_NUMBER% > build-version.txt
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
                        pytest tests/ -v --junitxml=test-results.xml --cov=app --cov-report=html --cov-report=term --cov-fail-under=80
                    '''
                }
            }
            post {
                always {
                    junit 'test-results.xml'
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
                        echo Build Number: %BUILD_NUMBER% >> test-summary.txt
                        echo Build Date: %DATE% %TIME% >> test-summary.txt
                        echo Tests completed successfully >> test-summary.txt
                        echo Coverage report generated in htmlcov/ >> test-summary.txt
                        type test-summary.txt
                    '''
                }
                archiveArtifacts artifacts: 'test-summary.txt, build-version.txt', allowEmptyArchive: true
                
                publishHTML(target: [
                    reportDir: 'htmlcov',
                    reportFiles: 'index.html',
                    reportName: 'Coverage Report',
                    keepAll: true,
                    alwaysLinkToLastBuild: true
                ])
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying to local server...'
                script {
                    bat '''
                        echo [%DATE% %TIME%] Starting deployment... >> deployment.log
                        
                        REM Stop existing instance
                        echo Stopping existing instance on port %APP_PORT%...
                        for /f "tokens=5" %%a in ('netstat -ano ^| findstr :%APP_PORT% ^| findstr LISTENING') do (
                            echo Killing PID %%a
                            taskkill /F /PID %%a 2>nul
                        )
                        
                        REM Wait for port to be released (using ping instead of timeout)
                        ping 127.0.0.1 -n 3 >nul
                        
                        REM Start new instance
                        echo Starting application build %BUILD_NUMBER%...
                        start /B python app.py > app.log 2>&1
                        
                        REM Wait for startup (using ping instead of timeout)
                        ping 127.0.0.1 -n 6 >nul
                        
                        REM Health check with retry
                        echo Performing health check...
                        python -c "import urllib.request, time, sys; [urllib.request.urlopen('http://localhost:%APP_PORT%/', timeout=3).read() or sys.exit(0) for i in range(3) if not time.sleep(2)]"
                        
                        if errorlevel 1 (
                            echo Health check failed!
                            type app.log
                            exit /b 1
                        )
                        
                        echo [%DATE% %TIME%] Deployment successful >> deployment.log
                        echo Deployment completed successfully!
                    '''
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed'
            archiveArtifacts artifacts: 'app.log, deployment.log', allowEmptyArchive: true
        }
        success {
            echo "✓ Pipeline succeeded! Application deployed on port ${env.APP_PORT}"
        }
        failure {
            echo '✗ Pipeline failed! Check logs for details'
            script {
                bat '''
                    for /f "tokens=5" %%a in ('netstat -ano ^| findstr :%APP_PORT% ^| findstr LISTENING') do taskkill /F /PID %%a 2>nul
                '''
            }
        }
    }
}
