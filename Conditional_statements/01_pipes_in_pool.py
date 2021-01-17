v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

pipe1 = p1 * h
pipe2 = p2 * h
total_pipes = pipe1 + pipe2

if total_pipes <= v:
    print(f'The pool is {total_pipes / v * 100:.2f}% full. Pipe 1: {pipe1 / total_pipes * 100:.2f}%. Pipe 2: {pipe2 / total_pipes * 100:.2f}%."')
else:
    print(f'For {h} hours the pool overflows with {abs(total_pipes - v):.2f} liters.')