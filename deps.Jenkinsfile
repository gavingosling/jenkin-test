pipeline {
    agent any
 
    stages {
        stage('Test Deps') {
            steps {
                sh("""
                echo TEST
                python --version
                python -m pip install --upgrade pip
                python -m pip install --user virtualenv
                python -m venv $JOB_BASE_NAME
                source $JOB_BASE_NAME/bin/activate
                python check_deps.py
                python test.py
                """)
            }
        }
        
    }
}
