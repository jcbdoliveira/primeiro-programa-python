from datetime import date

ano_atual = date.today()
ANO_NASCIMENTO = date(1980, 4, 27)

print(ano_atual.year)
print(ANO_NASCIMENTO.year)

idade = ano_atual.year - ANO_NASCIMENTO.year #variável
NOME = "Julio Cesar" #constante

print(f'Meu nome é {NOME}, tenho {idade} anos de idade')