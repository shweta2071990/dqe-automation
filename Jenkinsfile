pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install pytest pytest-html'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m pytest tests --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}
