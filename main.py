# Imports
import os, sys, socket, subprocess

# Array de opções e descrições
o = ['-l', '-c', '-h']
d = ["Listen. Esse parâmetro fala para ele definir esse computador como servidor", "Connect. Ele se conecta a outro computador, server, para controlar", "Help. Mostra essa interface de ajuda"]

# Vê se todas as opções estão presentes
try:
    sys.argv[1]
    sys.argv[2]
    sys.argv[3]

except:
    print("Erro 3")
    exit()

# Vê as opções
# Se a opção for de help
if sys.argv[1] == '-h':
    for i, a in enumerate(o):
        print("\n" + a + " --> " + d[i])

# Se a opção for de Listen
elif sys.argv[1] == '-l':
    try:
        # Pega as informações locais
        host = sys.argv[2]
        port = int(sys.argv[3])

        print("Rodando em " + host + ":" + str(port))

        # Cria o socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Binda e espera
        s.bind((host, port))
        s.listen(1)

    except:
        print("Erro 1")
        exit()

    # Aceita a conexão
    con, add = s.accept()

    # Escreve o ip conectado
    print(add[0], "conectou")

    # Executa os comandos
    while True:
        # Recebe
        com = con.recv(1024).decode()
        print(com)

        try:
            # Executa
            result = subprocess.check_output(com, shell=True)

            # Verifica sem há output
            if result.decode('utf-8') == '':
                con.send("Sem output".encode('utf-8'))

            else:
                # Manda o output
                con.send((result.decode("utf-8")).encode('utf-8'))

        except:
            # Escreve erro 2 caso há erro na execução do comando
            print("Erro 2")
            con.send("Erro 2".encode('utf-8'))

        # Espera uma confirmação
        con.recv(1024).decode('utf-8')

# Se a opção for de Connect
elif sys.argv[1] == '-c':
    # Define o endereço
    host = sys.argv[2]
    port = int(sys.argv[3])

    # Cria o socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta
    s.connect_ex((host, port))
    # Executa os comandos
    while True:
        # Guarda o comando
        c = input("> ")

        # Vê se o comando está em branco
        if c == '':
            try:
                s.send("Comando em branco".encode('utf-8'))

            except:
                print("Erro 1")
        else:
            try:
                # Manda o comando
                s.send(c.encode('utf-8'))

            except:
                print("Erro 1")
        # Recebe o output
        print(s.recv(1024).decode())

        # Confirma a entrega
        s.send("recebido".encode('utf-8'))
