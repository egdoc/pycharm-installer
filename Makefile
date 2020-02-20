INSTALLDIR = $(HOME)/.local/opt
LAUNCHERDIR = $(HOME)/.local/share/applications

.PHONY: install
install: pycharm.desktop pycharm
	@mkdir -p $(INSTALLDIR) $(LAUNCHERDIR)
	@cp -R pycharm $(INSTALLDIR)
	@cp pycharm.desktop $(LAUNCHERDIR)/pycharm.desktop

pycharm.desktop:
	@sed -e 's_{{INSTALLDIR}}_$(INSTALLDIR)_g' data/template.desktop > pycharm.desktop

pycharm:
	@scripts/download.py

.PHONY: uninstall
uninstall:
	@rm -rf \
	  $(INSTALLDIR)/pycharm \
	  $(LAUNCHERDIR)/pycharm.desktop

.PHONY: clean
clean:
	@rm -rf pycharm.desktop pycharm
