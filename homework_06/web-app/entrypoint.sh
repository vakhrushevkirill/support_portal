#!/bin/bash
echo "Starting..."

flask db upgrade
exec "$@"