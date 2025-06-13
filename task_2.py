import sys
import turtle


def koch_curve(t, order, length):
    if order == 0:
        t.forward(length)
    else:
        length = length / 3.0
        koch_curve(t, order - 1, length)
        t.left(60)
        koch_curve(t, order - 1, length)
        t.right(120)
        koch_curve(t, order - 1, length)
        t.left(60)
        koch_curve(t, order - 1, length)


def draw_koch_snowflake(order, length=300):
    window = turtle.Screen()
    window.bgcolor("white")
    window.title(f"Сніжинка Коха (рівень {order})")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, length)
        t.right(120)

    window.mainloop()


def main():
    if len(sys.argv) < 2:
        print("❌ Вкажіть рівень рекурсії, напр.: python task_2.py 3")
        sys.exit(1)

    try:
        level = int(sys.argv[1])
        if level < 0:
            raise ValueError("Рівень має бути ≥ 0")
    except ValueError as e:
        print(f"❌ Некоректне значення: {e}")
        sys.exit(1)

    draw_koch_snowflake(level)


if __name__ == "__main__":
    main()
