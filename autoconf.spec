Summary:	GNU autoconf - source configuration tools
Summary(pl):	GNU autoconf - narzêdzie do automatycznego konfigurowania ¼róde³
Name:		autoconf
Version:	2.13
Release:	8
Copyright:	GPL
Group:		Development/Building
Group(pl):	Programowanie/Budowanie
Source:		ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		autoconf-tmprace.patch
Patch1:		autoconf-info.patch
Patch2:		autoconf-mawk.patch
Patch3:		autoconf-man.patch
Patch4:		autoconf-notmp.patch
Patch5:		autoconf-pinard.patch
Patch6:		autoconf-fhs.patch
Requires:	gawk
Requires:	m4
Requires:	mktemp
Prereq:		/sbin/install-info
BuildRoot:	/tmp/%{name}-%{version}-root
Buildarch:	noarch

%description
GNU's "autoconf" is a tool for source and Makefile configuration. It
assists the programmer in creating portable and configurable packages, by
allowing the person building the package to specify various configuration
options. 

"autoconf" is not required for the end user - it is needed only to
generate the configuration scripts. 

%description -l pl
GNU autoconf jest narzêdziem wykorzystywanym do automatycznego
konfigurowania kodów ¼ród³owych pakietów programów oraz do generowania na
podstawie automatycznie rozoznanego ¶rodowiska plików Makefile i innch
zale¿nych od zawarto¶ci systemu w którym ma przebiegaæ proces kompilacji.
Pomaga programi¶cie w konfigurowaniu i tworzeniu opragramowania daj±cego siê
przenie¶æ na ró¿ne platformy. Umo¿liwia wybór wielu opcji podczas procesu
przygotowania do kompilacji.

GNU autoconf nie jest generalnie potrzebny dla u¿ytkownika koñcowego, a
tylko podczas generowania samych skryptów autokonfiguracyjnych.
 
%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
./configure \
	--prefix=/usr \
	--infodir=%{_infodir} \
	--mandir=%{_mandir}
make datadir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/share/{info,man/man1}

make install \
	prefix=$RPM_BUILD_ROOT/usr \
	datadir=$RPM_BUILD_ROOT%{_libdir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
install install-sh $RPM_BUILD_ROOT%{_libdir}/autoconf

install {autoconf,autoheader,autoreconf,autoscan,autoupdate,ifnames}.1 \
	$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/autoconf.info* \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%post
/sbin/install-info %{_infodir}/autoconf.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --del %{_infodir}/autoconf.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/*

%{_infodir}/autoconf.info*
%{_mandir}/man1/*

%{_libdir}/autoconf

%changelog
* Fri Apr 30 1999 Artur Frysiak <wiget@pld.org.pl>
  [2.13-7]
- added autoconf-pinard.patch from grep 2.3 
  (fixed lookup for opendir and gethostbyname)  
  
* Tue Apr 27 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.13-6]
- added patch with complet set autoconf man pages (from Debian),
- added patch for looking for gawk before mawk in ./configure
  (autoconf-mawk.patch from rawhide),
- added patch wich adds removing temporary files used by auconf
  scripts (autoconf-notmp.patch from rawhide),
- recompiled on new rpm.

* Wed Jan 26 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.13-1d]
- added Group(pl).

* Wed Dec 29 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.12-7]
- standarized {un}registering info pages 
  (added autoconf-info.patch).

* Mon Sep 21 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.12-5]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- modified pl translation,
- added full %attr description in %files.

* Thu Aug 27 1998 Cristian Gafton <gafton@redhat.com>
- patch for fixing /tmp race conditions

* Fri Jun 12 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.12-5]
- added pl transaltion,
- added %defattr support.

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- spec file cleanups
- made a noarch package
- uses autoconf
- uses install-info

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built with glibc
