lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
lista2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
s = set(lista1)
lista3 = [x for x in lista2 if x not in s]
print(lista3)




#file_exists = exists("C:\Program Files\Google\Chrome\Application\chrome.exe")
#if(file_exists):
#    print("True")
#else:
#    print("False")