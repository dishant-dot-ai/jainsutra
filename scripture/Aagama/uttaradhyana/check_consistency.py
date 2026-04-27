import os
import re

files = [
    "uttaradhyana-ch1.html", "uttaradhyana-ch2.html", "uttaradhyana-ch4.html",
    "uttaradhyana-ch5.html", "uttaradhyana-ch6.html", "uttaradhyana-ch7.html",
    "uttaradhyana-ch8.html", "uttaradhyana-ch9.html", "uttaradhyana-ch10.html",
    "uttaradhyana-ch11.html", "uttaradhyana-ch12.html", "uttaradhyana-ch13.html",
    "uttaradhyana-ch14.html", "uttaradhyana-ch15.html"
]

base_dir = "/Users/thefounder/Projects/active/JainSutra/scripture/Aagama/uttaradhyana/"

def check_file(filename):
    path = os.path.join(base_dir, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []

    # 1. About This Chapter BG
    # <section class="bg-surface-container-low py-24 border-y border-primary/5">
    if '<section class="bg-surface-container-low py-24 border-y border-primary/5">' not in content:
        issues.append("Condition 1: About This Chapter BG class mismatch")

    # 2. Sutra Section Width
    # <section class="max-w-screen-xl mx-auto px-6 md:px-12 py-24">
    if '<section class="max-w-screen-xl mx-auto px-6 md:px-12 py-24">' not in content:
        issues.append("Condition 2: Sutra Section Width class mismatch")
    
    # Check for nested max-w-4xl inside the sutra section
    sutra_section_match = re.search(r'<section class="max-w-screen-xl mx-auto px-6 md:px-12 py-24">(.*?)</section>', content, re.DOTALL)
    if sutra_section_match:
        sutra_content = sutra_section_match.group(1)
        if 'max-w-4xl' in sutra_content:
            # Check if it's a div wrapping the whole thing or just a small part
            # Actually the requirement says "NO nested max-w-4xl div"
            if '<div class="max-w-4xl mx-auto">' in sutra_content:
                issues.append("Condition 2: Nested max-w-4xl found")

    # 3. End of Chapter Signature
    # <div class="section-divider"><span>॥ अध्ययन-X सम्पूर्ण ॥</span></div>
    if '<div class="section-divider"><span>॥ अध्ययन-' not in content:
         if 'inline-flex items-center gap-4' in content:
             issues.append("Condition 3: End signature uses old inline-flex style")
         else:
             issues.append("Condition 3: End signature missing or malformed")

    # 4. Tag balance for sutra section
    # Simple count check for the sutra section
    sections = re.findall(r'<section', content)
    end_sections = re.findall(r'</section>', content)
    if len(sections) != len(end_sections):
        issues.append(f"Tag balance: <section> count ({len(sections)}) != </section> count ({len(end_sections)})")

    return issues

for f in files:
    errs = check_file(f)
    if errs:
        print(f"{f}:")
        for e in errs:
            print(f"  - {e}")
    else:
        print(f"{f}: OK")
