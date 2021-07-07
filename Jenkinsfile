def generateStage(job, branch) {
    return {
        stage("stage: ${job}") {
            catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){
                echo "This is ${job}."
                echo "This is ${branch}."
                sleep 1
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
                    def config = yaml.get('cross-selling')
                    def countries = []
                    def branch = 'ASDF'
                    config.each{k, v ->
                        countries << [country: k, branch: branch]
                    }
                    
                    def stages = countries.collectEntries {
                        ["${it.country}" : generateStage(it.country, it.branch)]
                    }
                    
                    (stages.keySet() as List).collate(1).each{
                        def map = stages.subMap(it)
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
