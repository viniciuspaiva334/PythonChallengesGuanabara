numProp = input('digite seu numero\n')


if len(numProp) <= 4 :
 
  
     print('unidade:  65',numProp[3:4])
     print('dezena:   ',numProp[2:3])
     print('centena:  ',numProp[1:2])
     print('milhar:   ', numProp[0:1])

 
else :
    while len(numProp) > 4 :
         numProp = input ('seu numero ultrapassa a casa dos 4 numeros, digite o numero com ate 4 digitos: \n')
         if len(numProp) <=4 : 
                 print('unidade:', numProp[3])
                 print('dezena:', numProp[2])
                 print('centena:', numProp[1])
                 print('milhar:', numProp[0])
         else: 
           numProp=input('seu numero numero ainda eh maior que 5 digitos\n')