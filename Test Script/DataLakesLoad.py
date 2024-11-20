import h5py
from netCDF4 import Dataset
import numpy as np
import json

# Save HDF5 
def save_to_hdf5(data_dict, output_path):
    with h5py.File(output_path, 'w') as hdf_file:
        for var_name, data in data_dict.items():
            hdf_file.create_dataset(var_name, data=data)
            print(f"Saved {var_name} to HDF5 with shape {data.shape} and dtype {data.dtype}")


# Load HDF5
def load_from_hdf5(input_path):
    data_dict = {}
    with h5py.File(input_path, 'r') as hdf_file:
        for var_name in hdf_file.keys():
            data_dict[var_name] = hdf_file[var_name][:]
            print(f"Loaded {var_name} from HDF5 with shape {data_dict[var_name].shape} and dtype {data_dict[var_name].dtype}")
    return data_dict



# Save NetCDF
def save_to_nc(data_dict, output_path):
    with Dataset(output_path, 'w', format='NETCDF4') as nc_file:
        # 創建維度
        nc_file.createDimension('x', data_dict[next(iter(data_dict))].shape[0])
        nc_file.createDimension('y', data_dict[next(iter(data_dict))].shape[1])
        
        # 創建變數
        for var_name, data in data_dict.items():
            var = nc_file.createVariable(var_name, data.dtype, ('x', 'y'))
            var[:, :] = data
            print(f"Saved {var_name} to NetCDF with shape {data.shape} and dtype {data.dtype}")

# Load NetCDF
def load_from_nc(input_path):
    data_dict = {}
    with Dataset(input_path, 'r') as nc_file:
        for var_name in nc_file.variables:
            data = nc_file.variables[var_name][:]
            data_dict[var_name] = data
            print(f"Loaded {var_name} from NetCDF with shape {data.shape} and dtype {data.dtype}")
    return data_dict



# Save NPZ
def save_to_npz(data_dict, output_path):
    np.savez_compressed(output_path, **data_dict)
    print(f"Saved data to NPZ file at {output_path} with variables: {list(data_dict.keys())}")

# Load NPZ
def load_from_npz(input_path):
    data_dict = {}
    with np.load(input_path, allow_pickle=True) as npz_file:
        for var_name in npz_file.files:
            data_dict[var_name] = npz_file[var_name]
            print(f"Loaded {var_name} from NPZ with shape {data_dict[var_name].shape} and dtype {data_dict[var_name].dtype}")
    return data_dict



# Save JSON
def save_to_json(data_dict, output_path):

    
    def convert_data_to_json_serializable(data_dict):
        json_data = {}
        for var_name, data in data_dict.items():
            json_data[var_name] = data.tolist() 
        return json_data
    
    json_data = convert_data_to_json_serializable(data_dict)
    with open(output_path, 'w') as json_file:
        json.dump(json_data, json_file)
    print(f"Saved data to JSON file at {output_path}")

# Load JSON
def load_from_json(input_path):
    with open(input_path, 'r') as json_file:
        json_data = json.load(json_file)
    data_dict = {var_name: np.array(data) for var_name, data in json_data.items()}
    for var_name in data_dict:
        print(f"Loaded {var_name} from JSON with shape {data_dict[var_name].shape} and dtype {data_dict[var_name].dtype}")
    return data_dict