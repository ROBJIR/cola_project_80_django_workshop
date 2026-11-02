![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)

# Important information

Read the following guidelines before doing the exercises.

## How do you begin?

1. [*Fork*](https://guides.github.com/activities/forking/) the repository containing exercises.
2. Clone the repository onto your computer using the command: `git clone repository_address`.
   You will find the address of the repository by pressing "Clone or download" button on its webpage.
3. Complete the exercises and commit changes to your repository using the commands below.
   `git add filename` will add a single file which you have changed.
   If you want to add all the changed files at once, use `git add .`.
   Remember that the fullstop (dot) at the end of this command is important!
   Next, commit changes using `git commit -m "description_of_changes"`.
4. Push changes to your repository on GitHub by typing: `git push origin main`.
5. Create a [*pull request*](https://help.github.com/articles/creating-a-pull-request) to the original repository when you have finished all the exercises.

### Do the exercises in appropriate files.

**The repository with the exercises will be removed 2 weeks after the end of the course. This will result in the removal of all forks made from this repository.**


# Workshop &ndash; Preparation of the Project

1. Make a fork of the workshop repository and clone it onto your computer.
2. Remember to back up your database (preferably every exercise)
    and create commits (also every exercise).
3. Create a virtual environment, and in it, install libraries for the project (from the requirements.txt file).
4. Create a database and configure access in the settings.py file
5. Run manage.py migrate
6. Run the tests using the pytest command and see the result.
7. Launch the server (manage.py runserver) and verify that the application is running.
8. Look at the application code.

#### Tests:

* The `tests.py` file, located in the `tests` directory, contains unit tests.
* `test_*` functions check various functionalities of the application and illustrate how to use them.
* Fixtures for the tests can be found in the file `conftest.py`.
* The helper functions for the tests can be found in the file `utils.py`.

#### Models:

* Look at the file `models.py` and analyze what data the application stores.
* Note the relationship between models `Movie` and `Person`.
> If you want to extend the model in some way, go ahead and do it. :-)

#### Views:

* The file `views.py` defines generic views that support all methods on the `Movie` resource.
* The `MovieView` class supports actions on a single object.
* `MovieListView` handles other actions, such as downloading all movies or adding a new one.

> You can read about generic views in Django Rest Framework in the documentation:
> [http://www.django-rest-framework.org/api-guide/generic-views/](http://www.django-rest-framework.org/api-guide/generic-views/)
    
#### Serializers

* The class contained in `serializers.py` defines how the **JSON** representing an object of the `Movie` model will look, that is, how the application will send it.
* Note the fields `SlugRelatedField`. They are responsible for representing `Person` objects linked by foreign keys to the movie we are serializing.
* In this case, the person is stored as a name and surname.
* Other representations of objects in the relation (e.g. id, link) are possible:
    [http://www.django-rest-framework.org/api-guide/relations/](http://www.django-rest-framework.org/api-guide/relations/)


#### **API** browser

* Using a web browser, access the page at **URL**: `/movies/`.
* A **HTML** page will be displayed containing the movie data in **JSON** format and some additional options.
* If we execute the same query from the script (e.g. via **curl**, **ajax**, **requests** library), we only get a JSON object. The application recognizes by the headers when the **HTML** version can be shown.
* To get raw data, you can use the menu under the **GET** button and select **json**.
* There is a form for adding new objects located under the list.
* Views also support **OPTIONS** requests. They then return a description of the given endpoint.
    Click the OPTIONS button to see it.

> More about the API browser in the Django Rest Framework:
> [http://www.django-rest-framework.org/topics/browsable-api/](http://www.django-rest-framework.org/topics/browsable-api/)


# Workshop &ndash; New application

Create a new application named `showtimes` inside the django project.
Use the `python manage.py startapp` command.
Perform all subsequent tasks in this application.


# Workshop &ndash; Models

Create models `Cinema` and `Screening`.

Model `Cinema` is to contain fields:
* `name` &ndash; cinema name (`string`, max 255 characters),
* `city` &ndash; (`string`, max 255 characters),
* `movies` &ndash; many-to-many relationship with `Movie` model (via `Screening` model).

`Screening` model is to include:
* `movie` &ndash; relation with `Movie` model,
* `cinema` &ndash; relation with `Cinema` model,
* `date` &ndash; screening date (field of the `datetime` type).

> If you want to extend the models in any way, go ahead and do it.


# Workshop &ndash; Cinema serializer

Create a serializer for the `Cinema` class:
* Add the file `serializers.py` in the directory of the new application,
* Create a serializer in it for the `Cinema` class,
* The movies in `movies` should be represented as links to their corresponding API resources.

> For information about serializers, see the Django REST Framework documentation:
> [https://www.django-rest-framework.org/api-guide/serializers/](https://www.django-rest-framework.org/api-guide/serializers/)


# Workshop &ndash; Cinema views

Create views for cinema:
* In the views.py file, write views that support the resource `cinemas`:
    * `CinemaListView`,
    * `CinemaView`.
* Add **URL** addresses to the views by modifying the file `urls.py` in the `moviebase`/ directory.
* Write tests to verify that all shared `url` addresses and `HTTP` methods work.


#### Tests:

Create tests:
* `test_add_cinema` &ndash; checking if adding a new cinema works.
* `test_get_cinema_list` &ndash; checking if listing all cinemas works.
* `test_get_cinema_detail` &ndash; checking if a detailed cinema view works.
* `test_delete_cinema` &ndash; checking removal of a cinema.
* `test_update_cinema` &ndash; checking if updating a cinema is working.


##### Hints:
* Use unit tests to check how newly created views work.
* Place them in the file `tests.py` in the `tests` directory (`showtimes` application).
* Before you start writing tests, add the file `conftest.py` to the `tests` directory.
* Start creating your tests by adding the `set_up` fixture, where you will create some objects in the test base. Put it in the file `conftest.py`.
* Don't forget the decorator `@pytest.mark.django_db` to be able to use the database.
* You can use the code of the existing tests from the `movielist` application to help you write your own tests.


# Workshop &ndash; Screening serializer

* Add a new serializer for the `Screening` class.
* Cinemas should be represented as their names.
* Movies should be represented as their titles.


# Workshop &ndash; Screening views

Create views for the screening:
* In the views.py file, write views that support the `screening` resource:
    * `ScreeningListView`,
    * `ScreeningView`.
* Add **URL** addresses to the views by modifying file `urls.py` in the `moviebase`/ directory.
* Write tests to verify the performance of all shared `url` addresses and `HTTP` methods.


#### Tests:

Create tests:
* `test_add_screening` &ndash; verifying that adding a new screening works.
* `test_get_screening_list` &ndash; verifying that list of all screenings works.
* `test_get_screening_detail` &ndash; checking if the detailed view of the screening works.
* `test_delete_screening` &ndash; checking if the screening removal works.
* `test_update_screening` &ndash; checking if the screening update works.


##### Hints:
* Use unit tests to check how newly created views work.
* Put them in the file `tests.py` in the `tests` directory (`showtimes` application).
* Don't forget the decorator `@pytest.mark.django_db` to be able to use the database.
* You can use the code of the existing tests from the `movielist` application to help you write your own tests.


# Workshop &ndash; Film filtering (non-obligatory task)

Modify the serializer for the cinema so that in the movies field it sends only the names of movies that will be played in the next 30 days.

Add a test to check the new functionality.


# Workshop &ndash; Screenings search (non-obligatory task)

* Add the option of filtering the screening list by movie name. Filtering parameters will be passed using GET method, i.e. written in the url.
* Add filtering by the city where the cinema is located.
> Hint: [https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend](https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend)


Add tests for the new functionality.
