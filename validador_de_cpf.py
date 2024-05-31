import re
#re = regular expression

# Validar CPF: Código básico

# O replace faz basicamente isso:
# def formatar_cpf(cpf):
#     cpf_formatado = ""
#     for i in range(len(cpf)):
#         if cpf[i] != "." and cpf[i] != "-":
#             cpf_formatado += str(cpf[i])
#     return cpf_formatado

def calcular_primeiro_digito(cpf_formatado):
    soma = 0
    for i in range(0,9):
        soma += int(cpf_formatado[i])*(10-i)
    primeiro_digito = (soma*10)%11
    primeiro_digito = primeiro_digito if primeiro_digito<= 9 else 0
    return primeiro_digito

def calcular_segundo_digito(cpf_formatado,primeiro_digito):
    soma = 0
    cpf_formatado_2 = cpf_formatado[:9]
    cpf_formatado_2 += str(primeiro_digito)
    for i in range(0,10):
        soma += int(cpf_formatado[i])*(11-i)
    segundo_digito = (soma*10)%11
    segundo_digito = segundo_digito if segundo_digito<= 9 else 0
    return segundo_digito

cpf = input("Insira seu CPF: ")

# cpf_formatado = cpf.replace(".","").replace("-","")
cpf_formatado = re.sub(r"[^0-9]","",cpf) # Isso faz com que retire tudo de 0 à 9 que não seja um número
# Verificar se o que o usuario mando é idêntico (111.111.111-11):
if cpf_formatado == cpf_formatado[0] * len(cpf_formatado):
    print("CPF sequencial inválido")
    exit()
primeiro_digito = calcular_primeiro_digito(cpf_formatado)
segundo_digito = calcular_segundo_digito(cpf_formatado,primeiro_digito)
if int(cpf_formatado[-1]) == segundo_digito and int(cpf_formatado[-2]) == primeiro_digito:
    print("O cpf é válido")
else:
    print("O cpf é inválido")
    
