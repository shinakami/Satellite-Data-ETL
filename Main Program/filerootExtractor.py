import os
import glob

def get_files_by_extension(directory, extension):
    """
    從指定路徑中選找特定類型檔案並整理成清單List。
    
    :param directory: 讀取檔案所在路徑
    :param extentsion: 文件類型 (例:.txt)
    :return: 文件路徑名稱的清單List
    """
    # 使用 glob 模組找出指定目錄下符合特定副檔名的檔案
    search_path = os.path.join(directory, f"*{extension}")
    files = glob.glob(search_path)
    return files

# 使用範例
#directory = "C:/Users/user/Desktop/Shina Local file/binfilePractice/2023_10_01"  # 指定目錄
#file_list = get_files_by_extension(directory, ".bin")
#print(file_list)
