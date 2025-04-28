import os

# 프로젝트 폴더로 이동
os.chdir("E:/MyPythonProject")  # 절대경로 확인

# Git 자동 동기화
os.system("git add .")
os.system('git commit -m "Auto commit from PyCharm"')  # 메시지만 살짝 수정 가능
os.system("git push origin master")  # 브랜치가 main이면 여기만 수정
