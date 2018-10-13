test:
	@echo "Hola"

commit:
	git commit -am "Commit"
	git push origin master

pull:
	git reset --hard HEAD
	git pull origin master

install:
	@-pip install astropy
	@-pip install --no-deps photutils
	@-pip install astroquery
	@-apt-get install imagemagick
	@-cp astrohum.py ..
	@-cp makefile ..
