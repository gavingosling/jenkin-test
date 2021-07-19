pipeline {
    agent any
 
    stages {
        stage('Test Deps') {
            steps {
                sh("""
                echo TEST
                python3 --version
                python3 -m pip install --user virtualenv
                python3 -m venv $JOB_BASE_NAME
                source $JOB_BASE_NAME/bin/activate
                python3 check_deps.py
                python3 test.py
                """)
            }
        }
        
    }
}
