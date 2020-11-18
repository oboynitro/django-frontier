from pathlib import Path
import shutil


class Bootstrap():
    def install(self, resource_path, base_dir):
        self.base_dir = base_dir
        self.resource_path = resource_path
        self.components_dir = Path.joinpath(self.resource_path, "js/")
        self.sass_components_dir = Path.joinpath(self.resource_path, "scss/")

        self.components_source = Path.joinpath(
            Path(__file__).resolve().parent, "samples/bootstrap/src/js")
        self.scss_components_source = Path.joinpath(
            Path(__file__).resolve().parent, "samples/bootstrap/src/scss")

        self.components_config = Path.joinpath(
            Path(__file__).resolve().parent, "samples/bootstrap/config")

        shutil.copytree(str(self.components_source), str(self.components_dir))
        shutil.copytree(str(self.scss_components_source),
                        str(self.sass_components_dir))
        for file in self.components_config.glob("*"):
            shutil.copy2(str(file), str(self.base_dir))
