def jobs = ["JobA", "JobB", "JobC", "JobD", "JobE", "JobF", "JobG", "JobH"]
def stagesMap = jobs.collectEntries {
    ["${it}" : generateStage(it)]
}
 
def generateStage(job) {
    return {
        stage("stage: ${job}") {
            catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){
                echo "This is ${job}."
                sleep 5
            }
        }
    }
}
 
pipeline {
    agent any
 
    stages {
        stage('non-parallel stage') {
            steps {
                echo 'This stage will be executed first.'
            }
        }
 
        stage('parallel stage') {
            steps {
                script {
                    def yaml = readYaml file: 'config.yaml'
                    println yaml
                    (stagesMap.keySet() as List).collate(1).each{
                        def map = stagesMap.subMap(it)
                        parallel map
                    }
                }
            }
        }
        
        stage('a') {
            steps {
                echo 'This stage will be executed first.'
            }
        }
        
    }
}
