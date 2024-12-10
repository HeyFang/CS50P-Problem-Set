def main():
    mass = int(input("Enter the mass(in kg): "))
    einstein(mass)

def einstein(mass):
    energy = mass * 300000000 ** 2
    print(energy)

main()