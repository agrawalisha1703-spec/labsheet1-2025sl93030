pipeline {
    agent any

    environment {
        EC2_HOST = '3.208.27.76'
        EC2_USER = 'ubuntu'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'python3 --version'
                sh 'ls -la'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '''
                python3 -c "
import calculator

assert calculator.add(2, 3) == 5, 'add function failed'
print('add: PASSED')

assert calculator.multiply(2, 3) == 6, 'multiply function failed'
print('multiply: PASSED')

assert calculator.subtract(5, 3) == 2, 'subtract function failed'
print('subtract: PASSED')

assert calculator.divide(6, 3) == 2.0, 'divide function failed'
assert calculator.divide(6, 0) is None, 'divide by zero failed'
print('divide: PASSED')

print('All tests passed!')
"
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying to AWS EC2...'
                withCredentials([sshUserPrivateKey(credentialsId: 'aws-ec2-key', keyFileVariable: 'SSH_KEY')]) {
                    sh """
                        scp -i \$SSH_KEY -o StrictHostKeyChecking=no calculator.py ${EC2_USER}@${EC2_HOST}:/home/${EC2_USER}/
                    """
                    sh """
                        ssh -i \$SSH_KEY -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_HOST} 'ls -la /home/${EC2_USER}/calculator.py'
                    """
                }
                echo 'Deployment successful!'
            }
        }
    }
}