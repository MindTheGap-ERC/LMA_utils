import subprocess

with open("parameters.yaml", "r") as file:
    for line in file:
        path = line.strip()
        name = line.strip().split("data/")[1].split("/")[0]
        subprocess.run(["quarto", "render", f"rendered_files/{name}.qmd", "-P", f"{path}"], capture_output=True, text=True, check=True, shell=True)