let mix = require('laravel-mix');

mix.ts('assets/js/app.ts', 'static/js');
mix.postCss("assets/css/app.css", "static/css", [
 require("tailwindcss"),
]);