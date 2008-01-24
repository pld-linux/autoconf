#
# Conditional build:
%bcond_without	emacs	# without emacs autoconf-mode
%bcond_without	xemacs	# without XEmacs autoconf-mode
#
%undefine	with_emacs
%undefine	with_xemacs
#
%include	/usr/lib/rpm/macros.perl
Summary:	GNU autoconf - source configuration tools
Summary(de.UTF-8):	Ein GNU-Hilfsmittel für Quellencode automatisch konfigurieren
Summary(es.UTF-8):	Una herramienta GNU para configurar automáticamente el código fuente
Summary(fr.UTF-8):	Un outil de GNU pour configurer automatiquement le code source
Summary(it.UTF-8):	Uno strumento di GNU per automaticamente la configurazione del codice sorgente
Summary(ko.UTF-8):	스스로 환경에 따라 소스 코드를 맞춰주는 GNU 도구
Summary(pl.UTF-8):	GNU autoconf - narzędzie do automatycznego konfigurowania źródeł
Summary(pt_BR.UTF-8):	GNU autoconf - ferramentas de configuração de fontes
Summary(ru.UTF-8):	GNU autoconf - автоконфигуратор исходных текстов
Summary(uk.UTF-8):	GNU autoconf - автоконфігуратор вихідних текстів
Name:		autoconf
Version:	2.61
Release:	9
License:	GPL
Group:		Development/Building
# stable releases:
Source0:	ftp://ftp.gnu.org/gnu/autoconf/%{name}-%{version}.tar.bz2
# Source0-md5:	36d3fe706ad0950f1be10c46a429efe0
# devel releases:
#Source0:	ftp://alpha.gnu.org/pub/gnu/autoconf/%{name}-%{version}.tar.bz2
Patch0:		%{name}-mawk.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-AC_EGREP.patch
Patch3:		%{name}-cxxcpp-warnonly.patch
Patch4:		%{name}-gettext.patch
Patch5:		%{name}-define.patch
URL:		http://www.gnu.org/software/autoconf/
BuildConflicts:	m4 = 1.4o
%{?with_emacs:BuildRequires:	emacs}
BuildRequires:	m4 >= 3:1.4.10-2
BuildRequires:	rpm-perlprov
BuildRequires:	texinfo >= 4.2
%{?with_xemacs:BuildRequires:	xemacs}
Conflicts:	gettext < 0.10.38-3
Requires:	/bin/awk
Requires:	diffutils
%requires_eq	m4
Requires:	mktemp
BuildArch:	noarch
Obsoletes:	autoconf252
Obsoletes:	autoconf253
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{_datadir}

%description
GNU's Autoconf is a tool for configuring source code and Makefiles.
Using Autoconf, programmers can create portable and configurable
packages, since the person building the package is allowed to specify
various configuration options.

You should install Autoconf if you are developing software and you'd
like to use it to create shell scripts which will configure your
source code packages.

Note that the Autoconf package is not required for the end user who
may be configuring software with an Autoconf-generated script;
Autoconf is only required for the generation of the scripts, not their
use.

%description -l de.UTF-8
GNU's Autoconf ist eines Hilfsmittels für das Konfigurieren des
Quellencodes und der Makefiles. Mit Autoconf können Programmierer die
beweglichen und konfigurierbaren Pakete erstellen, da der Person, die
das Paket aufbaut, erlaubt wird, verschiedene Konfiguration Optionen
zu spezifizieren.

Sie sollten Autoconf installieren, wenn Sie Software entwickeln und
Sie sie benutzen möchten, um Shellindexe zu erstellen, die Ihre
Quellencodepakete konfigurieren.

Beachten Sie, daß das Paket Autoconf nicht für den Endbenutzer
angefordert wird, der Software mit einem Autoconf-festgelegten Index
konfigurieren kann; Autoconf wird nur für das Erzeugung der Indexe,
nicht ihr Gebrauch angefordert.

%description -l es.UTF-8
Autoconf de GNU es una herramienta para configurar código y makefiles
de fuente. Usando Autoconf, los programadores pueden crear los
conjuntos portables y configurables, puesto que se permite a la
persona que construye el conjunto especificar varias opciones de la
configuración.

Usted debe instalar Autoconf si está desarrollando software y quisiera
utilizarlo para crear los shell scriptes que configurarán sus
conjuntos del código fuente.

Observe que el conjunto de Autoconf no está requerido para el
utilizador del extremo que puede configurar software con una escritura
Autoconf-generada; Autoconf se requiere solamente para la generación
de las escrituras, no su uso.

%description -l fr.UTF-8
GNU's Autoconf est un outil pour configurer le code source et les
fichiers makefile. En utilisant Autoconf, les programmeurs peuvent
créer les modules portatifs et configurables, puisqu'on permet à la la
personne établissant le module d'indiquer de diverses options de
configuration.

Vous devriez installer Autoconf si vous développez le logiciel et vous
voudriez l'employer pour créer les séquences type d'interpréteur de
commandes interactif qui configureront vos modules de code source.

