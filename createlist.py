def generate_multiplication_table(n):
     for i in range(1, 11):
          print("{} * {}".format(n,i, n*i))
     generate_multiplication_table(3)
