Name:           ros-jade-diagnostic-aggregator
Version:        1.9.1
Release:        0%{?dist}
Summary:        ROS diagnostic_aggregator package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/diagnostic_aggregator
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-bondcpp
Requires:       ros-jade-bondpy
Requires:       ros-jade-diagnostic-msgs >= 1.12.4
Requires:       ros-jade-pluginlib
Requires:       ros-jade-roscpp
Requires:       ros-jade-rospy
Requires:       ros-jade-xmlrpcpp
BuildRequires:  ros-jade-bondcpp
BuildRequires:  ros-jade-bondpy
BuildRequires:  ros-jade-catkin >= 0.5.68
BuildRequires:  ros-jade-diagnostic-msgs >= 1.12.4
BuildRequires:  ros-jade-pluginlib
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rospy
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-xmlrpcpp

%description
diagnostic_aggregator

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sat Jul 15 2017 Austin Hendrix <namniart@gmail.com> - 1.9.1-0
- Autogenerated by Bloom

* Tue Apr 25 2017 Austin Hendrix <namniart@gmail.com> - 1.9.0-0
- Autogenerated by Bloom

* Tue Jun 14 2016 Austin Hendrix <namniart@gmail.com> - 1.8.10-0
- Autogenerated by Bloom

* Wed Mar 02 2016 Austin Hendrix <namniart@gmail.com> - 1.8.9-1
- Autogenerated by Bloom

* Wed Mar 02 2016 Austin Hendrix <namniart@gmail.com> - 1.8.9-0
- Autogenerated by Bloom

* Thu Feb 12 2015 Austin Hendrix <namniart@gmail.com> - 1.8.7-0
- Autogenerated by Bloom

