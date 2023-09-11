print('Olá! Para esta operação será necessário seus dados para a aprovação do empréstimo.'
      ' Informe-os a seguir')
casa = float(input('Valor do imóvel: R$'))
sala = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prest = casa / (anos*12)
mínimo = sala <= 30/100
print('Para pagar um imóvel de R${:.2f} em {} anos '.format(casa, anos), end='')
print('a prestação mensal será de R${:.2f}.'.format(prest))
if prest <= mínimo:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')