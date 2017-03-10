# Makefile adapted from Alad Wenters (https://github.com/AladW/aurutils/)

PROGNM = aursec-tui
PREFIX ?= /usr/local
SHRDIR ?= $(DESTDIR)$(PREFIX)/share
BINDIR ?= $(DESTDIR)$(PREFIX)/bin
LIBDIR ?= $(DESTDIR)$(PREFIX)/lib

all: man/aursec-tui.1

install: all
	@install -Dm755 *.py                 -t $(LIBDIR)/$(PROGNM)
	mkdir -p $(BINDIR)
	ln -fs $(PREFIX)/lib/$(PROGNM)/tui.py   $(BINDIR)/aursec-tui
	@install -Dm644 man/*.1              -t $(SHRDIR)/man/man1	
	@install -Dm644 ../LICENSE	     -t $(SHRDIR)/licenses/$(PROGNM)

man/%.1: man/%.1.md
	pandoc -s -t man $< > $@

clean:
	$(RM) man/*.1
