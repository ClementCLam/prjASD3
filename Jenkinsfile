pipeline {
    agent any
    stages{
        stage("Start with a clean slate") {
            steps {
                deleteDir()
            }
        }
        stage("Build") {
            steps {
                sh "echo 'Build stage'"
            }
        }
        stage("Test stage") {
            steps {
                sh "echo "Test stage""
            }
        }
        stage("Deploy stage") {
            steps {
                sh "echo "Deploy stage""
            }
        }
    }
}
