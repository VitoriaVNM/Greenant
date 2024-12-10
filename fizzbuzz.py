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

  try:
    num = int(n)

    if num < 0:
      raise ValueError("Seu valor precisa ser um numero POSITIVO")
    elif num == 0:
      return jsonify([])
    
  except ValueError:
    return {"erro":"Seu valor precisa ser um NUMERO positivo"}

  else:
    fb_list = fizzBuzz(n)

  return jsonify(fb_list)
