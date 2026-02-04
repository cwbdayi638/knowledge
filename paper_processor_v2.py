import os
import subprocess
import time

def process_papers():
    base_url = "http://seismology.gl.ntu.edu.tw/"
    paths_file = "/tmp/pdf_paths_sub.txt"
    repo_path = "/tmp/knowledge_repo_sub"
    
    if not os.path.exists(paths_file):
        print("Error: pdf_paths_sub.txt not found.")
        return

    with open(paths_file, "r") as f:
        paths = [line.strip() for line in f.readlines()]

    # Check how many are already there
    summaries_dir = f"{repo_path}/paper_summaries"
    if not os.path.exists(summaries_dir):
        os.makedirs(summaries_dir)
    
    existing_files = os.listdir(summaries_dir)
    processed_count = len([f for f in existing_files if f.startswith("0") or f.startswith("1") or f.startswith("2")])
    
    # We want to start from the next one. 
    # Current processed: 001-005. So start_index = 5.
    start_index = 5
    batch_size = 5
    
    for i in range(start_index, len(paths), batch_size):
        batch = paths[i:i+batch_size]
        print(f"Processing batch {i//batch_size + 1} (Indices {i} to {i+len(batch)-1})...")
        
        for path in batch:
            filename = os.path.basename(path)
            pdf_path = f"/tmp/{filename}"
            txt_path = f"/tmp/{filename.replace('.pdf', '.txt')}"
            md_filename = filename.replace(".pdf", ".md")
            md_path = f"{summaries_dir}/{md_filename}"
            
            if os.path.exists(md_path):
                continue

            # 1. Download PDF
            subprocess.run(["curl", "-s", "-L", f"{base_url}{path}", "-o", pdf_path])
            
            # 2. Convert to Text (Page 1)
            subprocess.run(["pdftotext", "-l", "1", pdf_path, txt_path])
            
            summary_text = ""
            if os.path.exists(txt_path):
                with open(txt_path, "r", errors='ignore') as tf:
                    summary_text = tf.read().strip()
            
            # 3. Create MD summary
            with open(md_path, "w") as mf:
                mf.write(f"# 論文摘要：{filename}\n\n")
                mf.write(f"## 1. 基礎資訊\n- **檔案名稱**: {filename}\n- **原始連結**: {base_url}{path}\n\n")
                mf.write(f"## 2. 內容摘錄 (第一頁)\n```text\n{summary_text[:3000]}\n```\n\n")
                mf.write(f"---\n*自動生成日期: {time.strftime('%Y-%m-%d')}*\n")

        # 4. Commit and Push
        os.chdir(repo_path)
        subprocess.run(["git", "config", "user.email", "cwbdayi@gmail.com"])
        subprocess.run(["git", "config", "user.name", "cwbdayi638"])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", f"Add summaries for papers {i+1} to {i+len(batch)}"])
        subprocess.run(["git", "push", "origin", "main"])
        
        print(f"Pushed batch {i//batch_size + 1} to GitHub.")
        # Pause slightly to avoid rate limits or overlap
        time.sleep(5)

if __name__ == "__main__":
    process_papers()
