%define		_realname	sound-monitor

Summary:	Sound Monitor panel applet
Summary(pl):	Aplet panelu monitoruj�cy d�wi�k
Name:		gnome-applet-%{_realname}
Version:	1.99.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/gqapplets/%{_realname}-%{version}.tar.gz
# Source0-md5:	f70e1daa9822b87d787db17d0091e05c
URL:		http://gqapplets.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.13
BuildRequires:	gnome-panel-devel >= 2.0.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/gconf

%description
Panel applet for gnome. Displays sound output of esound. Included many
themes, can show sound volume, an oscilloscope, or a spectrum analyzer
in the display.

%description -l pl
Aplet panelu GNOME, wy�wietlaj�cy stan wyj�cia d�wi�ku esound. Zawiera
wiele motyw�w, mo�e wy�wietla� g�o�no��, oscyloskop lub analizator
widma.

%prep
%setup -q -n %{_realname}-%{version}

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure --with-gconf-schema-file-dir=%{_sysconfdir}/schemas
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog src/themes/SKIN-SPECS
%{_sysconfdir}/schemas/sound-monitor.schemas
%attr(755,root,root) %{_bindir}/esdpvd2
%{_libdir}/bonobo/servers/*
%attr(755,root,root) %{_libdir}/sound-monitor_applet2
%{_datadir}/gnome-2.0/ui/GNOME_SoundMonitorApplet.xml
%{_pixmapsdir}/*.png
%{_datadir}/sound-monitor2/*


#%{_sysconfdir}/CORBA/servers/sound-monitor2_applet.gnorba
#%{_datadir}/applets/Multimedia/sound-monitor2_applet.desktop
#%{_datadir}/sound-monitor2
