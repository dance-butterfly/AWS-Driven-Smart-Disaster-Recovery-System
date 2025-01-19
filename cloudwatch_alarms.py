### 4. CloudWatch Alarms (`cloudwatch_alarms.py`)
# This script sets up CloudWatch alarms to monitor key metrics.

python
import boto3

# Initialize CloudWatch client
try:
    cloudwatch_client = boto3.client('cloudwatch')
except Exception as e:
    print(f"Error initializing CloudWatch client: {e}")
    exit(1)

def create_alarm(instance_id):
    """
    Creates a CloudWatch alarm for an EC2 instance.
    """
    try:
        response = cloudwatch_client.put_metric_alarm(
            AlarmName=f"High-CPU-{instance_id}",
            MetricName='CPUUtilization',
            Namespace='AWS/EC2',
            Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
            Statistic='Average',
            Period=300,
            EvaluationPeriods=2,
            Threshold=80.0,
            ComparisonOperator='GreaterThanThreshold',
            AlarmActions=['<SNS_TOPIC_ARN>']
        )
        print(f"CloudWatch alarm created for instance: {instance_id}")
    except Exception as e:
        print(f"Error creating alarm: {e}")

if __name__ == "__main__":
    INSTANCE_ID = "i-1234567890abcdef0"
    create_alarm(INSTANCE_ID)
