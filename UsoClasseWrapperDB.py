#Programma che usa un oggetto di WrapperDB
from ClasseWrapperDB import WrapperDB         

# CREO OGGETTO WRAPPER--------------------------------------------------------
#wrp = WrapperDB()
wrp = WrapperDB("213.140.22.237\\SQLEXPRESS", "CRD2122", "xxx123##", "CRD2122")

print()
print("\n***** TEST elencoPost *****")
print(wrp.elencoPost(as_dict = True))
print("*****************************")


print()
print("\n***** TEST singoloPost *****")
print(wrp.singoloPost(1))
print("******************************")


print()
print("\n***** TEST daiLikeAPost *****")
print("Prima:")
print(wrp.singoloPost(1))
wrp.daiLikeAPost(1)
print("Dopo:")
print(wrp.singoloPost(1))
print("*******************************")

"""
print()
print("\n***** TEST inserisciPost *****")
parametri = ("Paolo", "test")
wrp.inserisciPost(parametri)
print(wrp.elencoPost(as_dict = True))
print("********************************")
"""

#print()
#print("\n***** TEST eliminaPost *****")
#print("Prima:")
#print(wrp.elencoPost(as_dict = True))
#wrp.eliminaPost(3)
#print("Dopo:")
#print(wrp.elencoPost(as_dict = True))
#print("******************************")


print()
print("***Inserimento commento***")
tupla1 = (2, "emanuele", "testo2")
print(wrp.inserisciCommenti(tupla1))
print()

print("***Visualizzazione***")
print(wrp.elencoCommenti())
