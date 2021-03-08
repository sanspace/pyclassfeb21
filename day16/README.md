# Day 16

## Topics

  - Microservices
  - DRF continued
    - Auth & Permissions
    - Relationships
    - Hyperlinked APIs
    - Viewsets
    - Routers

## Refer

  - Microservices
    - https://microservices.io/patterns/decomposition/decompose-by-business-capability.html
    - https://microservices.io/patterns/decomposition/decompose-by-subdomain.html
      - https://www.cosmicpython.com/book/chapter_01_domain_model.html
    - https://www.freecodecamp.org/news/python-microservices-course/
        - https://github.com/scalablescripts/python-microservices
    - https://eventuate.io/exampleapps.html Example apps

  - Repository Pattern
    - https://www.cosmicpython.com/book/chapter_02_repository.html#_introducing_the_repository_pattern
    - https://github.com/cosmicpython/code/blob/chapter_02_repository/repository.py

  - API Versioning
    - https://www.django-rest-framework.org/api-guide/versioning/#urlpathversioning

  - DRF continued
    - https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
    - https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/
    - https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/

## Practice

  - Use DRF to create your REST API for managing Developers and Skills that has the below features.
    - Developers should be able to add/modify/remove their own skills and skill level
    - Others should be able to view developers' skills
    - Responses should have links for the objects and their related objects
      - You should be able to see a skill URL in a developer details
    - Try writing as less code as possible by leveraging features of DRF

## Bonus Challenge

    - Use custom permissions to allow a dev to modify another dev's skill level only if they two have the same skill
    - Developers should be able to see skill level of their team members but for others they shuld only see the skill not the level.
