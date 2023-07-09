## Descrição
Coodesh challenge backend

# Estrutura

```
- alembic
|- versions
|- env.py
- app
|- config.py
|- database.py
|- main.py
|- models.py
|- products.py
|- routes.py
|- schemas.py
- alembic.ini
- Dockerfile
- README.md
- requirements.txt
```

# Rotas
http://0.0.0.0:8000/docs

![Alt text](image.png)
`/product/files`

POST route for saving in the API of files with information about product sales

`/product/list`

GET route returning product sales list saved in API