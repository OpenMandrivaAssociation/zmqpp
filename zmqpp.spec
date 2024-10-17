%define name	zmqpp
%define version	4.2.0
%define release 1
%define debug_package          %{nil}

%define libname_orig lib%{name} 
%define major	4
%define libname	%mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Software library for fast, message-based applications
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	https://github.com/zeromq/zmqpp/archive/%{version}/%{name}-%{version}.tar.gz
License:	LGPLv3+
Group:		Development/Other
Url:		https://www.zeromq.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  zeromq-devel
	
%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

%package -n	%{libname}
Summary: 	Software library for fast, message-based applications
Group:		System/Libraries
Provides:	%{libname_orig} = %{version}-%{release}
Obsoletes:	%{name}-utils

%description -n %{libname}
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the ${name} shared library.

%package -n	%{develname}
Summary: 	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}

%description -n %{develname}
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the libraries and header files needed to develop
applications that use %{name}.

%prep
%setup -q 

%build
%make_build PREFIX=/usr 

%install
%__rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}
%make_install PREFIX=/usr LIBDIR=%{buildroot}%{_libdir}

%clean
%__rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc LICENSE README.md
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}
%{_libdir}//libzmqpp.a
%{_libdir}//pkgconfig/libzmqpp.pc

