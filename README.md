# Controle remoto
Um programa que faz uma conexão entra 2 computadores, onde um deles irá controlar o outro pelo terminal

# Como utilizar
Execute em um dos computadores o main com o parâmetro -l (listen) com o ip e a porta
```
$ python3 main.py -l 127.0.0.1 2222
```

Depois, no computador que irá controlar o terminal, execute o main com o parâmetro -c (connect) com o ip e a porta após
```
$ python3 main.py -c 127.0.0.1 2222
```

Para todos os parâmetros, use o -h
```
$ python3 main.py -h
```

Observação: Se você quiser que o computador que estará controlando tenha acesso total, execute o comando como root
```
$ sudo python3 main.py ip porta
```

# Erros
Erro 1 - Erro na conexão. Veja se você colocou algum endereço errado.

Erro 2 - Erro na execução do comando. O comando que você pôs ou não existe ou resultou em erro.

Erro 3 - Erro na execução do programa. Você não colocou todas as opções necessárias.
