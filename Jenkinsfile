pipeline {
    agent any

    tools {
        allure 'AllureCLI'
    }

    stages {
        stage('Set Python Environment') {
            steps {
                script {
                    // Set environment variable dynamically
                    env.PYTHON = isUnix() ? 'python3' : 'python'
                }
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python environment') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                        ${PYTHON} -m venv venv
                        source venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        '''
                    } else {
                        bat """
                        ${PYTHON} -m venv venv
                        call venv\\Scripts\\activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        """
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                        source venv/bin/activate
                        pytest --alluredir=allure-results
                        '''
                    } else {
                        bat """
                        call venv\\Scripts\\activate
                        pytest --alluredir=allure-results
                        """
                    }
                }
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
