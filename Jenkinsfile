pipeline {
    agent any

    stages {

        stage('Install Python') {
            steps {
                sh '''
                apt-get update
                apt-get install -y python3 python3-pip
                '''
            }
        }

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