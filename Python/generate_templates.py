import os
import shutil

parameters_file = "parameters.yaml"
run_summary_template = "run_summary.qmd"
os.makedirs("rendered_files", exist_ok=True)

with open(parameters_file, "r") as f:
    lines = f.readlines()

for line in lines:
    name = line.strip().split("data/")[1].split("/")[0]
    new_file_name = f"{name}.qmd"
    new_file_path = os.path.join("rendered_files/", new_file_name)
    shutil.copy(run_summary_template, new_file_path)
