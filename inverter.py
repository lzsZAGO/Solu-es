def inverter_string(string):
    palavra_string = ''
    for char in string:
        palavra_string = char + palavra_string
    return palavra_string

texto = input("Informe uma String: ")
print("String invertida:", inverter_string(texto))