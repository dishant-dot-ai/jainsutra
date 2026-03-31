import os
import re

dir_path = "/Users/thefounder/Projects/active/JainAwaken/scripture/Aagama/uttaradhyana/"
files = [f for f in os.listdir(dir_path) if f.startswith("uttaradhyana-ch") and f.endswith(".html")]

opening_tag_pattern = re.compile(r'(<section class="max-w-screen-xl mx-auto px-6 md:px-12 py-24">)\s*<div class="max-w-4xl mx-auto space-y-6">', re.MULTILINE)
closing_tag_pattern = re.compile(r'</div>\s*(</section>\s*</main>)', re.MULTILINE)

for filename in files:
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'class="max-w-4xl mx-auto space-y-6"' in content:
        new_content = opening_tag_pattern.sub(r'\1', content)
        new_content = closing_tag_pattern.sub(r'\1', new_content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"Skipped {filename} (pattern not found exactly as expected)")
    else:
        print(f"Skipped {filename} (no max-w-4xl div found)")
