pipeline {
    agent {
        docker { 
            image 'python:3.10-slim'
            args '-u root'
        }
    }

    stages {
        stage('1. Build - Install Dependencies') {
            steps {
                echo "Menginstall dependensi langsung ke kontainer..."
                sh '''
                    pip install -r requirements.txt
                    pip install pytest bandit
                '''
            }
        }
        
        stage('2. Test - Unit Tests') {
            steps {
                echo "Menjalankan unit tests..."
                sh 'PYTHONPATH=. pytest'
            }
        }

        stage('3. Security Scan - Bandit') {
            steps {
                echo "Menjalankan security scan..."
                // FIX: Gunakan flag --severity-level versi panjang
                sh 'bandit -r src --severity-level medium'
            }
        }

        stage('4. Deploy to Staging') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying application to staging...'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
