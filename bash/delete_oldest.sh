#!/bin/bash

# Author: Elliot Weishaar

# Delete oldest file in passed in directory. Do not use trailing slash on directory declaration
# Example: delete_oldest.sh /path/to/dir

[ -d $1 ] && rm -f $1/$(ls -t "$1" | tail -1); echo "File Deleted" || echo "Errors occured, nothing deleted"
