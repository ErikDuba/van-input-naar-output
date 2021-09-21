#Erik Duba Pizza Calculator

smallPizza  = 8.5       #20cm
mediumPizza = 13.99     #30cm
largePizza  = 18.49     #40cm

print ('Kleine pizza 20 cm  €8.5 \nMedium 30 cm en €13.99 \nGrote pizza 40 cm €18.49')

aantal_smalls = int(input('Hoeveel kleine pizzas wilt u?: '))
aantal_mediums = int(input('Hoeveel medium pizzas wilt u?: '))
aantal_larges = int(input('Hoeveel grote pizzas wilt u?: '))
kosten = float(aantal_smalls * smallPizza) + (aantal_mediums * mediumPizza) + (aantal_larges * largePizza)

print('Dan kost het: €' + str(kosten))
