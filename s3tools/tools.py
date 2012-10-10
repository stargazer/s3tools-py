from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.exception import BotoClientError

class S3Tools:
    """
    Class that implements some lowlevel Amazon S3 functionality.
    """
    def __init__(self, AWS_access, AWS_secret):
        self.AWS_access = AWS_access
        self.AWS_secret = AWS_secret

    def _connect_and_get_bucket(self, bucket_name):
        """
        @param bucket_name: Bucket name
        @return: Bucket instance
        """
        try:
            conn = S3Connection(
                self.AWS_access,
                self.AWS_secret,
            )
            bucket = conn.get_bucket(bucket_name)
        except:
            raise BotoClientError('Error connecting to Amazon S3')        
        return bucket

    def create(self, bucket_name, key, data, headers=None, acl=None):
        """
        Creates a file on Amazon S3. 

        @param bucket_name: Bucket to use (string)
        @param key: Key to use (string)
        @param data: File contents
        @param headers: File headers (dict)
        @param acl: File permissions (string). Any string of:('private', 'public-read',
            'public-read-write', 'authenticated-read', 'bucket-owner-read', 
            'bucket-owner-full-control', 'log-delivery-write')
        """        
        # Returns bucket connection
        bucket = self._connect_and_get_bucket(bucket_name)

        # Create a Key instance for this bucket
        k = Key(bucket)
        k.key = key

        # Create the file in S3
        try:
            k.set_contents_from_string(
                data,
                headers=headers,
            )
            if acl:
                k.set_acl(acl)
        except:
            return BotoClientError("Error uploading file to Amazon S3")

    def delete(self, bucket_name, key):
        """
        Deletes a file from Amazon S3

        @param bucket_name: Name of the bucket (string)
        @param key: Key to delete (string)
        """
        bucket = self._connect_and_get_bucket(bucket_name)

        key = bucket.get_key(key)
        if not key:
            raise BotoClientError('Invalid Amazon S3 Key')

        try:
            key.delete()
        except:
            raise BotoClientError("Could not delete Amazon S3 file")
 
