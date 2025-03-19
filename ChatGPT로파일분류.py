import os
import shutil

# 다운로드 폴더 경로 설정
download_folder = r"C:\Users\student\Downloads"

# 파일을 이동할 대상 폴더 설정
destination_folders = {
    "images": [".jpg", ".jpeg"],
    "data": [".csv", ".xlsx"],
    "docs": [".txt", ".doc", ".pdf"],
    "archive": [".zip"]
}

# 대상 폴더 생성 (존재하지 않는 경우)
for folder in destination_folders.keys():
    folder_path = os.path.join(download_folder, folder)
    os.makedirs(folder_path, exist_ok=True)
    print(f"폴더 확인/생성: {folder_path}")

# 파일 이동
moved_count = 0
for file in os.listdir(download_folder):
    file_path = os.path.join(download_folder, file)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file)[1].lower()
        for folder, extensions in destination_folders.items():
            if file_ext in extensions:
                dest_path = os.path.join(download_folder, folder, file)
                # 이미 파일이 존재하는지 확인
                if os.path.exists(dest_path):
                    print(f"파일이 이미 존재합니다: {dest_path}")
                else:
                    shutil.move(file_path, dest_path)
                    print(f"Moved: {file} -> {folder}")
                    moved_count += 1

print(f"총 {moved_count}개의 파일이 이동되었습니다.")
