#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jinja2_time
Version  : 0.2.0
Release  : 20
URL      : https://files.pythonhosted.org/packages/de/7c/ee2f2014a2a0616ad3328e58e7dac879251babdb4cb796d770b5d32c469f/jinja2-time-0.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/de/7c/ee2f2014a2a0616ad3328e58e7dac879251babdb4cb796d770b5d32c469f/jinja2-time-0.2.0.tar.gz
Summary  : Jinja2 Extension for Dates and Times
Group    : Development/Tools
License  : MIT
Requires: pypi-jinja2_time-license = %{version}-%{release}
Requires: pypi-jinja2_time-python = %{version}-%{release}
Requires: pypi-jinja2_time-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(arrow)
BuildRequires : pypi(jinja2)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Jinja2 Time
        ===========
        
        |pypi| |pyversions| |license| |travis-ci|
        
        Jinja2 Extension for Dates and Times

%package license
Summary: license components for the pypi-jinja2_time package.
Group: Default

%description license
license components for the pypi-jinja2_time package.


%package python
Summary: python components for the pypi-jinja2_time package.
Group: Default
Requires: pypi-jinja2_time-python3 = %{version}-%{release}

%description python
python components for the pypi-jinja2_time package.


%package python3
Summary: python3 components for the pypi-jinja2_time package.
Group: Default
Requires: python3-core
Provides: pypi(jinja2_time)
Requires: pypi(arrow)
Requires: pypi(jinja2)

%description python3
python3 components for the pypi-jinja2_time package.


%prep
%setup -q -n jinja2-time-0.2.0
cd %{_builddir}/jinja2-time-0.2.0
pushd ..
cp -a jinja2-time-0.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672284209
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jinja2_time
cp %{_builddir}/jinja2-time-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jinja2_time/41557e04db2db0c86215609885cdc73ab769b848 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jinja2_time/41557e04db2db0c86215609885cdc73ab769b848

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
