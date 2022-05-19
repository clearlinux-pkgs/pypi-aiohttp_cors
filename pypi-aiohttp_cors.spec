#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-aiohttp_cors
Version  : 0.7.0
Release  : 35
URL      : https://files.pythonhosted.org/packages/44/9e/6cdce7c3f346d8fd487adf68761728ad8cd5fbc296a7b07b92518350d31f/aiohttp-cors-0.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/44/9e/6cdce7c3f346d8fd487adf68761728ad8cd5fbc296a7b07b92518350d31f/aiohttp-cors-0.7.0.tar.gz
Summary  : CORS support for aiohttp
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-aiohttp_cors-license = %{version}-%{release}
Requires: pypi-aiohttp_cors-python = %{version}-%{release}
Requires: pypi-aiohttp_cors-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(aiohttp)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-pytest_runner

%description
CORS support for aiohttp
        ========================
        
        ``aiohttp_cors`` library implements
        `Cross Origin Resource Sharing (CORS) <cors_>`__
        support for `aiohttp <aiohttp_>`__
        asyncio-powered asynchronous HTTP server.
        
        Jump directly to `Usage`_ part to see how to use ``aiohttp_cors``.
        
        Same-origin policy
        ==================
        
        Web security model is tightly connected to
        `Same-origin policy (SOP) <sop_>`__.

%package license
Summary: license components for the pypi-aiohttp_cors package.
Group: Default

%description license
license components for the pypi-aiohttp_cors package.


%package python
Summary: python components for the pypi-aiohttp_cors package.
Group: Default
Requires: pypi-aiohttp_cors-python3 = %{version}-%{release}

%description python
python components for the pypi-aiohttp_cors package.


%package python3
Summary: python3 components for the pypi-aiohttp_cors package.
Group: Default
Requires: python3-core
Provides: pypi(aiohttp_cors)
Requires: pypi(aiohttp)

%description python3
python3 components for the pypi-aiohttp_cors package.


%prep
%setup -q -n aiohttp-cors-0.7.0
cd %{_builddir}/aiohttp-cors-0.7.0
pushd ..
cp -a aiohttp-cors-0.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652994299
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-aiohttp_cors
cp %{_builddir}/aiohttp-cors-0.7.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-aiohttp_cors/25d1ec1e682bcde600e2e1e0a043ea705de7f30d
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-aiohttp_cors/25d1ec1e682bcde600e2e1e0a043ea705de7f30d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
