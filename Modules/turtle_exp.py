import turtle as t

# pip install turtle

def square():
    for i in range(4):
        t.forward(100)
        t.left(90)

def main():
    t.shape("turtle")
    t.speed(0)
    for i in range(100):
        square()
        t.left(11)
    t.done()
main()

