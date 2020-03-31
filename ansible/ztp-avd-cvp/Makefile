DOCKER_NAME ?= arista/avd-cvp-demo

help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

################################################################################
# AVD Commands
################################################################################

.PHONY: build
build: ## Run ansible playbook to build EVPN Fabric configuration.
	ansible-playbook dc1-fabric-deploy-cvp.yml --tags build

.PHONY: provision
provision: ## Run ansible playbook to deploy EVPN Fabric.
	ansible-playbook dc1-fabric-deploy-cvp.yml --tags provision

.PHONY: deploy
deploy: ## Run ansible playbook to deploy EVPN Fabric.
	ansible-playbook dc1-fabric-deploy-cvp.yml --extra-vars "execute_tasks=true" --tags "build,provision,apply"

.PHONY: reset
reset: ## Run ansible playbook to reset all devices.
	ansible-playbook dc1-fabric-reset-cvp.yml

.PHONY: clean
clean: ## Delete previously generated outputs
	sh repository-cleanup.sh

.PHONY: ztp
ztp: ## Configure ZTP server
	ansible-playbook dc1-ztp-configuration.yml

.PHONY: configlet-upload
configlet-upload: ## Upload configlets available in configlets/ to CVP.
	ansible-playbook dc1-upload-configlets.yml

# .PHONY: install
# install: ## Install Ansible collections
# 	ansible-galaxy collection install arista.cvp -p ansible-cvp
# 	ansible-galaxy collection install arista.avd -p ansible-avd

.PHONY: install
install: ## Install Ansible collections
	git clone https://github.com/aristanetworks/ansible-avd.git
	git clone https://github.com/aristanetworks/ansible-cvp.git

.PHONY: uninstall
uninstall: ## Remove collection from ansible
	rm -rf ansible-avd
	rm -rf ansible-cvp

.PHONY: install-requirements
install-requirements: ## Install python requirements
	pip install --upgrade wheel
	pip install -r requirements.txt

################################################################################
# Docker AVD Commands
################################################################################

# .PHONY: build-docker
# build-docker: ## Build docker image based on latest supported Python version
# 	docker build -f Dockerfile -t $(DOCKER_NAME):latest .

# .PHONY: run
# run: ## Connect to docker container
# 	docker run -it --rm -v $(PWD):/project $(DOCKER_NAME):latest sh

# .PHONY: configure-ztp-docker
# configure-ztp-docker: ## Connect to docker container
# 	docker run -it --rm -v $(PWD):/project $(DOCKER_NAME):latest ansible-playbook dc1-ztp-configuration.yml

# .PHONY: deploy-docker
# deploy-docker: ## Run ansible playbook to deploy EVPN Fabric.
# 	docker run -it --rm -v $(PWD):/project $(DOCKER_NAME):latest ansible-playbook dc1-fabric-deploy-cvp.yml

# .PHONY: reset-docker
# reset-docker: ## Run ansible playbook to reset all devices.
# 	docker run -it --rm -v $(PWD):/project $(DOCKER_NAME):latest ansible-playbook dc1-fabric-reset-cvp.yml
