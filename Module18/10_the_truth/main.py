def decryption(message):
    translated = ""
    for elem in message:
        if elem in letters:
            num_index = letters.find(elem)
            translated += letters[num_index -1]
        else:
            translated += elem
    return translated

def shift(text, key):
    word = len(text)
    shift = key % word
    text = text[-shift:] + text[:-shift]
    return text

text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/' \
       'dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/' \
       'ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju ' \
       'fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj ' \
       'gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ ' \
       'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /' \
       'ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq' \
       ' tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ ' \
       'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'.split()

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

text_2 = []
key = 3
for elem in text:
    text_decryption = decryption(elem)
    shift_text = shift(text_decryption, key)
    if shift_text.endswith("/"):
        key += 1
        text_2.append(shift_text)
    else:
        text_2.append(shift_text)

text_2 = " ".join(text_2)
text_2 = text_2.replace("+", "*")
text_2 = text_2.replace("-", ",")
text_2 = text_2.replace("(", "'")
text_2 = text_2.replace("..", "--")
text_2 = text_2.replace('"', "!")
text_2 = text_2.replace("/", ".\n")

print(text_2)


print("""\nКрасивое лучше, чем уродливое.
Явное лучше, чем неявное.
Простое лучше, чем сложное.
Сложный лучше, чем сложный.
Плоский лучше, чем вложенный.
Разреженный лучше, чем плотный.
Удобство чтения имеет значение.
Особые случаи не настолько особенные, чтобы нарушать правила.
Хотя практичность превосходит чистоту.
Ошибки никогда не должны проходить молча.
Если явно не замолчать.
Перед лицом двусмысленности откажитесь от искушения угадать.
Должен быть один - и желательно только один - очевидный способ сделать это.
Хотя поначалу это может показаться неочевидным, если вы не голландец.
Сейчас лучше, чем никогда.
Хотя "никогда" часто бывает лучше, чем "прямо" сейчас.
Если реализацию сложно объяснить, это плохая идея.
Если реализацию легко объяснить, это может быть хорошей идеей.
Пространства имен - это отличная идея - давайте сделаем больше таких!""")