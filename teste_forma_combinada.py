import turtle

# Inicializa a tela
tela = turtle.Screen()
tela.title("Desenho Interativo!!")
tela.bgcolor("white")

# Cria o "pincel"
t = turtle.Turtle()
t.speed(2)
turtle.delay(50)

# --- Formas Simples ---
def desenhar_quadrado(cor):
    t.color(cor)
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

def desenhar_triangulo(cor):
    t.color(cor)
    t.begin_fill()
    for _ in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()

def desenhar_circulo(cor):
    t.color(cor)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

# --- Desenhos prontos ---
def desenhar_casa(cor):
    # Casa
    desenhar_quadrado("yellow")
    # Telhado
    t.penup()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.pendown()
    desenhar_triangulo("brown")
    t.right(90)
    t.backward(100)
    t.left(90)

def desenhar_arvore(cor):
    t.color("black", "saddlebrown")
    t.begin_fill()
    for _ in range(2):
        t.forward(30)
        t.left(90)
        t.forward(60)
        t.left(90)
    t.end_fill()

    t.penup()
    t.left(90)
    t.forward(60)
    t.right(90)
    t.backward(35)
    t.pendown()

    t.color("black", cor)
    t.begin_fill()
    for _ in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()

    t.penup()
    t.forward(35)
    t.right(90)
    t.backward(60)
    t.left(90)
    t.pendown()

def desenhar_carro(cor):
    # Corpo do carro
    t.color("black", cor)
    t.begin_fill()
    for _ in range(2):
        t.forward(120)
        t.left(90)
        t.forward(40)
        t.left(90)
    t.end_fill()

    # Cabine do carro
    t.penup()
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.pendown()

    t.color("black", "lightgray")
    t.begin_fill()
    for _ in range(2):
        t.forward(80)
        t.left(90)
        t.forward(30)
        t.left(90)
    t.end_fill()

    # Janela da frente
    t.penup()
    t.forward(10)
    t.left(90)
    t.forward(5)
    t.right(90)
    t.pendown()
    t.color("black", "white")
    t.begin_fill()
    for _ in range(2):
        t.forward(25)
        t.left(90)
        t.forward(20)
        t.left(90)
    t.end_fill()

    # Janela de tras
    t.penup()
    t.forward(35)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(25)
        t.left(90)
        t.forward(20)
        t.left(90)
    t.end_fill()

    # Rodas
    t.penup()
    t.goto(20, -10)
    t.setheading(0)
    t.pendown()
    t.color("black", "black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    t.penup()
    t.goto(100, -10)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()


# --- Entrada de usuário ---
def escolher_forma():
    return tela.textinput("Forma", "Escolha:\n1 - Quadrado\n2 - Triângulo\n3 - Círculo\n4 - Casa\n5 - Árvore\n6 - Carro")

def escolher_cor():
    return tela.textinput("Cor", "Digite uma cor (ex: red, blue, green):")

# --- Desenho ---
forma = escolher_forma()
cor = escolher_cor()

t.penup()
t.goto(0, 0)
t.setheading(0)
t.pendown()

if forma == "1":
    desenhar_quadrado(cor)
elif forma == "2":
    desenhar_triangulo(cor)
elif forma == "3":
    desenhar_circulo(cor)
elif forma == "4":
    desenhar_casa(cor)
elif forma == "5":
    desenhar_arvore(cor)
elif forma == "6":
    desenhar_carro(cor)
else:
    t.write("Forma inválida", font=("Arial", 14, "bold"))

t.hideturtle()
tela.mainloop()