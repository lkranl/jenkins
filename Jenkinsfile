pipeline {
    agent any

    stages {
        stage('Setup') {
            when {
                branch 'develop'
            }
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            when {
                branch 'develop'
            }
            steps {
                sh 'python -m unittest discover -s tests'
            }
        }
        
        stage ('Failing') {
            when {
                branch 'develop'
            }
            steps {
                sh 'echo "Failing to send email"'
                sh 'exit 1'
            }
        }
    }

    post {
        failure {
            emailext body: "Something went wrong with ${env.JOB_NAME}. Please check the console output for more details: ${env.BUILD_URL}" recipientProviders: 'rodrigo.cruz@unillanos.edu.co' subject: "Jenkins Build Failed: ${currentBuild.fullDisplayName}",
                 
        }
    }
}