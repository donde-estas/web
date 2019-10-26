#!/bin/bash
set -e

python manage.py collectstatic --noinput  # Collect static files

# Exec the container's main process (what's set as CMD in the Dockerfile).
exec "$@"
