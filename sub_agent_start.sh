# 自動化處理腳本
# 此腳本由子代理人執行

cd /tmp
git clone https://github.com/cwbdayi638/knowledge.git /tmp/knowledge_repo_sub
cd /tmp/knowledge_repo_sub

# 下載論文路徑列表
curl -s http://seismology.gl.ntu.edu.tw/publications.htm | grep -oE "papers/[^\"'>]+\.pdf" | sort | uniq > /tmp/pdf_paths_sub.txt

# 修改 paper_processor.py 的路徑
# (我直接在主 session 寫好正確路徑的 script)

python3 /home/node/.openclaw/workspace/paper_processor_v2.py
