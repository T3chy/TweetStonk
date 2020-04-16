import matplotlib.pyplot as plt 
import pandas as pd    
def graphem(username):
    #### Gather Data and Import as Data Frames
    dir = r"C:\Users\Techy\Anaconda3\envs\poltweet\My Stuff\Data" + "/" + username + "_polarity" + ".csv" 
    pol = pd.read_csv(dir)
    dir = r"C:\Users\Techy\Anaconda3\envs\poltweet\My Stuff\Data" + "/" + username + "_prices" + ".csv"
    stk = pd.read_csv(dir)
    stk = stk.reindex(index=stk.index[::-1])
    #### Concatenate data making sure only data points contained on both lists are proccessed
    pos = 0
    for i in pol.Date.isin(stk.Date).astype(int):
        print(i)
        #print(pos)
        if i == 0:
            pol = pol.drop([pos])
        pos = pos + 1
    pos = len(stk.index) -1
    for i in stk.Date.isin(pol.Date).astype(int):
        if i == 0:
            stk = stk.drop([pos])
        pos = pos - 1
    print(pol)
    print(stk)
graphem('Microsoft')