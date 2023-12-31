import datahugger
import os

class Results:
    def __init__(self, DOI, path, template) :
        self.DOI = DOI
        self.path = path
        self.template = template
    
    def download(self):
        datahugger.download(self.DOI, self.path)

    def generate_qmds(self):
        os.makedirs("to_render", exist_ok=True)
        with open("_quarto.yml", 'w') as project_file:
            project_file.write(f"project:\n  output-dir: rendered_files\n  render:\n")
        directories = [entry.name for entry in os.scandir(self.path) if entry.is_dir()]
        for entry in directories:
            rendered_file = os.path.join("to_render/", f"{entry}.qmd")
            with open(rendered_file, 'w') as new_file:
                yaml_header = f"---\ntitle: \"{entry}\"\n---\n"
                parameters_cell = f"```{{python}}\n#| tags: [parameters]\nSolution_path = '../{path}{entry}/LMAHeureuxPorosityDiff.hdf5'\n```\n\n"
                analyses = f"{{{{< include ../{self.template} >}}}}"
                new_file.writelines([yaml_header, parameters_cell, analyses])
            with open("_quarto.yml", 'a') as project_file:
                project_file.write(f"    - to_render/{entry}.qmd\n")

if __name__ == "__main__":
    import sys
    Results.download(sys.argv[1], sys.argv[2])
    Results.generate_qmds(sys.argv[2], sys.argv[3])
