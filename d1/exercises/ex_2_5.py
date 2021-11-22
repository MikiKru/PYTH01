height = 1.82
weight = 50

bmi = weight / (height ** 2)
good_weight_low = 18.5 * (height ** 2)
good_weight_high = 24.99 * (height ** 2)

if(bmi < 16.00 ):
    print(f'wygłodzenie, twoja waga powinna być w zakresie od {good_weight_low} do {good_weight_high}')
elif(bmi <= 16.99):
    print(f'wychudzenie, twoja waga powinna być w zakresie od {good_weight_low} do {good_weight_high}')
elif (bmi <= 18.49):
    print(f'niedowaga, twoja waga powinna być w zakresie od {good_weight_low} do {good_weight_high}')
elif (bmi <= 24.99):
    print(f'waga prawidłowa, twoja waga powinna być w zakresie od {good_weight_low} do {good_weight_high}')
elif (bmi <= 29.99):
    print(f'nadwaga, twoja waga powinna być w zakresie od {good_weight_low} do {good_weight_high}')
elif (bmi <= 34.99):
    print(f'otylosc 1 stopnia, twoja waga powinna być w zakresie od {good_weight_low} do {good_weight_high}')
elif (bmi <= 39.99):
    print(f'otylosc 2 stopnia, twoja waga powinna być w zakresie od {good_weight_low} do {good_weight_high}')
else:
    print(f'otyłość 3 stopnia, twoja waga powinna być w zakresie od {good_weight_low} do {good_weight_high}')
