#!/bin/sh

celery -A web worker --loglevel=info --concurrency 1 -E
