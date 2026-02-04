import os
import subprocess
import re

def get_rich_summary(filename, text):
    # This function is a placeholder for the logic I'll give to the sub-agent.
    # The sub-agent will use its internal model to transform 'text' into a rich summary.
    pass

def process_batch(file_list):
    base_url = "http://seismology.gl.ntu.edu.tw/"
    repo_path = "/tmp/knowledge_repo_sub"
    dir_path = "papersummaries/ntu_seismo_lab_papers"
    
    results = []
    for md_file in file_list:
        md_path = os.path.join(repo_path, dir_path, md_file)
        with open(md_path, 'r') as f:
            content = f.read()
            
        # Extract PDF URL
        match = re.search(r'http://seismology\.gl\.ntu\.edu\.tw/papers/([^\s]+)', content)
        if not match:
            continue
            
        pdf_url = match.group(0)
        pdf_name = match.group(1)
        
        # Download and extract text
        tmp_pdf = f"/tmp/{pdf_name}"
        tmp_txt = f"/tmp/{pdf_name}.txt"
        subprocess.run(["curl", "-s", "-L", pdf_url, "-o", tmp_pdf])
        subprocess.run(["pdftotext", "-l", "1", tmp_pdf, tmp_txt])
        
        extracted_text = ""
        if os.path.exists(tmp_txt):
            with open(tmp_txt, 'r', errors='ignore') as tf:
                extracted_text = tf.read().strip()
        
        results.append({
            "file": md_file,
            "text": extracted_text,
            "url": pdf_url
        })
    return results

if __name__ == "__main__":
    import json
    import sys
    files = sys.argv[1:]
    data = process_batch(files)
    print(json.dumps(data))
