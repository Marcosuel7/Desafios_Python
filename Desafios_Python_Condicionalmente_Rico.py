print("Informe seu saldo: ")
saldo_total = int(input())
print("Dgite o valor a ser sacado: ")
valor_saque = int(input())

if valor_saque <= saldo_total :
    saldo_total -= valor_saque
    print(f"Saque realizado com sucesso! Novo saldo: {saldo_total}")
else:
    print("Saldo insuficiente. Saque nao realizado!")