import pandas as pd
Series 
values = [10,20,30,40]
s = pd.Series(values, index = ['a','b','c','d'])
s.loc['a']

#DataFrame
df = pd.DataFrame({
    'name': ['mike','bob','alice'],
    'age': [30,25,32],
    'job':['programmer','clerk','Designer']
})

df = df.set_index('name')
df.loc['mike']
---------------------------Operations

df1 = pd.DataFrame({
    'a':[1,2,3]
},index=[0,1,2])
df2 = pd.DataFrame({
    'a':[10,20,30]
},index=[1,2,0])

print(df1+df2)
print(df1*df2)
print(df1-df2)
print(df1/df2)


--------------------------Import Export 
df = pd.DataFrame({
    'name': ['mike','bob','alice'],
    'age': [30,25,32],
    'job':['programmer','clerk','Designer']
})
df = df.set_index('name')
df = df.reset_index()
print(df)
df.to_csv('mydata.csv')
pd.read_csv('mydata.csv',index_col=0) 
df = details(as_frame =  True).frame

------------------------------DataExploration functions
df.head() -> 5
df.tail() -> 5
df.head(10)
df.tail(10)  
df.sample()
df.sample(10)
list(df.columns) -> return every columns in a dataframe
display limits
pd.options.display.max_columns = 500
df.info() -> consize manner 

-----------------------------------Statistical Functions

df.describe() ---> count,mean,std,min,max will be get from the columns like a 
dashboard like one simple view
to get one specific column
type(df.HouseAge) -> return in series
df['HouseAge].mean().min().median().mod("common value")
.count().sum().max().avg() we can use these 
 
to visualize the dataframe
import matplotlib.pyplot as plt
df['HouseAge].plot.hist(figsize=(12,8))
df['HouseAge].plot(figsize=(12,8))
df['HouseAge].plot.bar(figsize=(12,8))
plt.tight_layout()
plt.title("the house age")
plt.show()

--------------------------------------------Accessing Data on a dataframe

df = pd.DataFrame(
    {
        'name':['alice','wonder','land'],
        'age':[20,30,40],
        'job':['cleark','programmer','realestateagenet']
    }
)
df.iloc[1]
# df.loc[1]
df = df.set_index('name')
df.loc['alice','age']
df.iloc[1,0]
df.at['alice','age']
df.iat['alice','age'] - one specific row


df.at['alice','age'] = 64
df.at['alice','age']
df = df.set_index('name')
df.loc['Jhon'] = [90, 'dev']
df = df.reset_index()
df.iloc[0:3, 1]
df.iloc[:, 0]


--------------------------------------manipulating Data
df = pd.DataFrame(
    {
        'name':['alice','wonder','land','Jhon'],
        'age':[20,30,40,90],
        'job':['clearr','programmer','realestateagenet','dev']
    }
)


def myfunction(x):
  if x %3 == 0:
    return x ** 2
  else:
    return x // 2
def myfunction2(x):
  if x.endswith('r'):
    return 'Without job'
  else:
    return x

df.age.apply(myfunction)
df.job = df.job.apply(myfunction2)
df


----------------------------------Data Cleaning 
df = pd.DataFrame(
    {
        'name':['alice','wonder','land','Jhon'],
        'age':[20,30,40,90],
        'job':['clearr','programmer','realestateagenet','dev']
    }
)
df = df.set_index('name')
df.at['alice','age'] = float('nan')
# df.dropna()

# df.age.fillna(df.age.mean())
df.at['Bob','job'] = None
df[df.age.notna()]

-----------------------------Iterating to Dataframes
df = pd.DataFrame(
    {
        'name':['alice','wonder','land','Jhon'],
        'age':[20,30,40,90],
        'job':['clearr','programmer','realestateagenet','dev']
    }
)
df = df.set_index('name')
df = df.reset_index() 
for i, row in df.iterrows():
   print(row['name'])


-------------------Filtering Querring the Data in the Pandas Dataframe
df = pd.DataFrame(
    {
        'name':['alice','wonder','land','Jhon'],
        'age':[20,30,40,90],
        'job':['clearr','programmer','realestateagenet','dev']
    }
)
df.age > 50 --> return boolean results
df.query('age > 30')
ages = [40,5]
df[df.age.isin(ages)]

-------------------------Grouping 
df = pd.DataFrame(
    {
        'name':['alice','wonder','land','Jhon'],
        'age':[20,30,40,90],
        'job':['clearr','programmer','realestateagenet','dev']
    }
)
df.groupby('job').agg({
    'age':['mean','sum','min',max]
})

---------------------------------df sorting
df.sort_values('age',ascending=False,kind = 'mergesort')
quick sort
heap sort
merge sort, stable sort
df.sort_index
