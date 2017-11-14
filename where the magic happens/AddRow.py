import sys
import csv



with open('Posts.csv','r') as postFile:
    posts = csv.writer(postFile)

def AddRow(row):
    with open('Posts.csv','w') as postFile:
        posts = csv.writer(postFile)
        print(row)
        posts.writerow([row])
    
