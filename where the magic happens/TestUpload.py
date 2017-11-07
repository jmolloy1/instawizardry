import ImageUtils
import csv



with open('Posts.csv','r') as postFile:
    posts = csv.reader(postFile)
    for post in posts:        
        user = post[0]
        password = post[1]
        imagePath = post[2]
        caption = post[3]
        print('Posting as: ' + user + ', with password: ' + password)
        print(imagePath)
        print(caption)
        print()
