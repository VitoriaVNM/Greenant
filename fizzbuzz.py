from flask import Flask, request, jsonify

app = Flask(__name__)

#gera a lista de números até n
def generate_list(n):
  fizzbuzz_list = []
  for i in range(1, n+1):
    fizzbuzz_list.append(i)
  return fizzbuzz_list

#função fizzbuzz principal
def fizzBuzz(n):
  try:
    num = int(n)
    if num < 0:
      raise Exception("Seu valor precisa ser positivo")
      
  except ValueError:
    print("Insira um valor inteiro positivo")

  else:
    fb_list = generate_list(n)

    for j in range(len(fb_list)):
      if fb_list[j] % 3 == 0 and fb_list[j] % 5 == 0:
        fb_list[j] = "FizzBuzz"

      elif fb_list[j] % 3 == 0:
        fb_list[j] = "Fizz"

      elif fb_list[j] % 5 == 0:
        fb_list[j] = "Buzz"

      else:
        fb_list[j] = fb_list[j]

  return fb_list

#rota da API
@app.route('/fizzbuzz', methods=['POST'])
def fb_api():
  valor = request.get_json()
  n = valor.get("n")
  if not n:
    raise Exception("Um valor inteiro e positivo é necessário")
  
  fb_list = fizzBuzz(n)
  return jsonify(fb_list)


fizzBuzz(15)
