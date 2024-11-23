import tkinter
from tkinter import messagebox
import os

# [메소드 구간]

# 파일 시스템 클래스
class FileSystem:
    # 초기화
    def __init__(self):
        # 현재 경로(os 모듈로 알아낸 경로는 str값입니다.)
        self.curPath = os.getcwd()

    # 파일 생성 메소드
    def createFile(self):
        # 입력값을 받아옵니다.
        fileName = entryFilename.get()
        content = entryContent.get()

        # 현재 경로 + 파일 이름을 해준 값을 filePath에 저장합니다.
        filePath = os.path.join(self.curPath, fileName)

        if fileName:
            try:
                with open(filePath, 'w') as file:
                    if content:
                        file.write(content)
                    else:
                        file.write("") # content를 입력하지 않으면 빈 파일을 생성합니다.
                statusLabel.config(text=f"'{fileName}' 파일을 생성했습니다.")
            except Exception as e:
                messagebox.showerror("Error", f"파일을 생성하지 못했습니다 : {e}")
        else:
            messagebox.showwarning("Input Error", "파일의 이름을 입력하세요.")
        # 메소드 종료 전에 display를 호출해서 화면 갱신을 해줍니다.
        self.display()
    
    # 파일 삭제 메소드
    def deleteFile(self):
        fileName = entryFilename.get()
        filePath = os.path.join(self.curPath, fileName)

        if fileName:
            # 파일이 있는지 검사해주고, 있으면 삭제해줍니다.
            if os.path.exists(filePath):
                try:
                    os.remove(filePath)
                    statusLabel.config(text=f"'{fileName}' 파일을 삭제했습니다.")
                except Exception as e:
                    messagebox.showerror("Error", f"'{e}' 파일을 삭제하지 못했습니다.")
            else:
                messagebox.showwarning("File Not Found", f"'{fileName}' 파일을 찾을 수 없습니다.")
        else:
            messagebox.showwarning("Input Error", "파일의 이름을 입력하세요.")
        self.display()

    # 파일 읽기 메소드
    def readFile(self):
        fileName = entryFilename.get()
        filePath = os.path.join(self.curPath, fileName)
        
        if fileName:
            # 파일이 있으면 읽고 없으면 에러처리 해줍니다.
            if os.path.isfile(filePath):
                try:
                    with open(filePath, 'r') as file:
                        statusLabel.config(text=f"'{fileName}' 파일을 읽어옵니다.")
                        printLabel.config(text=file.read())
                except Exception as e:
                    messagebox.showerror("Error", f"'{e}' 파일을 읽지 못했습니다.")
            else:
                messagebox.showwarning("File Not Found", f"'{fileName}' 파일을 찾을 수 없습니다.")
        else:
            messagebox.showwarning("Input Error", "파일의 이름을 입력하세요.")

    # 파일 쓰기 메소드
    def writeFile(self):
        fileName = entryFilename.get()
        content = entryContent.get()
        filePath = os.path.join(self.curPath, fileName)
        
        if fileName:
            # 파일이 있으면 쓰고 없으면 에러처리 해줍니다.
            if os.path.isfile(filePath):
                try:
                    with open(filePath, 'a') as file:
                        file.write(content)
                        statusLabel.config(text=f"'{fileName}' 파일의 내용을 썼습니다.")
                except Exception as e:
                    messagebox.showerror("Error", f"'{e}' 파일을 쓰지 못했습니다.")
            else:
                messagebox.showwarning("File Not Found", f"'{fileName}' 파일을 찾을 수 없습니다.")
        else:
            messagebox.showwarning("Input Error", "파일의 이름을 입력하세요.")

    # 파일 검색 메소드
    # 파일 검색 시 현재 디렉토리와 하부 디렉토리를 검사하게 해줍니다.
    # TODO : 과도한 양의 파일을 검사하는 경우 실패할 수 있음
    def searchFile(self):
        fileName = entryFilename.get()

        if fileName:
            # os.walk로 self.curPath부터 하위 디렉토리를 재귀 탐색합니다
            # 각 반복에서 세개의 값을 반환합니다.
            # - root는 현재 탐색중인 디렉토리 경로
            # - dirs는 root 디렉토리의 하위 디렉토리 목록
            # - files는 root 디렉토리에 있는 파일 목록
            for root, dirs, files in os.walk(self.curPath):
                if fileName in files:
                    statusLabel.config(text=f"'{fileName}' 파일을 찾았습니다.")
                    printLabel.config(text=os.path.join(root, fileName))
                    return
            statusLabel.config(text=f"'{fileName}' 파일을 찾지 못했습니다.")
        else:
            messagebox.showwarning("Input Error", "디렉토리 명을 입력하세요.")
        self.display()

    # 디렉토리 생성 메소드
    def mkDir(self):
        # 입력받은 디렉토리명
        dirName = entryDirname.get()
        # 현재경로 + 입력받은 디렉토리
        dirPath = os.path.join(self.curPath, dirName)

        # 디렉토리 생성
        if dirName:
            try:
                os.makedirs(dirPath, exist_ok = True)
                statusLabel.config(text=f"'{dirPath}' 디렉토리를 생성했습니다.")
            except Exception as e:
                    messagebox.showerror("Error", f"'{e}' 디렉토리를 생성하지 못했습니다.")
        else:
            messagebox.showwarning("Input Error", "디렉토리 명을 입력하세요.")
        self.display()

    # 디렉토리 제거 메소드
    def rmDir(self):
        dirName = entryDirname.get()
        dirPath = os.path.join(self.curPath, dirName)

        if dirName:
            # 현재 디렉토리 + 입력받은 디렉토리인 디렉토리가 존재하는지 검사
            if os.path.isdir(dirPath):
                try:
                    os.rmdir(dirPath)
                    statusLabel.config(text=f"'{dirPath}' 디렉토리를 삭제했습니다.")
                except Exception as e:
                    messagebox.showerror("Error", f"'{e}' 디렉토리를 삭제하지 못했습니다.")
            else:
                messagebox.showwarning("Dir Not Found", f"'{dirPath}' 디렉토리가 없습니다.")
        else:
            messagebox.showwarning("Input Error", "디렉토리 명을 입력하세요.")
        self.display()

    # 체인지 디렉토리 메소드
    def changeDir(self):
        beforPath = self.curPath
        dirName = entryDirname.get()
        dirPath = os.path.join(self.curPath, dirName)

        if dirName:
            if os.path.isdir(dirPath):
                try:
                    self.curPath = dirPath
                    statusLabel.config(text=f"'{beforPath}' 에서 '{dirPath}' 디렉토리로 이동했습니다.")
                except Exception as e:
                    messagebox.showerror("Error", f"'{e}' 디렉토리를 이동하지 못했습니다.")
            else:
                messagebox.showwarning("Dir Not Found", f"'{dirPath}' 디렉토리가 없습니다.")
        else:
            messagebox.showwarning("Input Error", "디렉토리 명을 입력하세요.")
        self.display()
 
    # 화면 왼쪽에 파일 리스트와 디렉토리를 표현해주는 메소드
    def display(self):
        # 리스트를 보여 주기 전에 기존에 있는 값을 정리해줍니다.
        # 리스트박스 내용물의 삭제는 0~(size-1)
        listboxSize = listbox.size()
        listbox.delete(0, int(listboxSize) - 1)

        elements = os.listdir(self.curPath)

        # listbox에 현재 파일의 구성요소들과 디렉토리를 넣어줍니다.
        rowCount=0
        for path in elements:
            listbox.insert(rowCount, path)
            rowCount += 1
        listbox.pack()
        scrollbar["command"]=listbox.yview


