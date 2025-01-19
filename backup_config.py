### 1. Backup Configuration (`backup_config.py`)
# This script automates the creation of backup vaults and plans.

python
import boto3
import json

# Initialize AWS Backup client
try:
    backup_client = boto3.client('backup')
except Exception as e:
    print(f"Error initializing AWS Backup client: {e}")
    exit(1)

def create_backup_vault(vault_name, kms_key_arn=None):
    """
    Creates a backup vault.
    """
    try:
        params = {
            'BackupVaultName': vault_name
        }
        if kms_key_arn:
            params['EncryptionKeyArn'] = kms_key_arn

        response = backup_client.create_backup_vault(**params)
        print(f"Backup vault '{vault_name}' created successfully.")
    except Exception as e:
        print(f"Error creating backup vault: {e}")

def create_backup_plan(plan_name, resources, iam_role_arn):
    """
    Creates a backup plan and assigns resources to it.
    """
    try:
        plan = {
            "BackupPlanName": plan_name,
            "Rules": [
                {
                    "RuleName": "DailyBackup",
                    "TargetBackupVaultName": "EnterpriseBackupVault",
                    "ScheduleExpression": "cron(0 0 * * ? *)",
                    "Lifecycle": {"MoveToColdStorageAfterDays": 30, "DeleteAfterDays": 365}
                }
            ]
        }

        response = backup_client.create_backup_plan(
            BackupPlan=plan,
            BackupSelection={
                'SelectionName': 'BackupSelection',
                'IamRoleArn': iam_role_arn,
                'Resources': resources
            }
        )
        print(f"Backup plan '{plan_name}' created successfully.")
    except Exception as e:
        print(f"Error creating backup plan: {e}")

if __name__ == "__main__":
    VAULT_NAME = "EnterpriseBackupVault"
    BACKUP_PLAN_NAME = "EnterpriseBackupPlan"
    RESOURCES = [
        "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
    ]
    IAM_ROLE_ARN = "arn:aws:iam::123456789012:role/AWSBackupRole"

    # Verify that the resources listed include the correct ARNs
    for resource in RESOURCES:
        if not resource.startswith("arn:aws:"):
            raise ValueError(f"Invalid ARN format: {resource}")

    # Specify a custom KMS key ARN if required
    KMS_KEY_ARN = "arn:aws:kms:us-east-1:123456789012:key/abcd1234-abcd-5678-efgh-12345678ijkl"

    create_backup_vault(VAULT_NAME, KMS_KEY_ARN)
    create_backup_plan(BACKUP_PLAN_NAME, RESOURCES, IAM_ROLE_ARN)
