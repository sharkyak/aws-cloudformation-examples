import json
import boto3


def lambda_handler(event, context):
    client = boto3.client('cloudformation')

    response = client.create_stack(
        StackName="wireguard",
        TemplateURL="https://cf-templates-b5s4k2sjkks5-us-east-1.s3.amazonaws.com/2021224YsL-openvpnloozuvpt9he",
        Parameters=[{"ParameterKey": "sshkey", "ParameterValue": "am1"}]
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
