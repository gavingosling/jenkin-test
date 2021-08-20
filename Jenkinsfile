import groovy.json.JsonBuilder

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
                    def builder = new JsonBuilder()
                    def json = builder([text:"test"]).toString()
                    sh "curl -v  -d ${json} -X POST https://www.example.com"
                }
            }
        }

    }
}
