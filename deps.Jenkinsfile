pipeline {
    agent { label 'PPFGH1DPLCPU' }
 
    stages {
        stage('Startup') {
            steps {
                sh("""
                cd folder
                python --version
                python -m pip install --upgrade pip
                python -m pip install --user virtualenv
                python -m venv $JOB_BASE_NAME
                source $JOB_BASE_NAME/bin/activate
                python -m pip install -r requirements.txt
                """)
            }
        }

        stage('Test') {
            steps {
                sh("""
                echo TEST
                source folder/$JOB_BASE_NAME/bin/activate
                python check_deps.py --path folder
                cd folder
                python test.py
                """)
            }
        }
    }
}
