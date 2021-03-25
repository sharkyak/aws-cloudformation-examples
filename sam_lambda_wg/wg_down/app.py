import boto3


def lambda_handler(event, context):
    client = boto3.client('cloudformation')

    client.delete_stack(
        StackName="wireguard"
    )

    return {
        'statusCode': 200
    }
