import turtle

# Fungsi untuk menggambar lingkaran dengan turtle
def draw_circle(radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Fungsi untuk menulis teks dengan turtle
def write_text(text, color, size, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.write(text, align="center", font=("Arial", size, "normal"))
    turtle.pendown()

# Fungsi untuk menggambar bunga matahari
def draw_sunflower():
    # Gambar batang bunga
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.color("green")
    turtle.width(20)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)

    # Gambar kepala bunga matahari
    draw_circle(100, "yellow")

    # Gambar kelopak matahari
    for _ in range(12):
        draw_circle(120, "orange")
        turtle.right(30)

# Inisialisasi turtle
turtle.speed(1)

# Animasi bunga matahari bergerak
for _ in range(36):
    turtle.clear()
    draw_sunflower()
    write_text("I Love You Zakiya", "red", 20, 0, -250)
    turtle.right(10)
    turtle.update()

# Tutup jendela saat diklik
turtle.exitonclick()
