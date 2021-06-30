#!/bin/bash
#DJANGO_SETTINGS_MODULE=settings.local celery -A recruitment flower
DJANGO_SETTINGS_MODULE=settings.production celery -A recruitment flower