import configparser
import os.path

DEFAULT_DATASET_SIZES = [25, 50, 100, 150, 200]
DEFAULT_EXAMPLES_PER_SIZE_IN_DATASET = 1000

CONFIG_FILE_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "config.cfg"))
config = configparser.ConfigParser()
config.read(CONFIG_FILE_PATH)
MODEL_WEIGHTS_FOLDER = config["MODELS"]["MODEL_WEIGHTS_FOLDER"]
CONCORDE_SCRIPT_PATH = config["CONCORDE"]["CONCORDE_SCRIPT_PATH"]
CONCORDE_WORK_DIR = config["CONCORDE"]["CONCORDE_WORK_DIR"]
CONCORDE_INPUT_FILE = config["CONCORDE"]["CONCORDE_INPUT_FILE"]
WEIGHTS_BACKUP_PATH = config["DATABASE"]["WEIGHTS_BACKUP_PATH"]
EVALUATION_DATABASE_LOCK_PATH = config["DATABASE"]["EVALUATION_DATABASE_LOCK_PATH"]
WEIGHTS_AND_BIASES_PROJECT = config["LOGGING"]["WEIGHTS_AND_BIASES_PROJECT"]

HAMILTONIAN_PROBABILITY = 0.8
MAX_NR_BATCHES_TO_USE_FOR_EVALUATION = 10
EVALUATION_DATA_FOLDERS = ["DATA"]
FHCP_BENCHMARK_DIR = config["DATABASE"]["FHCP_BENCHMARK_DIR"]
EVALUATION_MINIMAL_TEST_DATA_FOLDERS = ["DATA/Erdos_Renyi(25,02453).pt"]

MODEL_CHECKPOINT_SAVING_DIRECTORY = config["LOGGING"]["CHECKPOINT_STORAGE_DIRECTORY"]
WANDB_DIRECTORY = config["LOGGING"]["WANDB_DIRECTORY"]

DEFAULT_FINAL_TEST_TAG = "test/ER_80"

FHCP_HOMEPAGE = "https://sites.flinders.edu.au/flinders-hamiltonian-cycle-project/fhcp-challenge-set/"
FHCP_GRAPHS_URL = "http://sites.flinders.edu.au/flinders-hamiltonian-cycle-project/wp-content/uploads/sites/18/2020/01/FHCPCS.7z"
FHCP_SOLUTIONS_URL = "http://sites.flinders.edu.au/flinders-hamiltonian-cycle-project/wp-content/uploads/sites/18/2020/01/FHCPCS_sols.7z"
