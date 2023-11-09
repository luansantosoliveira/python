print("CALCULADORA DE META FINANCEIRA COM ECONOMIA MENSAL")

print("\n---> Neste programa, você define uma META FINANCEIRA e calcula o tempo que levará para ela ser atingida, com base em uma ECONOMIA MENSAL pré-definida.")

print("\nETAPA 1 - DEFINIÇÃO DA META FINANCEIRA")

def meta_fin():
    meta = float(input("\n---> Defina o valor que deseja atingir na sua META FINANCEIRA: R$ "))
    return meta

meta = meta_fin()

print("\nETAPA 2 - DEFINIÇÃO DA ECONOMIA MENSAL")

def econ():
    economia = float(input("\n---> Forneça um valor que você possa economizar mensalmente: R$ "))
    return economia

economia = econ()

tempo = meta / economia

print("\nETAPA 3 - APRESENTAÇÃO DOS RESULTADOS")

def results():
    print(f"\n---> O tempo estimado para atingir a sua META FINANCEIRA de R$ {meta:.2f} com uma ECONOMIA MENSAL de R$ {economia:.2f} será de: {tempo:.1f} MESES.")

resultados = results()

input("\nPressione ENTER para ENCERRAR O PROGRAMA...")

print("\nPrograma desenvolvido por Luan Santos Oliveira (luansantosoliveira14@gmail.com) como Projeto Final do Módulo 2 - Desenvovimento Web do Programa Match!, uma parceria da Mastertech com a IBM.")
