Django Eskiz SMS Integration
============================

Easily integrate EskizUz SMS functionality into your Django application.

Installation
------------

First, install the package using pip:

.. code-block:: sh

    pip install django-eskiz-sms

Then, add ``eskiz_sms`` to your ``INSTALLED_APPS`` in ``settings.py``:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'eskiz_sms',
    ]

Setup
-----

After adding the app, run migrations to set up the necessary database tables:

.. code-block:: sh

    python manage.py makemigrations eskiz_sms
    python manage.py migrate eskiz_sms

Next, go to the Django admin panel and add your EskizUz email and API token in the ``EskizSMS`` model.

Usage
-----

### Sending SMS

To send an SMS, you can use the ``send_sms`` method. Import it into any part of your application where you need to send an SMS:

.. code-block:: python

    from eskiz_sms.views import send_sms

    send_sms(phone_number, message)

### Testing

To test the SMS functionality through the browser, include ``eskiz_sms.urls`` in your project's ``urls.py``:

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('sms/', include('eskiz_sms.urls')),
    ]

Visit the provided URL in your browser to send test SMS messages. **For security reasons, remove this URL after testing.**

SMS Log
-------

You can view the statistics of sent SMS messages in the ``SMSLog`` model in the Django admin panel.

Support
-------

For additional help, join our Telegram group: `Telegram Support <https://t.me/RozmatOtajonov>`_

For a detailed guide, visit: `Django Eskiz SMS Documentation <https://otajonov.dev/django-eskiz-sms>`_

License
-------

MIT License
