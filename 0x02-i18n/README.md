0x02. i18n
==========

This repo is included in Specializations - Web Stack programming ― Back-end Course of Holberton School. We will cover the `i18n` concept for backend folder.

![Logo](https://www.howtogeek.com/wp-content/uploads/2021/05/laptop-with-terminal-big.png?height=200p&trim=2,2,2,50)

### 1\. Basic Babel setup

Install the Babel Flask extension:

    $ pip3 install flask_babel
    

Then instantiate the `Babel` object in your app. Store it in a module-level variable named `babel`.

In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.

Use `Config` to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).

Use that class as config for your Flask app.

**Repo:**

*   GitHub repository: `holbertonschool-backend`
*   Directory: `0x02-i18n`
*   File: [1-app.py](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/1-app.py)
          [templates/1-index.html](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/templates/1-index.html)

### 2\. Get locale from request

Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.

**Repo:**

*   GitHub repository: `holbertonschool-backend`
*   Directory: `0x02-i18n`
*   File: [2-app.py]() 
          [templates/2-index.html]()

### 3\. Parametrize templates

Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.

Create a `babel.cfg` file containing

    [python: **.py]
    [jinja2: **/templates/**.html]
    extensions=jinja2.ext.autoescape,jinja2.ext.with_
    

Then initialize your translations with

    $ pybabel extract -F babel.cfg -o messages.pot .
    

and your two dictionaries with

    $ pybabel init -i messages.pot -d translations -l en
    $ pybabel init -i messages.pot -d translations -l fr
    

Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:

msgid

English

French

`home_title`

`"Welcome to Holberton"`

`"Bienvenue chez Holberton"`

`home_header`

`"Hello world!"`

`"Bonjour monde!"`

Then compile your dictionaries with

    $ pybabel compile -d translations
    

Reload the home page of your app and make sure that the correct messages show up.

**Repo:**

*   GitHub repository: `holbertonschool-backend`
*   Directory: `0x02-i18n`
*   File: [3-app.py](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/3-app.py)
          [babel.cfg](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/babel.cfg)
          [templates/3-index.html](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/templates/3-index.html)
          [translations/en/LC_MESSAGES/messages.po](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/translations/en/LC_MESSAGES/messages.po)
          [translations/fr/LC_MESSAGES/messages.po](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/translations/fr/LC_MESSAGES/messages.po)
          [translations/en/LC_MESSAGES/messages.mo](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/translations/en/LC_MESSAGES/messages.mo)
          [translations/fr/LC_MESSAGES/messages.mo](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/translations/fr/LC_MESSAGES/messages.mo)

### 4\. Force locale with URL parameter

In this task, you will implement a way to force a particular locale by passing the `locale=fr` parameter to your app’s URLs.

In your `get_locale` function, detect if the incoming request contains `locale` argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting `http://127.0.0.1:5000?locale=[fr|en]`.

**Visiting `http://127.0.0.1:5000/?locale=fr` should display this level 1 heading:** ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/f958f4a1529b535027ce.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220830T170004Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e86105ccade65506b00c4431b2830831cc947136e601cefb6b69625d4f59f3b2)

**Repo:**

*   GitHub repository: `holbertonschool-backend`
*   Directory: `0x02-i18n`
*   File: [4-app.py](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/4-app.py)
          [templates/4-index.html](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/templates/4-index.html)

### 5\. Mock logging in

Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in `5-app.py`.

    users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }
    

This will mock a database user table. Logging in will be mocked by passing `login_as` URL parameter containing the user ID to log in as.

Define a `get_user` function that returns a user dictionary or `None` if the ID cannot be found or if `login_as` was not passed.

Define a `before_request` function and use the `app.before_request` decorator to make it be executed before all other functions. `before_request` should use `get_user` to find a user if any, and set it as a global on `flask.g.user`.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

msgid

English

French

`logged_in_as`

`"You are logged in as %(username)s."`

`"Vous êtes connecté en tant que %(username)s."`

`not_logged_in`

`"You are not logged in."`

`"Vous n'êtes pas connecté."`

**Visiting `http://127.0.0.1:5000/` in your browser should display this:**

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/2c5b2c8190f88c6b4668.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220830T170004Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0bd5826eca6de666061b1cde450cd63a0bc5c89ef0d2b00ad6e8ac4528aa5737)

**Visiting `http://127.0.0.1:5000/?login_as=2` in your browser should display this:** ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/277f24308c856a09908c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220830T170004Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5ce78fe6f6004c45793dd4464062180761038aa7c7d027aea74c61b90df8ee21)

**Repo:**

*   GitHub repository: `holbertonschool-backend`
*   Directory: `0x02-i18n`
*   File: [5-app.py](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/5-app.py)
          [templates/5-index.html](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/templates/5-index.html)

### 6\. Use user locale

Change your `get_locale` function to use a user’s preferred local if it is supported.

The order of priority should be

1.  Locale from URL parameters
2.  Locale from user settings
3.  Locale from request header
4.  Default locale

Test by logging in as different users

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/9941b480b0b9d87dc5de.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220830T170004Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4326f8a1f87ff98529a6aab28562465f83e34576b050ac93cc79110507d3fd86)

**Repo:**

*   GitHub repository: `holbertonschool-backend`
*   Directory: `0x02-i18n`
*   File: [6-app.py](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/6-app.py)
          [templates/6-index.html](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/templates/6-index.html)

### 7\. Infer appropriate time zone

Define a `get_timezone` function and use the `babel.timezoneselector` decorator.

The logic should be the same as `get_locale`:

1.  Find `timezone` parameter in URL parameters
2.  Find time zone from user settings
3.  Default to UTC

Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use `pytz.timezone` and catch the `pytz.exceptions.UnknownTimeZoneError` exception.

**Repo:**

*   GitHub repository: `holbertonschool-backend`
*   Directory: `0x02-i18n`
*   File: [7-app.py](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/7-app.py)
          [templates/7-index.html](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/templates/7-index.html)

### 8\. Display the current time

Based on the inferred time zone, display the current time on the home page in the default format. For example:

`Jan 21, 2020, 5:55:39 AM` or `21 janv. 2020 à 05:56:28`

Use the following translations

msgid

English

French

`current_time_is`

`"The current time is %(current_time)s."`

`"Nous sommes le %(current_time)s."`

**Displaying the time in French looks like this:**

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/bba4805d6dca0a46a0f6.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220830T170004Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5ce384c7fae84e8de88208891d24dbfc9d915b76cf5905b2d27caeb38d9e84bc)

**Displaying the time in English looks like this:**

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/54f3be802024dbcf06f4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220830T170004Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=71899a36b1af3a405c194713d7946af43c3ef8479f8bbb7950781c49b7710db9)

**Repo:**

*   GitHub repository: `holbertonschool-backend`
*   Directory: `0x02-i18n`
*   File: [app.py](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/app.py)
          [templates/index.html](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/templates/index.html)
          [translations/en/LC_MESSAGES/messages.po](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/translations/en/LC_MESSAGES/messages.po)
          [translations/fr/LC_MESSAGES/messages.po](https://github.com/Imanolasolo/holbertonschool-backend/blob/master/0x02-i18n/translations/fr/LC_MESSAGES/messages.po)


## Acknowledgments :mega: 

### **`Holberton School`** (*providing guidance*)
This program was written as part of the curriculum for Holberton School.
Holberton School is a campus-based full-stack software engineering program
that prepares students for careers in the tech industry using project-based
peer learning. For more information, visit [this link](https://www.holbertonschool.com/).
<p align="center">
	<img src="https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg" alt="This is a secret;)">
</p>


