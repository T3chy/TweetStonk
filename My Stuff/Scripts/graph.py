import matplotlib.pyplot as plt 
import pandas as pd    
def graphem(username):
    #### Gather Data and Import as Data Frames
    dir = r"C:\Users\Techy\Anaconda3\envs\poltweet\My Stuff\Data" + "/" + username + "_polarity" + ".csv" 
    stk = pd.read_csv(dir)
    dir = r"C:\Users\Techy\Anaconda3\envs\poltweet\My Stuff\Data" + "/" + username + "_prices" + ".csv"
    pol = pd.read_csv(dir)
    stk = stk.reindex(index=stk.index[::-1])
    #### Concatenate data making sure only data points contained on both lists are proccessed
    for i in pol.iterrows():
        print(i)
        if i[0] == "Date":
            continue
        if not (i[0] in stk):
            pol.drop(i['Date'])
    for i in stk.iterrows():
        if i[0] == "Date":
            continue
        if not (i[0] in pol):
            stk.drop(i)
    print(pol)
    print(stk)
graphem('Microsoft')