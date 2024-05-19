from utils.dataverse_controller import DataverseController
import utils.constant as constant
from utils.json_parser import Json
import json

def createDataset(args):
	json_file = args.json
	dataverse = args.dataverse
	datafile_dir = args.datafile_dir

	dataverse_controller = DataverseController(constant.base_url, constant.token)

	with open(json_file, 'r') as file:
		values = json.load(file)
		
	json_file = Json(values)
	json_file.parsing_dataset()
	ds_pid = dataverse_controller.create_dataset(dataverse, json_file.save_json())
	if datafile_dir:
		dataverse_controller.add_datafile_to_dataset(ds_pid, datafile_dir)