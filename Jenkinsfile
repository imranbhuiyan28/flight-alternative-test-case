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
                sh './venv/bin/behave --tags=@smoke --format html --outfile reports/report.html'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    reportName: 'Behave Test Report',
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    keepAll: true
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
            cleanWs()
        }
    }
}