# [GUI, main 구간]

# 파일 시스템 
fs = FileSystem()

# 기본 윈도우 생성
win = tkinter.Tk()
win.title("OS_FS_Jeong_Jae_Ho")
win.geometry("1280x600+300+300")
win.resizable(False, False)
# tkinter 창 왼쪽 상단 아이콘
# 절대경로 틀릴 시 실행 안됨 -> 주석처리 해놓겠습니다.
#win.iconbitmap('C:/Users/sean1/icon.ico')

# 프레임을 두개로 좌우 화면을 나눠줬습니다.
frame1 = tkinter.Frame(win)
frame1.pack(side="left", fill="both", expand=True)
frame2 = tkinter.Frame(win)
frame2.pack(side="right", fill="both", expand=False)

# 왼쪽화면은 리스트박스가 들어간 스크롤이 가능한 프레임
scrollbar=tkinter.Scrollbar(frame1)
scrollbar.pack(side="right", fill="y")
listbox=tkinter.Listbox(frame1, width=100, height=90, yscrollcommand = scrollbar.set)
# display메소드로 초기 파일들의 구성을 보여줍니다.
fs.display()

# 구분선
labelDivLine1 = tkinter.Label(frame2, text="ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡFileㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
labelDivLine1.grid(column=0, row=0, columnspan=4, padx=10, pady=10)

# 오른쪽 프레임들은 각종 명령어와 입력창을 넣어줬습니다.
# create, delete, read, write, search 명령을 위한 설명, 입력 부분입니다.
# grid 기능을 써서 행렬로 정리해줬습니다.
labelFileName = tkinter.Label(frame2, text="파일 이름")
labelFileName.grid(column=0, row=1)
labelContent = tkinter.Label(frame2, text="파일 내용")
labelContent.grid(column=0, row=2)
# 입력 창
entryFilename = tkinter.Entry(frame2, width=18)
entryFilename.grid(column=1, row=1)
entryContent = tkinter.Entry(frame2, width=18)
entryContent.grid(column=1, row=2)

# 각 버튼은 createFile, deleteFile, readFile, writeFile, searchFile 메소드를 실행시킵니다.
buttonCreate = tkinter.Button(frame2, text="create", command=fs.createFile, overrelief="solid", width=13)
buttonCreate.grid(column=2, row=1)
buttonDelete = tkinter.Button(frame2, text="delete", command=fs.deleteFile, overrelief="solid", width=13)
buttonDelete.grid(column=3, row=1)
buttonRead = tkinter.Button(frame2, text="read", command=fs.readFile, overrelief="solid", width=13)
buttonRead.grid(column=2, row=2)
buttonWrite = tkinter.Button(frame2, text="write", command=fs.writeFile, overrelief="solid", width=13)
buttonWrite.grid(column=3, row=2)
buttonSearch = tkinter.Button(frame2, text="search", command=fs.searchFile, overrelief="solid", width=13)
buttonSearch.grid(column=2, row=3)

# 구분선
labelDivLine = tkinter.Label(frame2, text="ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡDirectoryㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
labelDivLine.grid(column=0, row=4, columnspan=4, padx=10, pady=10)

# mkdir, rmdir, cd를 위한 설명, 입력 부분입니다.
labelDirName = tkinter.Label(frame2, text="디렉토리 명")
labelDirName.grid(column=0, row=5)
# 입력 창
entryDirname = tkinter.Entry(frame2, width=50)
entryDirname.grid(column=1, row=5, columnspan=3)

# 각 버튼은 mkDir, rmDir, cd 메소드를 실행시킵니다.
buttonMakeDir = tkinter.Button(frame2, text="mkdir", command=fs.mkDir, overrelief="solid", width=13)
buttonMakeDir.grid(column=1, row=6, padx=10, pady=10)
buttonRemoveDir = tkinter.Button(frame2, text="rmdir", command=fs.rmDir, overrelief="solid", width=13)
buttonRemoveDir.grid(column=2, row=6, padx=10, pady=10)
buttonCD = tkinter.Button(frame2, text="cd", command=fs.changeDir, overrelief="solid", width=13)
buttonCD.grid(column=3, row=6, padx=10, pady=10)

# 구분선
labelDivLine = tkinter.Label(frame2, text="ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡPrintㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
labelDivLine.grid(column=0, row=7, columnspan=4, padx=10, pady=10)

# 하단에 작업 성공 결과를 알려줍니다.
statusLabel = tkinter.Label(frame2, text="", fg="red")
statusLabel.grid(column=0, row=8, columnspan=4, padx=10, pady=10)

# 불러온 결과를 보여줍니다.
printLabel = tkinter.Label(frame2, text="출력 장소", relief="ridge")
printLabel.grid(column=0, row=9, columnspan=4, padx=10, pady=10)

win.mainloop()