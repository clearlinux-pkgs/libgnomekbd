#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgnomekbd
Version  : 3.28.1
Release  : 11
URL      : https://download.gnome.org/sources/libgnomekbd/3.28/libgnomekbd-3.28.1.tar.xz
Source0  : https://download.gnome.org/sources/libgnomekbd/3.28/libgnomekbd-3.28.1.tar.xz
Summary  : GNOME keyboard shared library
Group    : Development/Tools
License  : LGPL-2.0
Requires: libgnomekbd-bin = %{version}-%{release}
Requires: libgnomekbd-data = %{version}-%{release}
Requires: libgnomekbd-lib = %{version}-%{release}
Requires: libgnomekbd-license = %{version}-%{release}
Requires: libgnomekbd-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gdk-3.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxklavier)

%description


%package bin
Summary: bin components for the libgnomekbd package.
Group: Binaries
Requires: libgnomekbd-data = %{version}-%{release}
Requires: libgnomekbd-license = %{version}-%{release}

%description bin
bin components for the libgnomekbd package.


%package data
Summary: data components for the libgnomekbd package.
Group: Data

%description data
data components for the libgnomekbd package.


%package dev
Summary: dev components for the libgnomekbd package.
Group: Development
Requires: libgnomekbd-lib = %{version}-%{release}
Requires: libgnomekbd-bin = %{version}-%{release}
Requires: libgnomekbd-data = %{version}-%{release}
Provides: libgnomekbd-devel = %{version}-%{release}
Requires: libgnomekbd = %{version}-%{release}

%description dev
dev components for the libgnomekbd package.


%package lib
Summary: lib components for the libgnomekbd package.
Group: Libraries
Requires: libgnomekbd-data = %{version}-%{release}
Requires: libgnomekbd-license = %{version}-%{release}

%description lib
lib components for the libgnomekbd package.


%package license
Summary: license components for the libgnomekbd package.
Group: Default

%description license
license components for the libgnomekbd package.


%package locales
Summary: locales components for the libgnomekbd package.
Group: Default

%description locales
locales components for the libgnomekbd package.


%prep
%setup -q -n libgnomekbd-3.28.1
cd %{_builddir}/libgnomekbd-3.28.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662486675
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libgnomekbd
cp %{_builddir}/libgnomekbd-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/libgnomekbd/b256632dcce76559734ff0a23330d2898b7d3a3b || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang libgnomekbd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gkbd-keyboard-display

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Gkbd-3.0.typelib
/usr/share/GConf/gsettings/libgnomekbd.convert
/usr/share/applications/gkbd-keyboard-display.desktop
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.libgnomekbd.desktop.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.libgnomekbd.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.libgnomekbd.keyboard.gschema.xml
/usr/share/libgnomekbd/icons/kbdled-caps-lock.svg
/usr/share/libgnomekbd/icons/kbdled-num-lock.svg
/usr/share/libgnomekbd/icons/kbdled-scroll-lock.svg
/usr/share/libgnomekbd/ui/show-layout.ui

%files dev
%defattr(-,root,root,-)
/usr/include/libgnomekbd/gkbd-configuration.h
/usr/include/libgnomekbd/gkbd-desktop-config.h
/usr/include/libgnomekbd/gkbd-indicator-config.h
/usr/include/libgnomekbd/gkbd-indicator.h
/usr/include/libgnomekbd/gkbd-keyboard-config.h
/usr/include/libgnomekbd/gkbd-keyboard-drawing.h
/usr/include/libgnomekbd/gkbd-status.h
/usr/include/libgnomekbd/gkbd-util.h
/usr/lib64/libgnomekbd.so
/usr/lib64/libgnomekbdui.so
/usr/lib64/pkgconfig/libgnomekbd.pc
/usr/lib64/pkgconfig/libgnomekbdui.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgnomekbd.so.8
/usr/lib64/libgnomekbd.so.8.0.0
/usr/lib64/libgnomekbdui.so.8
/usr/lib64/libgnomekbdui.so.8.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgnomekbd/b256632dcce76559734ff0a23330d2898b7d3a3b

%files locales -f libgnomekbd.lang
%defattr(-,root,root,-)

