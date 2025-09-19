PROGRAM := virt-bypass-vpn

ifneq ($(DESTDIR),)
    PREFIX := /usr
else ifeq ($(PREFIX),)
    PREFIX := /usr/local
endif

install: $(PROGRAM)
	install -D --mode=0755 --target-directory=$(DESTDIR)$(PREFIX)/sbin $(PROGRAM)

.PHONY: install
