import requests
import json






# print(json.dumps(content, indent=1))

# print(content["rates"]["TRY"])


def Menu():
    baseBP = input("Bozduracağınız Para Birimini Seçiniz: ").upper()
    takenBP = input("Alacağınız Para Birimini Seçiniz: ").upper()
    miktar = int(input(f"Ne Kadar {baseBP} Bozdurmak İstersiniz: "))
    print(f"1 {baseBP} = {getter(baseBP, takenBP)} {takenBP} ")
    print(f"Alacığınız {takenBP} = {miktar * float(getter(baseBP, takenBP))} ")
    

def getter(baseBP, takenBP):
    url = requests.get(f"https://api.exchangeratesapi.io/latest?base={baseBP}")
    content = json.loads(url.text)
    return content["rates"][takenBP]

Menu()