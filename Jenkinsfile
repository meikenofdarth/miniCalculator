// Jenkinsfile
pipeline {
    agent none

    stages {
        stage('Checkout Source Code') {
            agent any
            steps {
                echo 'Checking out code from GitHub...'
                // 'scm' is a built-in variable that refers to the SCM
                // configured in the Jenkins UI. This is the preferred way.
                checkout scm
            }
        }

        stage('Run Unit Tests') {
            agent {
                docker { image 'python:3.9-slim' }
            }
            steps {
                echo 'Running unit tests inside a Python container...'
                sh 'python -m unittest test_calculator.py'
            }
        }
    }
}