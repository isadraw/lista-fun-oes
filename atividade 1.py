def temperatura (celcius):
    return (9 * celcius) / 5 + 32


celcius = float(input("qual a sua temperatura em celcius?"))

fah = temperatura(celcius)

print("sua temperatura convertida é", fah)