REM Correr este script dentro del ambiente
REM Este script carga los datos por defecto

python manage.py loaddata appEditorial/fixtures/autores.json
python manage.py loaddata appEditorial/fixtures/editoriales.json
python manage.py loaddata appEditorial/fixtures/libros.json