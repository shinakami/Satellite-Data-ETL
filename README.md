ReadMe: ETL Pipeline for Satellite Data Processing
Project Overview
This ETL (Extract, Transform, Load) pipeline processes satellite data, particularly focusing on cloud and radiation products. The pipeline is divided into four primary scripts:

CloudProductsExtractor.py: Extracts variables from binary files for cloud-related metrics.
BtpAlbExtractor.py: Processes broadband top-of-atmosphere radiance (btp) and albedo (alb) data.
filerootExtractor.py: Manages file discovery by type and extension.
DataLakesLoad.py: Handles data saving and loading in various formats (e.g., HDF5, NetCDF, JSON, NPZ).
File Details
1. CloudProductsExtractor.py
Functionality:

Extracts predefined variables (solzen, relaz, cm, cldphase, etc.) from satellite binary files.
Saves the extracted data to multiple formats (HDF5, NetCDF, JSON, NPZ).
Measures and logs the time taken for saving and loading operations.
Usage:

Input: Path to a binary file containing Himawari-08 satellite data.
Output: Data saved in user-defined formats.
2. BtpAlbExtractor.py
Functionality:

Reads and processes binary files containing btp and alb data.
Classifies and stores these metrics in respective categories.
Provides query functions to extract specific data points based on coordinates.
Usage:

Input: Directory containing .btp and .alb files.
Output: Processed data saved as HDF5 and JSON.
3. filerootExtractor.py
Functionality:

Identifies and lists files in a directory based on a given file extension.
Supports dynamic directory paths and extensions.
Usage:

Input: Directory path and desired file extension.
Output: List of file paths.
4. DataLakesLoad.py
Functionality:

Saves and loads data in various formats (HDF5, NetCDF, JSON, NPZ).
Ensures compatibility across formats for easy data sharing and analysis.
Usage:

Input: Data dictionary and output path.
Output: Serialized data file in the specified format.
Setup and Execution
Prerequisites
Python 3.x
Required libraries:
numpy
h5py
netCDF4
json
loguru
Steps to Run
Extract Cloud Data:

bash

python CloudProductsExtractor.py
Configure the file_path variable for the binary file.
Process Albedo and Radiance Data:

bash

python BtpAlbExtractor.py
Set the directory variable to the folder containing .btp and .alb files.
List Files:



from filerootExtractor import get_files_by_extension
files = get_files_by_extension(directory="path/to/folder", extension=".bin")
print(files)
Save and Load Data: Use methods in DataLakesLoad.py directly:


from DataLakesLoad import save_to_hdf5, load_from_hdf5
save_to_hdf5(data_dict, "output.h5")
loaded_data = load_from_hdf5("output.h5")
Sample Output
Example: Extracted Variables
After running CloudProductsExtractor.py, the following variables are saved:

Solar Zenith Angle (solzen)
Relative Azimuth Angle (relaz)
Cloud Mask (cm)
Cloud Phase (cldphase)
Cloud Optical Depth (cod_vis)
Logs
Logs are saved in file_operations.log, recording the time taken for each operation.

Authors
This pipeline was developed to streamline satellite data processing for environmental and atmospheric studies. For inquiries or contributions, please contact the development team.
