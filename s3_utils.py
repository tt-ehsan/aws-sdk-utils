import boto3


def searchFile(bucket_name, file_name):
    client = boto3.client('s3')
    paginator = client.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name)
    objects = page_iterator.search(f"Contents[?contains(Key, `{file_name}`)][]")
    found_items = list(map(lambda item: item['Key'], objects))
    return found_items
