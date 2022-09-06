import pandas as pd

def lambda_handler(event, context):
    d = {'col1': [10,12], 'col2': [100,50]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1.1')
