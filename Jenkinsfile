pipeline {
    agent {
        docker { 
            image 'python:3.10-slim'
            // FIX: Tambahkan baris ini untuk menjalankan kontainer sebagai root
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
                sh 'bandit -r src -l medium'
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
