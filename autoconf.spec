#
# Conditional build:
# _without_emacs	- without emacs autoconf-mode
# _without_xemacs	- without XEmacs autoconf-mode
#
%define		_without_emacs	yes
%define		_without_xemacs	yes

%include	/usr/lib/rpm/macros.perl
Summary:	GNU autoconf - source configuration tools
Summary(de):	Ein GNU-Hilfsmittel für Quellencode automatisch konfigurieren
Summary(es):	Una herramienta de GNU para automáticamente configurar código de fuente
Summary(fr):	Un outil de GNU pour configurer automatiquement le code source
Summary(it):	Uno strumento di GNU per automaticamente la configurazione del codice sorgente
Summary(ko):	½º½º·Î È¯°æ¿¡ µû¶ó ¼Ò½º ÄÚµå¸¦ ¸ÂÃçÁÖ´Â GNU µµ±¸
Summary(pl):	GNU autoconf - narzêdzie do automatycznego konfigurowania ¼róde³
Summary(pt_BR):	GNU autoconf - ferramentas de configuração de fontes
Summary(ru):	GNU autoconf - Á×ÔÏËÏÎÆÉÇÕÒÁÔÏÒ ÉÓÈÏÄÎÙÈ ÔÅËÓÔÏ×
Summary(uk):	GNU autoconf - Á×ÔÏËÏÎÆ¦ÇÕÒÁÔÏÒ ×ÉÈ¦ÄÎÉÈ ÔÅËÓÔ¦×
Name:		autoconf
Version:	2.58
Release:	1.2
License:	GPL
Group:		Development/Building
# stable releases:
Source0:	ftp://ftp.gnu.org/gnu/autoconf/%{name}-%{version}.tar.bz2
# Source0-md5:	db3fa3069c6554b3505799c7e1022e2b
# devel releases:
#Source0:	ftp://alpha.gnu.org/pub/gnu/autoconf/%{name}-%{version}.tar.bz2
Patch0:		%{name}-mawk.patch
Patch1:		%{name}-version.patch
Patch2:		%{name}-info.patch
Patch3:		%{name}-AC_EGREP.patch
Patch4:		%{name}-bashism.patch
URL:		http://www.gnu.org/software/autoconf/
BuildConflicts:	m4 = 1.4o
%{!?_without_emacs:BuildRequires:	emacs}
BuildRequires:	m4 >= 1:1.4p-0.pre2.2
BuildRequires:	rpm-perlprov
BuildRequires:	texinfo >= 4.2
%{!?_without_xemacs:BuildRequires:	xemacs}
Conflicts:	gettext < 0.10.38-3
Requires:	/bin/awk
Requires:	diffutils
Requires:	m4 >= 1:1.4p-0.pre2.2
Requires:	mktemp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	autoconf252
Obsoletes:	autoconf253

%define		_libdir		%{_datadir}

%description
GNU's Autoconf is a tool for configuring source code and Makefiles.
Using Autoconf, programmers can create portable and configurable
packages, since the person building the package is allowed to specify
various configuration options.

You should install Autoconf if you are developing software and you'd
like to use it to create shell scripts which will configure your
source code packages. If you are installing Autoconf, you will also
need to install the GNU m4 package.

Note that the Autoconf package is not required for the end user who
may be configuring software with an Autoconf-generated script;
Autoconf is only required for the generation of the scripts, not their
use.

%description -l de
GNU's Autoconf ist eines Hilfsmittels für das Konfigurieren des
Quellencodes und der Makefiles. Mit Autoconf können Programmierer die
beweglichen und konfigurierbaren Pakete erstellen, da der Person, die
das Paket aufbaut, erlaubt wird, verschiedene Konfiguration Optionen
zu spezifizieren.

Sie sollten Autoconf installieren, wenn Sie Software entwickeln und
Sie sie benutzen möchten, um Shellindexe zu erstellen, die Ihre
Quellencodepakete konfigurieren. Wenn Sie Autoconf installieren,
müssen Sie auch das Paket GNU m4 installieren.

Beachten Sie, daß das Paket Autoconf nicht für den Endbenutzer
angefordert wird, der Software mit einem Autoconf-festgelegten Index
konfigurieren kann; Autoconf wird nur für das Erzeugung der Indexe,
nicht ihr Gebrauch angefordert.

%description -l es
GNÚs Autoconf es una herramienta para configurar código y makefiles de
fuente. Usando Autoconf, los programadores pueden crear los conjuntos
portables y configurables, puesto que se permite a la persona que
construye el conjunto especificar varias opciones de la configuración.

