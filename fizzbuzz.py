def generate_list(n):
  fizzbuzz_list = []
  for i in range(1, n+1):
    fizzbuzz_list.append(i)
  return fizzbuzz_list


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

fizzBuzz(15)
