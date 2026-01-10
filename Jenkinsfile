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
                    . $VENV_DIR/bin/activate
                    cd Pytest_selenium/pytestsdemo
                    pytest -n auto -v -s \
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
