import os 
import shutil

#####

#  This code contain a snippet code that is repeated 3 times and may be in a function too 

#  Which means this code can be optimized 

#####


def organize_directory(relative_path) :
    abs_path = os.path.abspath(relative_path)
    is_exists = os.path.exists(abs_path)
    if not is_exists :
        print(f"There's no directory with the path {abs_path}")
    else :
        list_files = os.listdir(abs_path)
        txt_directory = os.path.join(abs_path,"txt")
        py_directory = os.path.join(abs_path,"py")
        jpeg_directory = os.path.join(abs_path,"jpeg")
        for file in list_files :
            __ , ext = os.path.splitext(file)
            if ext == ".txt" :
                is_exists_txt =os.path.exists(txt_directory)
                ancien_file_path = os.path.join(abs_path,file)
                if not is_exists_txt :
                    os.mkdir(txt_directory)
                    shutil.move(ancien_file_path,txt_directory)
                else :
                    shutil.move(ancien_file_path,txt_directory)
            elif ext == ".py" :
                is_exists_py =os.path.exists(py_directory)
                ancien_file_path = os.path.join(abs_path,file)
                if not is_exists_py :
                    os.mkdir(py_directory)
                    shutil.move(ancien_file_path,py_directory)
                else :
                    shutil.move(ancien_file_path,py_directory)
            elif ext == ".jpeg" :
                is_exists_jpeg =os.path.exists(jpeg_directory)
                ancien_file_path = os.path.join(abs_path,file)
                if not is_exists_jpeg :
                    os.mkdir(jpeg_directory)
                    shutil.move(ancien_file_path,jpeg_directory)
                else :
                    shutil.move(ancien_file_path,jpeg_directory)
    pass






