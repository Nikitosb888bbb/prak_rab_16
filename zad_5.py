adr_1 = set(input('Введите IP-адреса 1: ').split())
adr_2 = set(input('Введите IP-адреса 2: ').split())
adr_3 = set(input('Введите IP-адреса 3: ').split())

all_adr = adr_1 | adr_2 | adr_3
in_all_three = adr_1 & adr_2 & adr_3

suspicious = all_adr - in_all_three

print(' '.join(sorted(suspicious)))
