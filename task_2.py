'''Не смог сделать сам (копипаст)'''

def logical_statement(x, y, z):
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)
if (logical_statement(0, 0, 0) and logical_statement(0, 0, 1) and logical_statement(0, 1, 0) and 
logical_statement(0, 1, 1) and logical_statement(1, 0, 0) and logical_statement(1, 0, 1) and
logical_statement(1, 1, 0) and logical_statement(1, 1, 1)):
    print("True")
else:
    print("False")