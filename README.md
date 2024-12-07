Para testar, eu executei tanto nos terminais integrados do VS Code (bash) quanto no CMD do Windows.
Como executar:
  - Terminal bash no VS Code:
    1. Abra o arquivo no VS Code
    2. Abra um terminal Bash e navegue até o diretório do arquivo
    3. Utilize o comando: Flask --app fizzbuzz run
    4. Com o servidor rodando, abra outro terminal bash uma vez que o primeiro está ocupado
    5. Navegue novamente até o diretório onde está o arquivo
    6. Utilize o comando: curl -X POST http://127.0.0.1:5000/fizzbuzz -d '{"n": X}' -H "Content-Type: application/json"
    7. Certifique-se de substituir o X pelo número do tamanho da lista !!!
  - Terminal CMD do Windows:
    1. São os mesmos passos do 1 ao 5 anteriores.
    2. Utilize o comando: curl -X POST http://127.0.0.1:5000/fizzbuzz -d "{\"n\": X}" -H "Content-Type: application/json"
    3. A diferença está no scape das "" no n
    4. Certifique-se de substituir o X pelo número do tamanho da lista !!!
  
