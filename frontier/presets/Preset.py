from pathlib import Path
import shutil


class Preset():
    def prepareScarfold(self, components_dir):
        self.components_dir = components_dir
        if(Path.exists(self.components_dir)):
            shutil.rmtree(self.components_dir)
