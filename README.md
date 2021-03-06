# MMS_IMDB
Final project of multimedia system of Amirkabir University of Teconlogy

## Installation
1. [Clone](https://github.com/Amirrezat1379/MMS_IMDB.git) the repository.
2. Create a Virtual Environment
  - Linux:
      ```bash
      >> python3 -m pip install --upgrade pip
      >> python3 -m venv venv
      >> source venv/bin/activate
      ```
  - Windows:
      ```bash
      >> py -m pip install --upgrade pip
      >> py -m venv venv
      >> venv/Scripts/activate
      ```
3. Install the required packages and dependencies:
```bash
>> pip install -r requirements.txt
```
4. Apply migrations and create the database:
```bash
python3 manage.py migrate
```
5. Run the server:
```bash
python3 manage.py runserver
```
6. To run the project in Docker:
```bash
docker-compose up -d --build
```
7. Move each video generated from the script into nginx:
```bash
docker exec {container_id} mkdir -p /tmp/dash/
docker cp /home/keivanipchihagh/GitHub/MMS_IMDB/DASH/{movie_id} mms_imdb_nginx_1:/tmp/dash/{movie_id}

```
8. To access the files in the nginx server:
```bash
docker exec -it mms_imdb_nginx_1 /bin/sh
```