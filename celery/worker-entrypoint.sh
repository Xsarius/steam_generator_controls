#!/bin/sh

celery -A web worker --loglevel=info
