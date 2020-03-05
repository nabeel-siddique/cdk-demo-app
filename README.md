
# Containerized Application: Run on AWS Fargate

This is a simple application to demonstrate the usage of AWS CDK. We will deploy a docker container (from docker hub, you can also use AWS ECR to deploy a conatainerized application in AWS Fargate.

![Containerized Application: Run on AWS Fargate Architecture](images/cdk-demo-app-architecture-00.png)

1. ## Prerequisites

    This demo, instructions, scripts and cloudformation template is designed to be run in `us-east-1`. With few modifications you can try it out in other regions as well(_Not covered here_).

    - AWS CLI pre-configured

1. ## ⚙️ Setting up the environment

    - Get the application code

        ```bash
        git clone https://github.com/miztiik/cdk-demo-app.git
        cd cdk-demo-app
        ```

1. ## 🚀 Deployment using AWS CDK

    If you have AWS CDK installed you can close this repository and deploy the stack with,

    ```bash
    # If you DONT have cdk installed
    npm install -g aws-cdk

    # Make sure you in root directory
    cd cdk-demo-app
    source .env/bin/activate
    pip install -r requirements.txt
    ```

    The very first time you deploy an AWS CDK app into an environment _(account/region)_, you’ll need to install a `bootstrap stack`, Otherwise just go aheadand   deploy using `cdk deploy`

    ```bash
    cdk bootstrap
    cdk deploy
    ```

1. ## 🔬 Test the app

    The `cdk deploy` command should provide you the application load balancer url to access the web app. _You can get the same from cloudformation outputs or in the ALB page._

    You should be seeing something like this,
    ![Containerized Application: Run on AWS Fargate](images/predict-attire-for-weather.png)

1. ## 🧹 CleanUp

    If you want to destroy all the resources created by the stack, Execute the below command to delete the stack, or _you can delete the stack from console as well_

    ```bash
    cdk destroy
    ```

    This is not an exhaustive list, please carry out other necessary steps as maybe applicable to your needs.

### ℹ️ Metadata

**Level**: 300
