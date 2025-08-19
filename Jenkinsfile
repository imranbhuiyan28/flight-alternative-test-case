pipeline {
    agent any

    environment {
        VENV = "${WORKSPACE}/venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/imranbhuiyan28/flight-alternative-test-case.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Behave Tests') {
            steps {
                // Run all tests with Allure formatter
                sh './venv/bin/behave -f allure_behave.formatter:AllureFormatter -o reports/'
            }
        }

        stage('Generate Allure Report') {
            steps {
                // Generate HTML report from Allure results
                sh 'allure generate reports/ -o reports/html --clean'

                // Publish in Jenkins
                publishHTML(target: [
                    reportName: 'Allure Report',
                    reportDir: 'reports/html',
                    reportFiles: 'index.html',
                    keepAll: true
                ])
            }
        }
    }

    post {
        always {
            // Archive Allure results
            archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
            // Clean workspace after build
            cleanWs()
        }
    }
}
