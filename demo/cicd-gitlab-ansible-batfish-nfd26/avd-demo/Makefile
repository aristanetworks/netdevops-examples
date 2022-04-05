CONTAINER ?= avdteam/base:3.6
VSCODE_CONTAINER ?= avdteam/vscode:latest
VSCODE_PORT ?= 8080
HOME_DIR = $(shell pwd)
AVD_COLLECTION_VERSION ?= 2.0.0
CVP_COLLECTION_VERSION ?= 2.1.2

help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

################################################################################
# AVD Commands
################################################################################

.PHONY: build
build: ## Run ansible playbook to build EVPN Fabric configuration.
	ansible-playbook playbooks/dc1-fabric-deploy-cvp.yml --tags build

.PHONY: provision
provision: ## Run ansible playbook to deploy EVPN Fabric.
	ansible-playbook playbooks/dc1-fabric-deploy-cvp.yml --tags provision

.PHONY: deploy
deploy: ## Run ansible playbook to deploy EVPN Fabric.
	ansible-playbook playbooks/dc1-fabric-deploy-cvp.yml --extra-vars "execute_tasks=true" --tags "build,provision,apply"

.PHONY: reset
reset: ## Run ansible playbook to reset all devices.
	ansible-playbook playbooks/dc1-fabric-reset-cvp.yml

.PHONY: ztp
ztp: ## Configure ZTP server
	ansible-playbook playbooks/dc1-ztp-configuration.yml

.PHONY: configlet-upload
configlet-upload: ## Upload configlets available in configlets/ to CVP.
	ansible-playbook playbooks/dc1-upload-configlets.yml

.PHONY: install-git
install-git: ## Install Ansible collections from git
	git clone --depth 1 --branch v$(AVD_COLLECTION_VERSION) https://github.com/aristanetworks/ansible-avd.git
	git clone --depth 1 --branch v$(CVP_COLLECTION_VERSION) https://github.com/aristanetworks/ansible-cvp.git
	pip3 install -r ansible-avd/development/requirements.txt

.PHONY: install
install: ## Install Ansible collections
	ansible-galaxy collection install arista.avd:==${AVD_COLLECTION_VERSION}
	ansible-galaxy collection install arista.cvp:==${CVP_COLLECTION_VERSION}

.PHONY: uninstall
uninstall: ## Remove collection from ansible
	rm -rf ansible-avd
	rm -rf ansible-cvp

.PHONY: webdoc
webdoc: ## Build documentation to publish static content
	mkdocs build -f mkdocs.yml

.PHONY: shell
shell: ## Start docker to get a preconfigured shell
	docker pull $(CONTAINER) && \
	docker run --rm -it \
		-v $(HOME_DIR)/:/projects \
		-v /etc/hosts:/etc/hosts $(CONTAINER)

.PHONY: vscode
vscode: ## Run a vscode server on port 8080
	docker run --rm -it -d \
		-e AVD_GIT_USER="$(git config --get user.name)" \
		-e AVD_GIT_EMAIL="$(git config --get user.email)" \
		-v $(HOME_DIR):/home/avd/ansible-avd-cloudvision-demo \
		-p $(VSCODE_PORT):8080 $(VSCODE_CONTAINER)
	@echo "---------------"
	@echo "VScode for AVD: http://127.0.0.1:$(VSCODE_PORT)/?folder=/home/avd/ansible-avd-cloudvision-demo"