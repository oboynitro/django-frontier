import shutil
from pathlib import Path

from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from django.conf import settings

from frontier.presets import *
from frontier.utils import remove_scaffold_files


class Command(BaseCommand):
    help = "Swap the front-end scaffolding for your django project"
    available_presets = ("none", "react", "vue", "tailwindcss", "bootstrap")
    missing_args_message = "Preset missing, please provide a preset to use for scarfolding, {presets}".format(presets=", ".join(available_presets))
    requires_system_checks = False

    def add_arguments(self, parser: CommandParser):
        self.parser = parser
        self.parser.add_argument(
            'type', type=str,
            help="The preset type ({presets})".format(presets=", ".join(self.available_presets))
        )
        self.parser.add_argument(
            '--appname',
            help="The app to generate the scaffold in (configured in setings file 'INSTALLED_APP')" 
        )

    def handle(self, *args, **options):
        self.type = options["type"]
        self.appname = options["appname"]

        if(self.type is not None and (self.type not in self.available_presets)):
            return self.stdout.write(self.style.WARNING(
                "Invalid preset please choose between ({presets})".format(
                    presets=", ".join(self.available_presets))))
        if(self.appname is not None and self.appname not in settings.INSTALLED_APPS):
            return self.stdout.write(self.style.WARNING(
                f"App {self.appname} not found, did you forget to add it to your installed apps ?"))
        if(self.appname):
            self.scaffold_base = settings.BASE_DIR / self.appname
        else:
            self.scaffold_base = settings.BASE_DIR
        self.scaffold_resource = self.scaffold_base / "resources"

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
            f"Vue scaffolding installed successfully."))