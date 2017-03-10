# Makefile adapted from Alad Wenters (https://github.com/AladW/aurutils/)

PROGNM = aursec-tui
PREFIX ?= /usr/local
SHRDIR ?= $(DESTDIR)$(PREFIX)/share
BINDIR ?= $(DESTDIR)$(PREFIX)/bin
LIBDIR ?= $(DESTDIR)$(PREFIX)/lib

#all: man/aursec.1 man/aursec-hash.1 man/aursec-chain.1 man/aursec.7

install: all
	@install -Dm644 *.py               -t $(LIBDIR)/$(PROGNM)
	ln -fsr $(PREFIX)/lib/$(PROGNM)/tui.py  $(BINDIR)/aursec-tui
	@install -Dm644 ../LICENSE	   -t $(SHRDIR)/licenses/$(PROGNM)
