#!/bin/bash
QUESTION=""
DATABASE_NAME=""
DATABASE_USER=""
DATABASE_PASSWORD=
PROVIDER_NAME=""
MODEL_NAME=""
PROVIDER_API_KEY=""
PYTHON_SRC="" # Set to your Python interpreter path, e.g. /path/to/venv/bin/python

CMD="$PYTHON_SRC main.py --question \"$QUESTION\""

[ -n "$DATABASE_NAME" ] && CMD="$CMD --database_name \"$DATABASE_NAME\""
[ -n "$DATABASE_USER" ] && CMD="$CMD --database_user \"$DATABASE_USER\""
[ -n "$DATABASE_PASSWORD" ] && CMD="$CMD --database_password \"$DATABASE_PASSWORD\""
[ -n "$PROVIDER_NAME" ] && CMD="$CMD --provider_name \"$PROVIDER_NAME\""
[ -n "$MODEL_NAME" ] && CMD="$CMD --model_name \"$MODEL_NAME\""
[ -n "$PROVIDER_API_KEY" ] && CMD="$CMD --provider_api_key \"$PROVIDER_API_KEY\""

eval $CMD