# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке

# *Пример:*

# **Ввод:** па-ра-ра-рам рам-пам-па-пам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def count_syllables(sentence):
    vowels = "уеыаоэиюя"
    words = sentence.split("-")
    syllables = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if letter in vowels:
                num_vowels += 1
        if num_vowels > 1:
            syllables += num_vowels
        else:
            syllables += 1
    return syllables

poem = 'пара-ра-рам рам-пам-папам па-ра-па-да'

phrases = poem.split()

syllables_list = []

for phrase in phrases:
    syllables = count_syllables(phrase)
    syllables_list.append(syllables)

print(syllables_list)

if len(set(syllables_list)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")

"""вариант с семинара"""

def rythm_check(phrase: str) -> str:
    vovels = "уеыаоэиюя"
    vovels_count = set(map(lambda x: sum(1 for let in vovels)))
    if len(vovels_count) == 1:
        return 'Парам пам-пам'
    return 'Пам парам'

lirics = 'пара-ра-рам рам-пам-папам па-ра-па-да'
print(rythm_check(lirics))