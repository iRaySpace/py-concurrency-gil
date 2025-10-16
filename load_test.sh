#!/bin/bash
ab -n 10000 -c 2000 -p /dev/null http://127.0.0.1:8000/play