alphabet = ['a','o','i','u',"o'",'e',"A","O","I","U","E","Q","W","R","T","Y","P","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]

letter= input ('harf kiritng: ')

if (letter in alphabet):
     print('Boshqa til')
elif letter=='a' or letter=='o' or letter=='i' or letter=="o'" or letter=='u' or letter=='e':
    print('unli harf')
else :
     print('undosh harf')

list1=['audio','BWM','MERS','FERRARI','Tayotta','lada','KIA','HONDA','OPEL','MAZDA']
list2=[65000,70000,80000,50000,45000,65000,25000,23000,78000,90000]
list1.sort()
list2.sort(reverse=True)
list3=list1
list3.insert(1,list2[len(list2)-10])
list3.insert(3,list2[len(list2)-9])
list3.insert(5,list2[len(list2)-8])
list3.insert(7,list2[len(list2)-7])
list3.insert(9,list2[len(list2)-6])
list3.insert(11,list2[len(list2)-5])
list3.insert(13,list2[len(list2)-4])
list3.insert(15,list2[len(list2)-3])
list3.insert(17,list2[len(list2)-2])
list3.insert(19,list2[len(list2)-1])
print(list3)