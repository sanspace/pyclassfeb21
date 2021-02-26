# Day 10

## Topics

  - Review
    - Python
    - Pipenv
    - Flask
    - Flask RESTful
    - SQLAlchemy
    - Marshmallow
    - PyTest
  - Improve Code Quality
    - black
    - flake8
    - mypy

## Refer

  - https://semver.org/

## Practice

  - Apply everything you have learnt so far to create a REST API
    - supports CRUD operations
    - has valid DB model with all the criteria (unique, nullable etc.)
    - has validators using the schema for serizalizing/deserializing
    - returns appropriate HTTP codes
    - contains unit tests using pytest
    - use venv
  - There are tons of quizzes out there in varying level of difficulty. Pick your fav! As I had mentioned HackerRank (or leetcode or similar platforms) is your best bet as it makes you write code rather than just shooting for 1 out of 4 possibilities!
    - https://realpython.com/quizzes/
    - https://pynative.com/python-quizzes/
    - https://www.tutorialspoint.com/python/python_online_quiz.htm

  
## Bonus Challenge

  - Add black formatter to your code editor to format your code
  - Add type hints to your API (this is hard as you work with compound types. try at your own risk!)

## Q & A

i have a quesiton regarding validation of models using Marshmallow. Do we handle those errors by using try|Except block? and can we identify unique error and null error seperately?

  - https://marshmallow.readthedocs.io/en/stable/examples.html
  - https://medium.com/bitproject/recently-i-created-a-restful-api-with-flask-where-my-models-had-many-parameters-75da1db870b7
  - https://www.cameronmacleod.com/blog/better-validation-flask-marshmallow
