
pipeline {
    agent any
    environment {
        FULL_PATH_BRANCH = "${sh(script:'git name-rev --name-only HEAD', returnStdout: true)}"
        branch = FULL_PATH_BRANCH.substring(FULL_PATH_BRANCH.lastIndexOf('/') + 1, FULL_PATH_BRANCH.length()).trim()
    }
    stages {
 
        stage('stage') {
            steps {
                script {
                    sh 'curl -v  -d '{"text":"test"}' -X POST https://hooks.slack.com/services/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'
                }
            }
        }

    }
}
