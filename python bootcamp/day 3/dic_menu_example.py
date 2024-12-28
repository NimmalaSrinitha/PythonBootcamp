#RESTAURANT
menu={
    'chicken_bryni':299,
    'butter_chkn':250,
    'tandoori':300,
    'manchuria':100
}
print(menu['butter_chkn'])   #insert item
menu['chicken_noodles']=80
print(menu)

#pop
menu.pop('manchuria')
print(menu)

#update tandoori cost to 800
menu['tandoori']=800
print(menu)


#return all the keys
print(menu.values())


#print key to value 
for k,v in menu.items():
    print(k)