salario = float(input('Qual é o salário do funcionário? R$ '))
aumento1 = (15 * salario)/100 + salario
aumento2 = (10 * salario)/100 + salario
if salario <= 1225.00:
    print(f'Quem ganhava {salario} passa a ganhar {aumento1:.2f} agora. ')
if salario > 1225.00:
    print(f'Quem ganhava {salario} passa a ganhar {aumento2:.2f} agora. ')
