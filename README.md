# TodoList Django Project

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Moody2wayv/DjangoToDoList.git
    cd TodoList
    ```

2. Build and run the Docker containers:

    ```bash
    docker-compose build
    docker-compose up
    ```

3. Apply migrations and create a superuser:

    ```bash
    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py createsuperuser
    ```

4. Access the application:

    Open your browser and navigate to `http://localhost:8000`.

## Documentation

The documentation is available in the `docs` folder. To build the documentation, navigate to the `docs` folder and run:

```bash
make html
