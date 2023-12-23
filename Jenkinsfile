pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                git 'https://github.com/Danil-Sharipov/vagrant-spark-ansible-k8s.git'
                sh'''
                vagrant destroy -f && vagrant up && ansible-playbook -i inventory playbook.yml

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
                  sh "git push https://github.com/Danil-Sharipov/vagrant-spark-ansible-k8s.git"
            }
        }

    }
     post {
     success {
        withCredentials([string(credentialsId: 'botSecret', variable: 'TOKEN'), string(credentialsId: 'chatId', variable: 'CHAT_ID')]) {
        sh  ("""
            curl -s -X POST https://api.telegram.org/bot${TOKEN}/sendMessage -d chat_id=${CHAT_ID} -d parse_mode=markdown -d text='*${env.JOB_NAME}* : POC *Branch*: ${env.GIT_BRANCH} *Build* : OK *Published* = YES'
        """)
        }
     }

     aborted {
        withCredentials([string(credentialsId: 'botSecret', variable: 'TOKEN'), string(credentialsId: 'chatId', variable: 'CHAT_ID')]) {
        sh  ("""
            curl -s -X POST https://api.telegram.org/bot${TOKEN}/sendMessage -d chat_id=${CHAT_ID} -d parse_mode=markdown -d text='*${env.JOB_NAME}* : POC *Branch*: ${env.GIT_BRANCH} *Build* : `Aborted` *Published* = `Aborted`'
        """)
        }

     }
     failure {
        withCredentials([string(credentialsId: 'botSecret', variable: 'TOKEN'), string(credentialsId: 'chatId', variable: 'CHAT_ID')]) {
        sh  ("""
            curl -s -X POST https://api.telegram.org/bot${TOKEN}/sendMessage -d chat_id=${CHAT_ID} -d parse_mode=markdown -d text='*${env.JOB_NAME}* : POC  *Branch*: ${env.GIT_BRANCH} *Build* : `not OK` *Published* = `no`'
        """)
        }
     }
     }
}