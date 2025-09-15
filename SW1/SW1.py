def exhange(USD):
    USD=float(USD)
    php =USD * 57.17
    phpLimit = round(php,2)
    print(f"{USD} D = {phpLimit} Pesos")
    yen =USD * 146.67
    yenLimit = round(yen,2)
    print(f"{USD} D = {yenLimit} Yen")


num = (float(input("Enter currency in ($)")))

exhange(num)

def convert_currency(usd):
    peso = usd *57.17
    yen = usd * 146.67
    return peso,yen

input = str(input("Enter Number: "))

usd_values = input.split(",")

print("Dollar($)\tPeso(P)\t        Yen (Y)")

for val in usd_values:
    usd = int(val.strip())
    peso,yen=convert_currency(usd)
    print(f"{usd:<10}\t{peso:<12.2f}\t{yen:.2f}")