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
    post {
        // This block runs for any outcome
        always {
            script {
                // Using the emailext step from the Email Extension plugin
                emailext(
                    to: 'sanchit1472@gmail.com', 
                    subject: "${currentBuild.currentResult}: Pipeline '${env.JOB_NAME}' - Build #${env.BUILD_NUMBER}",
                    body: """
                    <h2>Pipeline Result: ${currentBuild.currentResult}</h2>
                    <p>A new build has completed for the pipeline: <strong>${env.JOB_NAME}</strong></p>
                    <p>Build Number: <strong>${env.BUILD_NUMBER}</strong></p>
                    <p>For more details, view the console output here:<br>
                    <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                    """
                )
            }
        }
    }
}