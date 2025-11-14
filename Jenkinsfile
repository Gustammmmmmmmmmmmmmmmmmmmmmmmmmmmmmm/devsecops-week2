pipeline {
    // Agent 'slim' sudah bagus, hemat resource
    agent {
        docker { image 'python:3.10-slim' }
    }

    stages {
        stage('1. Build - Install Dependencies') {
            steps {
                echo "Menginstall dependensi langsung ke kontainer..."
                sh '''
                    pip install -r requirements.txt
                    pip install pytest bandit
                '''
                // Kita juga bisa pisah pip install bandit di stage 3,
                // tapi ini lebih cepat.
            }
        }
        
        stage('2. Test - Unit Tests') {
            steps {
                echo "Menjalankan unit tests..."
                // Tidak perlu 'activate', langsung jalankan perintahnya
                sh 'PYTHONPATH=. pytest'
            }
        }

        stage('3. Security Scan - Bandit') {
            steps {
                echo "Menjalankan security scan..."
                // Tidak perlu 'activate'
                // Ganti '|| true' dengan '-l medium' agar gagal 
                // jika ada isu medium/high, sama seperti GitHub Actions.
                sh 'bandit -r src -l medium'
            }
        }

        stage('4. Deploy to Staging') {
            // Stage 'when' Anda sudah benar
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying application to staging...'
            }
        }
    }
    
    post {
        // Tambahan: Selalu bersihkan workspace setelah selesai
        always {
            cleanWs()
        }
    }
}
