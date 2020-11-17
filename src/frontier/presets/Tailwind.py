from pathlib import Path
import shutil


class Tailwind():
    def install(self, resource_path, base_dir):
        self.base_dir = base_dir
        self.resource_path = resource_path
        self.components_dir = Path.joinpath(self.resource_path, "css/")

        self.tailwind_source = Path.joinpath(
            Path(__file__).resolve().parent, "samples/tailwind/src")
        self.tailwind_config = Path.joinpath(
            Path(__file__).resolve().parent, "samples/tailwind/config")

        shutil.copytree(str(self.tailwind_source), str(self.components_dir))
        for file in self.tailwind_config.glob("*"):
            shutil.copy2(str(file), str(self.base_dir))
