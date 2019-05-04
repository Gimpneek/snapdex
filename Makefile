# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS      	=
SPHINXBUILD     	= sphinx-build
SOURCEDIR       	= docs/source
BUILDDIR        	= docs/build
export
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
	docker build -t $$IMAGE_REPO_URL:$$TRAVIS_TAG -t $$IMAGE_REPO_URL:latest .

# Test the docker image
test_docker:
	DISCORD_KEY=$$DISCORD_KEY pytest docker

# Publish the docker image to DockerHub
publish_docker:
	@echo $$DOCKER_HUB_PASSWORD | docker login --username $$DOCKER_HUB_USER --password-stdin
	docker tag $$IMAGE_REPO_URL:$$TRAVIS_TAG $$IMAGE_REPO_URL:$$TRAVIS_TAG
	docker push $$IMAGE_REPO_URL:$$TRAVIS_TAG

# Deploy the new version to AWS ECS
deploy_docker:
	bash scripts/ecs-deploy.sh -c $$CLUSTER_NAME -n $$SERVICE_NAME -i $$IMAGE_REPO_URL:$$TRAVIS_TAG

docker: build_docker test_docker

deploy: publish_docker deploy_docker

.PHONY: help Makefile install_aws install_deps build_docker test_docker publish_docker deploy_docker deploy unit_test sonarqube ci_test docker

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
