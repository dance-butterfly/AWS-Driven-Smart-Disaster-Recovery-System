AWS-Driven Smart Disaster Recovery System for Enterprises
Overview
This project implements a cost-efficient, AWS-driven smart disaster recovery (DR) system tailored for enterprises. Leveraging AWS services, it provides automation, scalability, and cost optimization, focusing on AWS Free Tier resources. The system showcases expertise in designing resilient architectures while adhering to best practices in disaster recovery and cloud management.

Architecture Overview
Key Components:
AWS Backup: Automates backups for EC2, RDS, and EFS.

AWS Elastic Disaster Recovery (DRS): Enables real-time replication and failover.

Amazon Route 53: Handles DNS failover for seamless traffic redirection.

AWS CloudFormation: Deploys infrastructure as code.

Amazon CloudWatch: Monitors resources and sends alerts.

AWS Lambda: Automates recovery and notification processes.

Amazon S3/Glacier: Stores backups cost-effectively.

AWS IAM: Secures resource access with fine-grained permissions.

AWS Cost Explorer/Budgets: Tracks and optimizes cloud spending.


Setup Guide
Prerequisites:
An active AWS account.

AWS CLI installed and configured with appropriate credentials.

Python 3.x environment with boto3 installed.

Deployment Steps:
1. Configure AWS Backup
Use the script in /scripts/backup_config.py to automate the creation of:

Backup Vault

Backup Plans

Integration with EC2, RDS, and EFS services.

2. Set Up Elastic Disaster Recovery
Install the AWS Replication Agent on your source servers.

Use the script /scripts/drs_failover.py to automate failover processes.

3. Configure Route 53 DNS Failover
Use the /scripts/route53_health_check.py to create health checks and DNS routing policies for automated failover.

4. Monitor and Alert with CloudWatch
Leverage /scripts/cloudwatch_alarm.py to set up alarms and notifications.

5. Enable Cost Monitoring
Use /scripts/cost_management.py to set budgets and monitor cloud usage.

Testing and Validation
Simulate Primary Site Failure
Shut down the primary instance or disable services in the primary region.

Verify:

Backup availability.

Failover initiation using AWS Elastic Disaster Recovery.

DNS routing through Amazon Route 53.

Restore the primary region and ensure traffic switches back.

Validate Cost Monitoring
Check budget alerts for compliance with the free-tier usage.

Review AWS Cost Explorer for trends and optimization insights.
