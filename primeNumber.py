number=int(input('Sayi giriniz.'))
#counter=0;
flag=True
for i in range(2, (number + 1)):
    flag=False;
    #counter = 0
    for k in range(2, i):
        if (i % k == 0):
            flag=True;
            #counter = counter + 1
            break


    if flag == False:
        print(i)
