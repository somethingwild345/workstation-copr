%global common_configure --disable-unity --srcdir=..

%global common_desc Arc is a flat theme with transparent elements for GTK 3, GTK 2 and GNOME Shell, Unity, Pantheon, Xfce, MATE, Cinnamon, Budgie Desktop.

Name:		arc-theme
Version:	20210127
Release:	1%{?dist}
Summary:	A flat theme with transparent elements

License:	GPLv3+
URL:		https://github.com/jnsh/arc-theme
Source0:	%{url}/archive/%{version}.tar.gz#/arc-theme-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  pkgconf
BuildRequires:	inkscape
BuildRequires:	optipng
BuildRequires:	sassc
BuildRequires:	gnome-shell
BuildRequires:	gtk3-devel
BuildRequires:	fdupes
BuildRequires:  make

Requires:	gnome-themes-extra
Requires:	gtk-murrine-engine

%description
%{common_desc}

%prep
%autosetup -p 1
%{_bindir}/autoreconf -fiv

%build
%{__mkdir} -p regular solid
pushd regular
%{__ln_s} -f ../configure configure
%configure %{common_configure}
popd
pushd solid
%{__ln_s} -f ../configure configure
%configure --disable-transparency %{common_configure}
popd
%make_build -C regular
%make_build -C solid

%install
%make_install -C regular
%make_install -C solid

# Link duplicate files.
%fdupes -s %{buildroot}%{_datadir}

%files
%license AUTHORS COPYING
%doc README.md
%{_datadir}/themes/*

%changelog
* Fri apr 2 2021 Muhammad Ahmad <mhdahmadx@gmail.com>
- New Version - 20210127

* Thu Oct 15 2020 Muhammad Ahmad <mhdahmadx@gmail.com>
- New Version - 20201013

* Wed Aug 19 2020 Muhammad Ahmad <mhdahmadx@gmail.com>
- Add Cinnamon and Xfce

* Wed Aug 19 2020 Muhammad Ahmad <mhdahmadx@gmail.com>
- New Version - 20200819

* Tue Aug 18 2020 Muhammad Ahmad <mhdahmadx@gmail.com>
- New Build
- Add Regular and Solid Variants

* Tue Jul 03 2020 Muhammad Ahmad <mhdahmadx@gmail.com>
- New Commit

* Wed Jun 03 2020 Muhammad Ahmad <mhdahmadx@gmail.com>
- Initial Commit
