exp = input("Expression: ").strip()
exp1 = exp.split()

x = int(exp1[0])
y = exp1[1]
z = int(exp1[2])

match y:
    case "+":
        ans = float(x + z)
    case "-":
        ans = float(x - z)
    case "*":
        ans = float(x * z)
    case "/":
        ans = float(x / z)
    case _:
        ans = "Invalid operator"

print(f"{ans:.1f}")

#check50 cs50/problems/2022/python/interpreter
#submit50 cs50/problems/2022/python/interpreter