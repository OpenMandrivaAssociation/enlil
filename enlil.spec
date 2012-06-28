#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/enlil enlil; \
#cd enlil; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf enlil-$PKG_VERSION.tar.xz enlil/ --exclude .svn --exclude .*ignore
# to disable debug build error
%define debug_package %{nil}

%define svndate 20120728
%define svnrev	70759

%define	major	0
%define	libname		%mklibname	enlil %{major}
%define	develname	%mklibname	enlil -d

Summary:	enil Library for EFL
Name:		enlil
Version:	0.6.0.%{svnrev}
Release:	0.%{svndate}.1
Group:		Graphical desktop/Enlightenment
License:	BSD
URL:		http://www.enlightenment.org/
Source0:	%{name}-%{version}.tar.xz

BuildRequires:	gettext-devel
BuildRequires:  pkgconfig(azy)
BuildRequires:  pkgconfig(efreet)
BuildRequires:  pkgconfig(emotion)
BuildRequires:  pkgconfig(eio)
BuildRequires:  pkgconfig(ethumb)
BuildRequires:	pkgconfig(flickcurl)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libiptcdata)

%description
Enlil is a library using the EFL which allows to manage
a list of albums and photos. EET is used to create the
database and ecore to manage events and file.

%package -n %{libname}
Summary:    Dynamic libraries from %{name}
Group:      System/Libraries
Provides:   %{name} = %{version}-%{release}
Obsoletes:	%{mklibname enlil1}

%description -n %{libname}
Enlil is a library for easily manipulating devices.

%package -n %{develname}
Summary:    Headers and development libraries from %{name}
Group:      Development/C
Requires:   %{libname} = %{version}-%{release}
Provides:   %name-devel = %{version}-%{release}

%description -n %{develname}
%{name} development headers and libraries.

%prep
%setup -qn %{name}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static
%make

%install
rm -fr %{buildroot}
%makeinstall

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/enlil_db_load_sync
%{_bindir}/enlil_db_print
%{_bindir}/enlil_db_sync
%{_bindir}/enlil_geocaching_print
%{_bindir}/enlil_transformations

%files -n %{libname}
%{_libdir}/libenlil.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}/
%{_includedir}/%{name}-0/
%{_libdir}/libenlil.so
%{_libdir}/pkgconfig/enlil.pc

