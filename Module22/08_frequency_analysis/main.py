import re
from collections import Counter

with open("text.txt", "w", encoding="utf-8") as text:
    text.write("Mama myla ramu.")

with open("text.txt", "r", encoding="utf-8") as text:
    f = ''
    for line in text:
        f += line
    g = Counter(re.findall('[a-z]', f.lower()))

with open("analysis.txt", "w", encoding="utf-8") as analysis:
    for elem in g:
        analysis.write(f'{elem} {g[elem] / sum(g.values()):.3f}\n')


