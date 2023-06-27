

"""
boucle while (tant que)
boucle for  (pour)
"""
terminal = True

while terminal:
    choixMenu=input(">")
    if choixMenu=="again":
        continue
    elif choixMenu=="quit":
        terminal = False
    elif choixMenu == "hello":
        print("goog morning") 
    else: 
        print("comande introuvable")
print("Terminer")               

mot="seraphin john"

for i in mot:
    print(i)              
    
for i in range(2,4): #for i-2;i<4;i++    
    print(i)

            
    

