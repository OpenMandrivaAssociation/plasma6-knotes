#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE notes application
Name:		plasma6-knotes
Version:	24.05.2
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/knotes/-/archive/%{gitbranch}/knotes-%{gitbranchd}.tar.bz2#/knotes-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/knotes-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Xml)
BuildRequires:	cmake(KF6TextUtils)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DNSSD)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6GlobalAccel)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6AkonadiNotes)
BuildRequires:	cmake(KPim6AkonadiMime)
BuildRequires:	cmake(KPim6CalendarUtils)
BuildRequires:	cmake(KPim6KontactInterface)
BuildRequires:	cmake(KPim6Libkdepim)
BuildRequires:	cmake(KPim6Mime)
BuildRequires:	cmake(KPim6PimCommon)
BuildRequires:	cmake(KPim6TextEdit)
BuildRequires:	cmake(KPim6AkonadiSearch)
BuildRequires:	cmake(KPim6GrantleeTheme)
BuildRequires:	xsltproc
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(x11)
Requires:	plasma6-kdepim-runtime

%description
KNotes aims to be a useful and full featured notes application for
the KDE project. It tries to be as fast and lightweight as possible
although including some advanced features.

%files -f knotes.lang
%{_datadir}/applications/org.kde.knotes.desktop
%{_bindir}/knotes
%{_datadir}/config.kcfg/knotesglobalconfig.kcfg
%{_datadir}/config.kcfg/notesagentsettings.kcfg
%dir %{_datadir}/knotes/
%{_datadir}/knotes/*
%{_datadir}/kxmlgui5/knotes
%{_docdir}/*/*/knotes
%{_iconsdir}/hicolor/*/actions/knotes_*.*
%{_iconsdir}/hicolor/*/apps/knotes.*
%{_datadir}/qlogging-categories6/knotes.categories
%{_datadir}/qlogging-categories6/knotes.renamecategories
%{_datadir}/knsrcfiles/knotes_printing_theme.knsrc
%{_datadir}/metainfo/org.kde.knotes.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.KNotes.xml
%{_datadir}/dbus-1/interfaces/org.kde.kontact.KNotes.xml
%{_qtdir}/plugins/pim6/kontact/kontact_knotesplugin.so
%{_qtdir}/plugins/pim6/kcms/knotes/kcm_knote_action.so
%{_qtdir}/plugins/pim6/kcms/knotes/kcm_knote_collection.so
%{_qtdir}/plugins/pim6/kcms/knotes/kcm_knote_display.so
%{_qtdir}/plugins/pim6/kcms/knotes/kcm_knote_editor.so
%{_qtdir}/plugins/pim6/kcms/knotes/kcm_knote_misc.so
%{_qtdir}/plugins/pim6/kcms/knotes/kcm_knote_network.so
%{_qtdir}/plugins/pim6/kcms/knotes/kcm_knote_print.so
%{_qtdir}/plugins/pim6/kcms/summary/kcmknotessummary.so
%{_libdir}/libknotesprivate.so*
%{_libdir}/libnotesharedprivate.so*
%{_bindir}/akonadi_notes_agent
%{_datadir}/akonadi/agents/notesagent.desktop
%{_docdir}/*/*/akonadi_notes_agent
%{_datadir}/knotifications6/akonadi_notes_agent.notifyrc

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n knotes-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang knotes --all-name
