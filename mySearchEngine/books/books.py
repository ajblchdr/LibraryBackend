import requests
import os

count = 0
for i in range(60130, 67250):
    print('-----------------------------------------------------------------')
    url = 'https://www.gutenberg.org/cache/epub/'+str(i)+'/pg'+str(i)+'.txt'
    r = requests.get(url, allow_redirects=True)
    print(r)
    if str(r) == '<Response [200]>':
        print('yes ')
        dataArray = r.content.decode('utf-8').split()
        print(len(dataArray))
        if len(dataArray) > 10000:
            with open(str(i)+'.txt','w',encoding='utf-8') as f:
                f.write(r.content.decode('utf-8'))
                count+=1
                print("TOTAL BOOKS : "+str(count))
                if(count > 1664):
                    break
    else:
        print(r)
        print('EEERRRROOOOOOOOOORRRRR')
        continue
