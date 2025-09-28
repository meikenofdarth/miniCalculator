// Jenkinsfile
pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = "smoothlake67"
        DOCKER_IMAGE_NAME   = "${DOCKER_HUB_USERNAME}/mini-calculator"
        DOCKER_CREDENTIALS_ID = "dockerhub-credentials"
    }

    stages {
        stage('Run Unit Tests') {
            steps {
                script {
                    docker.image('python:3.9-slim').inside {
                        echo 'Running unit tests inside a Python container...'
                        sh 'python -m unittest test_calculator.py'
                    }
                }
            }
        }

        stage('Build and Push Docker Image') {
            steps {
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

        stage('Deploy with Ansible') {
            steps {
                script {
                    docker.image('cytopia/ansible:latest').inside {
                        echo 'Installing Docker SDK for Python...'
                        // *** THIS IS THE NEW LINE ***
                        // Install the Python library needed by the Ansible Docker modules.
                        sh 'pip install docker'

                        echo 'Deploying application using Ansible...'
                        sh 'ansible-playbook -i inventory.ini deploy.yml'
                    }
                }
            }
        }
    }
}