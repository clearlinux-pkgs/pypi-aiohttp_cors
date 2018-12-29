#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : aiohttp-cors
Version  : 0.7.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/44/9e/6cdce7c3f346d8fd487adf68761728ad8cd5fbc296a7b07b92518350d31f/aiohttp-cors-0.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/44/9e/6cdce7c3f346d8fd487adf68761728ad8cd5fbc296a7b07b92518350d31f/aiohttp-cors-0.7.0.tar.gz
Summary  : CORS support for aiohttp
Group    : Development/Tools
License  : Apache-2.0
Requires: aiohttp-cors-python3
Requires: aiohttp-cors-license
Requires: aiohttp-cors-python
Requires: aiohttp
Requires: typing
BuildRequires : aiohttp
BuildRequires : buildreq-distutils3
BuildRequires : pytest-runner
BuildRequires : setuptools
BuildRequires : typing

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
Summary: license components for the aiohttp-cors package.
Group: Default

%description license
license components for the aiohttp-cors package.


%package python
Summary: python components for the aiohttp-cors package.
Group: Default
Requires: aiohttp-cors-python3

%description python
python components for the aiohttp-cors package.


%package python3
Summary: python3 components for the aiohttp-cors package.
Group: Default
Requires: python3-core

%description python3
python3 components for the aiohttp-cors package.


%prep
%setup -q -n aiohttp-cors-0.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534857985
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/aiohttp-cors
cp LICENSE %{buildroot}/usr/share/doc/aiohttp-cors/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/aiohttp-cors/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
