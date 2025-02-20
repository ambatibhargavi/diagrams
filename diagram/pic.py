from diagrams import Diagram
from diagrams.aws.network import Route53, ALB
from diagrams.aws.compute import EC2
from diagrams.aws.storage import S3
from diagrams.aws.database import RDS

with Diagram("AWS Web Application Architecture", show=False, direction="TB"):
    dns = Route53("DNS")
    lb = ALB("Load Balancer")
    web_servers = [EC2("App Server 1"), EC2("App Server 2")]
    storage = S3("Static Content")
    database = RDS("Database")

    # Define the connections
    dns >> lb >> web_servers
    web_servers >> database
    web_servers >> storage
