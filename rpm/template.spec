Name:           ros-indigo-diagnostic-common-diagnostics
Version:        1.8.8
Release:        0%{?dist}
Summary:        ROS diagnostic_common_diagnostics package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/diagnostic_common_diagnostics
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       hddtemp
Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-rospy
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-rospy

%description
diagnostic_common_diagnostics

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Aug 06 2015 Austin Hendrix <namniart@gmail.com> - 1.8.8-0
- Autogenerated by Bloom

* Fri Jan 09 2015 Austin Hendrix <namniart@gmail.com> - 1.8.7-0
- Autogenerated by Bloom

