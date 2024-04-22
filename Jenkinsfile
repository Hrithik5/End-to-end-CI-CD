pipeline{
  agent { dockerfile true }

  stages{
    stage('Build'){
      steps{
        echo 'Hello World'
        sh "python3 start.py"
      }
    }
  }
}
