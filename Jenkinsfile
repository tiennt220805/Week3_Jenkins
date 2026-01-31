pipeline {
    agent any 

    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing requirements...'
                sh '''
                    # Vào thư mục chứa code (Thay đổi tên thư mục cho đúng với Repo của bạn)
                    cd Practice_Jenkins_AtClass/demo-git-devops-master 
                    
                    # Dùng python3 thay vì python
                    python3 -m pip install --upgrade pip
                    pip3 install pytest pytest-cov
                    
                    if [ -f requirements.txt ]; then pip3 install -r requirements.txt; fi
                '''
            }
        }

        stage('Run Unit Test') {
            steps {
                echo 'Running tests with pytest...'
                sh '''
                    cd Practice_Jenkins_AtClass/demo-git-devops-master
                    python3 -m pytest test_baitap1.py --junitxml=results.xml
                '''
            }
        }
    }

    post {
        always {
            // Jenkins cần tìm đúng file results.xml trong thư mục con
            junit '**/results.xml' 
        }
    }
}