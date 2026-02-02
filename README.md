# GameMaster - Documentación _nt

## Descripción
API CRUD para gestión de videojuegos usando Python + FastAPI con SQL directo (sin ORM).

---

## Instalación

```bash
# Crear entorno virtual
python -m venv venv

# Activar (Windows)
.\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

---

## Base de Datos

1. Crear la base de datos en MySQL:
```bash
mysql -u root -p < init_db.sql
```

2. Configurar `.env`:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_password
DB_NAME=gamemaster
DB_PORT=3306
```

---

## Ejecutar

```bash
uvicorn app.main:app --reload
```

- Frontend: http://localhost:8000
- API Docs (Swagger): http://localhost:8000/docs

---

## Estructura

```
GameMaster/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app
│   ├── database.py      # SQL directo (CRUD)
│   ├── models.py        # Pydantic validaciones
│   └── routes.py        # Endpoints API
├── static/
│   ├── css/style.css
│   └── js/app.js
├── templates/
│   └── index.html
├── docs/
│   └── README_nt.md
├── init_db.sql
├── requirements.txt
└── .env
```

---

## Endpoints API

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /api/games | Listar todos |
| GET | /api/games/{id} | Obtener uno |
| POST | /api/games | Crear |
| PUT | /api/games/{id} | Actualizar |
| DELETE | /api/games/{id} | Eliminar |

---

## Validaciones Pydantic

- `name`: 1-100 caracteres
- `platform`: 1-50 caracteres
- `price`: > 0, <= 999.99
- `discount`: 0-100
- `image_url`: 1-500 caracteres

---

## Tecnologías

- Python 3.14
- FastAPI
- MySQL + mysql-connector-python
- Pydantic (validaciones)
- Jinja2 (templates)
- SQL directo (sin ORM)
