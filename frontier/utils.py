from pathlib import Path
import shutil


def prepare_scaffold(base_dir, resource_path):
    remove_scaffold_files(base_dir)
    create_or_save_resource_path(resource_path)


def remove_scaffold_files(base_dir):
    if Path.exists(base_dir / "package.json"):
        Path.unlink(base_dir / "package.json")
    if Path.exists(base_dir / "webpack.mix.js"):
        Path.unlink(base_dir / "webpack.mix.js")
    if Path.exists(base_dir / ".babelrc"):
        Path.unlink(base_dir / ".babelrc")
    if Path.exists(base_dir / "postcss.config.js"):
        Path.unlink(base_dir / "postcss.config.js")
    if Path.exists(base_dir / "tailwind.config.js"):
        Path.unlink(base_dir / "tailwind.config.js")
    if Path.exists(base_dir / "node_modules/"):
        shutil.rmtree(base_dir / "node_modules/")


def create_or_save_resource_path(resource_path):
    if not Path.exists(resource_path):
        return Path.mkdir(resource_path)
    return shutil.rmtree(f"{resource_path}/")
