import pandas as pd
data_basic={'Ind':[1,2,3,4],'Int rate':[2,3,2,2],'US GDP':[50,55,65,55]}
data_basic1={'Ind':[1,2,3,4],'Int rate':[2,3,2,2],'US GDP':[50,55,65,55]}
db=pd.DataFrame(data_basic,index=[2001,2002,2003,2004])
db1=pd.DataFrame(data_basic1,index=[2005,2006,2007,2008])
print(db)
print(db1)
#------Slicing--------
# print(db.head(2))#--first two
# print(db.tail(2))#---last two
#---------Merging
merge=pd.merge(db,db1,on="Ind")#----->Merging based on only Ind
print(merge)
#------Joining
#joined=db.join(db1)
#-----changing index and column names
#db.set_index("Ind", inplace=True) print(db)
#db=db.rename(columns={"Int rate":"Rate"}) print(db)
#----------Concatenation-----------
#concat=pd.concat([db,db1]) print(concat)
#-------data Munging-------(file type conversion) (Ex from csv to html)
#country=pd.read_csv('hello.csv',index_col=0)
#country.to_html('test.html')
#----Only including some columns and making them as indexx
#db=db.reindex(columns=['2010','2011'])
from statistics import mean,median,mode,variance,stdev
print(mean([1,5,5,7,8,7,9,5]))
print(median([1,5,5,7,8,7,9,5]))
print(mode([1,5,5,7,8,7,9,5]))
print(variance([6,9,10,8,2]))
print(stdev([4,5,6,5,3,2,8,0,4,6,7,8,4,5,7,9,8,6,7,5,5,4,2,1,9,3,3,4,6,4]))
