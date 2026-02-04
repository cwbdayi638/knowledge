mkdir -p /tmp/pdf_batch
BASE_URL="http://seismology.gl.ntu.edu.tw/"
PATHS=("papers/001_1997_Teng_et_al_BSSA_EWS.pdf" "papers/002_1997_Wu_et_al_SRL_EWS.pdf" "papers/003_1998_Wu_et_al_BSSA_EWS.pdf" "papers/004_1999_Wu_et_al_TAO_EWS.pdf" "papers/005_2000_Chang_et_al_TAO_Chi-Chi.pdf")

for i in "${!PATHS[@]}"; do
  path="${PATHS[$i]}"
  filename=$(basename "$path")
  echo "Processing $filename..."
  curl -s -L "${BASE_URL}${path}" -o "/tmp/pdf_batch/$filename"
  pdftotext -l 1 "/tmp/pdf_batch/$filename" "/tmp/pdf_batch/${filename%.pdf}.txt"
done
