
 
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
                    config.each{k, v ->
                        countries << k
                    }
                    def generateStage(job) {
                        return {
                            stage("stage: ${job}") {
                                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){
                                    echo "This is ${job}."
                                    sleep 1
                                }
                            }
                        }
                    }
                    def stages = countries.collectEntries {
                        ["${it}" : generateStage(it)]
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
