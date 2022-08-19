
import os 
import datetime

result = dir(os)
result = os.name

# dizin değiştirme
# os.chdir('C:\\')
# os.chdir('../..')

# etkin dizin öğrennme

result = os.getcwd()

# klasör oluşturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/newfolder")
# os.rename("newdirectory","newfolder")
# os.rmdir("newdirectory")
# os.removedirs("yeniklasör/yeniklasör")


# listeleme
# result = os.listdir()
# result = os.listdir('C:\\')
# for folder in os.listdir():
#     if folder.endswith('.py'):
#         print(folder)


# result = os.stat("Datetime.py")
# # result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_atime) # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_ctime) # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime) # değiştirilme tarihi

# os.system("notepad.exe")

# path 

# result = os.path.abspath("Datetime.py")
# result = os.path.dirname("C:/Users/Ali Osman/Desktop/Staj Programı-Python/AdvancedPythonModules/DateTimeModule>")
# result = os.path.dirname(os.path.abspath("osModule.py"))


print(result)
