Name:           ros-indigo-diagnostic-aggregator
Version:        1.8.6
Release:        0%{?dist}
Summary:        ROS diagnostic_aggregator package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/diagnostic_aggregator
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-xmlrpcpp
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-xmlrpcpp

%description
diagnostic_aggregator

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
* Wed Dec 10 2014 Austin Hendrix <namniart@gmail.com> - 1.8.6-0
- Autogenerated by Bloom

* Tue Jul 29 2014 Austin Hendrix <namniart@gmail.com> - 1.8.5-0
- Autogenerated by Bloom

* Fri Jul 25 2014 Austin Hendrix <namniart@gmail.com> - 1.8.4-0
- Autogenerated by Bloom

