agenda = []
def adicionarcontato():
    nome = input('Digite o nome: ')
    celular = input('Digite o número: ')
    email = input('Digite o email:')
    contato = {'nome': nome, 'celular': celular, 'email': email }
    agenda.append(contato)
    print('===============================')
    print('Registro Gravado com sucesso!')
    print('===============================')
    input('Pressione ENTER para voltar...')

def editarcontato():
    alvo = input('Quem você quer editar? ')
    for i in range(len(agenda)):
        if agenda[i]['nome'] == alvo:
            print('Achei!')
            agenda[i]['nome'] = input('Novo nome: ')
            agenda[i]['celular'] = input('Novo celular: ')
            agenda[i]['email'] = input ('Novo email:')
    input('Pressione ENTER para voltar...')        

def pesquisarcontato():
    chose = int(input('Deseja procurar pelo: \n1 - Nome\n2 - Número \n3 - Email:\n '))
    alvo2 = int(input('Digite o termo de busca: '))
    for i in range(len(agenda)):
        if chose == 1:
            comparar = agenda[i]['nome']
        if chose == 2:
            comparar = agenda[i]['celular']
        if chose == 3:
            comparar = agenda[i]['email']
        if comparar == alvo2:
            print(f"Achei! Nome: {agenda[i]['nome']} | Tel: {agenda[i]['celular']}")
            return
    input('Pressione ENTER para voltar...')
                
def listadecontatos():
    if len(agenda) == 0:
        print('A agenda esta vázia')
    else:
        for contato in agenda:
            print(f"Nome: {contato['nome']} | Cel: {contato['celular']} | Email: {contato['email']}")
    print("-----------------------------------------------------------------------\n")
    input('Pressione ENTER para voltar ao menu...')
    

def apagarcontato():
    if len(agenda) == 0:
        print('A agenda esta vázia')
        return
    posicao = 0
    for contato in agenda:
        print(f"Numero {posicao} - Nome: {contato['nome']}")
        posicao += 1
    escolher = int(input('Digite o NÚMERO do contato que deseja APAGAR: '))
    agenda.pop(escolher)
    print('Contato removido com sucesso')
    input('Pressione ENTER para voltar...')

while True:
    escolha = int(input('1 - Adicionar novo contato\n2 - Editar contato \n3 - Pesquisar contato \n4 - Lista de contatos \n5 - Apagar um contato \n6 - Sair \nEscolha uma opção: '))
    if escolha == 1:
        adicionarcontato()
    elif escolha == 2:
        editarcontato()
    elif escolha == 3:
        pesquisarcontato()
    elif escolha == 4:
        listadecontatos()
    elif escolha == 5:
        apagarcontato()
    else:
        print('Digite um número válido')
        input('Pressione ENTER para voltar...')
