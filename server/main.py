""" Event Driven process for file operations """

import glob
import shutil
import os
import subprocess


source_path = "../source/*"
destination_path = "../destination"

while True:
    file_in_source = glob.glob(source_path)

    if file_in_source:
        object_path = file_in_source[0]
        shutil.copy(object_path, ".")

        file_name, file_extension = object_path.split("/")[-1].split(".")

        if file_extension == "py":
            subprocess.call(f"python ./{file_name}.{file_extension} 1", shell=True)
            # removing processed file from server and source
            os.remove(object_path)
            os.remove(object_path.split("/")[-1])

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

            # removing processed file from server and source
            os.remove(object_path)
            os.remove(object_path.split("/")[-1])

        else:
            print("The file is not either .txt or .py. So further process stopped here")
            os.remove(object_path)
