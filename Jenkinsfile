def generateStage(job, branch) {
    return {
        stage("stage: ${job}") {
            script {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){
                    def text = "ABC"
                    if (branch == "master"){
                        text = "AAA"
                    } 
                    sh("echo ${text}")
                    }
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
                    def branch = 'master'
                    def filterCountries = "$country_filter"
                    filterCountries = filterCountries.split(',')
                    config.each{k, v ->
                        if("$country_filter" == "" || filterCountries.contains(k)){
                            countries << [country: k, branch: branch]
                        }
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
