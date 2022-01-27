import pandas as pd
import pymysql as p

df = pd.read_csv("movies.csv")
#print(df)

df.dropna(inplace = True) #delete all the missing data from dataset

table = []
for i,s,t,c,g,d,a in df.itertuples():
    table.append([i,s,t,c,g,d])

#  ---- Connect with the XAMPP MYSQL ----  #

#mysql -u root
def getconnect():
    return p.connect(host="localhost", user="root", password="", database="interview")

def insertrec(t):
    db = getconnect()
    cr = db.cursor()

    sql = "insert into mydata values(%s,%s,%s,%s,%s,%s)"
    cr.execute(sql,t)

    db.commit()
    db.close()



def senddata():
    for data in range(len(table)):
        insertrec (tuple(table[data]))
    print("Data transferted successfully...!")
    
