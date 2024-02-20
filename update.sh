#!/usr/bin/bash
cd "$(dirname "$0")"
git pull
docker compose down
docker compose up -d
