weight = input('体重(キロ単位)を入力してください: ')
height = input('身長(メートル単位)を入力してください: ')
bmi = print('あなたのBMI値は 'float(weight) / (float(height) ** 2)'です。')

if bmi < 18.5:
    print ('やせている')

elif bmi < 25:
    print ('ふつう')
elif bmi < 35:
    print ('ちょっと太っている')
else:
    print ('だいぶ太っている')
