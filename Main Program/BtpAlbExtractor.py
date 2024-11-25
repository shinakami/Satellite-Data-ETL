import numpy as np
import filerootExtractor as fer
import DataLakesLoad as dtl

def read_satellite_data(file_paths):
    """
    讀取並解析衛星文件數據，將數據按文件類型（'alb' 或 'btp'）分類。
    
    :param file_paths: 文件路徑的列表
    :return: 包含 'alb' 和 'btp' 類型數據的字典，並且以文件名為子鍵
    """
    # 定義數據網格大小和每個值的字節大小
    grid_size = 2750 * 2750  # 總元素數量
    dtype = np.float32       # 4 bytes float type
    
    # 初始化主字典，分為 'alb' 和 'btp' 類別
    data = {'alb': {}, 'btp': {}}
    
    # 遍歷每個文件路徑
    for file_path in file_paths:
        with open(file_path, 'rb') as f:
            # 讀取整個文件並轉換為浮點數數組
            data_array = np.fromfile(f, dtype=dtype, count=grid_size)
            # 重塑為 2750x2750 的矩陣
            data_array = data_array.reshape((2750, 2750))
            
            # 根據文件名稱中的 .alb 或 .btp 進行分類並存入主字典
            if '.alb' in file_path:
                data['alb'] = data_array
                print(f"File '{file_path}' classified as ALB data with shape {data_array.shape}")
            elif '.btp' in file_path:
                data['btp'] = data_array
                print(f"File '{file_path}' classified as BTP data with shape {data_array.shape}")
            else:
                print(f"File '{file_path}' does not match .alb or .btp categories.")
    
    return data

def query_data(data, category, x, y):
    """
    從指定類別的文件中查詢 (x, y) 位置的值。
    
    :param data: 包含所有數據的主字典
    :param category: 文件類型 ('alb' 或 'btp')
    :param file_key: 要查詢的文件名稱
    :param x: 要查詢的行索引
    :param y: 要查詢的列索引
    :return: 文件中 (x, y) 位置的數值
    """
    # 檢查類別和文件是否在字典中
    if category not in data not in data[category]:
        print(f"File '{data}' not found in the '{category}' category.")
        return None
    
    # 查詢指定位置的值
    try:
        value = data[category][x, y]
        print(f"Value at ({x}, {y}) in  [{category}]: {value}")
        return value
    except IndexError:
        print(f"Index ({x}, {y}) is out of bounds for file  [{category}].")
        return None


#使用範例

"""
directory = "C:/Users/user/Desktop/Shina Local file/binfilePractice"  ##存放衛星資料的資料夾

alb_filelist = fer.get_files_by_extension(directory=directory, extension='.alb')
btp_filelist = fer.get_files_by_extension(directory=directory, extension='.btp')


file_paths = alb_filelist + btp_filelist

# 使用函式讀取並分類數據
data_dict = read_satellite_data(file_paths)

output_hdf5_path = "satellite_data.h5"
dtl.save_to_hdf5(data_dict, output_hdf5_path)
output_json_path = "satellite_data.json"
dtl.save_to_json(data_dict, output_json_path)

data_satellite_hdf5 = dtl.load_from_hdf5(output_hdf5_path)
data_satellite_json = dtl.load_from_json(output_json_path)

print(data_dict['alb'])
print(len(data_dict['alb']))

# 範例查詢：查詢 ALB 和 BTP 文件中 (100, 100) 的數值
query_data(data_dict, 'alb', 100, 100)
query_data(data_dict, 'btp', 100, 100)

"""