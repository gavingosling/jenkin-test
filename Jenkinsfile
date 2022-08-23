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
