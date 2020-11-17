from pathlib import Path
import shutil


class VueBootstrap():
    def install(self, resource_path, base_dir):
        self.base_dir = base_dir
        self.resource_path = resource_path
        self.components_dir = Path.joinpath(self.resource_path, "js/")

        self.components_source = Path.joinpath(
            Path(__file__).resolve().parent, "samples/vue_bootstrap/src")

        self.components_config = Path.joinpath(
            Path(__file__).resolve().parent, "samples/vue_bootstrap/config")

        shutil.copytree(str(self.components_source), str(self.components_dir))
        for file in self.components_config.glob("*"):
            shutil.copy2(str(file), str(self.base_dir))
