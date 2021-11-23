print('''
                                                                      
  ,d    88              ,d                            ,d                          88
  88                    88                            88                          88
MM88MMM 88  ,adPPYba, MM88MMM ,adPPYYba,  ,adPPYba, MM88MMM ,adPPYba,   ,adPPYba, 88
  88    88 a8"     ""   88    ""     `Y8 a8"     ""   88   a8"     "8a a8P_____88 88
  88    88 8b           88    ,adPPPPP88 8b           88   8b       d8 8PP""""""" 88
  88,   88 "8a,   ,aa   88,   88,    ,88 "8a,   ,aa   88,  "8a,   ,a8" "8b,   ,aa  
  "Y888 88  `"Ybbd8"'   "Y888 `"8bbdP"Y8  `"Ybbd8"'   "Y888 `"YbbdP"'   `"Ybbd8"' 88
  
''')

row1 = list('   a     b     c')
row2 = list('      |     |     ')
row3 = list('1  -  |  -  |  -  ')
row4 = list(' _____|_____|_____')
row5 = list('2  -  |  -  |  -  ')
row6 = list(' _____|_____|_____')
row7 = list('3  -  |  -  |  -  ')
row8 = list('      |     |     ')

rowa = ''
rowb = ''
rowc = ''
rowd = ''
rowe = ''
rowf = ''
rowg = ''
rowh = ''


tictactoe = [row1, row2, row3, row4, row5, row6, row7, row8]
print(f'{rowa.join(row1)}\n{rowb.join(row2)}\n{rowc.join(row3)}\n{rowd.join(row4)}\n{rowe.join(row5)}\n{rowf.join(row6)}\n{rowg.join(row7)}\n{rowh.join(row8)}')

# letter tells me about column 3, 9 or 15
# number tells me about row 1(row3), 2(row5) or 3(row7)

player = 'b2'

col = player[0]
row = player[1]

print(col)
print(row)

if col == 'a':
    col = 3
elif col == 'b':
    col = 9
else:
    col = 15

if row == '1':
    row3[col] = 'O'
elif row == '2':
    row5[col] = 'O'
else:
    row7[col] = 'O'

print(f'{rowa.join(row1)}\n{rowb.join(row2)}\n{rowc.join(row3)}\n{rowd.join(row4)}\n{rowe.join(row5)}\n{rowf.join(row6)}\n{rowg.join(row7)}\n{rowh.join(row8)}')
