from sys import argv

scrip, filename = argv

txt = open(filename)

print(f"Here's your {filename}:")
print(txt.read())
txt.close()

print(f"Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
