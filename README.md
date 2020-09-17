# Wagtools

Wagtools is an app for Wagtail, a CMS built on Django and Python 3.  Wagtools helps you get Wagtail sites up and running really quickly by providing default pages with many Bootstrap elelments already available via streamfields.  Wagtail Streamfields allow you to choose which elements you would like to ue, and in what order.  The app also provides, social links fields, contact forms, blog / article sections and optional cookie acceptance.

The idea is that using Wagtail and Wagtools you can get a Django website up and hosted within an hour.  We recommend [pythonanywhere.com/](https://www.pythonanywhere.com/), you will need to create a Virtual Environment to use the latest version of Python.  I recommend starting here [Deploying Django to Python Anywhere](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/).  An alternative might be [CookieCutter](https://github.com/cookiecutter/cookiecutter), although for most basic sites this can get confusing.

Essentially an amalgamation of several projects I created which provided :

- All pages have drop-in Streamfield Bootstrap elements such as Carousels, Button Groups, Images, Jumbotrons (with background images), Cards Calendars, Maps etc.
- Form page ready to create contact pages and questionairres.
- Easily embed Facebook and Google Analytic codes through Snippets.
- Sections / Blog pages with 3 Index page styles to choose from.
- Built in Cookie acceptance popup built with JavaScript and CSS.
- Inject Boostrap styling via classes (or your own classes).  For example you can add the class text-dark on the carousel if you have a light image.  Or add "btn btn-success" to turn some links into buttons etc.  Very useful for helping things pop out with having to edit the site code.
- A Footer snippet has been added so you can add editable elements into the footer.

This app is under active development, please log bugs in the [issues section](https://github.com/chandra-kumala-school/wagtools/issues).

# Installation
*Note : Currently you will need to write your own Header, Footer and Nav partials :*
**yoursite/home/templates/partials/_footer.html** 
**yoursite/home/templates/partials/_header.html** && 
**yoursite/home/templates/partials/_nav.html** .  

Reference the header and footer in your base.html like so :
```
{% include 'partials/_header.html' %}
```
And your _nav.html inside your header like this :
{% block nav %}
{% include 'partials/_nav.html' %}
{% endblock %}
We use a **block** for the nav, so that the **orphan contact form** can override the nav and show nothing.  (Marketing campaigns often want a contact form with nav links so visitors fill out the form, rather than explore the site.) 

Ensure you are using Bootstrap 
https://getbootstrap.com/ - Install [Bootstrap 4](https://getbootstrap.com/) locally or use a CDN.
Currently bootstrap is required for this App to render correctly. In the future (asclasses are slowly moved into Wagtools own SCSS) it might be possible to avoid BS, and entirely.

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

# Add Editable Footer
Add this to **yoursite/home/templates/partials/_footer.html** :
```html
    {% editable_footer_tag %}
```

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
