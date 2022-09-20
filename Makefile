start:
	mpf -tbv

startv:
	mpf -tbv -X

watch:
	mpf monitor

lint:
	find config modes -type f -name "*.yaml" -exec mpf format "{}" --yes \;
