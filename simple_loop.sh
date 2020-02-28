#!/bin/bash

hook_url="https://hooks.zapier.com/hooks/catch/123456/abcdex/"
search_dir=($(dirname "$0")/webhook_examples)

for json in "$search_dir"/*; do
    curl "$hook_url" \
    -X POST \
    -d @"$json"
done