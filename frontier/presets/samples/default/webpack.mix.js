const mix = require('laravel-mix');

mix.js('resources/js/index.jsx', 'static/js')
    .postCss('resources/js/index.css', 'static/css', [
        //
    ]);
