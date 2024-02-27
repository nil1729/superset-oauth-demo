#!/bin/bash

echo "running docker-init.sh"

# db upgrade
echo "db upgrade"
superset db upgrade

# create admin user
echo "create admin user"
echo "SUPERSET_ADMIN_USERNAME: $SUPERSET_ADMIN_USERNAME"
superset fab create-admin \
    --username "$SUPERSET_ADMIN_USERNAME" \
    --firstname Superset \
    --lastname Admin \
    --email "${SUPERSET_ADMIN_USERNAME}@superset.com" \
    --password "$SUPERSET_ADMIN_PASSWORD"

# setup roles
echo "setup roles"
superset init

# existing
echo "completed docker-init.sh"