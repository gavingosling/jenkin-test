def generateStage(job, branch) {
    return {
        stage("stage: ${job}") {
            // Exception exception = null
            try {
                sh 'echo "Fail!"; exit 1'
            } catch (e) {
                echo 'catch'
                //exception = e
                throw e
            } finally {
                echo currentBuild.result
                def currentResult = currentBuild.result ?: 'SUCCESS'
                if(currentResult == 'SUCCESS'){
                    echo 'SUCCESS'
                }
                if(currentResult == 'FAILURE'){
                    echo 'FAILURE'
                    //echo exception
                }
                echo 'finally'
            }
        }
    }
}
 
pipeline {
    agent any
 
    stages {
        /*
        stage("stage") {
            steps {
                sh("echo a")
            }
            post { 
                success { 
                    echo 'SUCCESS'               
                }
                failure { 
                    echo 'FAILURE'
                 }
                aborted {
                    echo 'ABORTED'
                } 
            }
        }*/
 
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

    }
}
