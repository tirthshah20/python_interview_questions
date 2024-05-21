link: https://platform.stratascratch.com/coding/10310-class-performance?code_type=2
# Import your libraries
import pandas as pd

# Start writing code
box_scores.head()
box_scores['total_marks']=box_scores['assignment1']+box_scores['assignment2']+box_scores['assignment3']
box_scores['total_marks'].max()-box_scores['total_marks'].min()
