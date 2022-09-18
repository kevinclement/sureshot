start:
	mpf -tbv

startv:
	mpf -tbv -x

watch:
	mpf monitor

lint: lint_config lint_hardware_playfield

lint_config: config/config.yaml
	mpf format config/config.yaml --yes

lint_hardware_playfield: config/hardware_playfield.yaml
	mpf format config/hardware_playfield.yaml --yes