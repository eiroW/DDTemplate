import subprocess
args_list = [['python', 'fibergeneration.py',
              '--output_suffix', 'path/to/output',
              '--model_path', 'assets/model/whole_model.pt',
              '--data_path', 'path/to/Datasets/HCP_test',
              '--sub_num', '50',
              '--device', 'cuda:0',
              '--batch_size', '4',
              '--tracts_num', '-1'],]
for args in args_list:
    subprocess.run(args)