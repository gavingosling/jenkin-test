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
                    builder([text:"test"])
                    String result = builder.toString()
                    echo result
                    echo result.getClass().toString()

                    sh("""
                    curl -v  -d $result -X POST https://www.example.com
                    """)
                }
            }
        }

    }
}
