from pathlib import Path
import shutil
from frontier.utils import prepare_scaffold


class Vue():
    def install(self, resource_path, base_dir):
        self.base_dir = base_dir
        self.resource_path = resource_path
        prepare_scaffold(self.base_dir, self.resource_path)
        self.components_dir = Path.joinpath(self.resource_path, "js/")

        self.vue_source = Path.joinpath(
            Path(__file__).resolve().parent, "samples/vue/src")
        self.vue_config = Path.joinpath(
            Path(__file__).resolve().parent, "samples/vue/config")

        shutil.copytree(str(self.vue_source), str(self.components_dir))
        for file in self.vue_config.glob("*"):
            shutil.copy2(str(file), str(self.base_dir))
