#    1.create folder
# import os

# dir=("AIPA")

# try:
#    os.makedirs(dir)
#    print(f'Folder created : {dir}')
# except FileExistsError:
#     print(f'Folder already exists : {dir}')
# finally:
#     print("code is executed")

#    2.Rename folder name
# cur_name="AIPA"
# new_name="AI"
# os.rename(cur_name,new_name)

# os.rename("AI","AIPA")

#    3.Rename folder with try and exception
# import os
# cur_name="AI"
# new_name="AIPA"
# try:
#     os.rename(cur_name,new_name)
# except FileExistsError:
#     print(f'Folder already exists')
# finally:
#     print("code is executed")


#    4.Delete folder
# import shutil
# dir_del="AIPA"
# try:
#     shutil.rmtree(dir_del)
#     print("directory deleted")
# except FileNotFoundError:
#     print(f'Folder does not exist')
# except PermissionError:
#     print(f'Access denied')
# except Exception as e:
#     print(f'An error occurred: {e}')

#    5. write something in directory
# import os
# dir="xyz"
# os.makedirs(dir,exist_ok=True)
# file_name="abc.txt"
# file_path=os.path.join(dir,file_name)
# with open(file_path,"w") as file:
#     file.write("Hello EVERYONE")
#     print(f"File {file_name} created successfully in {dir}")

#    6. write something in directory with try and exception
# import os
# dir="xyz"
# try:
#     os.makedirs(dir,exist_ok=True)
#     file_name="abc.txt"
#     file_path=os.path.join(dir,file_name)
#     with open(file_path,"w") as file:
#         file.write("Hello EVERYONE")
#         print(f"File {file_name} created successfully in {dir}")
# except Exception as e:
#     print(f"An error occurred: {e}")


#    7. path of directory
# import os
# dir="."
# with os.scandir(dir) as entries:
#     print(f"contents of the folder are: {entries}")
#     for entry in entries:
#         print(entry.name)

# #    8.list of directory
# import os
# dir=os.listdir()
# print("contents of the folder are: ",dir)

#   8.path of current directory
# import os
# dir=os.getcwd()
# print("working directory is: ",dir)

#    9.copy directory
# import shutil
# dir_copy="xyz"
# try:
#     shutil.copytree(dir_copy,"abc")
#     print("Directory copied successfully")
# except Exception as e:
#     print(f"An error occurred: {e}")

#     10.move directory
# import shutil
# dir_move="xyz"
# try:
#     shutil.move(dir_move,"abc")
#     print("Directory moved successfully")
# except Exception as e:
#     print(f"An error occurred: {e}")

# #    11.Delete directory
# import shutil
# dir_del="xyz"
# try:
#     shutil.rmtree(dir_del)
#     print("directory deleted")
# except FileNotFoundError:
#     print(f'Folder does not exist')
# except PermissionError:
#     print(f'Access denied')
# except Exception as e:
#     print(f'An error occurred: {e}')

#    12 create csv file
# import csv
# with open ("Ai_MicroDegree.csv",mode="w",newline='')as csvfile:
#     add_csv=csv.writer(csvfile)
#     add_csv.writerow(["Name","Address","Trade"])
#     add_csv.writerow(["Sakshi","Bihar","AIPA"])
#     add_csv.writerow(["Kiran","Bihar","IT"])
#     add_csv.writerow(["Saumya","Bihar","AI"])
# print("CSV created sucessfully.")


#   13 view content inside csv file
# import csv
# with open ("Ai_MicroDegree.csv",newline='')as csvfile:
#     csv1=csv.reader(csvfile)
#     for row in csv1:
#         print(row)







