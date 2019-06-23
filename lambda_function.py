from oracle_query import ConnectionDetail
from oracle_query import query_database

sql = '''
select 

from 

where

and table.column = :var1

'''


def lambda_handler(event, context):
    binds = {'var1': event['<variable from event>']}
    print(binds)
    con_detail = ConnectionDetail('rds connection string',
                                  'user name',
                                  'parameter for passoword from parameter store')

    response = query_database(con_detail, sql, binds)

    return {
        'statusCode': 200,
        'body': response
    }
