pipeline {
    agent any
    tools {
        allure 'AllureCLI'
    }
    stages {
        stage('Clean Allure Results') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'rm -rf allure-results/*'
                    } else {
                        bat 'rmdir /s /q allure-results || exit 0'
                        bat 'mkdir allure-results'
                    }
                }
            }
        }
        stage('Set Python Environment') {
            steps {
                script {
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
                        pytest -v --cache-clear --alluredir=allure-results
                        '''
                    } else {
                        bat """
                        call venv\\Scripts\\activate
                        pytest -v --cache-clear --alluredir=allure-results
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
