"""
print(),input(),type(),str(),float(),int(),bool(),format()
"""

# age=input("entrer votre age ")
# print(int(age))  

# def Addition(a,b):
#     somme=a+b
#     return somme

# reponse=Addition(4,5)
# print("somme= {}".format(reponse))    

# def Dire(nom_personne,message_personne="salut",age=12):
#     print("je m'appelle {},jai {}, {}".format(nom_personne,age,message_personne))

# Dire(nom_personne="lorene",age=19)   
   
def Addition(*liste_item):
    somme=0
    for item in liste_item:
        somme=somme+item
    return somme
       

operation1=Addition(2,4,5)
print("Somme= {}".format(operation1))

operation2=Addition(1,2,3,4,5,6)
print("Somme= {}".format(operation2))