# Utility scripts to examine and plot outputs of the reactive transport model by L'Heureux

To be applied to the outputs of the [Python implementation](https://github.com/MindTheGap-ERC/reactive-transport-model-for-limestone-marl-sequences)
and possibly the [Fortran predecessor](https://github.com/astro-turing/lheureux)

These are attempts to reproduce the diagenetic model for the formation of limestone-marl alternations proposed in [L’Heureux, ‘Diagenetic Self-Organization and Stochastic Resonance in a Model of Limestone-Marl Sequences’. 2018. Geofluids e4968315, doi: 10.1155/2018/4968315](https://www.hindawi.com/journals/geofluids/2018/4968315/)

## Automating summaries of each run using Quarto

In the `Python` directory, the following steps are attempted:
- `download_files.py` get a batch of files from OSF and save in a `data` folder outside of the repository
- `generate_parameters.py` generate a `parameters.yaml` from the list of files saved in `data`
- `generate_templates.py` generate copies of the template Quarto document, `run_summary.qmd`, to be rendered one by one, saving them in the `rendered_files` folder
- `run_quarto.py` iterate through the files listed in `parameters.yaml` to execute `quarto render` for each file in `rendered_files`

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
