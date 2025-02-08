#!/bin/sh

echo "🕒 Waiting for database to be ready..."
while ! mysql -h"$MYSQL_HOST" -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SELECT 1" > /dev/null 2>&1; do
    sleep 2
done

echo "⚙️ Running makemigrations..."
python manage.py makemigrations --noinput

echo "⚙️ Running migrations..."
python manage.py migrate --noinput

echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo "✅ All setup complete, running Gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 myproject.wsgi:application
