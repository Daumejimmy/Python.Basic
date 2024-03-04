alter = 19
if alter >= 18: 
    print ("Du bist volljährig.")
    
alter = 17 
if alter >= 18:
    print ("Du bist volljährig.")
else:
    print ("Du bist nicht volljährig.")
    
    
alter = 12
if alter < 13:
    print ("Du bist ein Kind.")
elif alter < 18:
    print ("Du bist ein Jugendlicher")
else:
    print ("Du bist volljährig.")
    
    
   
alter = 18
hat_fuehrerschein = True
if alter >=18:
    if hat_fuehrerschein:
        print ("Du darfst Auto fahren.")
    else: 
        print("Du bist volljährig, aber darfst kein Auto fahren.")
else:
    print ("Du bist nicht volljährig.")