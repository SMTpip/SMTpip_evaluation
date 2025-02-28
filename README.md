# SMTpip Evaluation



## Setup Instructions

### 1. Unzip `KGraph.zip` and Copy `KGraph.json`

In the `example` folder, there is a file named `KGraph.zip`. Unzip the file and copy the `KGraph.json` file. Paste the `KGraph.json` file into the `example` folder. This file is necessary for the tool to function properly.

### 2. Install Required Packages

Install the dependencies specified in the `requirements.txt`:

`$ pip install -r requirements.txt`

### Usage Instructions:

Navigate to the SMTpip_src Directory.

Before running the tool, navigate to the SMTpip_src directory:

`$ cd SMTpip_src`

##  Evaluation
This guide provides instructions for evaluating SMTpip on four datasets: Watchman, HG2.9K, SD, and JupyterNotebook.

### Setup
Unzip Datasets:
Download and unzip datasets_evaluation.zip into the SMTpip/SMTpip_src directory. This folder contains the four datasets used in the evaluation.

Dataset-Specific Instructions:
Before running the evaluation script for each dataset, ensure that the base_directory variable in the corresponding test file points to the correct dataset location.

### Running Evaluations
Each dataset has a specific test file. Follow the instructions below for each one.

#### Watchman
Open test_Watchman.py and verify:

`base_directory = "datasets_evaluation/mytool_pip_smartPip_result_data/Datasets_Used/Watchman"`

Run the evaluation script:

`$ python .\test_Watchman.py`

The results will be generated in the evaluation_result folder.
#### HG2.9K
Open test_HG2.9K.py and verify:

`base_directory = "datasets_evaluation/mytool_pip_smartPip_result_data/Datasets_Used/HG2.9K"`

Run the evaluation script:

`$ python .\test_HG2.9K.py`

Results are saved in the evaluation_result folder.
#### SD
Open test_SD.py and verify:

`base_directory = "datasets_evaluation/mytool_pip_smartPip_result_data/Datasets_Used/SD"`

Run the evaluation script:

`$ python .\test_SD.py`

Results are saved in the evaluation_result folder.
#### JupyterNotebook
Open test_jupyterNotebook.py and verify:

`base_directory = "datasets_evaluation/mytool_pip_smartPip_result_data/Datasets_Used/jupyterNotebook"`

Run the evaluation script:

`$ python .\test_jupyterNotebook.py`

Results are saved in the evaluation_result folder.
Results
All results for each dataset evaluation will be located in the evaluation_result folder.

### Results
For each dataset, the evaluation generates two files in the evaluation_result folder:

#### Log File (.txt):
Contains the complete log of the evaluation for all projects in the dataset.
#### Timing Results (.csv):
Contains the timing details for each step of the SMTpip approach for all projects solved by SMTpip. Each row provides insights into the time taken in each step.
