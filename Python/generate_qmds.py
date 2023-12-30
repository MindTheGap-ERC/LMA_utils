import os

os.makedirs("to_render", exist_ok=True)

def get_directories(path):
  directories = []
  for entry in os.scandir(path):
    if entry.is_dir():
      directories.append(entry.name)
  return directories

def generate_qmds(path, template):
  with open("_quarto.yml", 'w') as project_file:
      project_file.write(f"project:\n  output-dir: rendered_files\n  render:\n")
  directories = get_directories(path)
  for entry in directories:
    rendered_file = os.path.join("to_render/", f"{entry}.qmd")
    with open(rendered_file, 'w') as new_file:
      yaml_header = f"---\ntitle: \"{entry}\"\n---\n"
      parameters_cell = f"```{{python}}\n#| tags: [parameters]\nSolution_path = '../{path}{entry}/LMAHeureuxPorosityDiff.hdf5'\n```\n\n"
      analyses = f"{{{{< include ../{template} >}}}}"
      new_file.writelines([yaml_header, parameters_cell, analyses])
    with open("_quarto.yml", 'a') as project_file:
      project_file.write(f"    - to_render/{entry}.qmd\n")
  
generate_qmds('../../data/', "analyses.qmd")
