# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS      	=
SPHINXBUILD     	= sphinx-build
SOURCEDIR       	= docs/source
BUILDDIR        	= docs/build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

unit_test:
	nosetests snapdex

sonarqube:
	sonar-scanner

ci_test: unit_test sonarqube

install_bot_deps:
	pip install -r requirements.txt

# Install awscli
install_aws:
	pip install awscli
	export PATH=$$PATH:$$HOME/.local/bin

# Install dependencies for the ecs-deploy.sh script
install_ecs_deps:
	sudo add-apt-repository ppa:eugenesan/ppa -y
	sudo apt-get update -y
	sudo apt-get install jq -y

# Build the docker image
build_docker:
	@docker build -t $$IMAGE_REPO_URL:$$TRAVIS_TAG -t $$IMAGE_REPO_URL:latest .

# Test the docker image
test_docker:
	@DISCORD_KEY=$$DISCORD_KEY pytest docker

.PHONY: help Makefile install_aws install_deps build_docker test_docker unit_test sonarqube ci_test

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
