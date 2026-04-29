pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install pytest pytest-html'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.html', fingerprint: true
        }
    }
}