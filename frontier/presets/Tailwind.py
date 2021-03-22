from pathlib import Path
import shutil
from frontier.utils import prepare_scaffold
from .Preset import update_packages


class Tailwind():
    def install(self, resource_path, base_dir):
        prepare_scaffold(base_dir, resource_path)
        components_dir = resource_path / "css"
        base_packages_path = Path.joinpath(
            Path(__file__).resolve().parent, "samples/default")
        tailwind_source = Path.joinpath(
            Path(__file__).resolve().parent, "samples/tailwind/src")
        tailwind_config = Path.joinpath(
            Path(__file__).resolve().parent, "samples/tailwind/config")

        shutil.copytree(str(tailwind_source), str(components_dir))
        for file in tailwind_config.glob("*"):
            shutil.copy2(str(file), str(base_dir))
        for conf_file in base_packages_path.glob("*"):
            shutil.copy2(str(conf_file), str(base_dir))
        devDependencies = {
            "tailwindcss": "^1.9.6",
            "postcss-cli": "^8.3.0",
            "postcss": "^8.1.14",
		    "postcss-import": "^12.0.1"
        }
        update_packages(
            base_dir, devDependencies=devDependencies)
