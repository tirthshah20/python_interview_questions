#link : https://platform.stratascratch.com/coding/9917-average-salaries?code_type=2
import pandas as pd
import numpy as np
# Start writing code
employee.head()

emp1=employee.groupby(['department'])['salary'].mean().reset_index()
emp1.rename(columns={'salary':'Avg_salary'},inplace=True)

result=pd.merge(employee,emp1,on='department',how='left')
result[['first_name','department','salary','Avg_salary']]
