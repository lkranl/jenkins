pipeline {
    agent any

    environment {
        CHROME_BIN = "/usr/bin/google-chrome"
        CHROME_DRIVER = "/usr/local/bin/chromedriver"
    }

    stages {
        stage('Checkout') {
            when {
                branch 'develop'
            }
            steps {
                git 'https://github.com/lkranl/jenkins.git'
            }
        }

        stage('Setup') {
            when {
                branch 'develop'
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -'
                sh 'sudo sh -c \'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list\''
                sh 'sudo apt-get update'
                sh 'sudo apt-get install -y google-chrome-stable'
                sh 'wget -N https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip -P ~/'
                sh 'unzip ~/chromedriver_linux64.zip -d ~/'
                sh 'sudo mv -f ~/chromedriver /usr/local/bin/chromedriver'
                sh 'sudo chmod +x /usr/local/bin/chromedriver'
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