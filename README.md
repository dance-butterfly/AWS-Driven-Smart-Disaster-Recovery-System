# AWS-Driven Smart Disaster Recovery System for Enterprises

## Overview

This project demonstrates the implementation of a smart disaster recovery (DR) system leveraging AWS services to provide a cost-efficient, scalable, and automated solution for enterprise use cases. Targeted primarily at mid-to-large enterprises, managed service providers, and industries with strict uptime requirements (e.g., finance, healthcare, and e-commerce), this solution ensures business continuity through advanced automation and monitoring capabilities. Designed to minimize downtime and ensure business continuity, the system incorporates AWS-native tools such as Backup, Elastic Disaster Recovery (DRS), S3, Route 53, and CloudWatch. 

### What sets this project apart?
This solution prioritizes ease of deployment and cost efficiency, making it particularly appealing for enterprises aiming to leverage AWS free-tier resources while maintaining high reliability. Compared to other solutions, it simplifies disaster recovery setup with AWS-native automation, ensuring minimal manual intervention while providing robust monitoring and failover mechanisms. By focusing on AWS services, this system eliminates reliance on third-party tools, reducing complexity and enhancing integration within AWS environments. With automated failover and detailed monitoring, the system ensures minimal manual intervention and robust disaster recovery readiness.

---

## Key Features

### Automated Backups
- Back up critical resources (e.g., EC2 instances, RDS databases) using AWS Backup.
- Store backups securely and cost-effectively in Amazon S3.

### Disaster Recovery
- Use AWS Elastic Disaster Recovery (DRS) for seamless workload replication and failover across AWS regions.
- Automate failover processes using Lambda for minimal downtime.

### DNS Failover
- Amazon Route 53 ensures automatic traffic redirection to the DR region during primary region failures through health checks and routing policies.

### Monitoring and Alerts
- Amazon CloudWatch tracks key metrics and triggers notifications via SNS to proactively manage issues.

### Cost Optimization
- Track and manage expenses with AWS Cost Explorer and Budgets.
- Implement S3 lifecycle policies for long-term storage to optimize costs further.

---

## Architecture Overview

### Primary Region
- Runs production workloads.
- Backups are secured in a dedicated S3 bucket using AWS Backup.

### Disaster Recovery (DR) Region
- Continuous replication of workloads via AWS DRS.
- Maintains recovery-ready resources, minimizing the recovery point objective (RPO).

### Failover Automation
- Lambda functions initiate failover processes based on health check results.
- Route 53 health checks and DNS failover ensure seamless traffic redirection during primary region failures.

---
### File Structure 

AWS-DR-System/
├── README.md
├── backup_config.py
├── drs_failover.py
├── route53_health_check.py
├── cloudwatch_alarms.py
├── setup/
│   ├── iam_roles.json
│   ├── policies/
│   │   ├── backup_policy.json
│   │   ├── drs_policy.json
│   │   ├── route53_policy.json
│   │   └── cloudwatch_policy.json
├── pipeline/
│   ├── buildspec.yml
│   └── template.yaml
└── docs/
    ├── architecture_diagram.png
    ├── setup_instructions.md
    ├── troubleshooting.md
    

## Prerequisites

### AWS CLI
- Ensure the AWS CLI is installed and configured with appropriate credentials.

### IAM Roles
- Permissions for Backup, DRS, Route 53, and CloudWatch must be configured.

### Python Environment
- Python 3.x installed with the boto3 library. Install it using:

```bash
pip install boto3
```

---

## Setup Guide

### Step 1: Clone the Repository
Clone the repository from AWS CodeCommit and navigate to the project directory:

```bash
git clone https://git-codecommit.us-east-1.amazonaws.com/v1/repos/your-repo
cd your-repo
```

### Step 2: Configure Backups
Run the backup configuration script to create backup vaults and plans:

```bash
python backup_config.py
```

This script will:
- Create an AWS Backup Vault for secure storage.
- Set up a daily backup plan with a 7-day retention policy.

### Step 3: Set Up Disaster Recovery
Run the disaster recovery failover script:

```bash
python drs_failover.py
```

This script will:
- Trigger recovery processes for workloads replicated in the DR region.
- Automate failover using AWS Elastic Disaster Recovery (DRS).

### Step 4: Configure DNS Failover
Set up Route 53 health checks and DNS failover policies:

```bash
python route53_health_check.py
```

This script will:
- Create Route 53 health checks to monitor the availability of the primary region.
- Configure DNS policies to redirect traffic to the DR region automatically during failures.

### Step 5: Monitoring and Alerts
Set up CloudWatch alarms to track critical metrics:

```bash
python cloudwatch_alarms.py
```

This script will:
- Configure alarms for key metrics (e.g., CPU utilization).
- Send alerts via SNS notifications for proactive issue management.

---

## Continuous Integration and Deployment with AWS CodePipeline

### Automate Deployment
To automate the deployment process, set up a pipeline in AWS CodePipeline:

1. **Create a Pipeline:**
   - Go to the AWS CodePipeline console.
   - Click on "Create pipeline".

   *Note: Automating deployment with AWS CodePipeline ensures consistent, repeatable, and efficient deployment processes. It reduces manual intervention, enhances reliability, and provides better integration with other AWS services, ultimately supporting a robust disaster recovery strategy.*

2. **Source Stage:**
   - Select AWS CodeCommit as the source provider.
   - Choose the repository and branch.

3. **Build Stage:**
   - Select AWS CodeBuild as the build provider.
   - Define the build project to execute deployment scripts.

4. **Deploy Stage:**
   - Use AWS CloudFormation to deploy infrastructure as code.
   - Specify the stack name and template.

---

## Testing the Solution

### Simulate Failover
- Simulate a failure in the primary region by stopping or terminating resources.
- Validate recovery in the DR region and traffic redirection via DNS failover.

### Monitor Backup and Recovery
- Check the AWS Backup console for successful backups.
- Verify that the recovery processes are functional in the DR region.

### Inspect Alerts
- Confirm that CloudWatch alarms trigger as expected and notifications are received.

---

## Key AWS Services Used

- **AWS Backup**: Automates resource backups and secures data in S3.
- **Amazon S3**: Provides scalable and cost-effective storage for backups.
- **AWS Elastic Disaster Recovery (DRS)**: Replicates workloads for failover.
- **Amazon Route 53**: Ensures DNS failover with health checks.
- **Amazon CloudWatch**: Monitors resource health and triggers alerts.
- **AWS CodeCommit**: Source code repository for version control.
- **AWS CodePipeline**: Continuous integration and deployment pipeline.

---

## Cost Optimization Tips

- Use Amazon S3 lifecycle policies to transition older backups to Glacier.
- Monitor resource usage with AWS Cost Explorer and set thresholds with Budgets.
- Terminate unused resources in the DR region after testing.
- Review AWS Trusted Advisor recommendations for additional savings.

---

## About the Developer

Developed by Russhi Gibbs, an experienced cloud solutions architect specializing in AWS. This project highlights expertise in designing scalable, cost-effective disaster recovery solutions leveraging AWS services. The project idea was formulated and refined using AI tools to ensure quality and efficiency. No code was created by AI tools for this project, it is my original work

