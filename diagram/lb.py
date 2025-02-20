from diagrams import Diagram
from diagrams.aws.network import APIGateway
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudwatch

with Diagram("AWS Microservices Architecture", show=False, direction="TB"):
    api_gateway = APIGateway("API Gateway")

    # Two microservices running on AWS Lambda
    microservice1 = Lambda("Microservice 1")
    microservice2 = Lambda("Microservice 2")

    # Data storage in DynamoDB
    database = Dynamodb("DynamoDB")

    # Storage for application assets
    storage = S3("Application Assets")

    # CloudWatch for monitoring logs
    monitoring = Cloudwatch("CloudWatch Logs")

    # Define connections
    api_gateway >> [microservice1, microservice2]
    microservice1 >> database
    microservice2 >> storage
    [microservice1, microservice2] >> monitoring
