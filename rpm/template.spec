Name:           ros-hydro-test-diagnostic-aggregator
Version:        1.8.7
Release:        1%{?dist}
Summary:        ROS test_diagnostic_aggregator package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/test_diagnostic_aggregator
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-diagnostic-aggregator
Requires:       ros-hydro-diagnostic-msgs
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rospy
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-diagnostic-aggregator
BuildRequires:  ros-hydro-diagnostic-msgs
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-rostest

%description
Basic diagnostic_aggregator tests are in the

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Aug 06 2015 Brice Rebsamen <brice.rebsamen@gmail.com> - 1.8.7-1
- Autogenerated by Bloom

* Fri Jan 09 2015 Brice Rebsamen <brice.rebsamen@gmail.com> - 1.8.7-0
- Autogenerated by Bloom

* Wed Dec 10 2014 Brice Rebsamen <brice.rebsamen@gmail.com> - 1.8.6-0
- Autogenerated by Bloom

* Tue Jul 29 2014 Brice Rebsamen <brice.rebsamen@gmail.com> - 1.8.5-0
- Autogenerated by Bloom

* Fri Jul 25 2014 Brice Rebsamen <brice.rebsamen@gmail.com> - 1.8.4-0
- Autogenerated by Bloom

