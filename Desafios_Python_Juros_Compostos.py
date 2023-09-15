valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial


while (periodo >= 1) :
    valor_final += valor_inicial * taxa_juros
    periodo = periodo - 1
    
    valor_inicial = valor_final

  ## //TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.
print(f"Valor final do investimento: R$ {valor_inicial:.2f}")
