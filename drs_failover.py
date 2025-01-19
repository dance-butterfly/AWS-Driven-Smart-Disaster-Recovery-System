### 2. Disaster Recovery Failover 
# This script triggers failover using AWS Elastic Disaster Recovery.

python
import boto3

# Initialize AWS Elastic Disaster Recovery client
try:
    dr_client = boto3.client('drs')
except Exception as e:
    print(f"Error initializing AWS DRS client: {e}")
    exit(1)

def initiate_failover(resource_ids):
    """
    Initiates disaster recovery failover.
    """
    try:
        for resource_id in resource_ids:
            response = dr_client.start_recovery(
                sourceServerID=resource_id
            )
            print(f"Failover initiated for resource: {resource_id}")
    except Exception as e:
        print(f"Error initiating failover: {e}")

if __name__ == "__main__":
    RESOURCE_IDS = ["resource-id-1", "resource-id-2"]
    initiate_failover(RESOURCE_IDS)
