# Wagtools
Drop-in app providing streamfields, social links field, contact form, sections and cookie acceptance.

Essentially an amalgamation of several existing projects which provide :

- All pages have drop-in Streamfield Bootstrap elements such as Carousels, Button Groups, Images, Jumbotrons (with background images), Cards Calendars, Maps etc.
- Form page ready to create contact pages and questionairres.
- Easily embed Facebook and Google Analytic codes through Snippets.
- Sections / Blog pages with 3 Index page styles to choose from.
- Built in Cookie acceptance popup built with JavaScript and CSS.
- Inject Boostrap styling via classes.  FOr example you can add the class text-dark on the carousel if you have a light image.  Or add "btn btn-success" to turn some links into buttons etc.  Very useful for helping things pop out with having to edit the site code.

This app is under active development, please log bugs in the [issues section](https://github.com/chandra-kumala-school/wagtools/issues).

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

# Bootstrap CSS Insertion

Many elements have CSS field which is intended to allow for you to insert Bootstrap classes such as **bg-success** or **text-warning** etc
See here :
https://getbootstrap.com/docs/4.5/utilities/colors/ - Use [Bootstrap 4](https://getbootstrap.com/docs/4.5/utilities/colors/) color classes.

However you can just as easily create your own CSS classes in the SASS files provided.

# Social Links
You can use the Social Links snippets to store and display a group of social media links with icons, which can be styled with BS classes or your own.  It is recommended that you use icons such as those available at 
https://fontawesome.com/ - Use [FontAwesome](https://getbootstrap.com/docs/4.5/utilities/colors/) choose social media icons.

Bootstrap has a growing number of SVG icons available, although they are **not yet supported** : 
https://icons.getbootstrap.com/ - [Built -in Bootstrap Icons](https://icons.getbootstrap.com/)


# Enable Cookie Consent

Create a Privacy Policy at **yourdomain.com/privacy-policy**.

In your base template add this to the top, just after your bootstrap code :
```
<!-- Cookie Consent -->
<link rel="stylesheet" href="{% static 'css/consent.css' %} " />
```
Include this partial in your base.html's main <body> :
```
{% include 'partials/_consent.html' %}
```
Add this at the bottom underneath the footer, and after any other Javascript imports :
  ```    
  <!-- Cookie Acceptance -->
  <script src="{% static 'js/consent.js' %}"></script>
  ```
