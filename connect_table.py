import boto3

# dynamoDB = boto3.resource("dynamodb", aws_access_key_id="ASIA5IBI6FTDRVK5XPSX",
#                           aws_secret_access_key="JlfXOxYvIYsHFTTRqvhDdJUhs2vU6K3XOeDhuErx",
#                           aws_session_token="FwoGZXIvYXdzEH0aDCWvtpgu+nbmkXJSyyLKAdI/012fujfCm1rhgBSPXrmxPhdx3Ivfcr7gnv5DmNxrbRzOzgqNqbnjn6irz5QxGkuomJ+jw1/7L/L2M0Ectp8yWz7kmIsqrkXZe/9HxvzWayz49BNAdAAVnCqGzvbbnuedpzdp9j++Ju98z3+c4digTeWK/4+jt8dMM/w9pKWvIS//YJW1UrhcIHKlrFmuBQ5h4TbC9yRDoFkBF0YPE4pc+p04tGFdZC6HDw1hVXf7bbjwqKHcEF52CfetuXb5cGyfS/0eo6FfAEQog5rgjQYyLeNa7yn7aBMs81czFcYMFfI+g1oGCSNKvx9uRHE8hFJwQ8sblP8E87OrneVWXA==")

dynamoDB = boto3.resource("dynamodb", region_name='us-east-1')

cogclient = boto3.client("cognito-idp", region_name="us-east-1")

snsclient = boto3.client("sns", region_name="us-east-1" )

# dynamoDB = boto3.resource("dynamodb", region_name='us-east-1')



table1 = dynamoDB.Table('userTable1')
table2 = dynamoDB.Table('recipeTable')
