%define module	httplib2

Summary:	Comprehensive HTTP client library for Python
Name:		python-httplib2
Version:	0.22.0
Release:	1
Group:		System/Libraries
License:	MIT
Url:		https://pypi.org/project/httplib2/
Source0:	https://files.pythonhosted.org/packages/source/h/httplib2/httplib2-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python-devel
BuildSystem:	python
%rename python3-httplib2
Obsoletes:	python2-httplib2 < %{EVRD}

%description
A comprehensive HTTP client library that supports many features left
out of other HTTP libraries.

%files
%doc python3/README
%{py3_puresitedir}/%{module}-*
%{py3_puresitedir}/%{module}/*

