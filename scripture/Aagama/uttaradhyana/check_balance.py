import os

dir_path = "/Users/thefounder/Projects/active/JainSutra/scripture/Aagama/uttaradhyana/"
files = [f for f in os.listdir(dir_path) if f.startswith("uttaradhyana-ch") and f.endswith(".html")]

for filename in files:
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    div_opens = content.count("<div")
    div_closes = content.count("</div")
    section_opens = content.count("<section")
    section_closes = content.count("</section")
    
    if div_opens != div_closes or section_opens != section_closes:
        print(f"{filename}: div({div_opens}/{div_closes}), section({section_opens}/{section_closes})")
