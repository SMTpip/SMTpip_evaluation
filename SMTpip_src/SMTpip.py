import os
import time
from z3 import Context
from create_requirements import generate_requirements_txt, read_solution_file
from dependency import fetch_direct_dependencies, fetch_transitive_dependencies_with_depth
from read import read_json_file, read_requirements
from requirements import parse_requirements
from smt import generate_smt_expression, smt_solver

# Import functionalities from python_version_resolver
from python_version_resolver import load_python_versions_json, collect_python_versions, merge_constraints, filter_python_versions, get_latest_version, update_install_script

def read_install_script(install_script_path):
    """
    Reads the generated installScript.txt file and parses package names and versions.
    Expects each line in installScript.txt to have the format 'package==version'.
    """
    with open(install_script_path, 'r') as file:
        lines = file.readlines()

    # Extract package name and version from each line and return as a list of tuples
    parsed_requirements = []
    for line in lines:
        if '==' in line:  # Check for 'package==version' format
            package, version = line.strip().split('==')
            parsed_requirements.append((package, version))
    
    return parsed_requirements

def main():
    """
    Main function to execute the dependency resolution process, including reading files,
    parsing requirements, fetching dependencies, generating SMT expressions, and solving them.
    """
    directory = "example"
    json_path = os.path.join(directory, "all_python_versions.json")  # Path to the JSON file

    # Read files from the directory
    start_time = time.time()
    requirements_txt = read_requirements(directory)
    projects_data = read_json_file(directory)  # This path is used for both the projects data and the JSON file

    # Parse requirements
    requirements = parse_requirements(requirements_txt)

    # Fetch matching versions and their dependencies
    direct_dependencies = fetch_direct_dependencies(requirements, projects_data)
    transitive_dependencies, max_depth, total_unique_packages, total_unique_versions = fetch_transitive_dependencies_with_depth(
        direct_dependencies, projects_data
    )

    # Generate SMT expression
    ctx = Context()
    solver = generate_smt_expression(
        direct_dependencies, transitive_dependencies, ctx, add_soft_clauses=False, minimize_packages=False
    )

    # Solve the SMT expression
    solution, proof, start_time, end_time = smt_solver(solver, ctx)
    if solution:
        with open(os.path.join(directory, "string_solution.txt"), "w") as file:
            file.write(str(solution))
        
        solution_dict = read_solution_file(
            os.path.join(directory, "string_solution.txt")
        )
        generate_requirements_txt(solution_dict, directory, "installScript.txt")

        # Now read the installScript.txt to get the packages and versions
        install_script_path = os.path.join(directory, "installScript.txt")
        parsed_install_script = read_install_script(install_script_path)

        # Load Python versions from the same JSON file
        python_versions_data = projects_data  # Since it's the same file, just reuse `projects_data`

        # Collect Python versions based on package dependencies from the installScript.txt
        python_versions = collect_python_versions(parsed_install_script)

        # Merge the Python version constraints
        merged_constraints = merge_constraints(python_versions)

        # Filter compatible Python versions from JSON data
        valid_python_versions = filter_python_versions(merged_constraints, python_versions_data)

        # Get the latest Python version
        latest_python_version = get_latest_version(valid_python_versions)

        # Update the installScript.txt with the latest Python version
        update_install_script(directory, latest_python_version)

        print("installScript.txt is generated")
        print("solved in : ", end_time - start_time)
    else:
        print(proof)
        with open(os.path.join(directory, "proof.txt"), "w") as file:
            file.write(proof)


if __name__ == "__main__":
    main()
