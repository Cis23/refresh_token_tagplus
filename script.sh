#!/bin/bash
echo ===================" $(date +"%d/%m/%Y %H:%M:%S")  ===================" >> historico.log
python index.py >> historico.log 2>&1