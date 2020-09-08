%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-diagnostic-aggregator
Version:        1.10.2
Release:        3%{?dist}%{?release_suffix}
Summary:        ROS diagnostic_aggregator package

License:        BSD
URL:            http://www.ros.org/wiki/diagnostic_aggregator
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-bondcpp
Requires:       ros-noetic-bondpy
Requires:       ros-noetic-diagnostic-msgs >= 1.11.9
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-rospy
Requires:       ros-noetic-xmlrpcpp
BuildRequires:  ros-noetic-bondcpp
BuildRequires:  ros-noetic-bondpy
BuildRequires:  ros-noetic-catkin >= 0.5.68
BuildRequires:  ros-noetic-diagnostic-msgs >= 1.11.9
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rospy
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-xmlrpcpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
diagnostic_aggregator

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Tue Sep 08 2020 Austin Hendrix <namniart@gmail.com> - 1.10.2-3
- Autogenerated by Bloom

* Tue Aug 11 2020 Austin Hendrix <namniart@gmail.com> - 1.10.0-1
- Autogenerated by Bloom

* Wed Apr 01 2020 Austin Hendrix <namniart@gmail.com> - 1.9.4-1
- Autogenerated by Bloom

