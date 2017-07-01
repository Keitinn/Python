weight = input('体重(キロ単位)を入力してください')
height = input('身長(メートル単位)を入力してください')
bmi = float(weight) / (float(height) **  2)

if bmi < 18.5:
    print(bmi)
    print ('やせている')
elif bmi < 25:
    print(bmi)
    print ('ふつう')
elif bmi < 35:
    print(bmi)
    print ('ちょっと太っている')
else:
    print(bmi)
    print ('だいぶ太っている')
