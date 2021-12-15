# import ./smconnect_table
import connect_table
from awscli.errorhandler import ClientError
import logging

connection = connect_table.dynamoDB
key_schema = [
    {
        "AttributeName": "username",
        "KeyType": "HASH"
    },
    {
        'AttributeName': 'password',
        'KeyType': 'RANGE'
    }
]
attribute_definitions = [
    {
        "AttributeName": "username",
        "AttributeType": "S"
    },
    {
        'AttributeName': 'password',
        'AttributeType': 'S'
    }
]
provisioned_throughput = {
    "ReadCapacityUnits": 1,
    "WriteCapacityUnits": 1
}

table_name = "userTable"


def create_table(table_name, key_schema, attribute_definitions, provisioned_throughput):
    try:
        dynamodb_resource = connection.create_table(TableName=table_name, KeySchema=key_schema,
                                                    AttributeDefinitions=attribute_definitions,
                                                    ProvisionedThroughput=provisioned_throughput)

        # Wait until the table exists.
        dynamodb_resource.meta.client.get_waiter('table_exists').wait(TableName=table_name)

    except ClientError as e:
        logging.error(e)
        return False
    return True


create_table(table_name, key_schema, attribute_definitions, provisioned_throughput)
