start:
	mpf -tbv

startv:
	mpf -tbv -x

watch:
	mpf monitor

lint:
	find config -type f -name "*.yaml" -exec mpf format "{}" --yes \;
