const mix = require('laravel-mix');

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel applications. By default, we are compiling the CSS
 | file for the application as well as bundling up all the JS files.
 |
 */
// sets the output directory for your compiled assets
mix.setPublicPath('static');

// your mix configuration goes here


// used only in production (to add versioning to complied files)
if (mix.inProduction()) {
    mix.version();
}
/*
copy one of the following mix configurations commented below and use per your scaffold type
and configure the input file and output directory as per your project settings.
DONT FORGET YOUR SEMI-COLONS, :)

example mix file
mix.js('resources/js/index.js', 'static/');

....'resources/js/index.js' = input file
....'static/' = output directory

NB** mix config can be chained eg: mix.js(...).css(...).sass(...).postCss(...) e.t.c
for more information on laravel-mix, visit "https://lravel-mix.com"



----------------------------------------------------------------------------
Example mix settings

----bootstrap mix
mix.js('resources/js/index.js', 'static/')
    .sass('resources/sass/app.scss', 'static/');

----tailwind mix
mix.postCss('resources/css/app.css', 'static/', [
        require('postcss-import'),
        require('tailwindcss'),
        require('autoprefixer'),
    ]);

----vuejs mix
mix.js('resources/js/src/index.js', 'static/').vue();

----reactjs mix
mix.js('resources/js/src/index.js', 'static/').react();
*/