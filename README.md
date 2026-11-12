# IT-Infrastructure-Asset-Management

## Local environment configuration

Install dependencies using a working Python virtual environment:

```powershell
python -m pip install -r requirements.txt
Copy-Item .env.example .env.local
```

Run the copy command only if `.env.local` does not already exist. Open
`.env.local` in your editor and enter your existing MySQL password in
`DB_PASSWORD`, inside the single quotes. Set `SECRET_KEY` to a private
Django secret key as well, unless it is already configured in your process
environment. Do not paste secrets into terminal commands or commit them.
If a value contains a single quote or backslash, escape it according to
python-dotenv's single-quoted syntax (`\'` and `\\`, respectively).

Settings load `.env.local` and then `.env` from the directory containing
`manage.py`. Existing process environment variables take priority, including
empty ones; `.env.local` takes priority over `.env`. Variable interpolation
is disabled so `${...}` in a password is preserved literally. Both local
files are ignored by Git; `.env.example` contains no credentials.

The database remains MySQL `itam_db`, user `root`, host `127.0.0.1`, port
`3306`. Run verification from the project directory:

```powershell
python manage.py check
python manage.py test assets --verbosity 2
```

Django uses its separate `test_itam_db` database for these tests. The MySQL
account needs permission to create and drop that test database. If Django
asks to delete an existing test database, stop and verify its contents before
agreeing. Do not run migrations or reset the existing `itam_db` to fix test
authentication.
Software Engineering mini project — IT Infrastructure &amp; Asset Management System (Team 08).
