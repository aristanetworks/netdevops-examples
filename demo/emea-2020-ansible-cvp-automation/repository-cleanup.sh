#!/bin/sh

echo 'Cleaning up repository from previous run'
echo '  - delete content in documentation/'
find documentation/ -name "*.md" -type f -delete
echo '  - delete content in documentation/'
find documentation/ -name "*.csv" -type f -delete
echo '  - delete content in intended/structured_configs/'
find intended/structured_configs/ -name "*.yml" -type f -delete
echo '  - delete content in intended/configs/'
find intended/configs/ -name "*.cfg" -type f -delete
