<h2>Como executar</h2>
<p>Testado nos terminais bash (integrado no VSCode) e cmd (Windows). Antes de começar, certifique-se ter ter as dependencias necessárias instaladas na sua máquina:</p>
<p>---> (cmd windows) $pip install flask flask-jsonpify flask-sqlalchemy flask-restful</p>

<ol>
  <li>Instale as dependencias necessárias com o comando acima</li>
  <li>Abra o arquivo no VS Code</li>
  <li>Abra um terminal Bash e navegue até o diretório do arquivo</li>
  <li>Utilize o comando: Flask --app fizzbuzz run</li>
  <li>Com o servidor rodando, abra outro terminal bash uma vez que o primeiro está ocupado</li>
  <li>Navegue novamente até o diretório onde está o arquivo</li>
  <li>Utilize o comando: curl -X POST http://127.0.0.1:5000/fizzbuzz -d '{"n": <b>X</b>}' -H "Content-Type: application/json"</li>
  <li>Substituir o <b>X em negrito na linha acima</b> pelo número que deseja</li>
</ol>
<p>Para rodar diretamente no cmd do windows, basta seguir os 5 primeiros passos. O comando curl no cmd é um pouco diferente:
<p>curl -X POST http://127.0.0.1:5000/fizzbuzz -d "{\\"n\\": <b>X</b>}" -H "Content-Type: application/json"</p>
