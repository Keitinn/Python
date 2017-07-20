weight = input('体重(キログラム単位)を入力してください: ')
height = input('身長(メートル単位)を入力してください: ')
bmi = float(weight) / (float(height) ** 2)

if bmi < 18.5:
    a = round(bmi, 2)
    style = 'やせています\n'
elif bmi < 25:
    a = round(bmi, 2)
    style = 'ふつう体型です\n'
elif bmi < 35:
    a = round(bmi, 2)
    style = 'すこし太っています\n'
else:
    a = round(bmi, 2)
    style = 'だいぶ太っています\n'

b = 'あなたは '

print(b + style)
print('あなたのBMI: ')
print(a)
