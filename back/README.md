## Descrição
Backend desafio coodesh

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
![Alt text](image.png)
`/product/files`
Rota POST para salvamento na API de arquivos com informações sobre venda de produtos
`/product/list`
Rota GET retornando lista de vendas de produtos salvas na API