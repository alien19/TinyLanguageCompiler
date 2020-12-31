import os
import pickle
import json
from distutils.dir_util import copy_tree
from shutil import copyfile
from shutil import move
from shutil import rmtree
from Exceptions.UtilityExceptions import JSONParsingExceptions
from scipy.io import savemat, loadmat
from Utility.aes import Cryptography


class FileSystem:
    @staticmethod
    def load_pickle_no_enc(path: str):
        with open(path, 'rb') as handle:
            out = pickle.load(handle)
        return out

    @staticmethod
    def load_pickle(path: str):
        f = open(path, 'rb')
        bytesD = f.read()
        f.close()
        out = Cryptography.decrypt_dict(bytesD)
        return out

    @staticmethod
    def load_mat(path: str) -> dict:
        return loadmat(path)

    @staticmethod
    def load_txt(path: str) -> str:
        f = open(path, "r")
        content = f.read()
        f.close()
        return content

    @staticmethod
    def load_json(path: str)-> dict:
        try:
            f = open(path, "r")
            content = "".join(f.readlines())
            f.close()
            return json.loads(content)
        except ValueError:
            raise JSONParsingExceptions(file_path=path)

    # Old save pickle just saves the pickle file
    # @staticmethod
    # def save_pickle(path: str, data) -> None:
    #     with open(path, 'wb') as handle: pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # new save pickle save the file encrypted by AES algorithm
    @staticmethod
    def save_pickle(path: str, data) -> None:
        bytes = Cryptography.encrypt_dict(data)
        f = open(path, 'wb')
        f.write(bytes)
        f.close()

    @staticmethod
    def save_mat(path: str, data: dict) -> None:
        savemat(path, data)

    @staticmethod
    def save_txt(path: str, content: str) -> None:
        f = open(path, "w")
        f.write(content)
        f.close()

    @staticmethod
    def save_json(path: str, data: dict) -> None:
        f = open(path, "w")
        content = json.dumps(data, indent=4)
        f.write(content)
        f.close()

    @staticmethod
    def file_exists(fileName: str):
        return FileSystem.is_file(fileName)

    @staticmethod
    def directory_exists(directoryName: str):
        return FileSystem.is_directory(directoryName)

    @staticmethod
    def is_file(fileName: str):
        return os.path.isfile(fileName)

    @staticmethod
    def is_directory(directoryName: str):
        return os.path.isdir(directoryName)

    @staticmethod
    def get_entries_names_in_directory(directoryName: str):
        return os.listdir(directoryName)

    @staticmethod
    def read_style_sheet_file():
        return "".join(open("styles.css").readlines())

    @staticmethod
    def path_exists(path: str) -> bool:
        return os.path.exists(path)

    @staticmethod
    def make_directory(directoryPath: str) -> None:
        if FileSystem.is_directory(directoryPath):
            return
        else:
            os.mkdir(directoryPath)

    @staticmethod
    def join_path(*parts) -> str:
        path = os.path.join(*parts)
        return path.replace("\\", "/")

    @staticmethod
    def get_current_working_directory() -> str:
        return os.getcwd().replace("\\", "/")

    @staticmethod
    def get_program_directory() -> str:
        path = os.path.dirname(os.path.realpath(__file__))
        return path[0:len(path) - 8] + "/"

    # another method with the same name check "get_current_working_directory"
    # @staticmethod
    # def get_cwd() -> str:
    #     return os.getcwd()

    @staticmethod
    def split(path: str) -> tuple:
        return os.path.split(path)

    @staticmethod
    def copy_file(sourcePath: str, destinationPath: str) -> None:
        copyfile(sourcePath, destinationPath)

    @staticmethod
    def rename_file(sourcePath: str, newName:str) -> None:
        os.rename(sourcePath, newName)

    @staticmethod
    def get_file_name(path:str):
        if "/" not in  path: return path
        else : return path[path.rindex("/")+1:]

    @staticmethod
    def copy_directory(sourcePath: str, destinationPath: str) -> None:
        copy_tree(sourcePath, destinationPath)

    @staticmethod
    def move_file(sourcePath: str, destinationPath: str) -> None:
        move(sourcePath, destinationPath)

    @staticmethod
    def remove_file(path):
        os.remove(path)

    @staticmethod
    def remove_folder(path):
        rmtree(path)

    @staticmethod
    def get_temp_folder_path(folder_name='tmp'):
        # return os.path.join(FileSystem.get_current_working_directory(), '{}'.format(hash(os.times())))
        return os.path.join(FileSystem.get_current_working_directory(),folder_name)

