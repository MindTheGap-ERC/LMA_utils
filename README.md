# Utility scripts to examine and plot outputs of the reactive transport model by L'Heureux

To be applied to the outputs of the [Python implementation](https://github.com/MindTheGap-ERC/reactive-transport-model-for-limestone-marl-sequences)
and possibly the [Fortran predecessor](https://github.com/astro-turing/lheureux)

These are attempts to reproduce the diagenetic model for the formation of limestone-marl alternations proposed in [L’Heureux, ‘Diagenetic Self-Organization and Stochastic Resonance in a Model of Limestone-Marl Sequences’. 2018. Geofluids e4968315, doi: 10.1155/2018/4968315](https://www.hindawi.com/journals/geofluids/2018/4968315/)

## Automating summaries of each run of [marlpde](https://github.com/MindTheGap-ERC/reactive-transport-model-for-limestone-marl-sequences) using Quarto

In the `Python` directory. Marlpde saves `hdf5` files, each run in a separate folder. To download and summarise an entire batch of `marlpde` output files, you can use a template with all analyses to be carried out for each output file. It uses a Quarto format, which is Markdown-based and can be rendered to various formats. 
- `analyses.qmd` has (will have) all the steps to be analysed for each output `hdf5` file. The `yaml` header of the file should be removed. This can probably be fixed by removing this in the Python script ot setting Quarto execution options to ignore unknown fields(?).
- `analyse_marlpde.py` takes following arguments: 
    -   DOI of the archive where the files are stored (must be public, this is a requirement of `datahugger`), 
    -   path where to save the files,
    -   template file with analyses to be carried out.
From the list of folders in 'data', it generates template Quarto files in `to_render`, including the same code for analyses to be carried our on each of the file, taken from the template file. It also generates a `_quarto.yml` file which makes this a project and allows rendering all files at once.

How to use:
```
poetry shell
python3
```
In a Python shell, you can run interactively an example:
```
import analyse_marlpde.py
jghsx = batch_results.Results("10.17605/OSF.IO/JGHSX", "../../data/jghsx/", "analyses.qmd")
```
The first time you have to download the files. Unless you have them locally (make up a DOI) or have downloaded them before. Downloading may take a while.
```
jghsx.download()
```
From local files, generate the Quarto project:
```
jghsx.generate_qmds()
```
Exit Python and render the project. You need Quarto for this.
```
quarto render
```
The default format is `html` but you can also render to something else:
```
quarto render --to gfm
```
Currently execution stops if `hdf5` files are broken. They are broken if `marlpde` had crashed. 

## Authors

__Emilia Jarochowska__  
Utrecht University  
email: e.b.jarochowska [at] uu.nl  
Web page: [www.uu.nl/staff/EBJarochowska](https://www.uu.nl/staff/EBJarochowska)  
ORCID: [0000-0001-8937-9405](https://orcid.org/0000-0001-8937-9405)

## Copyright

Copyright 2023 Netherlands eScience Center and Utrecht University

## License

Apache 2.0 License, see LICENSE file for license text.

## Funding information

Funded by the European Union (ERC, MindTheGap, StG project no 101041077). Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Council. Neither the European Union nor the granting authority can be held responsible for them.
![European Union and European Research Council logos](https://erc.europa.eu/sites/default/files/2023-06/LOGO_ERC-FLAG_FP.png)
