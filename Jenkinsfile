pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/shweta2071990/dqe-automation.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install pytest pytest-html'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m pytest --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}
