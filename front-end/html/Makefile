# Makefile for HB exercises
#

# You can set these variables from the command line.
SPHINXOPTS    = -c .. -a -n
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = _build

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Internal variables.
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

NAME = $(shell basename $(shell pwd))
SSH_HOST      = fellowship@fellowship.hackbrightacademy.com
SSH_DIR       = fellowship.hackbrightacademy.com/exercises/
SSH_URL       = http://fellowship.hackbrightacademy.com/exercises/

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  html    to make HTML files"
	@echo "  zip     to make ZIP files (first builds HTML)"
	@echo "  upload  to upload ZIP files & HTML (first builds HTML & ZIP)"
	@echo "  clean   to remove temporary files"

handouts: html

htmli:
	$(SPHINXBUILD) -b handouts $(ALLSPHINXOPTS) $(BUILDDIR)/handouts

html: htmli
	open $(BUILDDIR)/handouts/index.html

clean: 
	rm -f /tmp/$(NAME).zip /tmp/$(NAME)-solution.zip

zip: htmli
	rm -f /tmp/$(NAME).zip /tmp/$(NAME)-solution.zip
	cd ..; zip -r /tmp/$(NAME)-solution.zip $(NAME)/solution/ -x \*.rst -x \*.swp
	cd ..; zip -r /tmp/$(NAME).zip $(NAME) -x \*.rst -x $(NAME)/rubric/\* -x $(NAME)/solution/\* -x $(NAME)/Makefile -x \*.swp -x $(NAME)/_build/\* -x $(NAME)/meta/\*

upload: zip
	scp /tmp/$(NAME)-solution.zip /tmp/$(NAME).zip $(SSH_HOST):$(SSH_DIR)
	ssh $(SSH_HOST) rm -rf $(SSH_DIR)$(NAME)
	scp -r _build/handouts $(SSH_HOST):$(SSH_DIR)$(NAME)
	ssh $(SSH_HOST) $(SSH_DIR)../tools/update_content
	open $(SSH_URL)
	rm -f /tmp/$(NAME).zip /tmp/$(NAME)-solution.zip
	rm -rf $(BUILDDIR)/*
