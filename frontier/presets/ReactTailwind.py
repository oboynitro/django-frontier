from pathlib import Path
import shutil
from frontier.utils import prepare_scaffold
from .Preset import update_packages


class ReactTailwind():
    def install(self, resource_path, base_dir):
        prepare_scaffold(base_dir, resource_path)
        components_dir = Path.joinpath(resource_path, "js/")
        base_packages_path = Path.joinpath(
            Path(__file__).resolve().parent, "samples/default")
        components_source = Path.joinpath(
            Path(__file__).resolve().parent, "samples/react_tailwind/src")
        components_config = Path.joinpath(
            Path(__file__).resolve().parent, "samples/react_tailwind/config")
        babel_source = Path.joinpath(
            Path(__file__).resolve().parent, "samples/react/config")

        shutil.copytree(str(components_source), str(components_dir))
        for file in components_config.glob("*"):
            shutil.copy2(str(file), str(base_dir))
        for conf_file in base_packages_path.glob("*"):
            shutil.copy2(str(conf_file), str(base_dir))
        shutil.copy2(str(f"{babel_source}/.babelrc"), str(base_dir))
        dependencies = {
            "tailwindcss": "^1.9.6",
            "react": "^17.0.1",
            "react-dom": "^17.0.1"
        }
        devDependencies = {
            "@babel/core": "^7.12.3",
            "@babel/preset-env": "^7.12.1",
            "@babel/preset-react": "^7.12.5",
            "babel-loader": "^8.2.1"
        }
        update_packages(base_dir, dependencies, devDependencies)
