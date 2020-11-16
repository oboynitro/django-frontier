django-frontier package
=======================

The django front-end scaffold tool you requested.
--------------------------------------------------

Tired of always having to setup your front end apps **(react, vue, bootstrap tailwindcss)** for your django projects,
not any more. Every django developer knows how **annoying** it is to setup a front end for your django apps with the latest and
greatest frontend frameworks, with `django-frontier <https://pypi.org/django-frontier/>`_ you get to set up your *frontend scaffold* with a single command. *A breeze :)*.



Before you install
-------------------

Before you install `django-frontier <https://pypi.org/django-frontier/>`_, please make sure you have python installed and you have a working django project either with with your local python installation or a virtual environment. We recommend the *latter*



Installation guide
-------------------

**1.** Open your terminal and install the `django-frontier <https://pypi.org/django-frontier/>`_ package using pip
::
    $ pip install django-frontier

**2.** After the installation, add the 'frontier' app to the **INSTALLED_APPS** of your django project settings
::
    INSTALLED_APPS = [
        ...
        'frontier',
        ...
    ]

**3.** Now you can use the frontier command by navigating to the root of your project directory, where 'manage.py' file is and run the frontier with either preset *(react, tailwind, or react-tailwind)*

for example, a react scaffold looks like this:
::
    $ python manage.py frontier react

                or

    $ ./manage.py frontier react

This generates a resources directory with your react application scaffold. Your directory structure looks like this:
::
    your_project/
       resources/
       js/
        App.js
        index.js
        components/
          Example.js
       manage.py
       package.json
       .babelrc

       ..


**4.** You can then compile your assets by running
::
    $ npm run watch

This spits out the complied assets in a static/dist directory at the root of your project
::
    static/
      dist/
        index.js
        index.map.js

You can modify the output of the compiled assets in your *'package.json'* file.

**NOTE**: django-frontier uses `parcel js <https://parceljs.org>`_ to compile and bundle all of it assets. You can read more about `parcel js <https://parceljs.org>`_ on thier website

**5.** After compilation, setup your *STATIC_URL* and *STATICFILES_DIRS* in your django project settings.
::
    STATIC_URL = '/static/'
    STATICFILES_DIRS = BASE_DIR / 'static' #new in django 3.0 which uses pathlib module

**6.** Setup your template
::
    <!DOCTYPE html>
    {% load static %}
    <html>
        <head>
            ...
            <!-- if your dist folder includes css files -->
            <link rel="stylesheet" href="{% static 'dist/app.css' %}" />
            ...
        </head>
        <body>
            <!-- for your react / vue app, set up to include the compiled js files -->
            <div id="app"></div>
            <script src="{% static 'dist/index.js' %}"></script>
        </body>
    </html>

**7.** For production, run the **build** command to minify the js and css for a smaller bundle and replace *dist/* with *build/* in your templates
::
   $ npm run build

**MORE:** Run the frontier command with *-h* flag for help and more options
::
    $ python manage.py frontier -h

                or

    $ ./manage.py frontier -h

Enjoy :)