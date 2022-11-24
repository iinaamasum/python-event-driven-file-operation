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
    os.mkdir("TempDir")
    for i in range(1, 4):
        send_file_name = file_name + "_" + str(i) + "." + file_extension

        with open(f"./{file_name}.{file_extension}", "r") as file:
            lines = file.readlines()[0 : i * 10]
        file.close()
        # shutil.copy(object_path, f"./files/{send_file_name}")

        with open(f"TempDir/{send_file_name}", "w") as file:
            file.writelines([x for x in lines])
        file.close()

    # zipping files
    shutil.make_archive("send_files", "zip", "TempDir")
    shutil.rmtree("./TempDir")

    # sending files
    zip_file = "./send_files.zip"
    shutil.copy(zip_file, "../destination")

    # unzipping in the destination
    shutil.unpack_archive("../destination/send_files.zip", "../destination")


else:
    print("The file is not either .txt or .py. So further process stopped here")


# with open("some.txt", "w") as file:
#     file.write("")
#     for i in range(1, 31):
#         file.write(f"Line no. {i}\n")
# file.close()
