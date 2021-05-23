# CakeNBake

CakeNBake is an e-commerce website designed for selling cakes online. Users can buy cakes from the website after completing payment while admin can manage the cake products.

# Features

### Users can

* Create and login to their account
* View and filter out cakes based on categories
* Buy the cakes after successfully completing the payments
* Cancel already placed order if they wish 
* View order history
* Send message to admin about feedback or can ask for custom cakes

### Admin can

* View all the user accounts that have been created
* View and print recent orders and their details
* Update admin details
* Add, delete and update products

# Tech Stacks 

* Frontend: HTML, CSS, SCSS, JavaScript, JQUERY, BOOTSTRAP 4, MATERIAL-UI
* Backend : Django REST framework ( Django 3.2 ), MySQL
* Payment : Stripe API

# How to use

* Before begining make sure you have installed __python__ and __django__  in your machine.
* Make sure you have installed all the below packages
    ```python
        >> pip install mysqlclient
        >> pip install crispy_forms
        >> pip install stripe
  ```
* Now create the database
    ```python
        >> py manage.py migrate
  ```


# How to run

```python
        >> py manage.py runserver
```
## Happy Coding :)
