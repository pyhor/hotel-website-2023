import os
import re

dir_path = r"c:\my project\hotel-website-2023\Ojingeo-Hotel"
for filename in os.listdir(dir_path):
    if filename.endswith(".html"):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace href="something.html" -> href="something"
        # Excludes http, mailto, tel, etc.
        new_content = re.sub(r'href="((?!http|mailto|tel)[^"]+)\.html"', r'href="\1"', content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

# Fix root index.html
root_index = r"c:\my project\hotel-website-2023\index.html"
with open(root_index, 'r', encoding='utf-8') as f:
    content = f.read()
new_content = content.replace('Ojingeo-Hotel/home.html', 'Ojingeo-Hotel/home')
with open(root_index, 'w', encoding='utf-8') as f:
    f.write(new_content)
