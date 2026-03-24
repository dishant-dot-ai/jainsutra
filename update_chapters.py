import sys
import re
import os

def process_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Add CSS classes to <style> if missing
    STYLE_ADDITION = '''
      .simple-explanation { 
        margin-top: 1rem;
        padding-top: 1rem;
        border-top: 1px dashed rgba(201,168,76,0.3);
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        line-height: 1.7;
        color: #4d4637;
      }
      .simple-explanation b { color: #755b00; font-weight: 600; }
      .contemplation-box {
        margin-top: 1.5rem;
        padding: 1.5rem;
        background: rgba(117,91,0,0.03);
        border-left: 2px solid #c9a84c;
      }
      .contemplation-box h5 {
        font-family: 'Noto Serif', serif;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        color: #755b00;
        margin-bottom: 0.75rem;
      }
      .contemplation-box p {
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        color: #1d1c17;
        font-style: italic;
        line-height: 1.7;
      }
    '''
    if '.simple-explanation' not in content:
        content = content.replace('</style>', STYLE_ADDITION + '</style>')

    # 2. Process each Sutra <article>
    # We look for <article ... id="sutra-X"> ... </article>
    # We find the last <p> or </div> before </article> ends and insert the new parts.
    
    # This is complex to do purely by regex because we need unique content for each sutra.
    # I will have to provide the mapping or do it manually for high quality.
    # However, I can automate the STRUCTURE and then fill in.
    
    # Since I need to do this for ALL sutras, I will generate the full content for a few chapters first.
    
    with open(file_path, 'w') as f:
        f.write(content)

process_file(sys.argv[1])
