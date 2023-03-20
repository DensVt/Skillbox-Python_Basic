import requests
import re
import json

resopone = requests.get('http://www.columbia.edu/~fdc/sample.html')

# resopone = requests.get('https://convertmonster.ru/blog/seo-blog/html-tegi-h1-h2-h3-h4-h5-h6-zagolovki/')

# resopone = requests.get('https://www.techonthenet.com/html/elements/h3_tag.php')

h3_tags = re.findall(r'<h3.*?>(.*?)</h3>', resopone.text)
json_data = json.dumps(h3_tags, ensure_ascii=False)

print(json_data)
