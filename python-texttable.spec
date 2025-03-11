#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		texttable
%define		egg_name	texttable
%define		pypi_name	texttable
Summary:	Python module to generate a formatted text table, using ASCII characters
Name:		python-%{pypi_name}
Version:	1.2.1
# before STBR, ensure docker-compose is updated:
# pythonegg(texttable) < 0.10 is needed by docker-compose-1.19.0-1.noarch
Release:	8
License:	LGPL v2+
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	7761da214368903c2409c13f1280cffe
URL:		https://pypi.python.org/pypi/texttable/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module to generate a formatted text table, using ASCII
characters

%package -n python3-%{module}
Summary:	Python module to generate a formatted text table, using ASCII characters
Group:		Libraries/Python

%description -n python3-%{module}
Python module to generate a formatted text table, using ASCII
characters

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/%{module}.py[co]
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/__pycache__/%{module}.*.pyc
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
