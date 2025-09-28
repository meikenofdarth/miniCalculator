pipeline {
    agent any // Define a global agent to be used for all stages by default

    environment {
        DOCKER_HUB_USERNAME = "smoothlake67"
        DOCKER_IMAGE_NAME   = "${DOCKER_HUB_USERNAME}/mini-calculator"
        DOCKER_CREDENTIALS_ID = "dockerhub-credentials"
    }

    stages {
        stage('Checkout Source Code') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }

        stage('Run Unit Tests') {
            agent {
                // Override the global agent for this specific stage to use a Docker container
                docker {
                    image 'python:3.9-slim'
                }
            }
            steps {
                echo 'Running unit tests inside a Python container...'
                sh 'python -m unittest test_calculator.py'
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    echo "Building Docker image: ${DOCKER_IMAGE_NAME}"
                    // The 'docker.build()' command returns an image object
                    def appImage = docker.build(DOCKER_IMAGE_NAME)

                    echo "Logging in and pushing image to Docker Hub..."
                    // Use withRegistry to handle Docker Hub credentials securely
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_CREDENTIALS_ID) {
                        // Push the image with both 'latest' and the build number as tags
                        appImage.push('latest')
                        appImage.push(env.BUILD_NUMBER)
                    }
                }
            }
        }
    }
}