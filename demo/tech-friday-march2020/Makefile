.PHONY: help
help: # Display help message (*: main entry points / []: part of an entry point)
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

################################################################################
# Configlet Management
################################################################################

.PHONY: avd-configlet-upload
avd-configlet-upload: ## Upload configlets using AVD role approach
	ansible-playbook dc-configlet-avd-uploader.yml

.PHONY: raw-configlet-upload
raw-configlet-upload: ## Upload configlets using manual approach
	ansible-playbook dc-configlet-raw-upload.yml
