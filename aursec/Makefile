# Makefile copied from Alad Wenter (https://github.com/AladW/aurutils/)

PROGNM = aursec
PREFIX ?= /usr/local
SHRDIR ?= $(DESTDIR)$(PREFIX)/share
BINDIR ?= $(DESTDIR)$(PREFIX)/bin
LIBDIR ?= $(DESTDIR)$(PREFIX)/lib

.PHONY: check install

check:
	@shellcheck -x bin/*

install:
	@install -Dm755 bin/*	       -t $(BINDIR)
	@install -Dm644 cmp/zsh/*      -t $(SHRDIR)/zsh/site-functions
#	@install -Dm644 man1/*	       -t $(SHRDIR)/man/man1
#	@install -Dm644 man7/*	       -t $(SHRDIR)/man/man7
	@install -Dm644 lib/*          -t $(LIBDIR)/systemd/system
	@install -Dm644 share/*        -t $(SHRDIR)/$(PROGNM)

	@install -Dm644 ../LICENSE	   -t $(SHRDIR)/licenses/$(PROGNM)
#	@install -Dm644 ../THANKS ../README -t $(SHRDIR)/doc/$(PROGNM)
