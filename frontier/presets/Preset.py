from pathlib import Path
import json


def update_packages(base_dir, dependencies={}, devDependencies={}, scripts={}):
    packages_path = Path.joinpath(base_dir, "package.json")
    packages_file = open(f"{packages_path}",)
    packages = json.load(packages_file)

    packages["devDependencies"] = {
        **packages["devDependencies"], **devDependencies}
    packages["dependencies"] = {**packages["dependencies"], **dependencies}
    packages["dependencies"] = {**packages["dependencies"], **dependencies}
    packages["scripts"] = {**packages["scripts"], **scripts}
    output = json.dumps(packages, indent=4)

    with open(f"{packages_path}", "w") as file:
        file.writelines(output)
        file.close()
        packages_file.close()
