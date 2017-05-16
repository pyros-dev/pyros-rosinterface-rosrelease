Name:           ros-jade-pyros-interfaces-ros
Version:        0.4.0
Release:        0%{?dist}
Summary:        ROS pyros_interfaces_ros package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-message-runtime >= 0.4.12
Requires:       ros-jade-pyros-common >= 0.4.2
Requires:       ros-jade-pyros-utils >= 0.1.3
Requires:       ros-jade-rospy >= 1.11.19
Requires:       ros-jade-std-msgs >= 0.5.9
BuildRequires:  ros-jade-catkin >= 0.6.18
BuildRequires:  ros-jade-catkin-pip >= 0.1.17
BuildRequires:  ros-jade-message-generation >= 0.2.10
BuildRequires:  ros-jade-pyros-common >= 0.4.2
BuildRequires:  ros-jade-pyros-test >= 0.0.6
BuildRequires:  ros-jade-pyros-utils >= 0.1.3
BuildRequires:  ros-jade-roslint >= 0.10.0
BuildRequires:  ros-jade-rospy >= 1.11.19
BuildRequires:  ros-jade-rostest >= 1.11.19
BuildRequires:  ros-jade-rostopic >= 1.11.19
BuildRequires:  ros-jade-rosunit >= 1.11.12
BuildRequires:  ros-jade-std-msgs >= 0.5.9

%description
Dynamic ROS interface for Pyros

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
* Tue May 16 2017 AlexV <asmodehn@gmail.com> - 0.4.0-0
- Autogenerated by Bloom

