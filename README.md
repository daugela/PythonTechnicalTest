# Origin Markets Backend Test

### Solution

Clone this repo  
`git clone https://github.com/daugela/PythonTechnicalTest.git && cd PythonTechnicalTest`  
Inside a virtual environment running Python 3:  
`pip install -r requirements.txt`  

Make and run migrations:  
`python origin/manage.py makemigrations`  
`python origin/manage.py migrate`  

Create user:  
`python origin/manage.py createsuperuser`  

Run tests:  
`python origin/manage.py test`  

Run Django development server:  
`python origin/manage.py runserver 127.0.0.1:8000`  

See shiny new api endpoint (requires basic login):  
http://127.0.0.1:8000/bonds/  



### Spec:

We would like you to implement an api to: ingest some data representing bonds, query an external api for some additional data, store the result, and make the resulting data queryable via api.
- Fork this hello world repo leveraging Django & Django Rest Framework. (If you wish to use something else like flask that's fine too.)
- Please pick and use a form of authentication, so that each user will only see their own data. ([DRF Auth Options](https://www.django-rest-framework.org/api-guide/authentication/#api-reference))
- We are missing some data! Each bond will have a `lei` field (Legal Entity Identifier). Please use the [GLEIF API](https://www.gleif.org/en/lei-data/gleif-lei-look-up-api/access-the-api) to find the corresponding `Legal Name` of the entity which issued the bond.
- If you are using a database, SQLite is sufficient.
- Please test any additional logic you add.

#### Project Quickstart

Inside a virtual environment running Python 3:
- `pip install -r requirement.txt`
- `./manage.py runserver` to run server.
- `./manage.py test` to run tests.

#### API

We should be able to send a request to:

`POST /bonds/`

to create a "bond" with data that looks like:
~~~
{
    "isin": "FR0000131104",
    "size": 100000000,
    "currency": "EUR",
    "maturity": "2025-02-28",
    "lei": "R0MUWSFPU8MPRO8K5P83"
}
~~~
---
We should be able to send a request to:

`GET /bonds/`

to see something like:
~~~
[
    {
        "isin": "FR0000131104",
        "size": 100000000,
        "currency": "EUR",
        "maturity": "2025-02-28",
        "lei": "R0MUWSFPU8MPRO8K5P83",
        "legal_name": "BNPPARIBAS"
    },
    ...
]
~~~
We would also like to be able to add a filter such as:
`GET /bonds/?legal_name=BNPPARIBAS`

to reduce down the results.