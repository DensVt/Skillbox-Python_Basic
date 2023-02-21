zipped = zip('abcd', (10, 20, 30, 40))
print("Результат: ", list(zipped), sep='\n')


"""
text = 'abcd'; value = (10, 20, 30, 40)
zipped = ((text[elem], value[elem]) for elem in range(min(len(text), len(value))))

print("Результат: ", zipped, sep='\n')
print(*zipped, sep='\n')
"""
