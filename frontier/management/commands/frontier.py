from frontier.presets.React import React
from frontier.presets.Vue import Vue
from frontier.presets.Preset import Preset
from frontier.presets.ReactTailwind import ReactTailwind
from frontier.presets.VueTailwind import VueTailwind
from frontier.presets.ReactBootstrap import ReactBootstrap
from frontier.presets.VueBootstrap import VueBootstrap
from frontier.presets.Tailwind import Tailwind
from frontier.presets.Bootstrap import Bootstrap
from django.core.management import BaseCommand
from django.core.management.base import CommandParser


import shutil
from pathlib import Path


class Command(BaseCommand):
    help = "Swap the front-end scaffolding for your django project"
    missing_args_intro = "Preset missing, please provide a preset to use for scarfolding,"
    invalid_args_intro = "Invalid scaffold preset,"
    available_presets = """
    ** Available Presets:
        - none
        - react
        - vue
        - tailwindcss
        - bootstrap
        - react-tailwindcss
        - vue-tailwindcss
        - react-bootstrap
        - vue-bootstrap
    """
    missing_args_message = f"{missing_args_intro} {available_presets}"

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            'preset', nargs="?",
            help="""Specify the front-end framework to scarfold
                        (none, react, vue, tailwindcss, bootstrap, react-tailwindcss, vue-tailwindcss, react-bootstrap, vue-bootstrap)"""
        )

    def handle(self, *args, **options):
        self.preset = options["preset"]

        if(self.preset is not None and (self.preset not in ["none", "react", "vue", "tailwindcss", "bootstrap", "react-tailwindcss", "vue-tailwindcss", "react-bootstrap", "vue-bootstrap"])):
            self.stdout.write(self.style.WARNING(
                f"{self.invalid_args_intro} {self.preset} {self.available_presets}"))

        else:
            self.scaffoldSetup()

    def scaffoldSetup(self, *args, **options):
        self.base_dir = Path().resolve()
        self.resource_path = Path.joinpath(self.base_dir, "resources/")

        if not Path.exists(self.resource_path):
            Path.mkdir(self.resource_path)
        else:
            Preset().prepareScarfold(self.resource_path)

        if Path.exists(Path.joinpath(self.base_dir, "package.json")):
            Path.unlink(Path.joinpath(self.base_dir, "package.json"))
        if Path.exists(Path.joinpath(self.base_dir, ".babelrc")):
            Path.unlink(Path.joinpath(self.base_dir, ".babelrc"))
        if Path.exists(Path.joinpath(self.base_dir, "postcss.config.js")):
            Path.unlink(Path.joinpath(self.base_dir, "postcss.config.js"))
        if Path.exists(Path.joinpath(self.base_dir, "tailwind.config.js")):
            Path.unlink(Path.joinpath(self.base_dir, "tailwind.config.js"))
        if Path.exists(Path.joinpath(self.base_dir, "node_modules/")):
            shutil.rmtree(self.base_dir, "node_modules/")

        if self.preset == "none":
            self.default()

        elif self.preset == "react":
            self.react()

        elif self.preset == "vue":
            self.vue()

        elif self.preset == "tailwindcss":
            self.tailwind()

        elif self.preset == "bootstrap":
            self.bootstrap()

        elif self.preset == "react-tailwindcss":
            self.react_tailwind()

        elif self.preset == "react-bootstrap":
            self.react_bootstrap()

        elif self.preset == "vue-tailwindcss":
            self.vue_tailwind()

        elif self.preset == "vue-bootstrap":
            self.vue_bootstrap()

        else:
            self.stdout.write(self.style.WARNING(
                f"{self.invalid_args_intro} {self.preset} {self.available_presets}"))

    def default(self, *args, **options):
        if Path.exists(self.resource_path):
            shutil.rmtree(self.resource_path)

        self.stdout.write(self.style.SUCCESS(
            f"Scaffolding removed successfully."))

    def react(self, *args, **options):
        React().install(self.resource_path, self.base_dir)
        self.stdout.write(self.style.SUCCESS(
            f"React scaffolding installed successfully."))
        self.stdout.write(
            "Please run 'npm install && npm run watch' to compile your fresh scaffolding.")

    def tailwind(self, *args, **options):
        Tailwind().install(self.resource_path, self.base_dir)

        self.stdout.write(self.style.SUCCESS(
            f"Tailwindcss scaffolding installed successfully."))
        self.stdout.write(
            "Please run 'npm install && npm run watch' to compile your fresh scaffolding.")

    def bootstrap(self, *args, **options):
        Bootstrap().install(self.resource_path, self.base_dir)

        self.stdout.write(self.style.SUCCESS(
            f"Bootstrap scaffolding installed successfully."))
        self.stdout.write(
            "Please run 'npm install && npm run watch' to compile your fresh scaffolding.")

    def vue(self, *args, **options):
        Vue().install(self.resource_path, self.base_dir)
        self.stdout.write(self.style.SUCCESS(
            f"Vue scaffolding installed successfully."))
        self.stdout.write(
            "Please run 'npm install && npm run watch' to compile your fresh scaffolding.")

    def react_tailwind(self, *args, **options):
        ReactTailwind().install(self.resource_path, self.base_dir)

        self.stdout.write(self.style.SUCCESS(
            f"React with tailwindcss scaffolding installed successfully."))
        self.stdout.write(
            "Please run 'npm install && npm run watch' to compile your fresh scaffolding.")

    def react_bootstrap(self, *args, **options):
        ReactBootstrap().install(self.resource_path, self.base_dir)

        self.stdout.write(self.style.SUCCESS(
            f"React with bootstrap scaffolding installed successfully."))
        self.stdout.write(
            "Please run 'npm install && npm run watch' to compile your fresh scaffolding.")

    def vue_tailwind(self, *args, **options):
        VueTailwind().install(self.resource_path, self.base_dir)

        self.stdout.write(self.style.SUCCESS(
            f"Vue with tailwindcss scaffolding installed successfully."))
        self.stdout.write(
            "Please run 'npm install && npm run watch' to compile your fresh scaffolding.")

    def vue_bootstrap(self, *args, **options):
        VueBootstrap().install(self.resource_path, self.base_dir)

        self.stdout.write(self.style.SUCCESS(
            f"Vue with bootstrap scaffolding installed successfully."))
        self.stdout.write(
            "Please run 'npm install && npm run watch' to compile your fresh scaffolding.")
