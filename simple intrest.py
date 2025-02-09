def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
p=float(input("enter the principle"))
r=float(input("enter the rate"))
t=float(input("enter the time"))
print("Simple Interest (p, r, t):", simple_interest(p, r, t))
