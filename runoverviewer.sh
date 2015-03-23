#!/bin/bash
if [ -z $1 ]; then \
	echo "Usage: ./runoverviewer <mapname>"
	echo ""
	echo "	Example: ./runoverviewer.sh ftblite2-150330"
else	
	time nice -n 19 overviewer.py \
		--config=~minecraft/www/html/"$1"/config.py $*
fi
