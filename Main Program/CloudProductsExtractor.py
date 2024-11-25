import numpy as np
import time
import DataLakesLoad as dtl
import DataCleanTransform as dct
from loguru import logger





# 讀取所有變數並存儲於字典中
def extractor(file_path):
    # 定義每個變數的名稱和大小（byte_Cld），以及網格大小
    variables = ['solzen', 'relaz', 'cm', 'cldphase', 'cldtype', 
                'ctt', 'ctp', 'cth', 'cod_vis', 're', 'lwp', 'iwp']
    byte_Cld = [4, 4, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4]  # 每個變數的字節大小
    grid_size = 2750 * 2750  # 每個變數的網格大小

    # 定義對應的數據類型
    data_types = {4: np.float32, 1: np.int8}  # 定義 4 bytes 為 float32，1 byte 為 int8

    # 定義變數提取函數
    def extract_variable(file_path, var_index):
        # 計算偏移量 byte_skip
        byte_skip = 20 + 8 * var_index + sum(byte_Cld[:var_index]) * grid_size
        data_type = data_types[byte_Cld[var_index]]  # 根據 byte_Cld 選擇對應數據類型
        
        with open(file_path, 'rb') as f:
            f.seek(byte_skip)  # 移動到偏移量位置
            
            # 根據數據類型讀取
            if byte_Cld[var_index] == 1:  # int8，逐字節讀取
                data = np.frombuffer(f.read(grid_size), dtype=data_type).reshape((2750, 2750))
            elif byte_Cld[var_index] == 4:  # float32，可以直接讀取
                data = np.fromfile(f, dtype=data_type, count=grid_size).reshape((2750, 2750))
            else:
                raise ValueError("Unsupported byte size in byte_Cld.")
        
        return data
    

    data_dict = {}
    for i, var_name in enumerate(variables):
        data_dict[var_name] = extract_variable(file_path, i)
        print(f"Extracted {var_name} data with shape: {data_dict[var_name].shape} and dtype: {data_dict[var_name].dtype}")
    return data_dict


#使用範例

"""

# 日誌檔案設定
logger.add("file_operations.log", format="{time} {level} {message}", level="INFO")

# 路徑設置
file_path = "2023_10_01\Himawari08_CWBEA_L2_Cloud_20231001_1000.bin"
data_dict = extractor(file_path)

# 清理數據
data_dict = dct.clean_data(data_dict)

# 計算並記錄寫入時間
output_paths = {
    "hdf5": "output_data.h5",
    "nc": "output_data.nc",
    "npz": "output_data.npz",
    "json": "output_data.json"
}

for format_type, output_path in output_paths.items():
    start_time = time.time()
    if format_type == "hdf5":
        dtl.save_to_hdf5(data_dict, output_path)
    elif format_type == "nc":
        dtl.save_to_nc(data_dict, output_path)
    elif format_type == "npz":
        dtl.save_to_npz(data_dict, output_path)
    elif format_type == "json":
        dtl.save_to_json(data_dict, output_path)
    end_time = time.time()
    logger.info(f"Data saved to {output_path} in {end_time - start_time:.4f} seconds")

# 計算並記錄讀取時間
data_dicts_loaded = {}
for format_type, output_path in output_paths.items():
    start_time = time.time()
    if format_type == "hdf5":
        data_dicts_loaded["hdf5"] = dtl.load_from_hdf5(output_path)
    elif format_type == "nc":
        data_dicts_loaded["nc"] = dtl.load_from_nc(output_path)
    elif format_type == "npz":
        data_dicts_loaded["npz"] = dtl.load_from_npz(output_path)
    elif format_type == "json":
        data_dicts_loaded["json"] = dtl.load_from_json(output_path)
    end_time = time.time()
    logger.info(f"Data loaded from {output_path} in {end_time - start_time:.4f} seconds")

# 設定要顯示的變數
variables = ['solzen', 'relaz', 'cm', 'cldphase', 'cldtype', 
            'ctt', 'ctp', 'cth', 'cod_vis', 're', 'lwp', 'iwp']

# 顯示數據示例
for var in variables:
    for j in range(len(data_dicts_loaded["json"][var][0, :])):
        time.sleep(2.2)
        print(f"Sample data for {var} at row {j}:", data_dicts_loaded["json"][var][j, 1500:1600])
        print()
        print('=============================================================')
        print()

"""