Notez que le module d'Autoconf n'est pas exigé pour l'utilisateur qui
peut configurer le logiciel avec une séquence type Autoconf-produite;
Autoconf est seulement exigé pour la génération des séquences type,
non leur utilisation.

%description -l it.UTF-8
GNU's Autoconf è uno strumento per la configurazione il codice e dei
makefiles sorgente. Usando Autoconf, i programmatori possono creare i
pacchetti portatili e configurabili, poiché alla persona che sviluppa
il pacchetto è permessa specificare le varie opzioni di
configurazione.

Dovreste installare Autoconf se state sviluppando il software e
voleste usarli per creare gli scritti di coperture che configureranno
i vostri pacchetti di codice sorgente.

Si noti che il pacchetto di Autoconf non è richiesto per l'
utilizzatore finale che può configurare il software con uno scritto
Autoconf-generato; Autoconf è richiesto soltanto per la generazione
degli scritti, il non loro uso.

%description -l pl.UTF-8
GNU autoconf jest narzędziem wykorzystywanym do automatycznego
konfigurowania kodów źródłowych pakietów programów oraz do generowania
na podstawie automatycznie rozpoznanego środowiska plików Makefile i
innych zależnych od zawartości systemu, w którym ma przebiegać proces
kompilacji. Pomaga programiście w konfigurowaniu i tworzeniu
oprogramowania dającego się przenieść na różne platformy. Umożliwia
wybór wielu opcji podczas procesu przygotowania do kompilacji.

GNU autoconf nie jest generalnie potrzebny końcowemu użytkownikowi, a
tylko podczas generowania samych skryptów autokonfiguracyjnych.

%description -l pt_BR.UTF-8
GNU "autoconf" é uma ferramenta para configuração de fontes e
Makefiles. Ele ajuda o programador na criação de pacotes portáveis e
configuráveis, permitindo que a pessoa que programa o pacote
especifique várias opções de configuração. Autoconf é necessário
somente para gerar scripts de configuração.

%description -l ru.UTF-8
GNU autoconf - инструмент для автоконфигурации исходных текстов и
генерации Makefile'ов. Помогает программисту создавать портируемые и
конфигурируемые пакеты, позволяя тому, кто эти пакеты собирает,
задавать различные опции конфигурации.

"autoconf" не является необходимым для конечного пользователя, его
используют только для генерации конфигурационных скриптов.

%description -l uk.UTF-8
GNU autoconf - це інструмент для автоматичної конфігурації вихідних
текстів та генерації Makefile'ів. Допомогає програмісту створювати
мобільні пакети, що дозволяють конфігурацію. Це дозволяє тому, хто
займається зборкою таких пакетів, задавати різні опції конфігурації.

"autoconf" не є необхідним для кінцевого користувача, його
використовують тільки для генерації конфігураційних скриптів.

%package -n emacs-autoconf-mode-pkg
Summary:	emacs autoconf-mode
Summary(pl.UTF-8):	Tryb autoconf dla emacsa
Group:		Applications/Editors/Emacs
Requires:	emacs

%description -n emacs-autoconf-mode-pkg
Emacs autoconf-mode.

%description -n emacs-autoconf-mode-pkg -l pl.UTF-8
Tryb edycji autoconf dla emacsa.

%package -n xemacs-autoconf-mode-pkg
Summary:	xemacs autoconf-mode
Summary(pl.UTF-8):	Tryb autoconf dla emacsa
Group:		Applications/Editors/Emacs
Requires:	xemacs

%description -n xemacs-autoconf-mode-pkg
Emacs autoconf-mode.

%description -n xemacs-autoconf-mode-pkg -l pl.UTF-8
Tryb edycji autoconf dla emacsa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%configure \
	%{?with_xemacs:EMACS=xemacs}
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
%if %{with xemacs}
	lispdir=%{_datadir}/xemacs-packages/autoconf
%endif

%if %{with xemacs}
xemacs -batch -no-autoloads -l autoload -f batch-update-directory \
	$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/autoconf
xemacs -batch -vanilla -f batch-byte-compile \
	$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/autoconf/auto-autoloads.el
%endif

%if %{with emacs} && %{with xemacs}
rm lib/emacs/*.elc
%{__make} -C lib/emacs install-dist_lispLISP \
	DESTDIR=$RPM_BUILD_ROOT \
	EMACS=emacs \
	lispdir=%{_emacs_lispdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog ChangeLog.2 NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/autoconf
%{_infodir}/*.info*
%{_mandir}/man1/*

%if %{with emacs}
%files -n emacs-autoconf-mode-pkg
%defattr(644,root,root,755)
%{_emacs_lispdir}/autoconf/*.elc
%endif

%if %{with xemacs}
%files -n xemacs-autoconf-mode-pkg
%defattr(644,root,root,755)
%dir %{_datadir}/xemacs-packages/autoconf
%{_datadir}/xemacs-packages/autoconf/*.elc
%endif
