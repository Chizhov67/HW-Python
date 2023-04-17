LETTERS_VALUES = {
    1: 'AEIOULNSTRАВЕИНОРСТ',
    2: 'DGДКЛМПУ',
    3: 'BCMPБГЁЬЯ',
    4: 'FHVWYЙЫ',
    5: 'KЖЗХЦЧ',
    8: 'JXШЗЮ',
    10: 'QZФЩЪ'
       }
word = input('Введите слово: ')
word_value = 0
for letter in word:
 for letter_value, letters in LETTERS_VALUES.items():
  if letter in letters:
   word_value = word_value + letter_value
print(f'Стоимость слова {word}: {word_value}')