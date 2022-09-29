# Command Line Switches:
#   t   -  disable text UI
#   b   -  disable connection to media controller
#   v   -  verbose logging to disk (large: 1MB per minute)
#   V   -  verbose logging to console
#   X   -  forces smart virtual platform
#   P   -  Production mode. Will suppress errors, wait for hardware on start and try to exit when startup fails. 

start:
	mpf -tbv

startv:
	mpf -tbv -X

build:
	mpf build production_bundle -b

prod:
	mpf -tbP

watch:
	mpf monitor

lint:
	find config modes -type f -name "*.yaml" -exec mpf format "{}" --yes \;
