//import groovy.json.JsonBuilder
import groovy.json.JsonOutput

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
                    def data = [a:"a"]
                    def json_str = JsonOutput.toJson(data)
                    def test = "curl -v  -d '${json_str}' -X POST https://www.example.com"
                    sh(test)
                    //def builder = new JsonBuilder()
                    //builder([text:"test"])
                    //String result = builder.toString()
                    //builder = ''
                    //String test = "curl -v  -d '${result}' -X POST https://www.example.com"
                    //sh(test)
                    
                }
            }
        }

    }
}
