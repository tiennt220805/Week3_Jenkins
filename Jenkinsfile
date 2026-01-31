pipeline {
    agent any 

    stages {
        // Giai đoạn 1: Cài đặt thư viện
        stage('Install Dependencies') {
            steps {
                echo 'Installing requirements...'
                sh '''
                    # Kiểm tra xem python3 có tồn tại không
                    python3 -m pip install --upgrade pip
                    
                    # Cài đặt pytest và plugin để tạo báo cáo XML
                    pip3 install pytest pytest-cov
                    
                    # Cài đặt requirements nếu có
                    if [ -f requirements.txt ]; then pip3 install -r requirements.txt; fi
                '''
            }
        }

        // Giai đoạn 2: Chạy kiểm thử
        stage('Run Unit Test') {
            steps {
                echo 'Running tests with pytest...'
                // Chạy trực tiếp vì file đã nằm ở thư mục gốc
                sh 'python3 -m pytest test_baitap1.py --junitxml=results.xml'
            }
        }
    }

    post {
        always {
            // Jenkins quét toàn bộ workspace để tìm file kết quả
            junit 'results.xml'
        }
    }
}