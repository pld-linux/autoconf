#
# Conditional build:
# _without_emacs - without emacs autoconf-mode

%include	/usr/lib/rpm/macros.perl
Summary:	GNU autoconf - source configuration tools
Summary(de):	Ein GNU-Hilfsmittel fЭr Quellencode automatisch konfigurieren
Summary(es):	Una herramienta de GNU para automАticamente configurar cСdigo de fuente
Summary(fr):	Un outil de GNU pour configurer automatiquement le code source
Summary(it):	Uno strumento di GNU per automaticamente la configurazione del codice sorgente
Summary(pl):	GNU autoconf - narzЙdzie do automatycznego konfigurowania ╪rСdeЁ
Summary(pt_BR):	GNU autoconf - ferramentas de configuraГЦo de fontes
Summary(ru):	GNU autoconf - автоконфигуратор исходных текстов
Summary(uk):	GNU autoconf - автоконф╕гуратор вих╕дних текст╕в
Name:		autoconf
Version:	2.57
Release:	3
License:	GPL
Group:		Development/Building
# stable releases:
Source0:	ftp://ftp.gnu.org/gnu/autoconf/%{name}-%{version}.tar.bz2
# devel releases:
#Source0:	ftp://alpha.gnu.org/pub/gnu/autoconf/%{name}-%{version}.tar.bz2
Patch0:		%{name}-mawk.patch
Patch1:		%{name}-version.patch
Patch2:		%{name}-info.patch
Patch3:		%{name}-AC_EGREP.patch
URL:		http://www.gnu.org/software/autoconf/
Requires:	diffutils
Requires:	/bin/awk
Requires:	m4
Requires:	mktemp
Conflicts:	gettext < 0.10.38-3
BuildRequires:	m4
BuildRequires:	rpm-perlprov
BuildRequires:	texinfo >= 4.2
%{!?_without_emacs:BuildRequires:	emacs}
BuildConflicts:	m4 = 1.4o
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
GNU's Autoconf ist eines Hilfsmittels fЭr das Konfigurieren des
Quellencodes und der Makefiles. Mit Autoconf kЖnnen Programmierer die
beweglichen und konfigurierbaren Pakete erstellen, da der Person, die
das Paket aufbaut, erlaubt wird, verschiedene Konfiguration Optionen
zu spezifizieren.

Sie sollten Autoconf installieren, wenn Sie Software entwickeln und
Sie sie benutzen mЖchten, um Shellindexe zu erstellen, die Ihre
Quellencodepakete konfigurieren. Wenn Sie Autoconf installieren,
mЭssen Sie auch das Paket GNU m4 installieren.

Beachten Sie, daъ das Paket Autoconf nicht fЭr den Endbenutzer
angefordert wird, der Software mit einem Autoconf-festgelegten Index
konfigurieren kann; Autoconf wird nur fЭr das Erzeugung der Indexe,
nicht ihr Gebrauch angefordert.

%description -l es
GNзs Autoconf es una herramienta para configurar cСdigo y makefiles de
fuente. Usando Autoconf, los programadores pueden crear los conjuntos
portables y configurables, puesto que se permite a la persona que
construye el conjunto especificar varias opciones de la configuraciСn.

Usted debe instalar Autoconf si usted estА desarrollando software
lСgica y usted quisiera utilizarlo para crear los shell scriptes que
configurarАn sus conjuntos del cСdigo de fuente. Si usted estА
instalando Autoconf, usted tambiИn necesitarА instalar el conjunto de
GNU m4.

Observe que el conjunto de Autoconf no estА requerido para el
utilizador del extremo que puede configurar software lСgica con una
escritura Autoconf-generada; Autoconf se requiere solamente para la
generaciСn de las escrituras, no su uso.

%description -l fr
GNU's Autoconf est un outil pour configurer le code source et les
fichiers makefile. En utilisant Autoconf, les programmeurs peuvent
crИer les modules portatifs et configurables, puisqu'on permet Ю la la
personne Иtablissant le module d'indiquer de diverses options de
configuration.

