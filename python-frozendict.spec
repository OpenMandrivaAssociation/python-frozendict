Name:		python-frozendict
Version:	2.4.7
Release:	1
Summary:	Immutable dictionary implementation
License:	LGPL-3.0
Group:		Development/Python
URL:		https://github.com/Marco-Sulla/python-frozendict
Source0:	https://files.pythonhosted.org/packages/source/f/frozendict/frozendict-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

# Keep the pure-Python mapping so this stays noarch. The optional C
# accelerator is not worth an arch-specific package for ACE-Step.
%build -p
export FROZENDICT_PURE_PY=1

%description
An immutable mapping type for Python. Used by einx (and thus
vector-quantize-pytorch / ACE-Step).

%files
%doc README.md
%license LICENSE.txt
%{py_sitedir}/frozendict
%{py_sitedir}/frozendict-*.*-info
