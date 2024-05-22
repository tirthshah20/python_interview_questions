#link=https://platform.stratascratch.com/coding/10297-comments-distribution?code_type=2

# Import your libraries
import pandas as pd
import numpy as np
# Start writing code
fb_users.head()
fb_users['joinyear']=fb_users['joined_at'].dt.year
fb_users=fb_users[(fb_users['joinyear']>=2018)]
fb_comments['year']=fb_comments['created_at'].dt.year
fb_comments['month']=fb_comments['created_at'].dt.month
fb_comments=fb_comments[(fb_comments['year']==2020) & (fb_comments['month']==1)]
result=pd.merge(fb_users,fb_comments,left_on='id',right_on='user_id',how='inner')
result=result[result['created_at']>=result['joined_at']]
result1=result.groupby('id')['user_id'].count().reset_index(name='comment_cnt')
result2=result1.groupby('comment_cnt')['id'].count().reset_index(name='user_cnt')
