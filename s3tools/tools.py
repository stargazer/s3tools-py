from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.exception import BotoClientError

class S3Tools:
    """
    Class that implements some lowlevel Amazon S3 functionality.
    """
    def __init__(self, AWS_access, AWS_secret):
        """
        Initializes the ``S3Tools`` object with the AWS credentials.

        :param AWS_access:  AWS access key
        :param AWS_secret:  AWS secret key

        :type AWS_access:   string
        :type AWS_secret:   string
        """
        self.AWS_access = AWS_access
        self.AWS_secret = AWS_secret

    def _connect_and_get_bucket(self, bucket_name):
        """
        Connects to Amazon S3, and returns a Bucket instance.

        :param bucket_name: Name of bucket

        :type bucket_name:  string

        :return:            Bucket 
        :rtype:             Bucket
        :raises:            BotoClienterror
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

        :param bucket_name: Name of bucket to use
        :param key:         Key to use
        :param data:        File contents
        :param headers:     File headers
        :param acl:         File permissions.

        :type bucket_name:  string
        :type key:          string
        :type data:         anything
        :type headers:      dict
        :type acl:          string. Any string of: ('private', 'public-read', 'public-read-write', 'authenticated-read', 'bucket-owner-read', 'bucket-owner-full-control', 'log-delivery-write')

        :raises:            BotoClientError
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
        Deletes a file from Amazon S3.

        :param bucket_name: Name of the bucket
        :param key:         Key to delete

        :type bucket_name:  string
        :type key:          string

        :raises:            BotoClientError
        
        """
        bucket = self._connect_and_get_bucket(bucket_name)

        key = bucket.get_key(key)
        if not key:
            raise BotoClientError('Invalid Amazon S3 Key')

        try:
            key.delete()
        except:
            raise BotoClientError("Could not delete Amazon S3 file")
 
