# Scientific Calculator with a Full DevOps CI/CD Pipeline

This project implements a simple Python-based scientific calculator and builds a complete, automated CI/CD pipeline around it. The pipeline automatically tests, packages, and deploys the application every time a change is pushed to the repository.

## The DevOps Toolchain
*   **Source Control:** Git & GitHub
*   **Continuous Integration:** Jenkins
*   **Containerization:** Docker
*   **Configuration & Deployment:** Ansible

## Pipeline Workflow
`Git Push` -> `GitHub Webhook` -> `Jenkins Trigger` -> `Unit Tests` -> `Docker Build` -> `Docker Push to Hub` -> `Ansible Deploy`

---

## How to Run This Project After a System Restart

This guide explains how to restart the necessary services and run the pipeline after shutting down your local machine.

### Prerequisites
*   [Docker Desktop](https://www.docker.com/products/docker-desktop/) must be installed and running.
*   [Git](https://git-scm.com/) must be installed.
*   [ngrok](https://ngrok.com/download) must be downloaded and authenticated.

### Step 1: Start the Jenkins Service
The Jenkins server runs as a Docker container. If you have already created the container, you just need to start it.

```bash
# Start the existing Jenkins container
docker start jenkins-lts
```
*(In the rare case we need to recreate it from scratch, use the full `docker run` command from the setup process).*

```
docker run \
  -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -u root \
  --name jenkins-lts \
  my-jenkins-with-docker
```

#### Use the following to build my-jenkins-with-docker if the image is not present
```
docker build -f Dockerfile.jenkins -t my-jenkins-with-docker .
```
Navigate to `http://localhost:8080` to ensure Jenkins is up and running.

### Step 2: Expose Jenkins to the Internet with ngrok
GitHub needs a public URL to send webhooks to our local Jenkins instance.

```bash
# Navigate to the directory where you have the ngrok executable
# Start the tunnel for port 8080
ngrok http 8080 --domain unspasmed-milo-gymnastically.ngrok-free.dev
```
Keep this terminal window open to keep the tunnel active. The GitHub webhook is already configured for this address, so no further changes are needed.

<!-- ### Step 3: Update the GitHub Webhook
The free version of ngrok generates a new URL every time you start it. You must update this in your GitHub repository settings.

1.  Copy the new `httpss` URL from the ngrok terminal.
2.  Go to your GitHub repository: `https://github.com/meikenofdarth/miniCalculator`.
3.  Go to **Settings** -> **Webhooks**.
4.  Click **Edit** next to the existing webhook.
5.  Replace the old URL in the **Payload URL** field with the new one from ngrok. Make sure it ends with `/github-webhook/`.
6.  Click **Update webhook**. -->

### Step 4: Trigger the Pipeline
The setup is now complete. You can trigger the entire automated pipeline in two ways:

**A) The Automated Way (Recommended):**
Make a code change, commit it, and push it to the `main` branch.

```bash
# For example, edit this README file, then run:
git add README.md
git commit -m "Docs: Update project instructions"
git push origin main
```
This will automatically trigger the Jenkins pipeline.

**B) The Manual Way:**
1.  Go to your Jenkins dashboard at `http://localhost:8080`.
2.  Open the `scientific-calculator-pipeline` job.
3.  Click **Build Now** on the left sidebar.

### Step 5: Verify the Deployment
After the pipeline successfully completes, you can verify that the application was deployed on your local machine.

```bash
# Check if the container is running
docker ps
```
You should see `scientific-calculator-app` in the list of running containers.

```bash
# Interact with the running application
docker attach scientific-calculator-app
```
You can now use the calculator. To detach from the container without stopping it, press **`Ctrl+P`** followed by **`Ctrl+Q`**.

