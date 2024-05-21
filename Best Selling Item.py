#Link:https://platform.stratascratch.com/coding/10172-best-selling-item?code_type=2

# Import your libraries
import pandas as pd
#import datetime as dt
import numpy as np
# Start writing code
online_retail.head(10)
online_retail['totalprice']=online_retail['quantity']*online_retail['unitprice']
online_retail['month']=online_retail['invoicedate'].apply(pd.to_datetime).dt.month
#online_retail=online_retail[['description','totalprice','month']]
online_retail['totalprice']=online_retail.groupby(['month','description'])['totalprice'].transform(sum)

online_retail=online_retail[['description','totalprice','month']].drop_duplicates()
online_retail['rnk']=online_retail.groupby(['month'])['totalprice'].rank(method='max',ascending=False)
online_retail.sort_values(by='rnk',inplace=True)
online_retail=online_retail[online_retail['rnk']==1][['description','totalprice','month']]
online_retail.sort_values(by='month')
