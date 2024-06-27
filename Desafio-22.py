nome = input('digite seu nome\n')

nomeSplit = nome.split()
 
print('seu nome em letras em maiusculas:', nome.upper(), '\n')
print('seu nome em letras minusculas:  ', nome.lower() ,'\n')
print('a quantidade letras em seu nome:   ', len(''.join(nome.split())), '\n')
print('quantas letras tem seu primeiro nome: ', len(nomeSplit[0]), '\n')

