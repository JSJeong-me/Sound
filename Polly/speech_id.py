import boto3
import time

polly_client = boto3.Session(
                aws_access_key_id='AKIAWBMMPKS3UKXW5656',                  
    aws_secret_access_key='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',
    region_name='ap-northeast-2').client('polly')

response = polly_client.start_speech_synthesis_task(VoiceId='Joanna',
                OutputS3BucketName='polly100',
                OutputS3KeyPrefix='key',
                OutputFormat='mp3', 
                Text='What is a sample text to be synthesized?',
                Engine='neural')

taskId = response['SynthesisTask']['TaskId']

print( "Task id is {} ".format(taskId))

task_status = polly_client.get_speech_synthesis_task(TaskId = taskId)

print(task_status)