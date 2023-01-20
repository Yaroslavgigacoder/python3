text = 'Напишите проабвграмму удаляющую из текста вабвсе слова содержабвщие'
def delete_words(text2):
    list = text2.split()
    for el in list:
        if 'абв' in el:
            list.remove(el)
    return list
print(' '.join(delete_words(text)))