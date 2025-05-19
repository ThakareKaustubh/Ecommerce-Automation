pipeline {
    agent any

    tools {
        // Use the Allure CLI configured in Jenkins (name must match exactly)
        allure 'AllureCLI'
    }

    environment {
        // Path to Python executable (adjust if needed)
        PYTHON = "python"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                script {
                    // Create virtual environment
                    bat 'python -m venv venv' // Windows
                    // sh 'python3 -m venv venv' // Linux/Mac alternative

                    // Activate and install dependencies
                    bat """
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    """
                    // For Linux/Mac, use sh and source venv/bin/activate
                }
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                call venv\\Scripts\\activate
                pytest --alluredir=allure-results
                """
                // For Linux/Mac, use sh and source activate accordingly
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}
