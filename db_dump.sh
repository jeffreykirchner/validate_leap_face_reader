echo "Dump Database"
pg_dump --host=localhost --port=5432 --username=dbadmin --dbname=validate_leap_face_reader --file=database_dumps/validate_leap_face_reader.sql -v -Fc