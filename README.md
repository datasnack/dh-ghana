# Ghana Hub

[Data Hub](https://github.com/datasnack/datahub) instance for Ghana.

## Installation

First we need to prepare the Docker image of the Data Hub software:

- First clone the [Data Hub repository](https://github.com/datasnack/datahub) to your computer: `$ git clone git@github.com:datasnack/datahub.git`
- Inside this folder build the Docker container with `$ docker build -t datahub:latest .`


No we can clone the Ghana Hub instance (this repository):

- Clone the repository `$ git clone git@github.com:datasnack/dh-ghana.git`
- Copy the `.env.example` to `.env`: `$ cp .env.example .env`
- Set `SECRET_KEY=` inside the `.env` with a secret value. Use `python3 -c 'import secrets; print(secrets.token_hex(100))` to create a value
- Run `$ docker-compose up -d`
- Wait/check until [http://localhost:8000/](http://localhost:8000/) shows the Data Hub interface

Now either import an existing data dump, or create a new instance.

### Import

To import a [previously created dump](https://github.com/datasnack/dh-ghana/releases) into the hub place the dump file inside the `data/` directory and run `$ docker-compose exec datahub python manage.py restore <filename>`.

### Create new

- Create admin user with `$ docker-compose exec datahub python manage.py createsuperuser`
- Import [prepared shape file](https://github.com/datasnack/aoi-ghana) with: `$ docker-compose exec datahub python manage.py loadshapes ./data/shapes/ghana.gpkg`
- Import Data Layer specifications: `$ docker-compose exec datahub python manage.py import ./data/datalayerspec/datalayer.csv`
- Import Data Layer data with:
    - `$ docker-compose exec datahub python manage.py datalayer <layer_key> download`
    - `$ docker-compose exec datahub python manage.py datalayer <layer_key> process`

### Create dump

In case you need to export the data use: `$ docker-compose exec datahub python manage.py dump`. An export file will be created in the `./data/` directory.



## Customization

Create custom app to add new functionality and/or overload templates (i.e., start page).

    mkdir ./src/<name>
    docker-compose exec datahub python manage.py startapp <name> ./src/<name>

Then add it in the `.env` to the key `INSTALLED_USER_APPS` (comma separated list) like `src.<name>`.

Finally, inside the created app in `src/<name>/apps.py` change `name = <name>` to `name = src.<name>`.

After that you need to rebuild/start the container with `docker-compose up -d`.
