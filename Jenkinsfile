pipeline {
    agent any

    environment {
    VENV_DIR = "venv"
    BROWSER_NAME = "${BROWSER_NAME}" ?: "chrome"
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
                    python3 --version

                    # Create venv only if not exists
                    if [ ! -d "$VENV_DIR" ]; then
                        python3 -m venv $VENV_DIR
                    fi

                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest Selenium Tests') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    cd Pytest_selenium/pytestsdemo
                    pytest -v -s \
                        --browser_name=chrome \
                        --html=report.html \
                        --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'Pytest_selenium/pytestsdemo',
                reportFiles: 'report.html',
                reportName: 'Pytest Selenium Report'
            ])
        }

        failure {
            echo "❌ Build failed. Check Selenium logs and screenshots."
        }

        success {
            echo "✅ Build successful. Selenium tests passed."
        }
    }
}
