from math import *
from random import *
lst_cara=[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F","G","H","I" ,"J","K","L","M","N","O","P" ,"Q" ,"R" ,"S","T","U","V","W","X","Y","Z","#","€","@","&","-","_","*","'",":","/","!","?","=","%","(",")",",","à","é","è","ê","â","î","ô","ç","{","}"] 
rouages=[193,373,346,422,360,155,433,108,376,214]
nb_rouage=len(rouages)
cryptage1=[8, 3, 5, 3, 1, 9, 8, 7, 6, 8, 1, 3, 4, 7, 7, 7, 1, 0, 1, 5, 7, 7, 8, 1, 3, 2, 0, 6, 0, 9, 0, 4, 9, 2, 7, 3, 8, 8, 7, 2, 7, 7, 1, 7, 5, 3, 6, 8, 7, 2]
cryptage2=[9, 3, 5, 8, 2, 8, 7, 9, 2, 5, 4, 0, 5, 2, 3, 4, 9, 0, 8, 0, 9, 4, 6, 7, 8, 8, 2, 2, 7, 6, 8, 3, 4, 5, 8, 1, 1, 0, 4, 6, 9, 1, 4, 7, 6, 2, 3, 8, 6, 9]
premier_indice=0
var_flipflop=0
def cryptage(code):
   cle_cryptage1=cryptage1
   cle_cryptage2=cryptage2
   if len(code)>len(cle_cryptage1):
       while len(code)>len(cle_cryptage1):
          cle_cryptage1+=cle_cryptage1
          cle_cryptage2+=cle_cryptage2
   msg_crypte=""
   for val in range(0,10):
       val_random=randint(0,len(lst_cara)-1)
       msg_crypte+=lst_cara[val_random]
   flipflop=var_flipflop
   ancien_caras=premier_indice
   for i in range(0,len(code)):
      nouvelle_lettre=code[i]
      for j in range(0,len(lst_cara)):
         if code[i]==lst_cara[j]:
            indice_cara=j
            choix_rouage1=cle_cryptage1[i]
            choix_rouage2=cle_cryptage2[i]
            if flipflop==0:
               nouvel_indice=indice_cara+rouages[choix_rouage1]*rouages[choix_rouage2]+ancien_caras
               flipflop+=1
            elif flipflop>=1:
               nouvel_indice=indice_cara+rouages[choix_rouage1]+rouages[choix_rouage2]+ancien_caras
               flipflop=0
            ancien_caras=j+ancien_caras 
            if nouvel_indice>len(lst_cara)-1:
               while nouvel_indice>len(lst_cara)-1:
                  nouvel_indice-=len(lst_cara)
            nouvelle_lettre=lst_cara[nouvel_indice]
      msg_crypte+=nouvelle_lettre
      for i in range(0,2):
         val_random=randint(0,len(lst_cara)-1)      
         msg_crypte+=lst_cara[val_random] 
   for val in range(0,10):
       val_random=randint(0,len(lst_cara)-1)
       msg_crypte+=lst_cara[val_random]
   return msg_crypte

def decryptage(code):
   code_original=code[10:]
   code_original=code_original[:len(code_original)-10]
   cle_cryptage1=cryptage1
   cle_cryptage2=cryptage2
   if len(code)>len(cle_cryptage1):
       while len(code)>len(cle_cryptage1):
          cle_cryptage1+=cle_cryptage1
          cle_cryptage2+=cle_cryptage2
   msg_crypte=""
   flipflop=var_flipflop
   ancien_caras=premier_indice
   code=""
   for val in range(0,len(code_original),3):
       code+=code_original[val]
   for i in range(0,len(code)):
      nouvelle_lettre=code[i]
      for j in range(0,len(lst_cara)):
         if code[i]==lst_cara[j]:
            indice_cara=j
            choix_rouage1=cle_cryptage1[i]
            choix_rouage2=cle_cryptage2[i]
            if flipflop==0:
               nouvel_indice=indice_cara-rouages[choix_rouage1]*rouages[choix_rouage2]-ancien_caras
               flipflop+=1
            elif flipflop>=1:
               nouvel_indice=indice_cara-(rouages[choix_rouage1]+rouages[choix_rouage2])-ancien_caras
               flipflop=0
            if nouvel_indice>len(lst_cara)-1:
               while nouvel_indice>len(lst_cara)-1:
                  nouvel_indice-=len(lst_cara)
            elif nouvel_indice<0:
                while nouvel_indice<0:
                    nouvel_indice+=len(lst_cara)
            ancien_caras=nouvel_indice+ancien_caras
            nouvelle_lettre=lst_cara[nouvel_indice]
      msg_crypte+=nouvelle_lettre
   return msg_crypte 

msg=cryptage("") #entrez le message a crypter
print("message crypté:") 
print(msg)
msg_decrypte=decryptage("") #entrez le message a décrypter
print("message décrypté:") 
print(msg_decrypte) 