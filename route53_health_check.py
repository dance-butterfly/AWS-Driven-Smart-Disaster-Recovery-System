### 3. Route 53 Health Check (`route53_health_check.py`)
# This script configures Route 53 health checks and failover policies.

python
import boto3

# Initialize Route 53 client
try:
    route53_client = boto3.client('route53')
except Exception as e:
    print(f"Error initializing Route 53 client: {e}")
    exit(1)

def create_health_check(domain_name):
    """
    Creates a Route 53 health check.
    """
    try:
        response = route53_client.create_health_check(
            CallerReference='unique-string',
            HealthCheckConfig={
                'IPAddress': domain_name,
                'Type': 'HTTPS',
                'Port': 443,
                'ResourcePath': '/',
                'RequestInterval': 30,
                'FailureThreshold': 3
            }
        )
        print(f"Health check created for {domain_name}.")
    except Exception as e:
        print(f"Error creating health check: {e}")

if __name__ == "__main__":
    DOMAIN_NAME = "www.example.com"
    create_health_check(DOMAIN_NAME)
