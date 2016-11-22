# Makefile adapted from Alad Wenters (https://github.com/AladW/aurutils/)

PROGNM = aursec
PREFIX ?= /usr/local
SHRDIR ?= $(DESTDIR)$(PREFIX)/share
BINDIR ?= $(DESTDIR)$(PREFIX)/bin
LIBDIR ?= $(DESTDIR)$(PREFIX)/lib

all: man

.PHONY: check install clean

check:
	@shellcheck -x bin/*

install: all
	@install -Dm755 bin/*	       -t $(BINDIR)
	@install -Dm644 cmp/zsh/*      -t $(SHRDIR)/zsh/site-functions
	@install -Dm644 man/*.1	       -t $(SHRDIR)/man/man1
	@install -Dm644 man/*.7	       -t $(SHRDIR)/man/man7
	@install -Dm644 lib/*.service  -t $(LIBDIR)/systemd/system
	@install -Dm644 share/*        -t $(SHRDIR)/$(PROGNM)

	@install -Dm644 ../LICENSE	   -t $(SHRDIR)/licenses/$(PROGNM)
#	@install -Dm644 ../THANKS ../README -t $(SHRDIR)/doc/$(PROGNM)

man: man/aursec.1.md man/aursec-hash.1.md man/aursec-chain.1.md man/aursec.7.md
	pandoc -s -t man man/aursec.1.md -o man/aursec.1
	pandoc -s -t man man/aursec-hash.1.md -o man/aursec-hash.1
	pandoc -s -t man man/aursec-chain.1.md -o man/aursec-chain.1
	pandoc -s -t man man/aursec.7.md -o man/aursec.7

clean:
	$(RM) man/*.1 man/*.7
