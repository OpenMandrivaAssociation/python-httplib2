%define module	httplib2

Summary:	Comprehensive HTTP client library for Python
Name:		python-httplib2
Version:	0.9
Release:	1
Group:		System/Libraries
License:	MIT
Url:		https://github.com/jcgregorio/httplib2
Source0:	https://github.com/jcgregorio/httplib2/archive/%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python2-distribute
BuildRequires:	python3-distribute
BuildRequires:  python2-devel
BuildRequires:	python3-devel
%rename python3-httplib2

%description
A comprehensive HTTP client library that supports many features left
out of other HTTP libraries.

%package -n python2-httplib2
Summary:	Python 2 HTTP library module
Group:		System/Libraries
BuildRequires:	python2

%description -n python2-httplib2
A comprehensive HTTP client library that supports many features left
out of other HTTP libraries.

%prep
%setup -q -c
mv httplib2-%{version} python2
pushd python2
popd
cp -r python2 python3

%build
pushd python2
%{__python2} setup.py build
popd

pushd python3
%{__python3} setup.py build
popd

%install
pushd python2
PYTHONDONTWRITEBYTECODE= %{__python2} setup.py install --root=%{buildroot} --compile --optimize=2
chmod a+r %{buildroot}%{py2_puresitedir}/%{module}*egg-info/*
popd

pushd python3
PYTHONDONTWRITEBYTECODE= %{__python3} setup.py install --root=%{buildroot} --compile --optimize=2
chmod a+r %{buildroot}%{py3_puresitedir}/%{module}*egg-info/*
popd

%files
%doc python3/python3/README
%{py3_puresitedir}/%{module}-*
%{py3_puresitedir}/%{module}/*

%files -n python2-httplib2
%doc python2/python3/README
%{py2_puresitedir}/%{module}-*
%{py2_puresitedir}/%{module}/*

