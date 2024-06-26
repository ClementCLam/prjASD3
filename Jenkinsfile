pipeline {
    agent any

    stages {
/*         stage('Clone Repository') {
            steps {
                // Clone the GitHub repository
                git 'https://github.com/ClementCLam/prjASD3.git'
            }
        }

        stage('Set Up Environment') {
            steps {
                // Use ShiningPanda to set up Python environment
                withPythonEnv('Python 3') {
                    // Install dependencies
                    sh 'pip install -r requirements.txt'
                    sh 'pip install pytest'
                }
            }
        } */

/*         stage('Run Server') {
            steps {
                script {
                    // Run the server in the background
                    sh '''
                        nohup python3 server/server.py &
                    '''
                    // Sleep to give the server time to start
                    sleep 5
                }
            }
        }

        stage('Run Client') {
            steps {
                script {
                    // Run the client in the background
                    sh '''
                        nohup python3 client/client.py &
                    '''
                    // Sleep to give the client time to connect to the server
                    sleep 5
                }
            }
        } */

        stage('Run System Tests') {
            steps {
                script {
                    // Run the system tests using pytest
                    sh '''
                        python3 -m unittest discover -s system_tests -p 'test_system.py' > system_test_results.log
                    '''
                }
            }
        }

/*         stage('Cleanup') {
            steps {
                // Clean up the environment (e.g., kill the server)
                sh '''
                    pkill -f server.py || true
                    pkill -f client.py || true
                '''
            }
        } */
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