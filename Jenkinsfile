pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install pytest pytest-html'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest tests --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.html', fingerprint: true
        }
    }
}