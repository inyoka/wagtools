# wagtools
Drop-in app providing streamfields, social links field, contact form, sections and cookie acceptance.

Essentially an amalgamation of several existing projects which provide :

- All pages have drop-in Streamfield Bootstrap elements such as Carousels, Button Groups, Images, Jumbotrons (with background images), Cards Calendars, Maps etc.
- Form page ready to create contact pages and questionairres.
- Easily embed Facebook and Google Analytic codes through Snippets.
- Sections / Blog pages with 3 Index page styles to choose from.
- Built in Cookie acceptance popup built with JavaScript and CSS.

This app is under active development, please log bugs in the issues section.

# Installation
Ensure you are using Bootstrap
https://getbootstrap.com/ - Install [Bootstrap 4](https://getbootstrap.com/) locally or use a CDN.

Inside your Wagtail installation use ...
```
git clone https://github.com/chandra-kumala-school/wagtools.git
```
Add wagtools into **settings.py** in the INSTALLED_APPS section:

```
INSTALLED_APPS = [

  'wagtools', # << Add wagtools
  'wagtail.contrib.forms',
  'wagtail.contrib.redirects',
  'wagtail.embeds',
  ...
]
```
Run makemigrations and then migrate the database changes :
```
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
```
