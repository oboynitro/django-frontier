# Django-Frontier
![Github](https://img.shields.io/github/license/oboynitro/django-frontier)
![Build Status](https://img.shields.io/github/stars/oboynitro/django-frontier)
![Build Issues](https://img.shields.io/github/issues/oboynitro/django-frontier)
![Build Forks](https://img.shields.io/github/forks/oboynitro/django-frontier)
## The django front-end scaffold tool you requested.

Tired of always having to setup your front end apps **(react, vue, bootstrap tailwindcss)** for your django projects, not any more. Every django developer knows how annoying it is to setup a front end for your django apps with the latest and greatest frontend frameworks, with [django-frontier](https://pypi.org/django-frontier) you get to set up your frontend scaffold with a single command. A breeze 😇

---

### Before you install

Before you install [django-frontier](https://pypi.org/django-frontier), please make sure you have python installed and you have a working django project either with with your local python installation or a virtual environment. We recommend the latter

### Installation guide

1. Open your terminal and install the [django-frontier](https://pypi.org/django-frontier) package using pip

```bash
$ pip install django-frontier
```

2. After the installation, add the ‘frontier’ app to the **INSTALLED_APPS** of your django project settings

```python
INSTALLED_APPS = [
    ...
    'frontier',
    ...
]
```

3. Now you can use the frontier command by navigating to the root of your project directory, where ‘manage.py’ file is and run the frontier with either preset _(vue, react, tailwind, or bootstrap)_

for example, a react scaffold looks like this:

```bash
$ python manage.py frontier react
```

This generates a resources directory with your react application scaffold. Your directory structure looks like this:

```
your_project/
    resources/
        js/
            App.js
            index.js
            components/
                Example.js
    manage.py
    webpack.mix.js
    package.json
    .babelrc

    ...
```

4. Configure your static assets by editing webpack.mix.js file.

```js
const mix = require('laravel-mix');

mix.js('resources/js/index.js', 'static/').react();
```

**NOTE**: django-frontier uses `laravel-mix js <https://laravel-mix.com>`_ to compile and bundle all of it assets. You can read more about `laravel mix <https://laravel-mix.com>`_ on thier website


5. You can then compile your assets by running

```bash
$ npm run watch
```

This spits out the complied assets in a static/ directory at the root of your project

```
static/
      js/
        index.js
        index.map.js
      css/
        index.css
        index.map.css
```

You can modify the output of the compiled assets in your _‘webpack.mix.js’_ file.

6. After compilation, setup your _STATIC_URL_ and _STATICFILES_DIRS_ in your django project settings.

```python
# settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static/'] #new in django 3.0 which uses pathlib module
```

7. Setup your template

```html
<!DOCTYPE html>
{% load static %}
<html>
	<head>
		...
		<!-- if your dist folder includes css files -->
		<link rel="stylesheet" href="{% static 'css/index.css' %}" />
		...
	</head>
	<body>
		<!-- for your react / vue app, set up to include the compiled js files -->
		<div id="app"></div>
		<script src="{% static 'js/index.js' %}"></script>
	</body>
</html>
```

8. For production, run the **build** command to minify the js and css for a smaller bundle

```bash
$ npm run build
```

---

**MORE**: Run the frontier command with -h flag for help and more options

```bash
$ python manage.py frontier -h
```

### Enjoy 😇
