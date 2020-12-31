from PySide2.QtWidgets import QFileDialog
from Utility.fileSystem import FileSystem
from Exceptions.UtilityExceptions import JSONParsingExceptions
import os


class Tools:
    class LUTManager:
        LUT_SAVE_PATH = "TOOLS_LUT_SAVE_PATH"
        LUT_LOAD_PATH = "TOOLS_LUT_LOAD_PATH"

    class DDBManager:
        DDB_LOAD_PATH = "TOOLS_DDB_LOAD_PATH"

class LUTGenPaths:
    LUT_SAVE_PATH = "LUT_SAVE_PATH"
    NETLIST_PATH  = "NETLIST_PATH"
    SIM_COMMAND   = "SIMULATION_COMMAND"

class DDBGen:
    DDBGEN_SAVE_PATH = "DDBGEN_SAVE_PATH"


class License:
    LICENSE_SAVE_PATH = "LICENSE_SAVE_PATH"


filePathsVersion = 1
filePaths = {}
defaultFilePaths = {
    "VERSION": filePathsVersion,
    Tools.LUTManager.LUT_LOAD_PATH: os.getcwd(),
    Tools.LUTManager.LUT_SAVE_PATH: os.getcwd(),
    Tools.DDBManager.DDB_LOAD_PATH: os.getcwd(),
    DDBGen.DDBGEN_SAVE_PATH: os.getcwd(),
    License.LICENSE_SAVE_PATH: os.getcwd(),
    LUTGenPaths.LUT_SAVE_PATH: os.getcwd(),
    LUTGenPaths.NETLIST_PATH: os.getcwd(),
    LUTGenPaths.SIM_COMMAND: os.getcwd(),
}


def get_save_file_name(dialogParent, dialogTitle, defaultPath, extentions, defaultName=""):
    global filePaths
    if defaultPath not in filePaths:
        filePaths[defaultPath] = ""
    fileName = QFileDialog.getSaveFileName(dialogParent, dialogTitle, filePaths[defaultPath]+ "/" + defaultName, extentions)
    if fileName:
        if fileName[0] != "":
            if "." not in fileName[0]:
                fileName = fileName[0] + fileName[1][2:-1]
            else:
                fileName = fileName[0]
            filePaths[defaultPath] = fileName[:fileName.rindex("/")]
            print(defaultPath, filePaths)
            return fileName
    return None


def get_directory(dialogParent, dialogTitle, defaultPath):
    global filePaths
    if defaultPath not in filePaths:
        filePaths[defaultPath] = ""
    dir = str(QFileDialog.getExistingDirectory(dialogParent, dialogTitle, filePaths[defaultPath],
                                               QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks))
    if dir != "":
        filePaths[defaultPath] = dir
        return dir
    return None


def get_open_file_names(dialogParent, dialogTitle, defaultPath, extentions):
    global filePaths
    if defaultPath not in filePaths: filePaths[defaultPath] = defaultFilePaths[defaultPath]
    if filePaths[defaultPath][len(filePaths[defaultPath]) - 1] is not "/":
        filePaths[defaultPath] += "/"
    files = QFileDialog.getOpenFileNames(dialogParent, dialogTitle, filePaths[defaultPath], extentions)[0]
    if len(files) > 0:
        filePaths[defaultPath] = files[0][:files[0].rindex("/")]
        return files


def SaveData(defaultpath=FileSystem.get_program_directory() + "Data/cache/"):
    global filePaths
    if not (FileSystem.path_exists(defaultpath)): FileSystem.make_directory(defaultpath)
    FileSystem.save_json(defaultpath + "filePaths.json", filePaths)
    print("saving", filePaths)


def LoadData(path=FileSystem.get_program_directory()+"/Data/cache/"):
    global filePaths
    if FileSystem.file_exists(path + "filePaths.json"):
        try:
            data = FileSystem.load_json(path + "filePaths.json")
            filePaths = data
            print("loading", filePaths)
            if "VERSION" not in filePaths:
                filePaths = defaultFilePaths
        except JSONParsingExceptions as e:
            FileSystem.remove_file(path)
            filePaths = defaultFilePaths
    else:
        filePaths = defaultFilePaths