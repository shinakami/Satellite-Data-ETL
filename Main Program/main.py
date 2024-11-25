import CloudProductsExtractor as cpe
import DataCleanTransform as dct
import BtpAlbExtractor
import DataLakesLoad as dtl
import DataCleanTransform as dct
from loguru import logger
import time

if __name__ == '__main__':
    print("Main ETL Program...")

    # 日誌檔案設定
    logger.add("file_operations.log", format="{time} {level} {message}", level="INFO")

    # 路徑設置並取出數據 (Extract)
    file_path = "2023_10_01\Himawari08_CWBEA_L2_Cloud_20231001_1000.bin"
    data_dict = cpe.extractor(file_path)

    # 清理數據 (Transform:Clean)
    data_dict = dct.clean_data(data_dict)

  
    output_paths = {
        "hdf5": "output_data.h5",
        "nc": "output_data.nc",
        "npz": "output_data.npz",
        "json": "output_data.json"
    }


    #不同類型數據的存储，計算並記錄寫入時間 (Load) 
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
    for format_type, output_path in output_paths.items():
        for var in variables:
            for j in range(len(data_dicts_loaded[format_type][var][0, :])):
                time.sleep(2.2)
                print(f"Format: {format_type}, File: {output_path}")
                print(f"Sample data for {var} at row {j}:", data_dicts_loaded[format_type][var][j, 1400:1600])
                print()
                print('=============================================================')
                print()