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
