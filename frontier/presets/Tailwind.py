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
        shutil.copy2(str(f"{base_packages_path}/package.json"), str(base_dir))
        scripts = {
            "build": "rm -rf .cache static/build && npm run parcel && npm run postcss",
            "postcss": "postcss resources/css/index.css -o static/build/*.css",
            "parcel": "parcel build resources/css/index.css -d static/build"
        }
        devDependencies = {
            "parcel-bundler": "^1.12.4",
            "tailwindcss": "^1.9.6",
            "postcss-cli": "^8.3.0"
        }
        update_packages(
            base_dir, devDependencies=devDependencies, scripts=scripts)
