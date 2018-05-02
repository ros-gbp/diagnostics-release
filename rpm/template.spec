Name:           ros-kinetic-diagnostic-common-diagnostics
Version:        1.9.3
Release:        0%{?dist}
Summary:        ROS diagnostic_common_diagnostics package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/diagnostic_common_diagnostics
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       hddtemp
Requires:       python-psutil
Requires:       ros-kinetic-diagnostic-updater
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-tf
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-diagnostic-updater
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-rostest

%description
diagnostic_common_diagnostics

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed May 02 2018 Austin Hendrix <namniart@gmail.com> - 1.9.3-0
- Autogenerated by Bloom

* Sat Jul 15 2017 Austin Hendrix <namniart@gmail.com> - 1.9.2-0
- Autogenerated by Bloom

* Sat Jul 15 2017 Austin Hendrix <namniart@gmail.com> - 1.9.1-0
- Autogenerated by Bloom

* Tue Apr 25 2017 Austin Hendrix <namniart@gmail.com> - 1.9.0-0
- Autogenerated by Bloom

* Tue Jun 14 2016 Austin Hendrix <namniart@gmail.com> - 1.8.10-0
- Autogenerated by Bloom

* Thu Mar 31 2016 Austin Hendrix <namniart@gmail.com> - 1.8.9-0
- Autogenerated by Bloom

