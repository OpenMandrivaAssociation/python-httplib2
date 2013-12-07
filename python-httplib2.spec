%define module	httplib2

Summary:	Comprehensive HTTP client library for Python
Name:		python-httplib2
Version:	0.8
Release:	5
Group:		System/Libraries
License:	MIT
Url:		http://code.google.com/p/httplib2
Source0:	http://httplib2.googlecode.com/files/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
%py_requires -d

%description
A comprehensive HTTP client library that supports many features left
out of other HTTP libraries.

%package -n python3-httplib2
Summary:	Python 3 HTTP library module
Group:		System/Libraries
BuildRequires:	python3

%description -n python3-httplib2
A comprehensive HTTP client library that supports many features left
out of other HTTP libraries.

%prep
%setup -q -c
mv httplib2-%{version} python2
pushd python2
%patch0 -p0 -b .certfile
popd
cp -r python2 python3

%build
pushd python2
%{__python} setup.py build
popd

pushd python3
python3 setup.py build
popd

%install
pushd python2
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot} --compile --optimize=2
chmod a+r %{buildroot}%{py_puresitedir}/%{module}*egg-info/*
popd

pushd python3
PYTHONDONTWRITEBYTECODE= python3 setup.py install --root=%{buildroot} --compile --optimize=2
chmod a+r %{buildroot}%{py_puresitedir}/%{module}*egg-info/*
popd

%files
%doc python2/README
%{py_puresitedir}/%{module}-*
%{py_puresitedir}/%{module}/*

%files -n python3-httplib2
%doc python3/README
%{py3_puresitedir}/%{module}-*
%{py3_puresitedir}/%{module}/*

