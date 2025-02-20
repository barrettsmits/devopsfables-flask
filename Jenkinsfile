pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/barrettsmits/devopsfables-flask.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Build') {
            steps {
                // Build a Docker image for the Flask app (optional, if you want to containerize)
                sh 'docker build -t devopsfables-flask:latest .'
            }
        }
        stage('Deploy') {
            steps {
                // Run Gunicorn with Flask
                sh '''
                    . venv/bin/activate
                    gunicorn --bind 0.0.0.0:5000 app:app &
                '''
                // Update Nginx configuration (assuming Nginx is on the same host)
                sh 'echo "Updating Nginx configuration..."'
                // Copy or update Nginx config (see below for Nginx setup)
                sh 'docker cp nginx.conf nginx-container:/etc/nginx/nginx.conf'
                sh 'docker exec nginx-container nginx -s reload'
            }
        }
    }
    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed. Check logs.'
        }
    }
}