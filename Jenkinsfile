pipeline {
    agent any

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

# Test add
assert calculator.add(2, 3) == 5, 'add function failed'
print('add: PASSED')

# Test multiply
assert calculator.multiply(2, 3) == 6, 'multiply function failed'
print('multiply: PASSED')

# Test subtract
assert calculator.subtract(5, 3) == 2, 'subtract function failed'
print('subtract: PASSED')

# Test divide
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
                echo 'Deploying application...'
                echo 'Deployment successful!'
            }
        }
    }
}
