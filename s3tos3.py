
import json
import boto3

client =  boto3.client(
    's3',
    aws_access_key_id='xyz',
    aws_secret_access_key='pqr',
    region_name='ap-south-1'
)
sourcebucket = 'just-for-practise'
destinatiobucket = 'assignment-destination-bucket-25-08-26'

def copy_to_destination_bucket(fname):
    response = client.copy_object(Bucket='{}'.format(destinatiobucket),CopySource='/{}/{}'.format(sourcebucket,fname),Key='{}'.format(fname))


def delete_from_source_bucket(fname):
    response = client.delete_object(Bucket='{}'.format(sourcebucket),Key='{}'.format(fname))


def main():
    try:

        response = client.list_objects(Bucket='{}'.format(sourcebucket))
        for file in response['Contents']:
            filename = file['Key']
            print("{} file selected for copy to {}".format(filename,destinatiobucket))
            copy_to_destination_bucket(filename)
            print("{} deleted from {}".format(filename, sourcebucket))
            delete_from_source_bucket(filename)
        print("done")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()