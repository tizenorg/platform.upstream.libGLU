#
# Please submit bugfixes or comments via http://bugs.tizen.org/
#
%bcond_with x

Name:           libGLU
Version:        9.0.0
Release:        0
License:        SGI Free B
Summary:        Graphics Library Utilities (GLU)
Url:            http://www.mesa3d.org
Group:          Development/Libraries/C and C++
Source:         glu.tar.bz2
Source1001: 	libGLU.manifest
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gl)
Provides:       mesa:%{_libdir}/libGLU.so.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if !%{with x}
ExclusiveArch:
%endif

%description
GLU offers simple interfaces for building mipmaps; checking for the
presence of extensions in the OpenGL (or other libraries which follow
the same conventions for advertising extensions); drawing
piecewise-linear curves, NURBS, quadrics and other primitives
(including, but not limited to, teapots); tesselating surfaces;
setting up projection matrices and unprojecting screen coordinates to
world coordinates.

This package provides the SGI implementation of GLU shipped with the
Mesa package.

%package devel
Summary:        Development files for the Graphics Library Utilities (GLU)
Group:          Development/Libraries/C and C++
Requires:       libGLU = %{version}
Requires:       pkgconfig(gl) >= 9

%description devel
GLU offers simple interfaces for building mipmaps; checking for the
presence of extensions in the OpenGL (or other libraries which follow
the same conventions for advertising extensions); drawing
piecewise-linear curves, NURBS, quadrics and other primitives
(including, but not limited to, teapots); tesselating surfaces;
setting up projection matrices and unprojecting screen coordinates to
world coordinates.

This package contains includes headers and static libraries for
compiling programs with GLU.

%prep
%setup -q -n glu
cp %{SOURCE1001} .

%build
autoreconf -fi
%configure  --disable-static
make %{?_smp_mflags} OPT_FLAGS="%{optflags}"

%install
%make_install

%post  -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libGLU.so.1*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
/usr/include/GL
%{_libdir}/pkgconfig/glu.pc
%{_libdir}/libGLU.so

%changelog
