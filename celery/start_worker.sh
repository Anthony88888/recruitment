#!/bin/bash

celery --app tasks worker --loglevel=info
