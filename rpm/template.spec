Name:           ros-melodic-diagnostic-analysis
Version:        1.9.3
Release:        0%{?dist}
Summary:        ROS diagnostic_analysis package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/diagnostics_analysis
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-melodic-diagnostic-msgs
Requires:       ros-melodic-rosbag
Requires:       ros-melodic-roslib
BuildRequires:  ros-melodic-catkin >= 0.5.68
BuildRequires:  ros-melodic-diagnostic-msgs
BuildRequires:  ros-melodic-rosbag
BuildRequires:  ros-melodic-roslib
BuildRequires:  ros-melodic-rostest

%description
The diagnostic_analysis package can convert a log of diagnostics data into a
series of CSV files. Robot logs are recorded with rosbag, and can be processed
offline using the scripts in this package.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed May 02 2018 Austin Hendrix <namniart@gmail.com> - 1.9.3-0
- Autogenerated by Bloom

