# Infrastructure Diagrams with Python
This repository contains infrastructure diagrams created using Python's diagrams library. It helps visualize cloud architectures, DevOps pipelines, microservices, Kubernetes clusters, and more.

📌 Tools Used
1. Python (diagrams Library) 📊
The diagrams library is a powerful tool for creating infrastructure diagrams programmatically.

Supports AWS, Azure, GCP, Kubernetes, Docker, CI/CD, On-Premises Systems, and more.
Allows automation and reproducibility of diagrams.
Installation:

   pip install diagrams

 2. Graphviz 🎨
Graphviz is required to render diagrams into images.

It converts text-based descriptions into graphical outputs.
Installation:

  brew install graphviz

📜 How We Created These Diagrams
Define a Diagram using with Diagram("Diagram Name", show=False):.
Use Clusters (Cluster()) to group components logically.
Choose Components from available modules:
diagrams.aws → AWS services (EC2, S3, RDS, Lambda, etc.)
diagrams.azure → Azure services (VM, SQL Database, Functions, etc.)
diagrams.gcp → Google Cloud services (GKE, Cloud Run, Storage, etc.)
diagrams.k8s → Kubernetes (Pods, Services, Deployments, etc.)
diagrams.onprem → On-Premises infrastructure (Servers, Databases, etc.)
diagrams.devops → CI/CD tools (Jenkins, GitHub, GitLab, Docker, Terraform, etc.)
Connect Components using >> (forward flow) and - (bidirectional flow).

🚀 Example 1 : Grouped Workers on AWS
![grouped_workers](https://github.com/user-attachments/assets/1346484c-f43d-4bc1-afa1-4ea98352c8ef)

🚀 Example 2 : Kubernetes StatefulSet Architecture
![stateful_architecture](https://github.com/user-attachments/assets/a447542b-6bb2-45f5-a0d5-7fcca81100c1)

🚀 Example 3 : Web App on AWS
![aws_web_application_architecture](https://github.com/user-attachments/assets/c96e72b3-53a6-494b-abec-d25a1162fa1f)

🚀 Example 4 : Microservices on AWS
![aws_microservices_architecture](https://github.com/user-attachments/assets/23681611-6fa3-4123-9a01-0ddf54da70ad)

🚀 Example 5 : Advanced Web Service with On-Premise
![advanced_web_service_with_on-premise_(colored)](https://github.com/user-attachments/assets/f4171c56-4c70-4863-9e6f-022b92ae29bb)








