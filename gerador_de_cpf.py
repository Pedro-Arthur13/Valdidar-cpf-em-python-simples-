import random

def calcular_primeiro_digito(cpf_formatado):
    soma = 0
    for i in range(0,9):
        soma += int(cpf_formatado[i])*(10-i)
    primeiro_digito = (soma*10)%11
    primeiro_digito = primeiro_digito if primeiro_digito<= 9 else 0
    return primeiro_digito

def formatar_cpf(cpf_gerado):
    cpf_formatado = ""
    for i in range(len(cpf_gerado)):
        if i == 3 or i == 6:
            cpf_formatado += "."
        if i == 9:
            cpf_formatado += "-"
        cpf_formatado += cpf_gerado[i]
    return cpf_formatado
            

def calcular_segundo_digito(cpf_formatado,primeiro_digito):
    soma = 0
    cpf_formatado_2 = cpf_formatado[:9]
    cpf_formatado_2 += str(primeiro_digito)
    for i in range(0,10):
        soma += int(cpf_formatado_2[i])*(11-i)
    segundo_digito = (soma*10)%11
    segundo_digito = segundo_digito if segundo_digito<= 9 else 0
    return segundo_digito
def gerar_9_digitos():
    nove_digitos = ""
    for i in range(9):
        nove_digitos += str(random.randint(0,9))
    return nove_digitos
# cpf = input("Insira seu CPF: ")
nove_digitos = gerar_9_digitos()
primeiro_digito = calcular_primeiro_digito(nove_digitos)
segundo_digito = calcular_segundo_digito(nove_digitos,primeiro_digito)
cpf_gerado = nove_digitos + str(primeiro_digito) + str(segundo_digito)
print(cpf_gerado)
print(f"CPF formatado: {formatar_cpf(cpf_gerado)}")
