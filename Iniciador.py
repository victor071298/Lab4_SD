from sys import exit
import rpyc

#iniciando eleição 
eleicao = input("Pronto para iniciar a votação, indique o id do processo desejado e o tipo de eleicao que deseja executar,respectivamente(M para maior id e m para menor id separados por espaço)\nCaso deseje encerrar a eleicao, digite N\n")
#encerra caso o input seja 'N'
if eleicao[0] == 'N':
    exit()
#dividindo os termos da eleicao passados como input    
eleicao = eleicao.split(" ")
conn = rpyc.connect('localhost', 5000+int(eleicao[0]))
resultado = conn.root.exposed_election(eleicao[1])
print("eleicao concluida, com lider eleito sendo:{}".format(resultado))
conn.close()