Usted debe instalar Autoconf si usted está desarrollando software
lógica y usted quisiera utilizarlo para crear los shell scriptes que
configurarán sus conjuntos del código de fuente. Si usted está
instalando Autoconf, usted también necesitará instalar el conjunto de
GNU m4.

Observe que el conjunto de Autoconf no está requerido para el
utilizador del extremo que puede configurar software lógica con una
escritura Autoconf-generada; Autoconf se requiere solamente para la
generación de las escrituras, no su uso.

%description -l fr
GNU's Autoconf est un outil pour configurer le code source et les
fichiers makefile. En utilisant Autoconf, les programmeurs peuvent
créer les modules portatifs et configurables, puisqu'on permet à la la
personne établissant le module d'indiquer de diverses options de
configuration.

Vous devriez installer Autoconf si vous développez le logiciel et vous
voudriez l'employer pour créer les séquences type d'interpréteur de
commandes interactif qui configureront vos modules de code source. Si
vous installez Autoconf, vous devrez également installer le module de
GNU m4.

Notez que le module d'Autoconf n'est pas exigé pour l'utilisateur qui
peut configurer le logiciel avec une séquence type Autoconf-produite;
Autoconf est seulement exigé pour la génération des séquences type,
non leur utilisation.

%description -l it
GNU's Autoconf è uno strumento per la configurazione il codice e dei
makefiles sorgente. Usando Autoconf, i programmatori possono creare i
pacchetti portatili e configurabili, poiché alla persona che sviluppa
il pacchetto è permessa specificare le varie opzioni di
configurazione.

Dovreste installare Autoconf se state sviluppando il software e
voleste usarli per creare gli scritti di coperture che configureranno
i vostri pacchetti di codice sorgente. Se state installando Autoconf,
egualmente dovrete installare il pacchetto di GNU m4.

Si noti che il pacchetto di Autoconf non è richiesto per l'
utilizzatore finale che può configurare il software con uno scritto
Autoconf-generato; Autoconf è richiesto soltanto per la generazione
degli scritti, il non loro uso.

%description -l pl
GNU autoconf jest narzêdziem wykorzystywanym do automatycznego
konfigurowania kodów ¼ród³owych pakietów programów oraz do generowania
na podstawie automatycznie rozpoznanego ¶rodowiska plików Makefile i
innych zale¿nych od zawarto¶ci systemu, w którym ma przebiegaæ proces
kompilacji. Pomaga programi¶cie w konfigurowaniu i tworzeniu
oprogramowania daj±cego siê przenie¶æ na ró¿ne platformy. Umo¿liwia
wybór wielu opcji podczas procesu przygotowania do kompilacji.

GNU autoconf nie jest generalnie potrzebny koñcowemu u¿ytkownikowi, a
tylko podczas generowania samych skryptów autokonfiguracyjnych.

%description -l pt_BR
GNU "autoconf" é uma ferramenta para configuração de fontes e
Makefiles. Ele ajuda o programador na criação de pacotes portáveis e
configuráveis, permitindo que a pessoa que programa o pacote
especifique várias opções de configuração. Autoconf é necessário
somente para gerar scripts de configuração.

%description -l ru
GNU autoconf - ÉÎÓÔÒÕÍÅÎÔ ÄÌÑ Á×ÔÏËÏÎÆÉÇÕÒÁÃÉÉ ÉÓÈÏÄÎÙÈ ÔÅËÓÔÏ× É
ÇÅÎÅÒÁÃÉÉ Makefile'Ï×. ðÏÍÏÇÁÅÔ ÐÒÏÇÒÁÍÍÉÓÔÕ ÓÏÚÄÁ×ÁÔØ ÐÏÒÔÉÒÕÅÍÙÅ É
ËÏÎÆÉÇÕÒÉÒÕÅÍÙÅ ÐÁËÅÔÙ, ÐÏÚ×ÏÌÑÑ ÔÏÍÕ, ËÔÏ ÜÔÉ ÐÁËÅÔÙ ÓÏÂÉÒÁÅÔ,
ÚÁÄÁ×ÁÔØ ÒÁÚÌÉÞÎÙÅ ÏÐÃÉÉ ËÏÎÆÉÇÕÒÁÃÉÉ.

