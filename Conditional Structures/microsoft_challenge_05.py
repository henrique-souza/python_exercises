resposta_do_usuario = input('Você deseja mesmo continuar? ')

if resposta_do_usuario == 'no' or resposta_do_usuario == 'n' \
or resposta_do_usuario == 'não' or resposta_do_usuario == 'nao':
    print('Tudo bem. Saindo.')
elif resposta_do_usuario == 'yes' or resposta_do_usuario == 'y' \
or resposta_do_usuario == 'sim' or resposta_do_usuario == 's':
    print('Continuando...')
    print('Completo!')
else:
    print('Por favor, tente novamente respondendo "sim" ou "não", em Português ou Inglês.')
