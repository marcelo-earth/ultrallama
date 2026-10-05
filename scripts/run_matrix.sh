#!/usr/bin/env bash
set -euo pipefail

python -m src.load_profile --users 1 --requests 20
python -m src.load_profile --users 4 --requests 40
python -m src.load_profile --users 8 --requests 80
