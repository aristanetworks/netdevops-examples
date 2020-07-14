# Setting up your NetDevOps working environment (Mac)

Note: most of these can be done in Linux/Windows using apt/yum/dnf/choclatey

## Homebrew (Mac)

<https://brew.sh/>

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

## iTerm2

```bash
brew cask install iterm2
```

## tmux

```bash
brew install tmux
```

## Git

`brew install git`

## Docker

<https://hub.docker.com/editions/community/docker-ce-desktop-mac/>

## Python 3

![xkcd for Python Dependencyt](https://imgs.xkcd.com/comics/python_environment.png)

Use the pyenv method to make versioning Python sane

```bash
brew install pyenv pipenv
pyenv install 3.7.3
pyenv global 3.7.3
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
```

Also have a look at pipenv for project management

Alternate but less sustainable method (see above graphic):

```bash
brew install python3
echo "alias python=/usr/local/bin/python3" >> ~/.zshrc
echo "alias pip=/usr/local/bin/pip3" >> ~/.zshrc 
```

## Ansible (installing globally)

```bash
sudo pip install ansible
```

## vs code

<https://code.visualstudio.com/download>

## jq

```bash
brew install jq
```

### Example

```bash
curl https://gist.githubusercontent.com/fredhsu/baa4bb339e660a080f08d185718fa728/raw/f9c4b69c31758d853eac7a40ff8a3aece97abeec/showver.json | jq '.result[0].systemMacAddress'
```

## Virtualbox

<https://www.virtualbox.org/wiki/Downloads>

## Vagrant

<https://www.vagrantup.com/downloads>

## Extra stuff

### ZSH

```bash
brew install zsh
```

### Oh my zsh

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

### Go

<https://golang.org/doc/install>

### bat - replacement for cat(1)

```bash
brew install bat
```
