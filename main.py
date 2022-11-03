ACCESS_KEY = 'AKIAQ7JFMHWTDI6YWU4G'
SECRET_KEY = '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'
import boto3
session = boto3.Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key= SECRET_KEY)
dynamoDB = session.resource('dynamodb', region_name= 'us-east-1')

table = dynamoDB.Table('user')

def create_table():
    response = dynamoDB.create_table(
        TableName = 'student',
        KeySchema = [
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions = [
            {
                'AttributeName' : 'username',
                'AttributeType' : 'S'
            },
            {
                'AttributeName' : 'last_name',
                'AttributeType' : 'S'
            }
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits' : 5,
            'WriteCapacityUnits' : 5
        }
    )
    print(response)



def get_info():
    response = table.get_item(
        Key={
            'username': 'harsha',
            'last_name': 'sha'
        }
    )

    item = response['Item']
    print(item)



def post_info():
    response = table.put_item(
        Item={
            'username': 'rajesh',
            'first_name': 'raj',
            'last_name': 'esh',
            'age': 25,
            'account_type': 'standard_user',
        }
    )
    print(response)


def update_info():
    response=table.update_item(
        Key={
            'username': 'janedoe',
            'last_name': 'Doe'
        },
        UpdateExpression='SET age = :val1',
        ExpressionAttributeValues={':val1': 20}
    )
    print(response)


def delete_info():

    response = table.delete_item(
        Key={
            'username': 'harsha',
            'last_name': 'sha'
        }
    )
    print(response)


def main():
    #create_table()
    #get_info()
    post_info()
    #update_info()
    #delete_info()


if __name__ == "__main__":
    main()
