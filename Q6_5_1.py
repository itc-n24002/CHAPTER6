with open("my_math.py", "w") as f:
    f.write("""def my_pow(x, y):
    return x ** y\n""")

import my_math
x = my_math.my_pow(2, 5)
print(x)
