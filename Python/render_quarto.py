import subprocess
import yaml
import jinja2
import os

def render_quarto_with_parameters(qmd_file, parameters, output_dir):
    # Read the Quarto document
    with open(qmd_file, 'r') as qmd_file:
        qmd_content = qmd_file.read()

    # Print the parameters for debugging
    print("Parameters:", parameters)

    # Create a Jinja2 template environment
    env = jinja2.Environment()

    # Update the template environment with the parameters
    template = env.from_string(qmd_content)
    rendered_content = template.render(parameters)

    # Write the updated content to a temporary file
    temp_qmd_file = 'temp.qmd'
    with open(temp_qmd_file, 'w') as temp_file:
        temp_file.write(rendered_content)

    # Construct the quarto command
    output_pdf = os.path.join(output_dir, f"output_{parameters['solution_path']}.pdf")
    quarto_command = [
        "quarto",
        "render",
        "--to=pdf",
        "--output=" + output_pdf,
        temp_qmd_file
    ]

    # Run the quarto command
    subprocess.run(quarto_command, check=True)

    # Clean up the temporary file
    os.remove(temp_qmd_file)


def main():
    # Replace 'example.qmd' with your Quarto document file
    qmd_file = 'run_summary.qmd'

    # Replace 'parameters.yaml' with your YAML parameter file
    yaml_file = 'parameters.yaml'

    # Replace 'output_dir' with the desired output directory
    output_dir = 'runs'

    # Read parameters from the YAML file
    with open(yaml_file, 'r') as file:
        parameters_list = yaml.load(file, Loader=yaml.FullLoader)

    # Iterate through the parameter sets and render the Quarto document
    for parameters in parameters_list:
        render_quarto_with_parameters(qmd_file, parameters, output_dir)

if __name__ == "__main__":
    main()
