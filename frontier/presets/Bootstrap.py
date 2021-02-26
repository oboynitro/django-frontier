from .Preset import update_packages
from pathlib import Path
import shutil
from frontier.utils import prepare_scaffold


class Bootstrap():
    def install(self, resource_path, base_dir):
        prepare_scaffold(base_dir, resource_path)
        components_dir = Path.joinpath(resource_path, "js/")
        sass_components_dir = Path.joinpath(resource_path, "scss/")
        base_packages_path = Path.joinpath(
            Path(__file__).resolve().parent, "samples/default")
        components_source = Path.joinpath(
            Path(__file__).resolve().parent, "samples/bootstrap/src/js")
        scss_components_source = Path.joinpath(
            Path(__file__).resolve().parent, "samples/bootstrap/src/scss")

        shutil.copytree(str(components_source), str(components_dir))
        shutil.copytree(str(scss_components_source),
                        str(sass_components_dir))
        for conf_file in base_packages_path.glob("*"):
            shutil.copy2(str(conf_file), str(base_dir))
        dependencies = {
            "bootstrap": "^4.5.1",
            "jquery": "^3.2",
            "popper.js": "^1.14"
        }
        update_packages(base_dir, dependencies)
