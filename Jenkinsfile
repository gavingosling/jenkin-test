import groovy.transform.Field

@Field Map BuildStatus = [:]
def generateStage(job, branch) {
    return {
        stage("stage: ${job}") {
            Exception exception = null
            try {
                sh 'pip install pandas'
                sh 'python folder/test.py'
                currentBuild.result = 'SUCCESS'
            } catch (e) {
                currentBuild.result = 'FAILURE'
                exception = e
                throw e
            } finally {
                def currentResult = currentBuild.result
                if(currentResult == 'SUCCESS'){
                    BuildStatus[job] = 'SUCCESS'
                }
                if(currentResult == 'FAILURE'){
                    sh 'cat exception.txt'
                    BuildStatus[job] = 'FAILURE'
                }
            }
        }
    }
}
 
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
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){
                        if(branch == 'master'){
                            echo 'branch equals master!'
                        }
                    }
                }
            }
        }

    }
}
