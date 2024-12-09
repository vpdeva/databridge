
import boto3

def upload_to_s3(bucket_name, file_path, object_name=None):
    """
    Upload a file to an S3 bucket.
    """
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, object_name or file_path)
            