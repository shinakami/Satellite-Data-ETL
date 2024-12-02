專案簡介 (Project Overview)
該專案提供一個完整的ETL（提取、轉換、載入）工作流，用於處理Himawari-08衛星數據文件，支持 .bin, .alb, .btp 格式，並能將數據儲存為 HDF5、NetCDF、NPZ、JSON 格式。

This project delivers a complete ETL workflow for processing Himawari-08 satellite data files, supporting .bin, .alb, and .btp formats, with the ability to store data in HDF5, NetCDF, NPZ, and JSON formats.



環境需求 (Requirements)
Python 3.9+
依賴庫 (Dependencies):
numpy
h5py
netCDF4
loguru


模組功能 (Modules)
1. main.py
主程序，負責協調ETL流程。包括數據提取、清理、轉換、以及多種格式的保存與載入。
主要功能：

日誌記錄
支持數據格式：HDF5、NetCDF、NPZ、JSON
計時數據讀寫過程

2. CloudProductsExtractor.py
提取 .bin 文件中的雲產品數據。
功能：

根據字節偏移量提取數據。
支持變數包括 solzen, relaz, cm 等。

3. BtpAlbExtractor.py
從 .alb 和 .btp 文件中提取衛星輻射數據。
功能：

按文件類型 (alb 或 btp) 分類數據。
讀取並重塑數據為 2750x2750 網格。

4. DataCleanTransform.py
數據清理模組。
功能：

將無效數據值（如 -999）替換為 np.nan。

5. DataLakesLoad.py
數據存儲與載入模組。
功能：

支持 HDF5、NetCDF、NPZ、JSON 格式的數據存儲與讀取。

6. filerootExtractor.py
文件管理模組，用於搜索特定類型文件。
功能：

按副檔名篩選目錄中的文件並返回路徑列表。





Project Overview
This project provides a complete ETL (Extract, Transform, Load) workflow for processing Himawari-08 satellite data files. It supports .bin, .alb, and .btp formats and enables storing the processed data in HDF5, NetCDF, NPZ, and JSON formats.

Requirements
Python: 3.9+
Dependencies:
numpy
h5py
netCDF4
loguru



Modules
1. main.py
The main program coordinates the ETL process, including data extraction, cleaning, transformation, and saving/loading in various formats.
Key Features:

Logging data operations.
Supports data formats: HDF5, NetCDF, NPZ, JSON.
Records the time taken for data read/write operations.

2. CloudProductsExtractor.py
Extracts cloud product data from .bin files.
Features:

Extracts data based on byte offsets.
Supports variables such as solzen, relaz, cm, etc.

3. BtpAlbExtractor.py
Extracts satellite radiation data from .alb and .btp files.
Features:

Classifies data by file type (alb or btp).
Reads and reshapes data into a 2750x2750 grid.

4. DataCleanTransform.py
A module for cleaning data.
Features:

Replaces invalid values (e.g., -999) with np.nan.

5. DataLakesLoad.py
A module for data storage and loading.
Features:

Supports storing and reading data in HDF5, NetCDF, NPZ, and JSON formats.

6. filerootExtractor.py
A file management module used for searching specific file types.
Features:

Filters files by extension within a directory and returns a list of paths.
