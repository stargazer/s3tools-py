# s3tools-py

A very simple python library for (so far) creating and deleting files on Amazon
S3.

## Usage

    from s3tools.tools import S3Tools
    
    # Instantiate S3Tools class giving AWS credentials
    s3_tools = S3Tools(AWS_access_key, AWS_secret_key)

    # Create file
    s3_tools.create(bucket_name, key, data, headers, acl)

    # Delete file
    s3_tools.delete(bucket_name, key)

## Note

The code is very simple and well documented, so feel free to consult it for a
better insight on method parameters.

