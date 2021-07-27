def BuildStatus = [:]
def generateStage(job, branch) {
    return {
        stage("stage: ${job}") {
            Exception exception = null
            try {
                echo 'a'
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
                    def error = exception.toString()
                    writeFile(file: 'exception.txt', text: error)
                    sh 'python post_to_slack.py --file exception.txt'
                    BuildStatus[job] = 'FAILURE'
                }
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

        stage('Shutdown') {
            steps {
                script {
                        def log = "PIPELINE: $JOB_BASE_NAME, BUILD: $BUILD_NUMBER \n"
                        BuildStatus.each{ k, v -> log+= "${k}: ${v}\n" }
                        writeFile(file: 'status.txt', text: log)
                        sh("""
                           cat status.txt
                        """)
                    }
            
                }
            }
    }
}
