all: l p

.PHONY: l p f r

l:
	git pull

p: f
	git pull
	git add .
	git commit -m "Update."
	git push origin master

f:
	yapf -ir .

r:
	python main.py