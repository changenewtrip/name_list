names = []

while True:
    name = input("Enter the names you want, Or type EXIT to finish. : ")

    if name == "exit":
        break

    names.append(name)

print("Registered names:")
print(names)
