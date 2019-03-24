# English Shops

This is an open source API, were you can _POST_, _GET_ and _DELETE_ items from two different tables _Shop_ and _Product_. This was built in ``Django``.

 ### Requirements:
> ***
> - **Python** >= 3.5
> - **Postgresql** >= 4.X

### Set Up
***
> - Pull this repository into your machine:
> - ``$ git clone https://github.com/marcmelchor/english-shops.git``
> - ``$ cd english-shops``
> - Install libraries in the virtual environment (this example is provided on PC, if you have a Unix distribution change _'Scripts'_ by _'bin'_):
> - ``$ virtualenv\Scripts\activate``
> - Install all the libraries.
> - ``$ pip install -r requirements.txt``

### Migrate database
> - Create a database in _Postgres_, this documentation, provide the example with Postgres but, you can use the supported database of your election.
> - In the file development ``engslish_shops.settings.development`` substitute the database credentials for yours.
> - Change ``ENGINE``, in case of you are using another supported database, ``NAME``, ``USER`` and ``PASSWORD`` by your local credentials.
> - Migrate database, in this case is not necessary to ``makemigrations``, due to is already done:
> - ``$ py manage.py migrate``

### Populate database with _english_shops.json_
> - In the file ``english_shops.setttings.development`` modify the os environment ``JSON_FILE`` by the location of the json file in your machine.
> - Create **Super User**
> - ``$ py manage.py createsuperuser``
> - Run the server
> - ``$ py manage.py runserver``
> - Go to this _url_ ``localhost:8080/api/v1.0/populate_db/`` to populate automatically  the database. **IMPORTANT:** _this process will take **several minutes**, so I suggest you to grab a coffee and wait for it ;)_.

### API
> - You are close to start using the API, so let's do it.
> - This are the collections (GET, POST)
> - ``api/v1.0/shop/`` this get all the shops
> - If you want to **post** a new shop you can do it using the Django Rest Framework, in the section **Content** type a dictionary like this:
> - 	{"shop":
> 			{
>  				"title": "<title_name>"
>  			}
>  		}
> - And press _POST_
> - To **delete** a shop you can do it in two ways, using the **DRF** (Django Rest Framework), go to this url ``api/v1.0/shops/<int:shop_id>/`` and press the button delete and confirm that you want to delete. The other option is making an **http_request** with _delete_ mode using the url above.
> - If you want to use the api for the products is totally the same that the last collection but, this is the url ``api/v1.0/shops/<int:shop_id>/products/``
> - This is the content dictionary if you want to create a **product**:
> - 	{"product":
> 			{
> 				"shop_name": "<shop_id>",
> 				"title": "<product_title>",
> 				"link": "<product_link>",
> 				"description": "<product_description>",
> 				"image_link": "<prduct_image_link>",
> 			}
> 		}

### Bonus
> - This project uses code styling ``PEP-8``.
> - All the modules have ``setter and getters``.
> - Exist a ``development`` environment to make easier the movement to ``production``.

#### Developer opinion
> * Due to the big amount of data that is consumed by this API, I would suggest to migrate from ``.json`` and use ``protobuf``, here is the link of the official website ``https://developers.google.com/protocol-buffers/``.

##### TODO
> - Implement testing.
> - Set the resource to load only the products wich ``link and media_link`` are available. The call has been implemented in ``api/v1.0/shops/<int:shop_id>/validated_products/`` but, it contains bugs.

#### Report
> 1. **Outline your architecture:**
> - 	Collection: (GET, POST)
>			shops/
>			shops/<int:shop_id>/products/
>			shops/<int:shop_id>/products_validated/
>			
>		Resource: (GET, DELETE)
>			shops/<int:shop_id>/
>			products/<int:product_id>/
>			validated_products/<int:product_id>/
> 2. **What did you focus on?**
> - Create a lean and clean code that every developer does not matter the expertise can read it and understand it.
> - Population of the database, due to most probably it that would be the first thing I'd do if it is my project in the real world.
> - Easy to understand file structure.
> - Every new file, extra line and architecture was designed to be scalable since day 1.
> 3. **What was particularly challenging?**
> - In my case were two things, one: the machine I am using currently is super outdated (it has Intel Inside and 3 GB of RAM), so all the process was at least three times slower due to the characteristics of the PC.
> - And to work again with ``.json`` because during my former project I was using ``protobuf`` and I needed to refresh those concepts.
> 4. **What would you do if you had more time?**
> - Finish up the two things I missed from the optional part (test with ``pytest``, that I have experience on it thanks to my former job and to load only the products with the ``image and image_link`` currently working).
> - Add the method ``PATCH`` to all the resources.