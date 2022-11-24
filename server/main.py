""" Event Driven process for file operations """

import glob
import shutil
import os
import subprocess


source_path = "../source/*"
destination_path = "../destination"


file_in_source = glob.glob(source_path)
object_path = file_in_source[0]
shutil.copy(object_path, ".")

file_name, file_extension = object_path.split("/")[-1].split(".")

print(file_name, file_extension)

if file_extension == "py":
    subprocess.call(f"python ./{file_name}.{file_extension} 1", shell=True)
elif file_extension == "txt":
    for i in range(1, 4):
        send_file_name = file_name + "_" + str(i) + "." + file_extension

        with open(f"./{file_name}.{file_extension}", "r") as file:
            lines = file.readlines()[0 : i * 10]
        file.close()
        print(lines)

        shutil.copy(object_path, send_file_name)
        with open(send_file_name, "w") as file:
            file.writelines([x for x in lines])
        file.close()

else:
    print("The file is not either .txt or .py. So further process stopped here")


# with open("some.txt", "w") as file:
#     file.write("")
#     for i in range(1, 31):
#         file.write(f"Line no. {i}\n")
# file.close()
