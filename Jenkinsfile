// Jenkinsfile
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Get the code from the GitHub repository
                git 'https://github.com/meikenofdarth/miniCalculator'
                // If your repo is private, you would need to add credentials
            }
        }

        stage('Run Tests') {
            steps {
                // Execute the unit tests
                sh 'python3 -m unittest test_calculator.py'
            }
        }
    }
}