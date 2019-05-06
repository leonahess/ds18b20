pipeline {
  agent any
  triggers {
    pollSCM('H/15 * * * *')
  }
  stages {
    stage('Build Container') {
      agent {
        label "Pi_Zero"
      }
      steps {
        sh "docker build -t ds18b20 ."
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
    stage('Deploy') {
      parallel {
        stage('Deploy to leon-pi-zero-1') {
          agent {
            label "master"
          }
          steps {
            sshagent(credentials: ['d36bc821-dad8-45f5-9afc-543f7fe483ad']) {
              sh "ssh -o StrictHostKeyChecking=no pirate@leon-pi-zero-1 docker kill ds18b20"
              sh "ssh -o StrictHostKeyChecking=no pirate@leon-pi-zero-1 docker rm ds18b20"
              sh "ssh -o StrictHostKeyChecking=no pirate@leon-pi-zero-1 docker run --restart always -d --name=ds18b20 --privileged fx8350:5000/ds18b20:latest"
            }
          }
        }
        stage('Deploy to leon-pi-zero-2') {
          agent {
            label 'master'
          }
          steps {
            sshagent(credentials: ['d36bc821-dad8-45f5-9afc-543f7fe483ad']) {
              sh "ssh -o StrictHostKeyChecking=no pirate@leon-pi-zero-2 docker kill ds18b20"
              sh "ssh -o StrictHostKeyChecking=no pirate@leon-pi-zero-2 docker rm ds18b20"
              sh "ssh -o StrictHostKeyChecking=no pirate@leon-pi-zero-2 docker run --restart always -d --name=ds18b20 --privileged fx8350:5000/ds18b20:latest"
            }
          }
        }
      }
    }
  }
}
