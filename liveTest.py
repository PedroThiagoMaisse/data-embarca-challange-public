import boto3
import time
import json


client = boto3.client('stepfunctions')

execution_name = 'teste8'
input_payload= json.dumps({
    "Payload": "input/inp_2023-09-20T14-29-57-ec.json"
    }) # use essa variavel para ler o arquivo no bucket e processar nas lambdas

state_machine_arn = 'arn:aws:states:us-east-1:321102677516:stateMachine:embarca-challenge-step-function'

response = client.start_execution(
    stateMachineArn=state_machine_arn,
    input=input_payload
)

execution_arn = response['executionArn']

time.sleep(5) # delay para extração da descrição de execução para ter certeza de 'status': 'SUCCEEDED'
response_2 = client.describe_execution(
    executionArn=execution_arn
)
print(response_2)
