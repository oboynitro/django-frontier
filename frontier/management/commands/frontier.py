from frontier.utils import remove_scaffold_files
from frontier.presets import *
from django.core.management import BaseCommand
from django.core.management.base import CommandParser


import shutil
from pathlib import Path


class Command(BaseCommand):
    help = "Swap the front-end scaffolding for your django project"
    available_presets = ("none", "react", "vue", "tailwindcss", "bootstrap", "react_tailwindcss", "vue_tailwindcss", "react_bootstrap", "vue_bootstrap")
    missing_args_message = "Preset missing, please provide a preset to use for scarfolding, {presets}".format(presets=", ".join(available_presets))
    requires_system_checks = False

    def add_arguments(self, parser: CommandParser):
        self.parser = parser
        self.parser.add_argument(
            'type', type=str,
            help="The preset type ({presets})".format(presets=", ".join(self.available_presets))
        )

    def handle(self, *args, **options):
        self.type = options["type"]
        if(self.type is not None and (self.type not in self.available_presets)):
            return self.stdout.write(self.style.WARNING(
                "Invalid preset please choose between ({presets})".format(
                    presets=", ".join(self.available_presets))))
        self.scaffold_base = Path().resolve()
        self.scaffold_resource = Path.joinpath(self.scaffold_base, "resources/")

        if self.type == "none":
            return self.none()
        getattr(self, self.type)()
        return self.stdout.write(
            self.style.WARNING("Please run 'npm install && npm run watch' to compile your fresh scaffolding."))

    def none(self):
        confirm = input(
            'Are you sure you want to delete default frontend files and directories? (y/n): '
        )
        if confirm.lower() != 'y':
            return self.stdout.write('Canceled.')
        remove_scaffold_files(self.scaffold_base)
        if Path.exists(self.scaffold_resource):
            shutil.rmtree(self.scaffold_resource)

        self.stdout.write(self.style.SUCCESS(
            f"Frontend scaffolding removed successfully."))

    def react(self):
        React().install(self.scaffold_resource, self.scaffold_base)
        self.stdout.write(self.style.SUCCESS(
            f"React scaffolding installed successfully."))

    def tailwindcss(self):
        Tailwind().install(self.scaffold_resource, self.scaffold_base)
        self.stdout.write(self.style.SUCCESS(
            f"Tailwindcss scaffolding installed successfully."))

    def bootstrap(self):
        Bootstrap().install(self.scaffold_resource, self.scaffold_base)
        self.stdout.write(self.style.SUCCESS(
            f"Bootstrap scaffolding installed successfully."))

    def vue(self):
        Vue().install(self.scaffold_resource, self.scaffold_base)
        self.stdout.write(self.style.SUCCESS(
            f"Vuejs scaffolding installed successfully."))

    def react_tailwindcss(self):
        ReactTailwind().install(self.scaffold_resource, self.scaffold_base)
        self.stdout.write(self.style.SUCCESS(
            f"React with Tailwindcss scaffolding installed successfully."))

    def react_bootstrap(self):
        ReactBootstrap().install(self.scaffold_resource, self.scaffold_base)
        self.stdout.write(self.style.SUCCESS(
            f"React with Bootstrap scaffolding installed successfully."))

    def vue_tailwindcss(self):
        VueTailwind().install(self.scaffold_resource, self.scaffold_base)
        self.stdout.write(self.style.SUCCESS(
            f"Vuejs with Tailwindcss scaffolding installed successfully."))

    def vue_bootstrap(self):
        VueBootstrap().install(self.scaffold_resource, self.scaffold_base)
        self.stdout.write(self.style.SUCCESS(
            f"Vuejs with Bootstrap scaffolding installed successfully."))
