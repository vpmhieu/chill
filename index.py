import requests
from bs4 import BeautifulSoup
import os
import json

#  python3 -m venv path/to/venv
# source path/to/venv/bin/activate
# python3 -m pip install xyz
# pip install --upgrade pip
# pip3 install requests
#  python3 index.py

# a=1
# for i in range(1,100):
#     print(i)
#     URL = "https://truyenfull.io/xich-tam-tuan-thien/chuong-"+str(i)+"/"
#     r = requests.get(url = URL)
#     html_content=r.text
#     soup = BeautifulSoup(html_content, "html")
#     box_chap_div = soup.find("div",{"class":"chapter-c"})
#     box_chap_tit = soup.find("a",{"class":"chapter-title"})
#     content = box_chap_tit.get_text(separator="$$$$").strip() + "$$$$" + box_chap_div.get_text(separator="$$$$").strip()
#     path = "xichtam/"+str(a)+"/"+str(i)+".txt"
#     os.makedirs(os.path.dirname(path), exist_ok=True)
#     with open(path, "w") as f:
#         f.write(content)
def find_substring_first_occurrence(string, A, B):
    start_index = string.find(A)
    if start_index == -1:
        return None  # Không tìm thấy A

    try:
        end_index = string.index(B, start_index)
        return string[start_index:end_index + len(B)]
    except ValueError:
        return None  # Không tìm thấy B sau A
    
m = ""
for a in range(1,93):
    URL = "https://truyendocviet.io.vn/doc-truyen/co-duyen-cua-nguoi-rat-tot-ta-vui-long-nhan/read/chapters.html/"+str(a)+".html"
    r = requests.get(url = URL)
    html_content=r.text
    content = find_substring_first_occurrence(html_content,'"arrChapters":',',"arrDocuments')
    content = content[14:len(content)-14]
    idx = content.find("CreatedDate")
    while idx > 0:
        content = content[0:idx-1] + content[idx+50:len(content)]
        idx = content.find("CreatedDate")
    obj = json.loads(content)
    for index, value in enumerate(obj):
        print("Quyển " + str(a) + " - chap " + str(index+1))
        URL = "https://truyendocviet.io.vn/doc-truyen/co-duyen-cua-nguoi-rat-tot-ta-vui-long-nhan/read/"+value['_id']+".html"
        r = requests.get(url = URL)
        html_content=r.text
        ncont = find_substring_first_occurrence(html_content,'"CurrentChapter":','ContentOrder')
        lcont = find_substring_first_occurrence(ncont,'ContentTitle":',',"Description')
        lcont = lcont[15:len(lcont)-14]
        print(lcont)
        ncont = find_substring_first_occurrence(ncont,'"Description":','ContentOrder')
        ncont = ncont[15:len(ncont)-15]
        ncont = ncont.replace(r'\n', '\n\n').replace('\\', '')
        lcont = lcont.replace(r'\n', '\n\n').replace('\\', '')
        path = "co-duyen-cua-nguoi-rat-tot-ta-vui-long-nhan/"+str(a)+"/"+str(index+1)+".txt"
        m = m + str(a) + "_" + str(index+1) + "=" + lcont + "\n"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(ncont)
with open("co-duyen-cua-nguoi-rat-tot-ta-vui-long-nhan/mucluc.txt", "w") as f:
  f.write(m)
    # print(content)