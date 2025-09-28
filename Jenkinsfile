// Jenkinsfile
pipeline {
    // 1. Define the agent at the top level.
    // This creates ONE workspace for the entire pipeline.
    agent any

    environment {
        // Use your Docker Hub username
        DOCKER_HUB_USERNAME = "smoothlake67"
        DOCKER_IMAGE_NAME   = "${DOCKER_HUB_USERNAME}/mini-calculator"
        DOCKER_CREDENTIALS_ID = "dockerhub-credentials"
    }

    stages {
        // 2. Jenkins automatically checks out the code because of the top-level 'agent'.

        stage('Run Unit Tests') {
            steps {
                script {
                    // 3. Use 'inside' to run steps within a container
                    // without needing a separate agent or workspace.
                    docker.image('python:3.9-slim').inside {
                        echo 'Running unit tests inside a Python container...'
                        sh 'python -m unittest test_calculator.py'
                    }
                }
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                // 4. This stage runs in the same workspace. The Dockerfile is guaranteed to be here.
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

        // --- NEW STAGE ADDED BELOW ---

        stage('Deploy with Ansible') {
            steps {
                script {
                    // 5. Use 'inside' again to get a clean Ansible environment.
                    // This container has Ansible pre-installed.
                    docker.image('cytopia/ansible:latest').inside {
                        echo 'Deploying application using Ansible...'
                        // 6. The playbook runs and connects to the host's Docker daemon
                        // via the socket we mounted for the main Jenkins agent.
                        sh 'ansible-playbook -i inventory.ini deploy.yml'
                    }
                }
            }
        }
    }
}