pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/imranbhuiyan28/All-Test-Case.git', branch: 'main'
            }
        }

        stage('Set up Python Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    source $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install behave selenium webdriver-manager
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source $VENV_DIR/bin/activate
                    behave features/tests/sauce_demo.feature
                '''
            }
        }
    }
}
