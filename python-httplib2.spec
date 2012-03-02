%define module	httplib2

Name:		python-httplib2
Summary:	Comprehensive HTTP client library for Python
Version:	0.7.3
Release:	1
Source0:	http://httplib2.googlecode.com/files/%{module}-%{version}.tar.gz
URL:		http://code.google.com/p/httplib2
Group:		System/Libraries
License:	MIT
BuildArch:	noarch
BuildRequires:	python-setuptools
%py_requires -d

%description
A comprehensive HTTP client library that supports many features left
out of other HTTP libraries.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot} --record=FILE_LIST

%files -f FILE_LIST
%defattr(-,root,root)
%doc README
