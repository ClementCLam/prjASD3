pipeline {
    agent any

    stages {
/*         stage('Clone Repository') {
            steps {
                // Clone the GitHub repository
                git 'https://github.com/ClementCLam/prjASD3.git'
            }
        } */

        stage('Install Python') {
            steps {
                sh '''
                    apt-get update && apt-get install -y sudo
                    sudo apt-get update
                    sudo apt-get install -y python3 python3-venv python3-pip
                    sudo apt-get clean
                '''
            }
        }

        stage('Set Up Environment') {
            steps {
                // Set up a Python virtual environment and install dependencies
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
                sh '. venv/bin/activate && pip install pytest' // Install pytest
            }
        }

        stage('Run Server') {
            steps {
                script {
                    // Run the server in the background
                    sh 'nohup . venv/bin/activate && python server/server.py &'
                    // Sleep to give the server time to start
                    sleep 5
                }
            }
        }

        stage('Run Client') {
            steps {
                script {
                    // Run the client in the background
                    sh 'nohup . venv/bin/activate && python client/client.py &'
                    // Sleep to give the client time to connect to the server
                    sleep 5
                }
            }
        }

        stage('Run System Tests') {
            steps {
                script {
                    // Run the system tests using pytest
                    sh '. venv/bin/activate && pytest system_tests/test_system.py > system_test_results.log'
                }
            }
        }

        stage('Cleanup') {
            steps {
                // Clean up the environment (e.g., kill the server)
                sh 'pkill -f server.py'
                sh 'pkill -f client.py'
            }
        }
    }

    post {
        always {
            // Archive the test results and any other relevant files
            archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true
            // Clean up the workspace
            cleanWs()
        }
    }
}