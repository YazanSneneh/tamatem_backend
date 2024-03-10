# tamatem task backend

### Setting up and running the application.
#### Run the app.
1. Create python env file and activate.
2. Install requirements: `pip install -r requirements.txt`

#### Database
 1. Prepare models for migration to database.
   `python manage.py makemigrations`
 2. Migrate to database
    `python manage.py migrate`
#### Create Data and user
* To be able to access database & manipulate data.
To create a Django admin user you can follow these steps:

`python manage.py createsuperuser`

* **You'll be prompted to enter a username, email address, and password. follow these steps:**

  * Enter **username** when prompted for the username.
  * Press Enter to skip the email address.
  * Enter **password** when prompted for the password.
  * Confirm the password by typing  **password** again.

**After creating the superuser:**
  * Visit **baseUrl/admin** or if you run the app on localhost:8000 [admin panel](http://127.0.0.1:8000/admin/)
  * Fill admin user you created in the login box.
  * You will see item and item image models they have **1:1** relation fill the data you desire.

#### Endpoints
* If app is running on port 8000 use blue text to visit links: 
* [users](http://127.0.0.1:8000/api/v1/auth/users/)
  * `POST {{baseUrl}}/api/v1/auth/users/`
  * Request body: `{ "username", "email", "password" }`
  * Response: User object
  * **Note**: Fill admin user you created or use users endpoint to create user then fill data in the login box in the frontend.
* [login](http://127.0.0.1:8000/api/v1/auth/jwt/create/)
  * `POST {{baseUrl}}/api/v1/auth/jwt/create/`
* [all items](http://127.0.0.1:8000/api/v1/store/items/)
  * `GET {{baseUrl}}/api/v1/store/items`
  * Response: List of items
* [Item details](http://127.0.0.1:8000/api/v1/store/items/1/)
  * `GET {{baseUrl}}/api/v1/store/items/:id/`
  * Response: `{ "description": "Item description" }`
* [Item details](http://127.0.0.1:8000/api/v1/store/items/1/)
  * `PUT {{baseUrl}}/api/v1/store/items/:id/`
  * Header: `{ "Authorization": "JWT token" }`
  * Request body:` { "name", "price", "description" }`

#### Note
* if you are using a different url for client rather than angular default add the url to key `CORS_ALLOWED_ORIGINS` inside `app/setting.py`

### Reasoning behind choosing database
* I used SQLlite3 because it's lightweight and suitable for the project requirements

### Provide a brief explanation of your design decisions and any challenges faced.
### Django as Backend
* I chose Django based on my expertise and its suitability for the project requirements.
* Project Structure: I organized the Django backend using a standard Django project layout, with separate directories for apps, static files, media files, and configurations.
* App Structure: Within each Django app, I followed the MVC (Model-View-Controller) pattern, with models representing database entities, views handling business logic and HTTP requests.
* API Endpoints: For the RESTful API, I adopted Django REST Framework and structured the API endpoints logically, grouping related resources under separate routers or views.
* Authentication and Authorization: I implemented user authentication using the Djoser library, which provides an alternative to Django's built-in authentication system. Additionally, I applied permissions and authentication classes from Django REST Framework for securing API endpoints.