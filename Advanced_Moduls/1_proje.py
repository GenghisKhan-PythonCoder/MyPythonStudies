import os

mp4_list = []
txt_list = []
pdf_list = []

for folder_path,folder_name,file_name in os.walk("C:/Users/User"):
    for mp4 in file_name:
        if (mp4.endswith(".mp4")):
            mp4_list.append(mp4)
    for txt in file_name:
        if (txt.endswith(".txt")):
            txt_list.append(txt)
    for pdf in file_name:
        if (pdf.endswith(".pdf")):
            pdf_list.append(pdf)

def write(i):
    return i + "\n"

with open("files_of_mp4.txt","w",encoding="utf-8")as file_mp4:
    for i in mp4_list:
        file_mp4.write(write(i))
with open("files_of_txt.txt","w",encoding="utf-8")as file_txt:
    for i in txt_list:
        file_txt.write(write(i))
with open("files_of_pdf.txt","w",encoding="utf-8")as file_pdf:
    for i in pdf_list:
        file_pdf.write(write(i))