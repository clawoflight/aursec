# Makefile adapted from Alad Wenters (https://github.com/AladW/aurutils/)

PROGNM = aursec
PREFIX ?= /usr/local
SHRDIR ?= $(DESTDIR)$(PREFIX)/share
BINDIR ?= $(DESTDIR)$(PREFIX)/bin
LIBDIR ?= $(DESTDIR)$(PREFIX)/lib

all: man/aursec.1 man/aursec-hash.1 man/aursec-chain.1 man/aursec.7

.PHONY: check install clean

check:
	@shellcheck -x bin/*

install: all
	@install -Dm755 bin/*	       -t $(BINDIR)
	@install -Dm644 cmp/zsh/*      -t $(SHRDIR)/zsh/site-functions
	@install -Dm644 man/*.1	       -t $(SHRDIR)/man/man1
	@install -Dm644 man/*.7	       -t $(SHRDIR)/man/man7
	@install -Dm644 lib/*.service  -t $(LIBDIR)/systemd/system
	@install -Dm644 lib/*.timer    -t $(LIBDIR)/systemd/system
	@install -Dm644 share/*        -t $(SHRDIR)/$(PROGNM)

	@install -Dm644 ../LICENSE	   -t $(SHRDIR)/licenses/$(PROGNM)
#	@install -Dm644 ../THANKS ../README -t $(SHRDIR)/doc/$(PROGNM)

man/%.1: man/%.1.md
	pandoc -s -t man $< > $@

man/%.7: man/%.7.md
	pandoc -s -t man $< > $@

clean:
	$(RM) man/*.1 man/*.7
