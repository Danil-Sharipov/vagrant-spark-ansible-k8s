pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                git 'https://github.com/Danil-Sharipov/vagrant-spark-ansible-k8s.git'
                sh'''
                echo '5'

                whoami

                '''
            }
        }
        stage('merge'){
            steps{
                  // Переходим в ветку master
                  sh "git checkout -f master"
                  // Подтягиваем изменения из удаленного репозитория
                  sh "git pull origin master"

                  // Вливаем изменения из ветки dev
                  sh "git merge origin/dev"

                  // Отправляем изменения в удаленный репозиторий
                  sh "git push git push https://github.com/Danil-Sharipov/vagrant-spark-ansible-k8s.git"
            }
        }
                
    }
}