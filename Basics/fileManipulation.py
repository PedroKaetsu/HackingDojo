file = open('file.txt', 'w') 
#open file by name, can be especified the path
    # ('file', 'modo de abertura') 
        # r(read) 
        # w(write) [Create file if the file dont exist] [Sobrescreve conteudo]
        # r+(read/write)
        # a(append) [Create file if the file dont exist]
        # [r/w/a]b (binarios)

file.write('Test \n')
file.close

file = open('file.txt','r')

print(file.read())
file.close
