import pandas as pd
import numpy as np
print("\n--- 4. Merging DataFrames ---")
df1=pd.DataFrame({'ID':[1,2,3,4],'Name':['Sam','Vir','Mil','Ayush']})
df2=pd.DataFrame({'ID':[1,2,5,4],'Score':[25,50,75,100]})
print(f"DataFrame 1:\n{df1}\n")
print(f"DataFrame 1:\n{df2}\n")
merged_df=pd.merge(df1,df2,on='ID')
print(f"Merged DataFrame (inner join):\n{merged_df}\n")
o_merged_df=pd.merge(df1,df2,on='ID',how='outer')
print(f"Merged DataFrame (inner join):\n{o_merged_df}\n")
print("-"*30)
