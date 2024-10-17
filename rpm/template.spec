%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-tiago-bringup
Version:        4.6.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS tiago_bringup package

License:        Apache License 2.0
URL:            https://github.com/pal-robotics/tiago_simulation
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-geometry-msgs
Requires:       ros-humble-joy-linux
Requires:       ros-humble-joy-teleop
Requires:       ros-humble-launch-pal
Requires:       ros-humble-play-motion2
Requires:       ros-humble-teleop-tools-msgs
Requires:       ros-humble-tiago-controller-configuration
Requires:       ros-humble-tiago-description
Requires:       ros-humble-twist-mux
Requires:       ros-humble-twist-mux-msgs
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake-auto
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-ament-lint-common
%endif

%description
Launch files to upload the robot description and start the controllers

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Thu Oct 17 2024 Jordi Pages <jordi.pages@pal-robotics.com> - 4.6.0-1
- Autogenerated by Bloom

* Fri Sep 13 2024 Jordi Pages <jordi.pages@pal-robotics.com> - 4.5.0-1
- Autogenerated by Bloom

* Fri Aug 09 2024 Jordi Pages <jordi.pages@pal-robotics.com> - 4.3.0-1
- Autogenerated by Bloom

* Tue Aug 06 2024 Jordi Pages <jordi.pages@pal-robotics.com> - 4.2.21-1
- Autogenerated by Bloom

* Tue Jul 09 2024 Jordi Pages <jordi.pages@pal-robotics.com> - 4.2.17-1
- Autogenerated by Bloom

* Fri Jun 28 2024 Jordi Pages <jordi.pages@pal-robotics.com> - 4.2.16-1
- Autogenerated by Bloom

* Tue Jun 18 2024 Jordi Pages <jordi.pages@pal-robotics.com> - 4.2.13-1
- Autogenerated by Bloom

* Fri Mar 01 2024 Jordi Pages <jordi.pages@pal-robotics.com> - 4.2.3-1
- Autogenerated by Bloom

* Fri Jan 19 2024 Jordi Pages <jordi.pages@pal-robotics.com> - 4.1.2-1
- Autogenerated by Bloom

* Fri Jan 19 2024 Jordi Pages <jordi.pages@pal-robotics.com> - 4.1.1-1
- Autogenerated by Bloom

* Fri Dec 22 2023 Jordi Pages <jordi.pages@pal-robotics.com> - 4.0.28-1
- Autogenerated by Bloom

* Mon Dec 18 2023 Jordi Pages <jordi.pages@pal-robotics.com> - 4.0.27-1
- Autogenerated by Bloom

* Tue Jul 11 2023 Jordi Pages <jordi.pages@pal-robotics.com> - 4.0.13-1
- Autogenerated by Bloom

* Wed Jul 05 2023 Jordi Pages <jordi.pages@pal-robotics.com> - 4.0.12-1
- Autogenerated by Bloom

* Fri Jun 30 2023 Jordi Pages <jordi.pages@pal-robotics.com> - 4.0.11-1
- Autogenerated by Bloom

* Tue May 02 2023 Jordi Pages <jordi.pages@pal-robotics.com> - 4.0.7-1
- Autogenerated by Bloom

* Mon Apr 17 2023 Jordi Pages <jordi.pages@pal-robotics.com> - 4.0.6-1
- Autogenerated by Bloom

* Mon Mar 13 2023 Jordi Pages <jordi.pages@pal-robotics.com> - 4.0.5-1
- Autogenerated by Bloom

* Wed Mar 01 2023 Jordi Pages <jordi.pages@pal-robotics.com> - 4.0.3-1
- Autogenerated by Bloom

* Wed Feb 08 2023 Jordi Pages <jordi.pages@pal-robotics.com> - 4.0.2-1
- Autogenerated by Bloom

* Thu Nov 10 2022 Jordi Pages <jordi.pages@pal-robotics.com> - 4.0.1-1
- Autogenerated by Bloom

* Tue Nov 08 2022 Jordi Pages <jordi.pages@pal-robotics.com> - 4.0.0-1
- Autogenerated by Bloom

