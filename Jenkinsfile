pipeline {
  agent any
  stages {
    stage('Build Container') {
      agent {
        label "Pi_3"
      }
      steps {
        sh "docker build -t hs110 ."
      }
    }
    stage('Tag Container') {
      agent {
        label "Pi_Zero"
      }
      steps {
        sh "docker tag ds18b20 fx8350:5000/ds18b20:latest"
        sh "docker tag ds18b20 fx8350:5000/ds18b20:${env.BUILD_NUMBER}"
        sh "docker tag ds18b20 leonhess/ds18b20:latest"
        sh "docker tag ds18b20 leonhess/ds18b20:${env.BUILD_NUMBER}"
      }
    }
    stage('Push to local Registry') {
      agent {
        label "Pi_Zero"
      }
      steps {
        sh "docker push fx8350:5000/ds18b20:${env.BUILD_NUMBER}"
        sh "docker push fx8350:5000/ds18b20:latest"
      }
    }
    stage('Push to DockerHub') {
      agent {
        label "Pi_Zero"
      }
      steps {
        withDockerRegistry([credentialsId: "dockerhub", url: ""]) {
          sh "docker push leonhess/ds18b20:${env.BUILD_NUMBER}"
          sh "docker push leonhess/ds18b20:latest"
        }
      }
    }
    stage('Cleanup') {
      agent {
        label "Pi_Zero"
      }
      steps {
        sh "docker rmi fx8350:5000/ds18b20:latest"
        sh "docker rmi fx8350:5000/ds18b20:${env.BUILD_NUMBER}"
        sh "docker rmi leonhess/ds18b20:latest"
        sh "docker rmi leonhess/ds18b20:${env.BUILD_NUMBER}"
      }
    }
  }
}