"autoconf" ÎÅ Ñ×ÌÑÅÔÓÑ ÎÅÏÂÈÏÄÉÍÙÍ ÄÌÑ ËÏÎÅÞÎÏÇÏ ÐÏÌØÚÏ×ÁÔÅÌÑ, ÅÇÏ
ÉÓÐÏÌØÚÕÀÔ ÔÏÌØËÏ ÄÌÑ ÇÅÎÅÒÁÃÉÉ ËÏÎÆÉÇÕÒÁÃÉÏÎÎÙÈ ÓËÒÉÐÔÏ×.

%description -l uk
GNU autoconf - ÃÅ ¦ÎÓÔÒÕÍÅÎÔ ÄÌÑ Á×ÔÏÍÁÔÉÞÎÏ§ ËÏÎÆ¦ÇÕÒÁÃ¦§ ×ÉÈ¦ÄÎÉÈ
ÔÅËÓÔ¦× ÔÁ ÇÅÎÅÒÁÃ¦§ Makefile'¦×. äÏÐÏÍÏÇÁ¤ ÐÒÏÇÒÁÍ¦ÓÔÕ ÓÔ×ÏÒÀ×ÁÔÉ
ÍÏÂ¦ÌØÎ¦ ÐÁËÅÔÉ, ÝÏ ÄÏÚ×ÏÌÑÀÔØ ËÏÎÆ¦ÇÕÒÁÃ¦À. ãÅ ÄÏÚ×ÏÌÑ¤ ÔÏÍÕ, ÈÔÏ
ÚÁÊÍÁ¤ÔØÓÑ ÚÂÏÒËÏÀ ÔÁËÉÈ ÐÁËÅÔ¦×, ÚÁÄÁ×ÁÔÉ Ò¦ÚÎ¦ ÏÐÃ¦§ ËÏÎÆ¦ÇÕÒÁÃ¦§.

"autoconf" ÎÅ ¤ ÎÅÏÂÈ¦ÄÎÉÍ ÄÌÑ Ë¦ÎÃÅ×ÏÇÏ ËÏÒÉÓÔÕ×ÁÞÁ, ÊÏÇÏ
×ÉËÏÒÉÓÔÏ×ÕÀÔØ Ô¦ÌØËÉ ÄÌÑ ÇÅÎÅÒÁÃ¦§ ËÏÎÆ¦ÇÕÒÁÃ¦ÊÎÉÈ ÓËÒÉÐÔ¦×.

%package -n emacs-autoconf-mode-pkg
Summary:	emacs autoconf-mode
Summary(pl):	Tryb autoconf dla emacsa
Group:		Applications/Editors/Emacs
Requires:	emacs

%description -n emacs-autoconf-mode-pkg
Emacs autoconf-mode.

%description -n emacs-autoconf-mode-pkg -l pl
Tryb edycji autoconf dla emacsa.

%package -n xemacs-autoconf-mode-pkg
Summary:	xemacs autoconf-mode
Summary(pl):	Tryb autoconf dla emacsa
Group:		Applications/Editors/Emacs
Requires:	xemacs

%description -n xemacs-autoconf-mode-pkg
Emacs autoconf-mode.

%description -n xemacs-autoconf-mode-pkg -l pl
Tryb edycji autoconf dla emacsa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure \
	%{!?_without_xemacs:EMACS=xemacs}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
%if 0%{!?_without_xemacs:1}
	lispdir=%{_datadir}/xemacs-packages/autoconf
%endif

%if 0%{!?_without_xemacs:1}
xemacs -batch -no-autoloads -l autoload -f batch-update-directory \
	$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/autoconf
xemacs -batch -vanilla -f batch-byte-compile \
	$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/autoconf/auto-autoloads.el
%endif

%if 0%{!?_without_emacs:%{!?_without_xemacs:1}}
rm lib/emacs/*.elc
%{__make} -C lib/emacs install-dist_lispLISP \
	DESTDIR=$RPM_BUILD_ROOT \
	EMACS=emacs \
	lispdir=%{_emacs_lispdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog ChangeLog.2 NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/autoconf
%{_infodir}/*.info*
%{_mandir}/man1/*

%if 0%{!?_without_emacs:1}
%files -n emacs-autoconf-mode-pkg
%defattr(644,root,root,755)
%{_emacs_lispdir}/autoconf/*.elc
%endif

%if 0%{!?_without_xemacs:1}
%files -n xemacs-autoconf-mode-pkg
%defattr(644,root,root,755)
%dir %{_datadir}/xemacs-packages/autoconf
%{_datadir}/xemacs-packages/autoconf/*.elc
%endif
