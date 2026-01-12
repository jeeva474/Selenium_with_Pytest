pipeline {
    agent any

    parameters {
        choice(name: 'BROWSER_NAME', choices: ['chrome', 'firefox', 'edge'], description: 'Select browser to run the pytests')
    }
    environment {
        BROWSER = "${params.BROWSER_NAME}"  // Just take the parameter directly
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest Selenium Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    cd Pytest_selenium/pytestsdemo
                    mkdir -p reports
                    pytest -n auto -v -s \
                        --browser_name=$BROWSER \
                        --junitxml=reports/junit-report.xml
                '''
            }
        }
    }

    post {
    always {
        junit allowEmptyResults: true,
              testResults: 'Pytest_selenium/pytestsdemo/reports/junit-report.xml'
    }

        failure {
            echo "❌ Build failed. Check Selenium logs and screenshots."
        }

        success {
            echo "✅ Build successful. Selenium tests passed."
        }
    }
}