Vous devriez installer Autoconf si vous dИveloppez le logiciel et vous
voudriez l'employer pour crИer les sИquences type d'interprИteur de
commandes interactif qui configureront vos modules de code source. Si
vous installez Autoconf, vous devrez Иgalement installer le module de
GNU m4.

Notez que le module d'Autoconf n'est pas exigИ pour l'utilisateur qui
peut configurer le logiciel avec une sИquence type Autoconf-produite;
Autoconf est seulement exigИ pour la gИnИration des sИquences type,
non leur utilisation.

%description -l it
GNU's Autoconf Х uno strumento per la configurazione il codice e dei
makefiles sorgente. Usando Autoconf, i programmatori possono creare i
pacchetti portatili e configurabili, poichИ alla persona che sviluppa
il pacchetto Х permessa specificare le varie opzioni di
configurazione.

Dovreste installare Autoconf se state sviluppando il software e
voleste usarli per creare gli scritti di coperture che configureranno
i vostri pacchetti di codice sorgente. Se state installando Autoconf,
egualmente dovrete installare il pacchetto di GNU m4.

Si noti che il pacchetto di Autoconf non Х richiesto per l'
utilizzatore finale che puР configurare il software con uno scritto
Autoconf-generato; Autoconf Х richiesto soltanto per la generazione
degli scritti, il non loro uso.

%description -l pl
GNU autoconf jest narzЙdziem wykorzystywanym do automatycznego
konfigurowania kodСw ╪rСdЁowych pakietСw programСw oraz do generowania
na podstawie automatycznie rozpoznanego ╤rodowiska plikСw Makefile i
innych zale©nych od zawarto╤ci systemu, w ktСrym ma przebiegaФ proces
kompilacji. Pomaga programi╤cie w konfigurowaniu i tworzeniu
oprogramowania daj╠cego siЙ przenie╤Ф na rС©ne platformy. Umo©liwia
wybСr wielu opcji podczas procesu przygotowania do kompilacji.

GNU autoconf nie jest generalnie potrzebny koЯcowemu u©ytkownikowi, a
tylko podczas generowania samych skryptСw autokonfiguracyjnych.

%description -l pt_BR
GNU "autoconf" И uma ferramenta para configuraГЦo de fontes e
Makefiles. Ele ajuda o programador na criaГЦo de pacotes portАveis e
configurАveis, permitindo que a pessoa que programa o pacote
especifique vАrias opГУes de configuraГЦo. Autoconf И necessАrio
somente para gerar scripts de configuraГЦo.

%description -l ru
GNU autoconf - инструмент для автоконфигурации исходных текстов и
генерации Makefile'ов. Помогает программисту создавать портируемые и
конфигурируемые пакеты, позволяя тому, кто эти пакеты собирает,
задавать различные опции конфигурации.

"autoconf" не является необходимым для конечного пользователя, его
используют только для генерации конфигурационных скриптов.

%description -l uk
GNU autoconf - це ╕нструмент для автоматично╖ конф╕гурац╕╖ вих╕дних
текст╕в та генерац╕╖ Makefile'╕в. Допомога╓ програм╕сту створювати
моб╕льн╕ пакети, що дозволяють конф╕гурац╕ю. Це дозволя╓ тому, хто
займа╓ться зборкою таких пакет╕в, задавати р╕зн╕ опц╕╖ конф╕гурац╕╖.

"autoconf" не ╓ необх╕дним для к╕нцевого користувача, його
використовують т╕льки для генерац╕╖ конф╕гурац╕йних скрипт╕в.

%package -n emacs-autoconf-mode-pkg
Summary:	emacs autoconf-mode
Summary(pl):	Tryb autoconf dla emacsa
Group:		Applications/Editors/Emacs
Requires:	emacs

%description -n emacs-autoconf-mode-pkg
Emacs autoconf-mode.

%description -n emacs-autoconf-mode-pkg -l pl
Tryb edycji autoconf dla emacsa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*

%{_infodir}/*.info*
%{_mandir}/man1/*

%{_libdir}/autoconf

%if%{!?_without_emacs:1}%{?_without_emacs:0}
%files -n emacs-autoconf-mode-pkg
%defattr(644,root,root,755)
%{_datadir}/emacs/site-lisp/*.elc
%endif
