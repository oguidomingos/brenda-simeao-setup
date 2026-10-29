#!/bin/bash
# uso: build.sh <md> <pdf> <título>
set -e
D=/root/work/brenda-cliente
pandoc "$1" -f commonmark_x-yaml_metadata_block -t html5 -s --metadata pagetitle="$3" -c $D/build/style.css -o /tmp/b_$$.html -V lang=pt-BR --embed-resources --standalone 2>/dev/null || pandoc "$1" -f commonmark_x -t html5 -s --metadata pagetitle="$3" -c $D/build/style.css -o /tmp/b_$$.html
sed -i 's#<body>#<body><div class="brand">Expoente · Dra. Brenda Simeão</div>#' /tmp/b_$$.html
google-chrome --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf="$2" file:///tmp/b_$$.html >/dev/null 2>&1
rm -f /tmp/b_$$.html
