import numpy as np

def clean_data(data_dict):
    """
    清理數據字典，將數值 -999 替換為 np.nan。

    :param data_dict: 包含數據陣列的字典
    :return: 清理後的數據字典
    """
    cleaned_data = {}
    for var_name, data in data_dict.items():
        # 使用 numpy 將數值 -999 替換為 np.nan
        cleaned_data[var_name] = np.where(data == -999, np.nan, data)
        print(f"Cleaned data for variable '{var_name}' with shape {cleaned_data[var_name].shape}")
    return cleaned_data