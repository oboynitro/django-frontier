from frontier.presets.Preset import Preset
from pathlib import Path
import shutil


class React():
    def install(self, resource_path, base_dir):
        self.base_dir = base_dir
        self.resource_path = resource_path
        self.components_dir = Path.joinpath(self.resource_path, "js/")

        self.react_source = Path.joinpath(
            Path(__file__).resolve().parent, "samples/react/src")
        self.react_config = Path.joinpath(
            Path(__file__).resolve().parent, "samples/react/config")

        shutil.copytree(str(self.react_source), str(self.components_dir))
        for file in self.react_config.glob("*"):
            shutil.copy2(str(file), str(self.base_dir))
