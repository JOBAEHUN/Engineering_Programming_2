import os

# Git 프로젝트 폴더로 이동 (본인 경로 수정)
os.chdir("E:/MyPythonProject")  # 여기를 본인 프로젝트 폴더로 변경!

# 테스트 문장

# Git 자동 동기화 실행
os.system("git add .")
os.system('git commit -m "Auto commit from Spyder"')
os.system("git push origin master")  # master 브랜치인 경우
