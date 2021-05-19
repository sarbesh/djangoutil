# Installation instructions

Detailed instructions on how to install, configure, and get the project running.

    1. Clone the repo.

    2. Create a python virtual environment.

    3. Install modules present in requirements.txt to the virtual environment.

    4. Run 
    ```
        python manage.py migrate 
    ```

    5. Create superuser 
    ``` 
        python manage.py createsuperuser --email admin@example.com --username admin
    ```
