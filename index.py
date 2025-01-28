import os


#  python3 -m venv path/to/venv && source path/to/venv/bin/activate
#  python3 index.py
# Đường dẫn đến folder chứa các file txt
path = "truong-sinh-bat-dau-tu-tap-dich-nuoi-ga/"

# Duyệt qua tất cả các file trong folder
for x in range(5,39):
  folder_path = path+str(x)
  for filename in os.listdir(folder_path):
      if filename.endswith(".txt"):  # Chỉ xử lý file .txt
          file_path = os.path.join(folder_path, filename)
          
          # Đọc nội dung file
          with open(file_path, "r", encoding="utf-8") as file:
              content = file.read()
          
          # Replace '\n' thành ký tự xuống dòng thực sự và xóa ký tự '\'
          content = content.replace(r'\n', '\n\n').replace('\\', '')

          # Ghi lại nội dung đã chỉnh sửa vào file
          with open(file_path, "w", encoding="utf-8") as file:
              file.write(content)
  print("Hoàn tất xử lý folder "+ str(x))

print("Hoàn tất xử lý các file trong thư mục.")
