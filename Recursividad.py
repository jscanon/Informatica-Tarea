
from random import randrange, choice
def Gene_Cart(a,d,t,c,ci,s,sie,o,n,di,j,q,k,u,m,l,n_cart,n_cartm):
 
  if n_cart>0:
      if l=="A" and a!=0:
        print("Su carta es A pero debe decidir si quiere que valga 1 ó 11")
        Gene_Cart(a-1,d,t,c,ci,s,sie,o,n,di,j,q,k,u+int(input("Digite el Valor que desea tomar   ")),m,l,n_cart-1,n_cartm)
      elif l=="2" and d!=0:
        print("Su carta es 2")
        Gene_Cart(a,d-1,t,c,ci,s,sie,o,n,di,j,q,k,u+2,m,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart-1,n_cartm)
      elif l=="3" and t!=0:
        print("Su carta es 3")
        Gene_Cart(a,d,t-1,c,ci,s,sie,o,n,di,j,q,k,u+3,m,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart-1,n_cartm)
      elif l=="4" and c!=0:
        print("Su carta es 4")
        Gene_Cart(a,d,t,c-1,ci,s,sie,o,n,di,j,q,k,+4,m,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart-1,n_cartm)
      elif l=="5" and ci!=0:
        print("Su carta es 5")
        Gene_Cart(a,d,t,c,ci-1,s,sie,o,n,di,j,q,k,u+5,m,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart-1,n_cartm)
      elif l=="6" and s!=0:
        print("Su carta es 6")
        Gene_Cart(a,d,t,c,ci,s-1,sie,o,n,di,j,q,k,u+6,m,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart-1,n_cartm)
      elif l=="7" and sie!=0:
        print("Su carta es 7")
        Gene_Cart(a,d,t,c,ci,s,sie-1,o,n,di,j,q,k,u+7,m,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart-1,n_cartm)
      elif l=="8" and o!=0:
        print("Su carta es 8")
        Gene_Cart(a,d,t,c,ci,s,sie,o-1,n,di,j,q,k,u+8,m,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart-1,n_cartm)
      elif l=="9" and n!=0:
        print("Su carta es 9")
        Gene_Cart(a,d,t,c,ci,s,sie,o,n-1,di,j,q,k,u+9,m,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart-1,n_cartm)
      elif l=="10" and di!=0:
        print("Su carta es 10")
        Gene_Cart(a,d,t,c,ci,s,sie,o,n,di-1,j,q,k,u+10,m,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart-1,n_cartm)
      elif l=="J" and j!=0:
        print("Su carta es J")
        Gene_Cart(a,d,t,c,ci,s,sie,o,n,di,j-1,q,k,u+10,m,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart-1,n_cartm)
      elif l=="Q" and q!=0:
        print("Su carta es Q")
        Gene_Cart(a,d,t,c,ci,s,sie,o,n,di,j,q-1,k,u+10,m,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart-1,n_cartm)
      elif l=="K" and k!=0:
        print("Su carta es K")
        Gene_Cart(a,d,t,c,ci,s,sie,o,n,di,j,q,k-1,u+10,m,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart-1,n_cartm)
    
  elif n_cartm>0:
      if l=="A" and a!=0:
        if m+11>21:
         Gene_Cart(a-1,d,t,c,ci,s,sie,o,n,di,j,q,k,u,m+1,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart,n_cartm-1)
         print("La carta del repartidor es 1")
        else:
         Gene_Cart(a-1,d,t,c,ci,s,sie,o,n,di,j,q,k,u,m+11,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart,n_cartm-1)  
         print("La carta del repartidor es 11")
      elif l=="2" and d!=0:
        print("La carta del repartidor es 2")
        Gene_Cart(a,d-1,t,c,ci,s,sie,o,n,di,j,q,k,u,m+2,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart,n_cartm-1)
      elif l=="3" and t!=0:
        print("La carta del repartidor es 3")
        Gene_Cart(a,d,t-1,c,ci,s,sie,o,n,di,j,q,k,u,m+3,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart,n_cartm-1)
      elif l=="4" and c!=0:
        print("La carta del repartidor es 4")
        Gene_Cart(a,d,t,c-1,ci,s,sie,o,n,di,j,q,k,u,m+4,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart,n_cartm-1)
      elif l=="5" and ci!=0:
        print("La carta del repartidor es 5")
        Gene_Cart(a,d,t,c,ci-1,s,sie,o,n,di,j,q,k,u,m+5,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart,n_cartm-1)
      elif l=="6" and s!=0:
        print("La carta del repartidor es 6")
        Gene_Cart(a,d,t,c,ci,s-1,sie,o,n,di,j,q,k,u,m+6,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart,n_cartm-1)
      elif l=="7" and sie!=0:
        print("La carta del repartidor es 7")
        Gene_Cart(a,d,t,c,ci,s,sie-1,o,n,di,j,q,k,u,m+7,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart,n_cartm-1)
      elif l=="8" and o!=0:
        print("La carta del repartidor es 8")
        Gene_Cart(a,d,t,c,ci,s,sie,o-1,n,di,j,q,k,u,m+8,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart,n_cartm-1)
      elif l=="9" and n!=0:
        print("La carta del repartidor es 9")
        Gene_Cart(a,d,t,c,ci,s,sie,o,n-1,di,j,q,k,u,m+9,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart,n_cartm-1)
      elif l=="10" and di!=0:
        print("La carta del repartidor 10")
        Gene_Cart(a,d,t,c,ci,s,sie,o,n,di-1,j,q,k,u,m+10,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart,n_cartm-1)
      elif l=="J" and j!=0:
        print("La carta del repartidor es J")
        Gene_Cart(a,d,t,c,ci,s,sie,o,n,di,j-1,q,k,u,m+10,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart,n_cartm-1)
      elif l=="Q" and q!=0:
        print("La carta del repartidor es Q")
        Gene_Cart(a,d,t,c,ci,s,sie,o,n,di,j,q-1,k,u,m+10,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart,n_cartm-1)
      elif l=="K" and k!=0:
        print("La carta del repartidor es K")
        Gene_Cart(a,d,t,c,ci,s,sie,o,n,di,j,q,k-1,u,m+10,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart,n_cartm-1)
  
  elif n_cart==0 and n_cartm == 0 and u<21:
      print(u)
      print("Si desea tomar otra carta digite 1 si desea plantar digite 0")
      if input()=="1" and u<21:
          print(u)
          Gene_Cart(a,d,t,c,ci,s,sie,o,n,di,j,q,k,u,m,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),1,n_cartm)
      else:
          print(m)
          if m<21 and m<u:
              Gene_Cart(a,d,t,c,ci,s,sie,o,n,di,j,q,k,u,m,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),n_cart,2)
          elif m>u and m<=21:
              print("Perdiste2")
          elif m>21:
              print("Ganaste")
  elif n_cart==0 and n_cartm == 0 and u>21:
        print(u)
        print("Perdiste1")
            

        
    


print("Vamos a Iniciar a Jugar")
Gene_Cart(4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,choice(["A","2","3","4","5","6","7","8","9","10","J","K","Q"]),2,1)





