%global common_configure --with-gnome-shell=3.36 --disable-cinnamon --disable-unity --disable-xfwm --disable-openbox --disable-lighter --disable-plank

%global common_desc Arc is a flat theme with transparent elements for GTK 3, GTK 2 and GNOME Shell, Unity, Pantheon, Xfce, MATE, Cinnamon, Budgie Desktop.


Name:		arc-gtk-theme
Version:	20200513
Release:	1%{?dist}
Summary:	A flat theme with transparent elements

License:	GPLv3+
URL:		https://github.com/jnsh/arc-theme
Source0:	%{url}/archive/%{version}.tar.gz#/arc-theme-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk3-devel
BuildRequires:	gtk-murrine-engine
BuildRequires:	inkscape
BuildRequires:	optipng
BuildRequires:	sassc
BuildRequires:   pkgconf

Requires:	filesystem
Requires:	gnome-themes-extra
Requires:	gtk-murrine-engine

%description
%{common_desc}

%prep
%autosetup -n arc-theme-%{version}
%{_bindir}/autoreconf -fiv

%build	
%configure %{common_configure}
%make_build

%install	
%make_install

%files
%license AUTHORS COPYING
%doc README.md
%{_datadir}/themes/*

%changelog
* Wed Jun 03 2020 Muhammad Ahmad <mhdahmadx@gmail.com>
- Initial Commit

