pipeline {
    // 1. Chỉ định Jenkins sử dụng Docker để tạo môi trường Python sạch
    agent {
        docker {
            image 'python:3.10-slim'
        }
    }

    stages {
        // 2. Giai đoạn chuẩn bị môi trường
        stage('Install Dependencies') {
            steps {
                echo 'Installing requirements...'
                sh '''
                    python -m pip install --upgrade pip
                    pip install pytest pytest-cov
                    # Cài đặt các thư viện trong dự án của bạn nếu có
                    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                '''
            }
        }

        // 3. Giai đoạn chạy Unit Test
        stage('Run Unit Test') {
            steps {
                echo 'Running tests with pytest...'
                // Chạy pytest và xuất kết quả ra file XML để Jenkins đọc được
                sh 'pytest test_baitap1.py --junitxml=results.xml'
            }
        }
    }

    // 4. Các hành động sau khi chạy xong (Dù thành công hay thất bại)
    post {
        always {
            // Hiển thị kết quả test dưới dạng biểu đồ trên giao diện Jenkins
            junit 'results.xml'
        }
    }
}