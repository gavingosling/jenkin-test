def utils = null;

pipeline {
    agent any
    environment {
        FULL_PATH_BRANCH = "${sh(script:'git name-rev --name-only HEAD', returnStdout: true)}"
        branch = FULL_PATH_BRANCH.substring(FULL_PATH_BRANCH.lastIndexOf('/') + 1, FULL_PATH_BRANCH.length()).trim()
    }
    stages {
 
        stage('stage 1') {
            steps {
                script {
                    utils = load "Utils.gvy"
                    echo utils.toString()
                    utils.greet()
                    sh("python --version")
                    sh("python3 --version")
                    sh("""
                    python3 --version
                    python3 -m pip install --upgrade pip
                    python3 -m pip install --user virtualenv
                    python3 -m venv $JOB_BASE_NAME
                    source $JOB_BASE_NAME/bin/activate
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                    """)
                }
            }
        }

        stage('stage 2') {
            steps {
                script {
                    utils.greet()
                }
            }
        }

    }
}
