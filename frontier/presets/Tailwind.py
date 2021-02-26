from pathlib import Path
import shutil
from frontier.utils import prepare_scaffold
from .Preset import update_packages


class Tailwind():
    def install(self, resource_path, base_dir):
        self.base_dir = base_dir
        self.resource_path = resource_path
        prepare_scaffold(self.base_dir, self.resource_path)
        self.components_dir = Path.joinpath(self.resource_path, "css/")
        base_packages_path = Path.joinpath(
            Path(__file__).resolve().parent, "samples/default")
        self.tailwind_source = Path.joinpath(
            Path(__file__).resolve().parent, "samples/tailwind/src")
        self.tailwind_config = Path.joinpath(
            Path(__file__).resolve().parent, "samples/tailwind/config")

        shutil.copytree(str(self.tailwind_source), str(self.components_dir))
        for file in self.tailwind_config.glob("*"):
            shutil.copy2(str(file), str(self.base_dir))
        for conf_file in base_packages_path.glob("*"):
            shutil.copy2(str(conf_file), str(base_dir))
        devDependencies = {
            "tailwindcss": "^1.9.6",
            "postcss-cli": "^8.3.0"
        }
        update_packages(
            base_dir, devDependencies=devDependencies)
