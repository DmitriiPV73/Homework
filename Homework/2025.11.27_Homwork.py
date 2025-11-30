# print('_'*(5-1)+'*'*(1+0))
# print('_'*(5-2)+'*'*(2+1))
# print('_'*(5-3)+'*'*(3+2))
# print('_'*(5-4)+'*'*(4+3))
# print('_'*(5-5)+'*'*(5+4))
#
# for i in range(size):
#     print(' '*(size-i)+'*'*(2*i+1))

size=6

def print_triangle_a(size):
    for i in range(size):
        print(' ' * (size - (size-i)) + '*' * (size-i))

def print_triangle_b(size):
    for i in range(size + 1):
        print('*' * i)

def print_triangle_q(size):
    s = size//2
    for i in range(s):
        print(' ' * (s - i) + '*' * (2*i+1))

def print_triangle_v(size):
    s = size // 2
    for i in range(s):
        print(' '*(s-(s-i))+'*'*((s-i)+(s-i-1)))

def print_triangle_d(size):
    s=size//2
    for i in range(s):
        print(' ' * (s - (s - i)) + '*' * ((s - i) + (s - i - 1)))
    for i in range(s):
        print(' ' * (s - i-1) + '*' * (2 * i + 1))

def print_triangle_e(size):
    s = size // 2
    for i in range(s-1):
        print('*'*(i+1)+' '*(s-(i*2)+1)+'*'*(s-(s-i)+1))
    for i in range(s):
        print('*' * (s-i) + ' ' * (i*2) + '*' * (s - i))

def print_triangle_g(size):
    s=size//2
    for i in range(s+1):
        print('*'*i)
    for i in range(s+1):
        print('*'*(s-i+1))

def print_triangle_z(size):
    s=size//2
    for i in range(s+1):
        print(' '*(s-i)+'*'*(i+1))
    for i in range(s+1):
       print(' ' * (s - (s - i)+1) + '*' * (s - i))

def print_triangle_i(size):
    for i in range(size):
        print('*'*(size-i))

def print_triangle_k(size):
    for i in range(size):
        print(' ' * (size - i) + '*' * (i + 1))

def main():
    while True: #Бесконечный цикл

        print("Для вывода фигуры укажите соответствующую букву:")
        print("или \"а\", или \"б\", или \"в\", или \"г\", или \"д\"")
        print("или \"е\", или \"ж\", или \"з\", или \"и\", или \"к\"")
        print("Для завершения введите \"с\"")
        value=input("Буква (РАСКЛАДКА РУССКАЯ!):  ")

        value=value.lower()

        if value=="с":
            print("До свидания!")
            break

        if value not in ["a","б","в","г","д","е","ж","з","и","к"]:
            print("Неверный выбор. Попробуйте снова.")
            continue

        if value=="a":
            print_triangle_a(size)
        elif value=="б":
            print_triangle_b(size)
        elif value=="в":
            print_triangle_v(size)
        elif value=="г":
            print_triangle_q(size)
        elif value=="д":
            print_triangle_d(size)
        elif value=="е":
            print_triangle_e(size)
        elif value=="ж":
            print_triangle_g(size)
        elif value=="з":
            print_triangle_z(size)
        elif value=="и":
            print_triangle_i(size)
        elif value=="к":
            print_triangle_k(size)

if __name__ == "__main__":
    main()