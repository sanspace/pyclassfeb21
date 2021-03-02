# Day 12

## Topics

  - Django ORM
  - Django Templating Engine and Language
  - Django Shortcuts
  - Django HTTP utilities

## Refer

  - https://docs.djangoproject.com/en/3.0/intro/tutorial02/
  - https://docs.djangoproject.com/en/3.0/intro/tutorial03/
  - https://docs.djangoproject.com/en/3.1/topics/db/queries/ Django ORM
  - https://docs.djangoproject.com/en/3.1/topics/templates/ Django Template Language
  - If you need a refresher on Web Dev Basics 
    - Learn https://developer.mozilla.org/en-US/docs/Learn
    - Refer https://developer.mozilla.org/en-US/docs/Web/Reference

## Practice

  - Implement a Database and some views for your Django project that contains a `ninjas` app.
    - create a new django project
    - create a new app in this project called `ninjas`. The following tasks to be completed using this app.
    - Have two models
      - Developer(name, experience, country)
      - Skill(name, level, developer) (it should depend on developer with a foreign key releationship)
    - Have index, detail views for these
      - index - show all devs
      - details - show a speicific dev with his skills
        - instead of just a list you can make it a table with the skill level (get creative with any format you like)
        - throw 404 if the dev id does not exist
      - use django templates
    - For adding test data for developers use admin interface
      - register your Developer model in the admin site
      - register your `ninjas` app in the `INSTALLED_APPS` setting
      - use the admin interface forms to add developers
    - For adding test data for skills use django shell
      - use `python manage.py shell` to bring up django shell in your root dir of the app
      - import your models and add skills to your devs (hint: remember to leverage the foreign key relationship here)

## Bonus Challenge

  - Implement filtering for the devs
    - if you receive skill filter as python show only python devs
  - Register your Skill model as well in the admin site and try editing it using the admin interface
