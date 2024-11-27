pipeline {
	agent any

	stages {
		stage('Checkout') {
			steps {
				git branch: 'main', url: 'https://github.com/banattila/k8s-python-example.git'

			}
		}
		stage('Build docker image') {
			steps {
				sh 'docker build -t banattila/k8s-python-example:latest .'
			}
		}
		stage('Push docker image') {
			steps {
				sh 'docker push banattila/k8s-python-example:latest'
			}
		}
		stage('deploy on localhost') {
			steps {
				sh '''
				kubectl apply -f 'k8s-python-example.yaml'
				kubectl rollout restart deployment/k8s-python-example
				'''
			}
		}
	}
}
