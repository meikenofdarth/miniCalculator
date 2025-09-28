// Jenkinsfile
pipeline {
    agent none

    environment {
        DOCKER_HUB_USERNAME = "smoothlake67"
        DOCKER_IMAGE_NAME   = "${DOCKER_HUB_USERNAME}/mini-calculator"
        DOCKER_CREDENTIALS_ID = "dockerhub-credentials"
    }

    stages {
        stage('Checkout Source Code') {
            agent any
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm

                // Stash all files ('**/*') and name the stash 'source'
                echo 'Stashing source code...'
                stash name: 'source', includes: '**/*'
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

        stage('Build and Push Docker Image') {
            agent any
            steps {
                // Before we do anything, unstash the source code here
                echo 'Unstashing source code...'
                unstash 'source'
                
                script {
                    echo "Building Docker image: ${DOCKER_IMAGE_NAME}"
                    def appImage = docker.build(DOCKER_IMAGE_NAME)

                    echo "Logging in and pushing image to Docker Hub..."
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_CREDENTIALS_ID) {
                        appImage.push('latest')
                        appImage.push(env.BUILD_NUMBER)
                    }
                }
            }
        }
    }
}