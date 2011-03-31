%define livearches %{ix86} x86_64 ppc ppc64

Summary: Graphical system installer
Name:    anaconda
Version: 16.4
Release: 1%{?dist}
License: GPLv2+
Group:   Applications/System
URL:     http://fedoraproject.org/wiki/Anaconda

%define debug_package %{nil}

# To generate Source0 do:
# git clone http://git.fedorahosted.org/git/anaconda.git
# git checkout -b archive-branch anaconda-%{version}-%{release}
# ./autogen.sh
# make dist
Source0: %{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).
%define dmver 1.02.17-6
%define gettextver 0.11
%define genisoimagever 1.1.9-4
%define gconfversion 2.28.1
%define intltoolver 0.31.2-3
%define libnlver 1.0
%define libselinuxver 1.6
%define pykickstartver 1.81
%define rpmpythonver 4.2-0.61
%define slangver 2.0.6-2
%define yumver 2.9.2
%define partedver 1.8.1
%define pypartedver 2.5-2
%define syscfgdatever 1.9.48
%define pythonpyblockver 0.45
%define e2fsver 1.41.0
%define nmver 1:0.7.1-3.git20090414
%define dbusver 1.2.3
%define createrepover 0.4.7
%define yumutilsver 1.1.11-3
%define iscsiver 6.2.0.870-3
%define pythoncryptsetupver 0.0.6
%define mehver 0.8
%define sckeyboardver 1.3.1
%define libblkidver 2.17.1-1
%define fcoeutilsver 1.0.12-3.20100323git
%define isomd5sumver 1.0.6

BuildRequires: audit-libs-devel
BuildRequires: bzip2-devel
BuildRequires: device-mapper-devel >= %{dmver}
BuildRequires: e2fsprogs-devel >= %{e2fsver}
BuildRequires: elfutils-devel
BuildRequires: gettext >= %{gettextver}
BuildRequires: gtk2-devel
BuildRequires: intltool >= %{intltoolver}
BuildRequires: isomd5sum-static >= %{isomd5sumver}
BuildRequires: libarchive-devel
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: libXxf86misc-devel
BuildRequires: libblkid-devel >= %{libblkidver}
BuildRequires: libcurl-devel
BuildRequires: libnl-devel >= %{libnlver}
BuildRequires: libselinux-devel >= %{libselinuxver}
BuildRequires: libsepol-devel
BuildRequires: libxml2-python
BuildRequires: newt-devel
BuildRequires: pango-devel
BuildRequires: pykickstart >= %{pykickstartver}
BuildRequires: python-devel
BuildRequires: python-pyblock >= %{pythonpyblockver}
BuildRequires: python-urlgrabber >= 3.9.1-5
BuildRequires: python-nose
BuildRequires: rpm-devel
BuildRequires: rpm-python >= %{rpmpythonver}
BuildRequires: slang-devel >= %{slangver}
BuildRequires: xmlto
BuildRequires: yum >= %{yumver}
BuildRequires: zlib-devel
BuildRequires: NetworkManager-devel >= %{nmver}
BuildRequires: NetworkManager-glib-devel >= %{nmver}
BuildRequires: dbus-devel >= %{dbusver}, dbus-python
BuildRequires: system-config-keyboard >= %{sckeyboardver}
%ifarch %livearches
BuildRequires: desktop-file-utils
%endif
BuildRequires: iscsi-initiator-utils-devel >= %{iscsiver}
%ifarch s390 s390x
BuildRequires: s390utils-devel
%endif

Requires: python-meh >= %{mehver}
Requires: policycoreutils
Requires: rpm-python >= %{rpmpythonver}
Requires: comps-extras
Requires: parted >= %{partedver}
Requires: pyparted >= %{pypartedver}
Requires: yum >= %{yumver}
Requires: libxml2-python
Requires: python-urlgrabber >= 3.9.1-5
Requires: system-logos
Requires: pykickstart >= %{pykickstartver}
Requires: system-config-date >= %{syscfgdatever}
Requires: device-mapper >= %{dmver}
Requires: device-mapper-libs >= %{dmver}
Requires: dosfstools
Requires: e2fsprogs >= %{e2fsver}
Requires: gzip
Requires: libarchive
%ifarch %{ix86} x86_64 ia64
Requires: dmidecode
%endif
Requires: python-pyblock >= %{pythonpyblockver}
Requires: libuser-python
Requires: newt-python
Requires: authconfig
Requires: system-config-firewall-base
Requires: cryptsetup-luks
Requires: python-cryptsetup >= %{pythoncryptsetupver}
Requires: mdadm
Requires: lvm2
Requires: util-linux-ng >= 2.15.1
Requires: system-config-keyboard >= %{sckeyboardver}
Requires: dbus-python
Requires: cracklib-python
Requires: python-bugzilla
Requires: python-nss
Requires: tigervnc-server-minimal
%ifarch %livearches
Requires: usermode
Requires: zenity
%endif
Requires: createrepo >= %{createrepover}
Requires: squashfs-tools
Requires: genisoimage >= %{genisoimagever}
Requires: GConf2 >= %{gconfversion}
%ifarch %{ix86} x86_64
Requires: syslinux >= 3.73
Requires: makebootfat
Requires: device-mapper
%endif
%ifarch s390 s390x
Requires: openssh
%endif
Requires: isomd5sum
Requires: yum-utils >= %{yumutilsver}
Requires: NetworkManager >= %{nmver}
Requires: dhclient
Requires: anaconda-yum-plugins
Requires: libselinux-python >= %{libselinuxver}
Requires: fcoe-utils >= %{fcoeutilsver}
%ifarch %{sparc}
Requires: elftoaout piggyback
%endif
Obsoletes: anaconda-images <= 10
Provides: anaconda-images = %{version}-%{release}
Obsoletes: anaconda-runtime < %{version}-%{release}
Provides: anaconda-runtime = %{version}-%{release}
Obsoletes: booty

%description
The anaconda package contains the program which was used to install your
system.

%prep
%setup -q

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
find %{buildroot} -type f -name "*.la" | xargs %{__rm}

%ifarch %livearches
desktop-file-install --vendor="" --dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/liveinst.desktop
%else
%{__rm} -rf %{buildroot}%{_bindir}/liveinst %{buildroot}%{_sbindir}/liveinst
%endif

%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%ifarch %livearches
%post
update-desktop-database &> /dev/null || :
%endif

%ifarch %livearches
%postun
update-desktop-database &> /dev/null || :
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING
%doc docs/command-line.txt
%doc docs/install-methods.txt
%doc docs/mediacheck.txt
%doc docs/anaconda-release-notes.txt
/lib/udev/rules.d/70-anaconda.rules
%{_sbindir}/anaconda
%{_sbindir}/logpicker
%ifarch i386 i486 i586 i686 x86_64
%{_sbindir}/gptsync
%{_sbindir}/showpart
%endif
%{_datadir}/anaconda
%{_prefix}/libexec/anaconda
%{_libdir}/python*/site-packages/pyanaconda/*
%{_libdir}/python*/site-packages/log_picker/*
%{_libdir}/anaconda*
%{_bindir}/analog
%{_bindir}/anaconda-cleanup
%ifarch %livearches
%{_bindir}/liveinst
%{_sbindir}/liveinst
%config(noreplace) %{_sysconfdir}/pam.d/*
%config(noreplace) %{_sysconfdir}/security/console.apps/*
%{_sysconfdir}/X11/xinit/xinitrc.d/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*
%endif

%changelog
* Thu Mar 31 2011 Chris Lumens <clumens@redhat.com> - 16.4-1
- Fix a syntax error from the previous translation commit. (clumens)
- crypttab should not be world-readable (#692254). (clumens)
- Improve the translatability of strings with more than one format specifier.
  (clumens)
- Stop user if we have no /boot and / is an LV (dcantrell)
- Prevent singlePV lv requests from being > the size of any pv (dcantrell)
- Do not print out traceback when localedef is not present (msivak)
- Update our storage/crypto interface to use new cryptsetup API (msivak)
- Fix the logic surrounding use of the filterfunc for get_file_list (#691880).
  (clumens)
- mount needs to be told "nfs" or it assumes any argument is a device
  (#678414). (clumens)
- Fix rebooting after a kickstart error is detected. (akozumpl)

* Mon Mar 28 2011 Chris Lumens <clumens@redhat.com> - 16.3-1
- Use a more general EnvironmentError to catch timezone-file errors. (akozumpl)
- Add shell command to upd-bootiso (bcl)
- Set debug_package to %{nil} so we don't strip our binaries. (pjones)
- Return values, not strings (bcl)
- Use proper store types for DataComboBoxes. (akozumpl)
- Fixup rindex usage (#678086) (bcl)
- Ensure new kernel is default in zipl.conf on upgrade installs (#683891)
  (dcantrell)
- shutdown: kill processes in the anaconda process group. (akozumpl)
- After 17233a16, vncS is no longer a global. (akozumpl)
- shutdown.c: pidof and killall5 are in /sbin on rawhide. (akozumpl)
- Check size limits on pre-existing partitions (bcl)
- gui.py: nuke createRepoWindow() (akozumpl)
- gui.py: nuke titleBar*() (akozumpl)
- Fix --mtu option to kickstart network command (#689081) (icomfort)
- Implement a general version of InstallInterfaceBase.methodstrRepoWindow().
  (akozumpl)
- Update icons and add a new 256x256 version (#689014). (clumens)
- Fix the filesystem migration dialog in text mode (#688314). (clumens)
- Don't fatal_error if required mounts are already mounted (wwoods)
- Don't fatal_error if remounting root read-write fails (wwoods)
- Align lv sizes when adding to vg total space used. (dlehman)
- Clean up display of free space in partitioning gui. (dlehman)
- Fix a syntax error in my last upgrade-related commit. (clumens)
- Remove some more xutils-related code. (clumens)
- Prevent Platform from importing storage stuff until it's necessary. (clumens)
- Restore stats from original mount on livecd (#683682) (bcl)
- Properly filter out new mounts for livecd install (#683682) (bcl)
- Mount livecd filesystems under /mnt (#683682) (bcl)
- Fix order of opts and host when processing kickstart nfs lines. (clumens)
- Rework the upgrade swap suggestion (#684603). (clumens)
- Log running version number as soon as possible (bcl)
- Collect LUKS passphrases to avoid making users enter them repeatedly.
  (dlehman)
- Don't include incomplete md arrays in the devicetree. (dlehman)
- Detect live environment if no args passed to anaconda-cleanup. (dlehman)

* Mon Mar 14 2011 Chris Lumens <clumens@redhat.com> - 16.2-1
- iscsi: use the --target parameter from the iscsi kickstart command.
  (akozumpl)
- Make the "comps" translation domain dynamic. (akozumpl)
- Add a missing include to fix the build. (clumens)
- Remove the last of the xutils module. (clumens)
- Fix a missing exception variable. (akozumpl)
- Add cmdline options and f15 support to upd-bootiso (bcl)
- Use yum's new callback mode when available (pmatilai)
- Pressing enter on the keyboard screen should go to the next screen (#683448).
  (clumens)
- Do not allow use of preexisting root filesystem. (#629311) (dlehman)
- Stop using --update=super-minor when starting md arrays. (dlehman)
- Fix kickstart handling of md spares. (#683605) (dlehman)
- Fix sensitivity of options in text network config UI (#681580) (jlaska)
- Consolidate ip address checking into functions. (rvykydal)
- Add support for ipv6 to gateway boot option (#677609) (rvykydal)
- Fix parsing of ipv6 --gateway in kickstart (#677609) (rvykydal)
- Remove 'Back' button on depsolving exception for ks installs (#673170)
  (dcantrell)
- Shorten the anaconda repo names (#679434). (clumens)
- fix mnemonics in the 'Add Repository' dialog (akozumpl)
- Create the virtio-ports on time. (akozumpl)
- Do not pass --sshd to stage2. (akozumpl)
- Handle boot loader upgrades on s390 (#682783) (dcantrell)
- Don't assume BOOTIF present for ksdevice=bootif. (rvykydal)
- syntax errors correcting (vpodzime)
- Apply one more fix for "logvol --label=" (#673584) (clumens)
- Fix test for resized LV to ensure we schedule the format resize action.
  (dlehman)
- Make sure a bootloader device is selected (#595951) (bcl)
- Another fix for the loader translations. (akozumpl)
- /var/log/dmesg doesn't exist in a live install. messages does, though.
  (dlehman)
- Don't try to unlink a config file that isn't there. (dlehman)
- Handle md name-mangling based on hostname/homehost WRT exclusiveDisks.
  (dlehman)
- Adjust DeviceTree.isIgnored's handling of loop, ram, and live devices.
  (dlehman)
- Allow scanning of already-active md devices. (#680226) (dlehman)
- Don't clobber exclusiveDisks unless there are disk images. (dlehman)
- Do on-demand scanning of md container if needed. (#678877) (dlehman)
- Fix md array spares test. (dlehman)
- Fix udev_device_is_md. (dlehman)
- Add /var/lib/yum to the list of directories we set context on (#681494).
  (clumens)
- Pass createUser and createGroup an arguments dict. (clumens)
- Check all PV ancestor devices for growable partitions. (dlehman)
- Enable network if sshd boot option is used (#643738) (rvykydal)
- Fix setting of loaderData->method from repo= cmdline option. (rvykydal)
- Gotta catch 'em all parted exceptions. (akozumpl)
- Give an indication how many packages are left in cmdline mode (#681614).
  (clumens)
- Dynamic strings make gettext translations fail. (akozumpl)
- devt.h is no longer useful, remove it. (clumens)
- Remove 'Back' button on depsolving exception for ks installs (#673170)
  (dcantrell)
- Ensure remount requests go through isys.mount() (#678520) (dcantrell)
- Check repo instead of method type when enabling network in loader (#673824)
  (rvykydal)
- Fix setting of some network values in loader kickstart (#679825). (rvykydal)
- Loader should activate, stage 2 configure network devices. (rvykydal)
- Do not activate first ks network device automatically in non-network
  installs. (rvykydal)
- Always activate first kickstart network device (rvykydal)
- Make kickstart network command reconfigure active device in loader (rvykydal)
- Use NM for ibft configuration (rvykydal)
- Reset only ifcfg file of device we failed to activate (rvykydal)
- Initialize iface structure properly (rvykydal)
- Add kickstart network --nodefroute option (rvykydal)
- Add support for ks network --bootproto=ibft (rvykydal)
- Wait for activation of specific devices instead of NM (rvykydal)
- Parse all kickstart network commands in loader too (rvykydal)
- Activate all devices set by kickstart network --activate command (rvykydal)
- Parse new kickstart options network --activate and --nodefroute. (rvykydal)
- Fixup upgrade test for findExistingRoots change (#681267) (bcl)
- Change upgrade to use findExistingRootDevices (#681267) (bcl)
- Initialize locale before the kickstart/virtio check (#679702) (msivak)

* Tue Mar 01 2011 Chris Lumens <clumens@redhat.com> - 16.1-1
- Fix another unused return value error message. (clumens)

* Tue Mar 01 2011 Chris Lumens <clumens@redhat.com> - 16.0-1
- Pass correct class to super in SELinuxFS.mountable. (#677450) (dlehman)
- Clarify that loader method entries are looking for a tree. (clumens)
- Fix up remaining anaconda.id references (#680296) (bcl)
- Wipe out pre-existing problems before running transaction (#678201, pmatilai). (clumens)
- Attempt at fixing reboot behavior in kickstart (#676968). (clumens)
- brcm_iscsiuio is not in Fedora yet, handle that you can't find it. (akozumpl)
- Fix downloading .treeinfo files for --noverifyssl repos. (akozumpl)
- Fix syntax error from 0bf0cf13. (akozumpl)
- Pass --force when calling vgreduce --removemissing. (#679206) (dlehman)
- Only apply global passphrase to devices with no passphrase. (#679223) (dlehman)
- Perform terminations before unmounting filesystems on shutdown. (dlehman)
- Get size + summary from yum package object instead of callback key (pmatilai)
- Test for stringiness instead of explicit rpm.hdr class in install callback (pmatilai)
- Remove unused doneFiles counting from transaction callback (pmatilai)
- Handle nfsiso in promptForNfs as well (#678413). (clumens)
- If the umount in getFileFromNfs fails, log it. (clumens)
- Correct the return values of some backend base class methods. (#679107) (dlehman)
- Change xhost auth when doing a liveinst (#663294) (bcl)
- Override kernel cmdline updates (bcl)
- Write --noverifyssl to repos and urls in kickstart where fit. (akozumpl)
- Do all dm handling inside addUdevDMDevice. (#672030) (dlehman)
- Remove storage/miscutils.py, it is not used. (akozumpl)
- Be better at handling killed metacity. (akozumpl)
- Remove Dispatcher.firstStep. (akozumpl)
- remove InstallerControllerWindow.setup_theme() (akozumpl)
- Make the dispatcher call the shots. (akozumpl)
- icw._doExit is now icw.close() (akozumpl)
- remove trailing whitespace from gui.py and installclass.py (akozumpl)
- gui: remove ics.setScreenNext() and ics.getScreenNext(). (akozumpl)
- Clean up vg name generator and default to "vg_image" in image installs. (dlehman)
- Fix calculation of md array spare count. (dlehman)
- createSuggestedVGName takes a hostname, not a Network instance. (dlehman)
- Show correct device path in PV create progress window. (dlehman)
- VNC does not support runtime SecurityTypes changes (#678150) (mgracik)
- Support cciss devices in get_sysfs_path_by_name(). (akozumpl)
- Don't clear partition 1 from mac disks even if it has no name. (#674105) (dlehman)
- Handle quotes around labels and UUIDs in /etc/fstab. (#670496) (dlehman)
- Clean up a bunch of exception handling code. (dlehman)
- Don't show loaderSegvHandler or its glibc entry point in tracebacks. (pjones)
- The default kickstart UI is graphical, specify other if you want it (#678095). (clumens)
- Only check for the addons of enabled repos (#677773). (clumens)
- Fix build - add Makefiles for new unittests to configure.ac (wwoods)
- Fix a thinko when setting up the base repo for NFSISO (#676821). (clumens)
- Take out the part about anaconda being of little use (#677522). (clumens)
- Fix loading translations in loader (#677648). (clumens)
- Don't always attempt to load updates on kickstart installs (#677131). (clumens)
- s390x has firstboot now (dcantrell)
- Don't fail on missing %includes during loader kickstart processing (#676940). (clumens)
- Prompt for media check on DVD installs (#676551). (clumens)
- Tighten the focus of the dogtail and X try/except blocks. (dlehman)
- Stop overriding ext[234] filesystem defaults. (dlehman)
- Make Storage function in the absence of an Anaconda instance. (dlehman)
- Fix DeviceTree to function in the absence of an InstallInterface. (dlehman)
- Remove some udev hackery that was only needed for two-stage env. (dlehman)
- Move large anaconda.__main__ tasks into functions. (dlehman)
- Generate locale files on request (msivak)
- Fix up tests for changes in split media handling (wwoods)
- Update unit testing targets in Makefile.am (tmlcoch)
- Add new tests from the unittests branch (tmlcoch)
- Fix open method in mock/disk.py. (tmlcoch)
- Improve of mock/disk.py. (tmlcoch)
- Remove the old suite() crud from kickstart testing, python-nose work differenlty (msivak)
- Tag tests as slow or acceptance tests and split full testing from devel unit testing (msivak)
- Mock _isys and block modules in fw test. They are not needed. (msivak)
- In text mode we have to treat strings and lists separately while printing them (#676942) (msivak)
- Fix some whitespace errors in iscsi kickstart code. (pjones)

* Thu Feb 10 2011 Chris Lumens <clumens@redhat.com> - 15.20-1
- Check for valid mountpoint before unmounting image. (#671922) (dlehman)
- Fix mis-management of luks dict when renaming encrypted lvs. (dlehman)
- Don't raise NotImplementedError from  non-essential backend methods.
  (dlehman)
- Remove upgrade.findExistingRoots since it does nothing. (dlehman)
- tui: add reinitializeWindow() to the text interface. (akozumpl)
- typo: missing dot in the reinitialization dialog glade file. (akozumpl)
- gui: remove an unneeded parameter from questionInitializeDisk() (akozumpl)
- Remove quotes from udisks command in liveinst (#672022) (bcl)
- Fix iutil import in bootloader config screen (#676032). (clumens)

* Mon Feb 07 2011 Chris Lumens <clumens@redhat.com> - 15.19-1
- Fix a typo. (clumens)
- Don't write our own udev persistent net rules; use udev's generator.
  (notting)
- Add upd-bootiso script (bcl)
- Fix typo in GPT warning (#675242) (bcl)
- remove unused variables (mschmidt)
- Fix support for "logvol --label=" (#673584). (clumens)
- Fix the taint flag check. (clumens)
- Set default resolution of anaconda.glade to 800x600 (dcantrell)
- Make singlePV a more useful boolean, clean up _getSinglePV() (dcantrell)
- Remove width and height parameters from gui.readImageFromFile() (dcantrell)
- Sort singlePV=True requests so they come first. (dcantrell)
- Move reipl step to be after instbootloader step. (dcantrell)
- Remove 'Change device' button from bootloader screen on EFI systems (#582143)
  (wwoods)
- Add anaconda --version support (#673150). (clumens)
- Remove forced 800x600 geometry switch for Xvnc (dcantrell)
- writeMtab -> makeMtab (#673158). (clumens)
- Let dm_node_from_name admit it's defeated. (akozumpl)
- Disable partition resize support for DASD labels (#605912) (dcantrell)

* Tue Jan 25 2011 Chris Lumens <clumens@redhat.com> - 15.18-1
- GCC seriously needs to be less picky. (clumens)

* Tue Jan 25 2011 Chris Lumens <clumens@redhat.com> - 15.17-1
- Don't call preprocessKickstart from within anaconda as well. (clumens)
- We don't need the command names anymore. (clumens)
- Convert kickstart functions to use Python. (clumens)
- Move all kickstart functions into kickstart.c. (clumens)
- Get rid of the kickstart command codes, and alphabetize the command table.
  (clumens)
- Add the flags required to link against python. (clumens)
- Remove ksReadCommands, convert to using pykickstart for parsing. (clumens)
- Add functions to support interfacing loader with pykickstart. (clumens)
- Fix syntax error from fdd06a4053e2965bdc1719425b6d99fe80ab1e18. (akozumpl)
- Only remove /tmp/updates and /tmp/updates.img if they exist. (clumens)
- YumBackend doesn't inherit from YumBase. AnacondaYum does. (#671577)
  (dlehman)
- After copying live rootfs to root device, grow it to fill the device.
  (dlehman)
- Make sure /boot is mapped to a single LVM PV on s390x (dcantrell)
- Unmount filesystems before shutdown or reboot on s390x (#605577) (dcantrell)
- And update to the latest version of the RAID command. (clumens)
- Make the advanced storage dialogs stay in the foreground. (akozumpl)

* Thu Jan 20 2011 Chris Lumens <clumens@redhat.com> - 15.16-1
- Support passing updates= to liveinst via the boot command line. (clumens)
- Make lighter-weight versions of dm map name/node resolution functions.
  (dlehman)
- Make /etc/mtab a symlink to /proc/self/mounts. (#670381) (dlehman)
- Require the pykickstart version with "raid --label=" support. (clumens)
- No longer run hal-lock on live installs (#670312). (clumens)
- Add support for "raid --label=" (#670643). (clumens)
- self.storage -> storage in kickstart execute methods. (clumens)
- Don't prompt on broken lvm or uninitialized disks in cleanup mode. (dlehman)

* Wed Jan 19 2011 Chris Lumens <clumens@redhat.com> - 15.15-1
- Fix booty error on s390 when /boot is not on LVM. (dcantrell)
- Don't offer minors of ignored md devices when creating new md devices.
  (dlehman)
- Make sure devices ignored by the devicetree are in _ignoredDisks. (dlehman)
- Don't try to add spares to active md arrays. (#652874) (dlehman)
- Fix the traceback from c6228535b26a63b0544f4a558a69076581b2a69f. (akozumpl)
- Those missing mnemonicks will not stand. (akozumpl)
- Provide a new mpath devicelib interface that does not reorder the devices.
  (akozumpl)
- Enable support for static ipv6= cmdline option. (rvykydal)
- mpath: create /etc/multipath/bindings file. (akozumpl)
- Fix DMLinearDevice._postSetup to not take or pass an 'orig' arg. (dlehman)
- There's no more MainframeDiskDevice, so don't call its __str__. (clumens)
- We have to pass a blank argument list to execWithCapture. (clumens)
- We have to mount /boot/efi when we find an old one. (pjones)
- Only allow one EFI System Partition to exist at a time. (pjones)
- Conditionalize use of UEFI on boot.iso (pjones)
- Check fstab entries against fmt.mountType not fmt.type (pjones)
- Fix nfsiso install with options (#667839) (mgracik)
- Split out common code from device setup/teardown/create/destroy for reuse.
  (dlehman)
- Remove createParents methods. They don't do anything. (dlehman)
- Add status/progress ui abstraction to device classes. (dlehman)
- Remove unused code related to device probe methods. (dlehman)
- Suddenly, we need gnome-themes-standard. (akozumpl)
- Bold the warning for GPT on non-EFI (#614585) (bcl)
- Warn the user when using a GPT bootdisk on non-EFI systems (#614585) (bcl)
- Support /boot on logical volume on s390x (#618376) (dcantrell)
- Update example ssh command in linuxrc.s390 (dcantrell)
- Start rsyslogd from linuxrc.s390 (#601337) (dcantrell)
- Update spinbutton value in dialogs (#621490) (bcl)
- Convert livecd.py to use the storage module where appropriate. (dlehman)
- Don't try to teardown the live device or associated loop devices. (dlehman)
- Add flag indicating whether a device can be activated/deactivated. (dlehman)
- Include the livecd OS image devices in the device tree. (dlehman)
- Include file-backed loop devices in the device tree. (dlehman)
- Use sysfs instead of losetup to find loop devs' backing files. (dlehman)
- Clean up and close yum/rpm files once we're done with them. (dlehman)
- logging: log_method_return() for devicetree.getDeviceByName() (akozumpl)
- logging: get rid of storage_log.py (akozumpl)
- mpath: filter out the slave devices and their partitions. (akozumpl)
- mpath: use both 'multipath -d' and 'multipath -ll' to get the topology.
  (akozumpl)
- mpath: remove a harmful udev_trigger() in filter_gui (akozumpl)
- Support enabling repos listed but disabled in /etc/yum.repos.d (#663992).
  (clumens)
- Add /sbin to the $PATH for the shell on tty2. (clumens)
- Make sure to set a self.anaconda reference on data objects too. (clumens)

* Thu Jan 06 2011 Chris Lumens <clumens@redhat.com> - 15.14-1
- Adjust main window size based on install type (#667566) (bcl)
- Remove mknod-stub.  We have the full one around now. (clumens)
- Use a different method to get the sysfs_path for device-mapper devices
  (#665643). (clumens)
- Allow existing /var/log (bcl)

* Wed Dec 22 2010 Chris Lumens <clumens@redhat.com> - 15.13-1
- Fix a syntax error in f16a565aa3a879a94862f4c3e5b2ede792ed05ef. (clumens)
- Pass --noeject to anaconda (#477887) (bcl)

* Wed Dec 22 2010 Chris Lumens <clumens@redhat.com> - 15.12-1
- Use cio_ignore and *_cio_free commands in linuxrc.s390 (#633469) (dcantrell)
- Add /sbin/cio_ignore to the KEEPFILE list on s390x (dcantrell)
- Remove MainframeDiskDevice class, use description property. (dcantrell)
- Focus the dialog after a message window is closed (mgracik)
- Change the device reinitialization dialog (mgracik)
- Rename anaconda-image-cleanup and use it for all cleanup in liveinst.
  (dlehman)
- Add handling for cleanup of luks devices with unexpected map names. (dlehman)
- Add ability to clean up prior to live install. (dlehman)
- Fix looking up storage device IDs when writing out anaconda-ks.cfg (#591713).
  (clumens)
- Don't write out a duplicate mtab to /mnt/sysimage (#568539). (clumens)
- Raise an exception if X*Display functions fail (#663294). (clumens)
- mpath: make sure /var/log exists exists early. (akozumpl)
- mpath: log the /etc/multipath.conf contents (akozumpl)

* Tue Dec 14 2010 Chris Lumens <clumens@redhat.com> - 15.11-1
- Don't crash if losetup doesn't know anything about a device. (#662513)
  (dlehman)
- Set up disk images earlier so kickstart device filtering works on them.
  (dlehman)
- Don't try to parse network device info when doing disk image installs.
  (dlehman)
- Fix DeviceTree cleanup w/ inactive luks devs in cmdline mode. (dlehman)
- Add losetup to the install image, re-remove it from isys (#662183). (clumens)
- "anaconda" -> "self.anaconda" in kickstart execute methods. (clumens)
- Override the BaseHandler.dispatcher method. (clumens)
- Use chreipl to set the IPL device on s390x (#632325) (dcantrell)
- Add /usr/sbin/chreipl to KEEPFILE. (dcantrell)
- Create a MainframeDiskDevice class for common s390 attributes. (dcantrell)
- Do not shut down zFCP storage in Storage.shutdown() (#612626) (dcantrell)
- Clarify the ssh modes for installation on s390x (#621590). (dcantrell)
- devicelibs/mpath.py: do not rely on other modules to import logging.
  (akozumpl)
- filter_gui: device discovery configuration is under anaconda.storage.config.
  (akozumpl)

* Wed Dec 08 2010 Chris Lumens <clumens@redhat.com> - 15.10-1
- Fix the build. (clumens)

* Wed Dec 08 2010 Chris Lumens <clumens@redhat.com> - 15.9-1
- Set installer environment hostname for sw raid LABELs (#640743) (rvykydal)
- Device destroy actions can only require other destroy actions. (#651589)
  (dlehman)
- Use wipefs from util-linux-ng instead of dd to wipe old sigs. (dlehman)
- Add cleanup-only mode to DeviceTree.populate. (dlehman)
- Add unit tests for storage.partitioning.getNextPartitionType. (dlehman)
- Only try logging to tty3 if we have permission to do so. (dlehman)
- Enable network when getting .treeinfo (#632526) (rvykydal)
- Fix default of network --device option to match rhel5 (#647462). (rvykydal)
- Do not backtrace if repo is specified through kickstart only (#659781).
  (akozumpl)
- Restore list-harddrives output to what users expect (#654436) (dcantrell)
- Permit ext4 and ext2 for /boot on s390x (#638734) (dcantrell)
- Check for ARPHRD_ETHER and ARPHRD_SLIP types in getDevices (#596826)
  (dcantrell)
- Preserve and otherwise ignore noauto fstab entries. (#660017) (dlehman)
- Fix "logvol --percent=" (#651445, jruemker). (clumens)
- Add chroot command to bash_history. (pjones)
- support for partial offload in udev_*_iscsi() functions. (akozumpl)
- iscsi: partial offload drivers. (akozumpl)
- analog: put it under /usr/bin so it's on the path in an installed system.
  (akozumpl)
- Remove commented out broken code from LoopDevice.status. (dlehman)
- Don't traceback when the action list is empty. (#657891) (dlehman)
- Remove unused udev_device_is_{multipath,dmraid}_partition functions.
  (dlehman)
- Set dm-uuid for anaconda disk image devices from devicetree. (dlehman)
- Remove some unnecessarily hard-coded "/dev/mapper" strings. (dlehman)
- Put the backend logger's config file in /tmp. (dlehman)
- Move handling of /proc/bus/usb and /selinux into storage. (dlehman)
- swapoff -a is only needed for livecd, so only do it for livecd. (dlehman)
- Unlink backend logger config file when stopping logger. (dlehman)
- Make FileDevice.path more consistent. (dlehman)
- Add support for detecting already-active lvm. (dlehman)
- Fix addUdevDevice so we can actually handle already-in-tree devices.
  (dlehman)
- Make it possible to ignore md-fwraid member disks. (dlehman)
- Revert rpmdb symlink hack. (dlehman)
- Remove some unused code from storage.devicelibs.dm. (dlehman)
- Add support for installing onto block device image files. (dlehman)
- Generalize some of the device-mapper partition handling. (dlehman)
- Add support for loop devices. (dlehman)
- Add support for linear device-mapper devices. (dlehman)
- Fix PartitionDevice.path to work with device-mapper disks. (dlehman)
- There's no need to pass exclusiveDisks to doPartitioning separately.
  (dlehman)
- Move storage device scanning parameters into a separate class. (dlehman)
- Don't ignore %packages if --default is given (#621349, dcantrell). (clumens)
- Don't traceback when displaying %post error messages (#654074). (clumens)
- Display a warning message on TAINT_HARDWARE_UNSUPPORTED (#623140). (clumens)
- If getting .treeinfo fails, try treeinfo (#635065). (clumens)
- instPath -> rootPath (clumens)
- Add rdate, tty, which to install image (mgracik)
- Don't add --enablefingerprint unless fprintd-pam is installed (#656434).
  (clumens)

* Tue Nov 30 2010 Chris Lumens <clumens@redhat.com> - 15.8-1
- Ignore immutable disks in clearPartitions (#657115) (bcl)
- Add biosdevname to installer environment (Matt_Domsch)
- Add ntpdate to install.img (#614399) (mgracik)
- It's /usr/bin/gdbserver. (akozumpl)
- Handle dm-N devices pointed to by /dev/disk/ paths (#605312) (bcl)
- Resolve /dev/disk/ devices during rescue (#605312) (bcl)
- Do not auto-check all drives when creating a RAID partition (#641910).
  (akozumpl)
- (Un)select all button in Partition Editor. (akozumpl)
- Show the total amount of space used by snapshots in the VG editor dialog.
  (dlehman)
- Add support for detecting lvm vorigin snapshot volumes. (#633038) (dlehman)
- Don't display free space at end of extended unless > 1MB. (#626025) (dlehman)
- Set SELinux context on /etc/localtime (#653867). (clumens)
- Get a little more output from the unittest runner. (clumens)
- Remove writeRpmPlatform, adjust callers. (#651132, #650490) (notting)
- Import as "pyanaconda.anaconda_log", not "anaconda_log". (clumens)
- A little too much got deleted from imount.c. (clumens)
- Remove the popping portion of kickstart %pre script notification. (clumens)
- Add pyanaconda/.libs to the PYTHONPATH for pylint. (clumens)
- Ignore several false positives and import errors while running pylint.
  (clumens)
- Remove the parts required to make "make tests" work. (clumens)
- nosetests will only run tests if they are not executable and end in _test.py.
  (clumens)
- Set up the PYTHONPATH for running nosetests. (clumens)
- tsort_dict -> tsort in the test case. (clumens)
- Return mount's actual error codes instead of obfuscating them. (dlehman)
- Remove log message saying we don't know how to sanity check storage.
  (dlehman)
- Move check for ext2 filesystem journal from FS to Ext2FS. (dlehman)
- Remove mkdirChain() from isys, use g_mkdir_with_parents() (dcantrell)
- Do not force -O2 in CFLAGS. (dcantrell)
- Remove unused unpackCpioBall() function. (dcantrell)
- Use unpack_archive_file() instead of unpackCpioBall() (dcantrell)
- Use libarchive helper functions in explodeRPM() (dcantrell)
- Add libarchive helper functions for loader in unpack.c (dcantrell)
- Remove include lines for stubs.h from isys. (dcantrell)
- Remove isys cpio extraction code. (dcantrell)

* Tue Nov 09 2010 Chris Lumens <clumens@redhat.com> - 15.7-1
- Unset bootloader password checkbox (#650865) (bcl)
- Fix typo in my ctc commit (#648858) (bcl)
- Fix ctc check logic (#648858) (bcl)
- timezones: fix a scrolling problem with the scdate's GUI TreeView. (akozumpl)
- timezones: remove unneeded imports (akozumpl)
- Fix variable substitution in kickstart files (bcl)
- Don't show the cleardisk dialog on upgrades (#649865). (clumens)
- Use a stronger RNG for password salt (mitr)
- Use SHA-512 for bootloader password encryption (mitr)
- Support grub --encrypted when set from kickstart (mitr, #554874). (clumens)
- use different approach to tweak gconf settings in the image (#642358).
  (akozumpl)
- Allow loader to re-prompt for networking when network activation fails
  (jlaska)
- Support devices larger than 1.5TB (#649095, rspanton AT zepler DOT net).
  (clumens)
- Fix test for CTC devices from yesterday. (clumens)
- iscsi, logging: reuse the global ISCSID in has_iscsi(). (akozumpl)
- iscsi: refactor the kickstart processing to use the new iscsi methods.
  (akozumpl)
- Do not rely on presence of DEVICE setting in ifcfg files. (rvykydal)
- Do not sort settings in ifcfg file. (rvykydal)
- Remove obsolete networking code. (rvykydal)
- Support installation to CTC devices in loader (#648858, karsten). (clumens)
- Add more modules to the list of things liveinst must load. (clumens)
- Don't look for a CD number in readStampFileFromIso. (clumens)
- mediaCheckCdrom now supports checking only one piece of media. (clumens)
- Remove support for writing disc number info to .treeinfo and .discinfo.
  (clumens)
- Remove support for split media transactions from yuminstall.py. (clumens)
- Remove unused currentMedia parameter. (clumens)
- mediaHandler no longer needs to worry about mounting anything. (clumens)
- Rework _switchCD and _switchMedia for a one-image world. (clumens)
- umountImage shouldn't care about currentMedia. (clumens)
- Remove presentRequiredMediaMessage and related code. (clumens)
- Rename findIsoImages to findFirstIsoImage. (clumens)
- verifyMedia no longer looks at the disc number. (clumens)

* Fri Oct 29 2010 Chris Lumens <clumens@redhat.com> - 15.6-1
- We now need to BuildRequire dbus-python. (clumens)

* Fri Oct 29 2010 Chris Lumens <clumens@redhat.com> - 15.5-1
- ui: mnemonics for autopartitioning type. (akozumpl)
- hwclock lives in /sbin now. (akozumpl)
- timezone_text.py: remove the commented out parts and never called methods.
  (akozumpl)
- gui: remove "swapped" attribute from anaconda.glade (akozumpl)
- Errors downloading .treeinfo files should not be logged as errors. (clumens)
- When we can't fetch group metadata, log why. (clumens)
- Log which step we're on in doLoaderMain. (clumens)
- On upgrades, inform the user what action is taking place (#493249). (clumens)
- Fix import to not drag in a conflicting ConfigParser. (clumens)
- If there are any troubles reading the treeinfo file, return no addons.
  (clumens)
- Only build EFI images on x86_64 (jlaska, #646869). (clumens)
- restart-anaconda: full path to iscsiadm (akozumpl)
- iscsi: ISCSID needs to be declared global in has_iscsi() (akozumpl)
- Fix two problems with initrds for multipla kernels during a pungi compose.
  (akozumpl)
- Fix the locale value for Bengali (India) (mgracik)
- specfile: anaconda requires GConf2 during runtime. (akozumpl)
- timezones: use more of s-c-date (#520631). (akozumpl)
- Don't hardcode the sshd location, either. (clumens)
- Move StorageTestCase into its own file for use by other tests. (dlehman)
- Actions' devices must be in the tree except for ActionCreateDevice. (dlehman)
- Fix StorageDevice.resizable to check self.format.type, not self.format.
  (dlehman)
- Cleanup some preconditions in DeviceAction constructors. (dlehman)
- Add device action test suite. (dlehman)
- Fix test environment python path. (dlehman)
- Reimplement action pruning and sorting using tsort and action deps. (dlehman)
- Add requires and obsoletes methods to DeviceAction classes. (dlehman)
- Add a topological sort implementation for use in sorting device actions.
  (dlehman)
- Only log storage to tty3 if we have permission to do so. (dlehman)
- Remove PartitionDevice.path hack. (dlehman)
- Use 'name' instead of 'device' for device name ctor arg in all Device
  classes. (dlehman)
- Qualify devicelibs.lvm instead of relying on namespace clutter. (dlehman)
- Make the various DeviceAction.isFoo methods into properties. (dlehman)
- Establish a unique id for each DeviceAction instance. (dlehman)
- Add logpicker to keepfile list in upd-instroot. (tmlcoch)

* Thu Oct 21 2010 Chris Lumens <clumens@redhat.com> - 15.4-1
- Allow importing product.py in places where you won't have a .buildstamp.
  (clumens)
- Search for iscsid in the $PATH, not in a hardcoded list of places (#645523).
  (clumens)
- Use glib for getPartitionsList() (dcantrell)
- Include the SELinux policy file, not just the directory. (clumens)
- Remove the last references to install.img. (clumens)
- Properly identify device-mapper partitions set up by kpartx. (#644616)
  (dlehman)
- Don't ever try to mount ntfs filesystems. (#637319) (dlehman)
- We don't need to worry about 2.4 -> 2.6 updates anymore. (clumens)
- scsiWindow is unused.  Kill it. (clumens)

* Mon Oct 18 2010 Chris Lumens <clumens@redhat.com> - 15.3-1
- Don't recommend /usr as a mount point anymore (#643640). (clumens)
- Add some debugging prints. (clumens)
- Don't prompt for kbd, lang, or network on CD/DVD installs. (clumens)
- We no longer need to copy the install.img over and lochangefd to it.
  (clumens)
- Also rework image loading for CD/DVD installs. (clumens)
- Remove a bunch of unused support functions. (clumens)
- Use parseDeviceAndDir instead of reimplementing the same things two more
  times. (clumens)
- Rework how image loading works for HD installs. (clumens)
- Remove the unused mountNfsImage and all code that was only called by it.
  (clumens)
- Rework how image loading works for NFS installs. (clumens)
- Remove the unused iurlinfo, urlInstallData, and fix up URL kickstarts.
  (clumens)
- Initialize loaderData->method. (clumens)
- Remove the unused mountUrlImage function. (clumens)
- Rework how loading images works for URL installs. (clumens)
- urlinstTransfer and support functions do not operate on iurlinfo anymore.
  (clumens)
- urlMainSetupPanel no longer takes an iurlinfo. (clumens)
- Deprecate stage2=, keep method= as it's been for a long time now. (clumens)
- migrate_runtime_directory no longer does anything useful. (clumens)
- Remove the method selection block from the beginning of doLoaderMain.
  (clumens)
- Fix up copying of firmware. (clumens)
- Correct paths of things started by loader/init that have moved. (clumens)
- Step 3 of merging installer images:  No longer create install.img. (clumens)
- makeinstimage is no longer used. (clumens)
- instbin is no longer used. (clumens)
- A couple minor changes to mk-images. (clumens)
- Step 2 of merging installer images:  Move most everything out of makeinitrd.
  (clumens)
- Step 1 of merging installer images:  Don't copy files into a new root.
  (clumens)
- No longer do the bin -> usr/bin copy song and dance. (clumens)
- Fix typo in examine_gui.py (bcl)
- Clean up tabs in examine_gui.py (bcl)
- Rework proxy handling so that .treeinfo also uses proxy (#634655) (bcl)
- Translate task and repo names based on the product.img (#622064). (clumens)
- Use baseurl instead of methodstr to get .treeinfo (#604246) (rvykydal)
- Be more resilient to config files missing sections and options (#590591).
  (clumens)
- Add repos for all addons in all enabled repositories (#580697). (clumens)
- Add a method that fetches and returns the .treeinfo file. (clumens)
- All uses of perl must die. (clumens)

* Thu Oct 14 2010 Chris Lumens <clumens@redhat.com> - 15.2-1
- And remove welcome_{gui,text}.py from the translations too. (clumens)
- A block quote in the middle of a python file does nothing. (clumens)
- Fix traceback after Delete in nm-c-e (#642370) (rvykydal)
- Fix ifcfg logging message. (rvykydal)
- Fix porting of ifcfg logging. (rvykydal)
- Rescan disks when moving back through upgrade check (#635778) (bcl)
- anaconda: Disable X server regenerations (#609245) (ajax)
- Attempt to bring the network up before saving a bug report (#635821).
  (clumens)
- No one likes the welcome step anymore, so remove it. (clumens)
- iscsi, cosmetic: fix grammar in the iscsi dialogs. (akozumpl)
- iscsi: call iscsi.stabilize() at the end of the iscsi configuration.
  (akozumpl)
- iscsi: consolidate logging in the UI (akozumpl)
- iscsi: allow separate discovery/login credentials in TUI. (akozumpl)
- iscsi: migrate the CRED_ constants and parse_ip() to partIntfHelpers.
  (akozumpl)
- iscsi gui: use abstract methods in the iSCSIWizard interface. (akozumpl)
- iscsi gui: factor out the drive adding code. (akozumpl)
- iscsi gui: make the iSCSI wizard never return gtk constants. (akozumpl)
- isci: typo in a GUI checkbox (akozumpl)
- Add logpicker support into Makefiles, anaconda.spec.in, configure.ac and upd-
  instroot. (tmlcoch)
- Add logpicker tool into utils (tmlcoch)
- gui: hide text in the proxy password field (#611825). (akozumpl)
- logging: be smarter logging UI module import errors. (akozumpl)
- text.messageWindow(): make it more resilient to the input. (akozumpl)
- Log that we are running %pre scripts to the console (#640256). (clumens)
- Preset default config for immediate Close in nm-c-e enablement (#636526)
  (rvykydal)
- Fix non-dhcp network enablement in stage 2 (#640951) (rvykydal)
- Set focus after error message (#611430) (tmlcoch)
- When upgrading a package instead of installing, say so (#636520, jlaska).
  (clumens)
- Do a better job of explaining how much memory is required to install
  (#639056). (clumens)
- Get rid of mountLoopback and umountLoopback. (clumens)
- copyright notice in add_drive_text.py (akozumpl)
- restart-anaconda: log out of all iscsi nodes (akozumpl)
- remove EXN_ constants from constants.py (akozumpl)
- Honor selected hostname on Live CD (#638634) (rvykydal)
- Do not try to prompt for network for escrow in kickstart (#636533) (rvykydal)
- Sync up list of languages with contents of po/ directory. (clumens)
- Fix a storage logging import (#636621). (clumens)
- Fix a couple pylint-found errors. (clumens)
- Copy ifcfg.log into traceback and target system. (rvykydal)
- Improve logging of ifcfg stuff. (rvykydal)
- Refactor DNS resolver reset. (rvykydal)
- Add placeholders to ambiguous python strings (#634385). (clumens)
- Dynamically initialize MALLOC_PERTURB_ when loader starts. (pjones)
- btrfs will be a supported filesystem in F15 (josef). (clumens)
- Fix setting of $HOME (pjones)
- Limit progress bar amount to 1.0 (bcl)

* Fri Sep 24 2010 Chris Lumens <clumens@redhat.com> - 15.1-1
- Properly rescan storage with Reset in partition GUI (#635778) (bcl)
- Save the partition type selection when moving back (#635778) (bcl)
- Properly rescan disks when moving back (#635778) (bcl)
- Reset resolver after network device activation (#632489) (rvykydal)
- Don't include the product name in the translation (#636415). (clumens)
- Clarify loopback mount log message (#633444). (clumens)
- pykickstart now raises KickstartError instead of IOError. (clumens)
- Fix EFI bootloader install problems (#635873, #635887) (bcl)
- Re-add cleardiskssel step when autopart is chosen. (#635332) (dlehman)
- Pull boot splash image from correct location (#635330) (bcl)
- Add files for polkit to initrd.img (#633315) (rvykydal)
- Remove old kernels with new bootloader (#633234) (bcl)
- Both the inittab and systemd sections can return. Move this part earlier.
  (notting)
- iscsi: discovery and node login wizard. (akozumpl)
- Pass xdriver to anaconda in liveinst (#633827) (bcl)
- Add test cases for the new Size class. (dcantrell)
- Add exceptions specific to the new Size class. (dcantrell)
- Create Size class for specifying device and fs sizes. (dcantrell)
- Fix importing the netconfig UI in rescue mode (#632510). (clumens)
- Add noeject support to cdrom eject handling (#477887) (bcl)
- Cleanup tabs in flags.py (bcl)
- Add noeject support to loader (#477887) (bcl)
- Remove BETANAG, instead reading it from .buildstamp (#628688). (clumens)
- Convert .buildstamp into a .ini-style file. (clumens)
- Remove productPath. (clumens)
- Remove any /tmp/yum.log that may be present on the installed system
  (#630327). (clumens)
- If the filesystem doesn't support resize, there's no resizesb (#627153).
  (clumens)
- Run anaconda in fullscreen mode. (clumens)
- minor: gtk.CellRendererText has no property 'active'. (akozumpl)
- restart-anaconda: kill iscsid too (akozumpl)
- ui: fix the default choice in the 'advanced storage options' dialog.
  (akozumpl)
- iscsi: rename variable in addIscsiDrive. (akozumpl)
- ui: a couple of storage mnemonics. (akozumpl)
- updates: .glade files are in data/ui now. (akozumpl)
- Re-fix systemd default link (#627401, mschmidt). (clumens)
- Remove losetup and unlosetup from isys (bcl)
- Remove losetup usage (bcl)
- Various upd-instroot cleanups, most importantly for firstaidkit (#627758).
  (clumens)
- Shrink locale-archive down to just what we support. (clumens)
- Remove the icon-theme.cache file from the initrd. (clumens)
- Remove /etc/selinux/targeted/modules/active from the initrd (clumens)
- Remove the DRI modules from the initrd. (clumens)
- i18n: do not build translatable sentences from parts (#622545). (akozumpl)
- memory: install.img is now >150 MB so count 192 MB extra for it. (akozumpl)
- memory: check_memory() displays GUI dialog on livecd (#624534). (akozumpl)
- readvars should split variables into at most 2 pieces (bcl)
- Adding output to method selection process (bcl)

* Fri Aug 27 2010 Chris Lumens <clumens@redhat.com> - 15.0-1
- systemd symlinks now reside in /lib (#627401). (clumens)
- filtering UI: don't be picky about udev wwid length. (akozumpl)
- mpath: put quotes around the wwids, they can have spaces. (akozumpl)
- Use blacklist_exceptions for mpath devices (#612399) (mfuruta)
- typo: repeated line in lvm.py (akozumpl)
- mpath: do not deactivate mpath device upon its teardown. (akozumpl)
- mpath: teardown format from MultipathDevice.teardown() (#616273). (akozumpl)
- And change the tigervnc requires in the spec file too. (clumens)
- Kill joe. (pjones)
- Require tigervnc-server-minimal to remove perl from livecd (#627280).
  (clumens)
- Use ID_SERIAL_RAW for multipath, if available (#626842). (clumens)
- mpath: filter member partitions wiser in lvm. (dcantrell)
- mpath: do not deactivate mpath partitions in teardown(). (akozumpl)
- Fix comparison between /dev/disk/* paths and udev symlinks (#621515).
  (clumens)
- Remove telnetd.h from POTFILES.in so make works again. (clumens)
- Reset labels on /var/cache/yum as well (#623434). (clumens)
- NetworkManager uses a different config file now (#623937). (clumens)
- Don't touch resolv.conf which is handled by NM (#622927) (rvykydal)
- logging: turn the loglevels into proper enum. (akozumpl)
- loader: parseCmdLineIp* takes just the value as an argument now. (akozumpl)
- logging: refactor printLogHeader (akozumpl)
- Remove the nousbstorage command line option (#624556). (clumens)
- Remove telnet support. (dlehman)
- Allow omission of --size for partitions, use default size. (dlehman)
- Fix the provides we look for when installing DUD (#618862) (msivak)
- Fix the paths for DD in postinstall phase Related: rhbz#619745 (msivak)
- Remove the final use of $LOADERBIN from scripts. (clumens)
- Only set noverifyssl on URL installs (#621469). (clumens)
- Base install/upgrade default on whether any candidates were found (#590505).
  (clumens)
- fix 899f401611da021b3ec3882577ad860eae47f265 (akozumpl)
- Do not use autoconfiguration for DHCPv6 (#623216) (rvykydal)
- Add scripts/githooks/ with commit-msg script. (dcantrell)
- I don't need to pass "nomodeset" to stage2 after all. (clumens)
- After cancelled stage 2 network enablement remove temporary repo (#623639)
  (rvykydal)
- Fix traceback when using duplicate name for added/edited repo (#623080)
  (rvykydal)
- Fix traceback after Cancel in stage 2 network enablement dialog (#623017)
  (rvykydal)
- Make sure "nomodeset" and "xdriver=" get passed on to stage2 (#623129).
  (clumens)
- We checked for updated driver with wrong path prefix (#619745) (msivak)
- Proper detection of successful module update (#618862) (msivak)
- LVM and LUKS now align everything to 1MB boundaries. (#623458) (dlehman)
- Clearing of formatting from unpartitioned disks belongs in clearPartitions.
  (dlehman)
- Do disklabel handling for whole disk formats unknown to anaconda (#619721)
  (hdegoede)
- Do not support "part --grow raid.XX" (#577432). (clumens)
- Update systemd's default.target for the desired runlevel (#623102, mschmidt).
  (clumens)
- Skip cleardiskssel on custom partitioning (#620647). (clumens)
- logging: typo in analog (akozumpl)
- logging: fix logic in getSyslog(). (akozumpl)
- Use full EFI path to map drives for grub (#598572) (bcl)
- Don't complain about upgrading the same release (#620953) (bcl)
- Don't crash on unnamed installs (#621685) (bcl)
- mpath: add MultipathDevices first, before their partitions. (akozumpl)
- ibft: always configure network devices if there's ibft available (#617860).
  (akozumpl)
- Log exclusiveDisks, ignoredDisks, and reasons for ignoring devices. (dlehman)
- Include mpath/fwraid member devices in exclusiveDisks. (dlehman)
- Use part instead of device in PartitionWindow.populate() (#575749)
  (dcantrell)
- Add support for ipv6 to text UI network enablement (#612476) (rvykydal)
- Remember user's choice when going back in Configure TCP/IP (#609570)
  (rvykydal)
- Update generating of anaconda-ks.cfg for ipv6. (rvykydal)
- Update ks network command for ipv6 in anaconda. (rvykydal)
- Fix typo and set mpaths' sysfs path before querying udevdb. (#620712)
  (dlehman)
- The --loaderbin parameter to makeinitrd is unused.  Kill it. (clumens)
- services is a set, not a list (#620900, akozumpl). (clumens)
- Set AUTO_VLAN=yes in fcoe config files (#618875) (dcantrell)
- The --initrdsize parameter to makeinitrd is unused.  Kill it. (clumens)
- Honor bootdrive selection when autopartitioning (#620442) (hdegoede)
- shutdown: Use lstat to test for /lib64 (hdegoede)
- shutdown: don't unmount /sys and /proc (hdegoede)

* Mon Aug 02 2010 Chris Lumens <clumens@redhat.com> - 14.14-1
- Write out correct nfs url for repo= in /root/anaconda-ks.cfg (#584580)
  (rvykydal)
- mdadm -I no longer accepts --no-degraded (#620359) (hdegoede)
- Update buildinstall because of new man package name (mgracik)
- Clarify name of function that identifies biosraid member devices. (dlehman)
- Use dm subsystem functions to identify dmraid,mpath partitions. (dlehman)
- Move disk enumeration to a method of FilterWindow. (dlehman)
- Check if an mpath should be ignored before adding it to the devicetree.
  (dlehman)
- Add handling for mpath and fwraid devices in exclusiveDisks. (dlehman)
- Add functions to identify specific types of device-mapper devices. (dlehman)
- Ignore active fwraids and mpaths when setting up the filter ui. (dlehman)
- Include pyconfig*.h so that we can actually run python2.7 . (pjones)
- Remove translation of error strings in uncpio.c (bcl)
- Clean up tabs in uncpio.c (bcl)
- Redirect uncpio errors to syslog (#618181) (bcl)
- Make sure multipathd starts on systems using mpath storage (#615040)
  (dcantrell)
- Handle systems where all disks have a whole disk format (#617554) (dcantrell)
- Include modprobe file for Mellanox 10GB driver (#611997) (dcantrell)
- Remove some more kickstart duplication (#617512). (clumens)
- Fix setup of LVs (bcl)
- Include the kickstart file in the traceback (bcl)

* Tue Jul 27 2010 Ales Kozumplik <akozumpl@redhat.com> - 14.13-1
- Use readvars_parse_file in loader/init.c (dcantrell)
- Use readvars_parse_*() in loader/loader.c (dcantrell)
- Use readvars_parse_file() in loader/modules.c (dcantrell)
- Add readvars.c for parsing command line args and shell vars. (dcantrell)
- Check return value of chdir() (dcantrell)
- Remove handling for the "vesa" boot argument. (dcantrell)
- Remove USE_MINILIBC cruft from loader/init.c (dcantrell)
- Whitespace cleanup in loader/Makefile.am (dcantrell)
- logging: remote logging for traceback dumps. (akozumpl)
- logging: also log X.log remotely (akozumpl)
- logging: autodetect the virtio-serial port. (akozumpl)
- does not properly recognize hpt45x_raid_member (#617438) (hdegoede)
- Show allowable prepboot size range in exception (#603188) (dcantrell)
- Remove storage init duplication (#6176512). (clumens)
- Skip the Filter UI in Basic Storage mode (#598420) (hdegoede)
- Make the shell in tty2 and ssh all go to /root like on a real system.
  (pjones)

* Thu Jul 22 2010 Ales Kozumplik <akozumpl@redhat.com> - 14.12-1
- Only write changed DASD attributes to rd_DASD params (#606783) (dcantrell)
- Propagate MACADDR from loaderData to iface (#595388) (dcantrell)
- Deal with media only for media repo package failures (#573492) (rvykydal)
- Support for ks: --ipv6 command, and ipv6 values for --gateway (#490794)
  (rvykydal)
- analog: support reading the installation logs from a unix socket. (akozumpl)
- logging: support logging through virtio-serial (#576439). (akozumpl)
- modules.c: only log from _doLoadModule() if logging has been initialized.
  (akozumpl)
- break the dependency of modules.c on loader.h (akozumpl)
- Enforce limits on partition start/end sectors. (dlehman)
- Fix up import to make rescue mode work again (#616090). (clumens)
- Init g_type in is_wireless_device. (rvykydal)
- Add resolver reset to some network enablement places (#614001) (rvykydal)
- Fix config of ipv6 and ipv4 (auto + manual) in loader (#609576) (rvykydal)
- text: remove the needless complexity in the screen switching loop. (akozumpl)
- text.py: do not traceback when can't go back (#598493). (akozumpl)
- remove doShutdownX11Actions(). (akozumpl)
- Add uname to initrd.img (#614770) (dcantrell)
- Some people like to specify MAC addresses in lower case. (clumens)
- Remove support for interactive kickstart installs. (clumens)
- Improve parsing and pass the devel flag to loader through the command line
  (msivak)
- When in devel mode, do not catch tracebacks, we want the core file (msivak)
- Add better debugging capabilities to loader (msivak)
- Add confirmation dialog when loading dlabel DDs (#570053) (msivak)

* Wed Jul 14 2010 Chris Lumens <clumens@redhat.com> - 14.11-1
- Add the gobject-introspection package (#613695) (mgracik)
- Update pylint test for pylint 0.20.1 (bcl)
- Use long ints for comparisons, not floats (#608172) (bcl)
- Enforce the same logic on autopart shrink as on resize (#608172) (bcl)
- Don't crash when putting mpath devices into the filter name cache (#597223).
  (clumens)
- Handle serial = None in the right place (#613623). (clumens)
- There's still no instdata on master (#613075). (clumens)

* Thu Jul 08 2010 Chris Lumens <clumens@redhat.com> - 14.10-1
- Handle 16 digit hex strings for ID_SERIAL_SHORT (#611554) (dcantrell)
- Focus default advanced storage type in add dialog (#603726) (dcantrell)
- Add multipath member with addUdevDiskDevice instead of DiskDevice (#582254)
  (dcantrell)
- add mime.cache to the stage2 image (#609596). (akozumpl)
- makeupdates: treat files under pyanaconda/ individually. (akozumpl)
- ssl: propagate 'url --noverifyssl' into yum repo configuration (#599040).
  (akozumpl)
- ssl: support for 'url --noverifyssl' in loader. (akozumpl)
- ssl: support --noverifyssl in the repo kickstart command. (akozumpl)
- Fix a file descriptor leak in getDevices (#612153, mganisin). (clumens)
- Pass size of structure not a size of pointer to calloc (#592227) (msivak)
- Properly iterate over the netdevices list (#610769). (clumens)
- Require the static package instead of the devel one (#610797). (clumens)
- ui: C_reate mnemonics in Create Storage dialog. (akozumpl)
- fix insensitivities of 0783c488 (akozumpl)
- During an update don't erase old kernels (#594411) (bcl)
- booty and isys have moved, so update runpylint.sh. (clumens)
- Translate MAC addresses to devices in the second stage, too. (clumens)
- Fix prototype of getIPAddresses (#605659) (rvykydal)
- Account for ipv6 addresses too (#605659) (rvykydal)
- Use progressbar instead of waitwindow for repo setup (#584996) (rvykydal)
- Don't deactivate active device before running nm-c-e (#608773) (rvykydal)
- Control all devs by NM by default + filtering (iSCSI, FCoE) (#606745)
  (rvykydal)
- anaconda's lvm vgreduce invocation is not filtering out disks (609479)
  (hdegoede)
- Clean up proxy handling in yuminstall.py (#604137) (bcl)
- Write out missing space on 'part' lines in ks file (#605938) (dcantrell)
- Make sure swap devices are included in dracut args (#607646) (dcantrell)
- Catch DeviceNotFoundError in cleardisks (#607661) (dcantrell)
- Do not proceed after partitioning errors in text mode (#599484) (bcl)
- fixup exclude/excludepkgs usage (#607664) (bcl)
- yum calls it "exclude" instead of "excludepkgs" (#607664). (clumens)
- Add full proxy URL to writeKS (#602705) (bcl)
- Fix repo --includepkgs=, and add more to anaconda-ks.cfg's repo line
  (#602705). (clumens)
- Add a slash to the path pointing to hdinstall dir (#592154) (msivak)
- Don't resize lv's formatting unless also resizing the lv. (#575046) (dlehman)
- Show sane non-removable drives too in the DD dialog (#594548) (msivak)

* Mon Jun 28 2010 Chris Lumens <clumens@redhat.com> - 14.9-1
- Update to use the latest pykickstart. (clumens)
- Import anaconda_log correctly to avoid the double import problem. (clumens)
- Move isys and booty into the pyanaconda/ directory, adjust paths to match.
  (clumens)
- network.dracutSetupstring: properly handle ipv6 (#605232) (hdegoede)
- Support for converged traffic during install to FCoE LUN (#604763) (hdegoede)
- Take into account the fact that some formats have no min/max size. (dlehman)
- Put dhcp configuration files in /etc/dhcp (#468436) (dcantrell)
- Autopart PVs require enough space for a default-sized partition. (dlehman)
- Enforce format min/max size for fixed-size requests. (dlehman)
- Fix min/max size definitions for PReP Boot format class. (dlehman)
- Constrain lvmpv, mdmember, and swap partitions to a single disk. (#605756)
  (dlehman)
- Enforce maximum start sector for partitions. (#604059) (dlehman)
- Handle nm-c-e using prefix instead of netmask (#607762) (hdegoede)
- Handle "(#BUGNUM, author)" in git log summary lines. (dcantrell)
- Allow running an alternate program from liveinst. (clumens)
- fix network.py syntax error. (akozumpl)
- modules: make iscsi and similar imports look less ridiculous (akozumpl)
- modules: fix getlangnames. (akozumpl)
- updates: link files in also on lower directory levels. (akozumpl)
- modules: dont treat booty special. (akozumpl)
- modules: dont treat isys special. (akozumpl)
- modules: necessary changes to the import statements under pyanaconda/textw
  (akozumpl)
- modules: a change to an import statements in isys/ (akozumpl)
- modules: necessary changes to the import statements under pyanaconda/iw
  (akozumpl)
- modules: changes to the import statements directly under pyanaconda/
  (akozumpl)
- modules: necessary changes to the installclasses import statements.
  (akozumpl)
- modules: necessary changes to the import statements under booty/ (akozumpl)
- modules: necessary changes to the import statements under storage/ (akozumpl)
- modules: pyanaconda.textw and pyanaconda.iw are now regular modules.
  (akozumpl)
- modules: remove the hacks in setupPythonPath(). (akozumpl)
- Be specific when telling lvm to ignore devices. (dlehman)
- analog: fix options.output traceback (akozumpl)
- Handle questionInitializeDASD in cmdline mode (#605846) (dcantrell)
- Set SELinux context on dasd.conf and zfcp.conf (#605597) (dcantrell)
- Add --fsprofile= to the anaconda-ks.cfg (#605944). (clumens)
- Add the proxy tests to the top-level test framework. (clumens)
- Fix pyanaconda.kickstart import, and init logging before doing anything else.
  (clumens)
- Do not assume /dev/loop0 and /dev/loop1 are available. (clumens)
- tearDown -> tearDownModules. (clumens)
- Fix test suite Makefile.am files. (clumens)
- Check before running post scripts on kickstart rescue (#605754, atodorov).
  (clumens)
- Make sure lvm ignores unknown devicemapper devices (hdegoede)
- Put [] around ipv6 addr on the dracut cmdline (#605300) (hdegoede)
- Revert "Select default and mandatory packages when enabling repos."
  (#605289). (clumens)
- Fix the build. (clumens)
- Set repo.proxy only after fully assembled (#602712) (bcl)
- Change proxy regex in loader to match python proxy regex (#602712) (bcl)
- Add test cases for proxy regex (#602712) (bcl)
- Replace POSIX regex classes with character ranges (#602712) (bcl)
- Set wireless devices to NM_CONTROLLED by default (#594881) (rvykydal)
- Add iSCSI radio button to button group (#603726) (dcantrell)
- Fall back on regular device name (#604776) (dcantrell)
- Honor --timeout=NUM from kickstart files on s390 (#603032) (dcantrell)
- Use Decimal instead of float for label calculations (#604639) (bcl)
- Check for proper Proxy URL in loader (#604126) (bcl)
- fix: syntax error in network.py (akozumpl)
- fix: zfcp.startup() survives without an interface (#604542). (akozumpl)
- Fix a typo (#604628) (rvykydal)
- Revert "Retain user's UTC checkbox setting (#591125)" (bcl)
- Use method from isys for wireless devs checking (#473803) (rvykydal)
- Do not ask for interface twice in stage 1 (#594802) (rvykydal)
- Fix parsing of ifcfg OPTIONS parameter (#597205) (rvykydal)
- Don't overwrite 70-persistent-net.rules (#597625) (rvykydal)
- Wait only for activation of devices controlled by NM (#598432) (rvykydal)
- Show zFCP errors in dialog boxes rather than tracebacks (#598087) (maier)
- Show by-path names for DASD and zFCP, WWID for mpath (#580507) (maier)
- Remember autopart UI choice when going back (#596146) (dcantrell)
- Make parent directories for ks scriptlet log files (#597279) (dcantrell)
- Adjust the paths used for updates (bcl)
- Raise an error when an md dev is not in the tree after scanning all slaves
  (hdegoede)
- Raise an exception when an md dev is in the tree under the wrong name
  (hdegoede)

* Fri Jun 11 2010 Chris Lumens <clumens@redhat.com> - 14.8-1
- Rebind hybrid lcs/ctc network devices to correct driver if necessary
  (#596826) (maier)
- Get netdev name without CONFIG_SYSFS_DEPRECATED_V2 in linuxrc.s390 (#596826)
  (maier)
- Replace rd_CCW with final dracut option rd_ZNET for network-rootfs on s390
  (maier)
- Do parse DOMAIN for DNS search suffixes in loader (#595388) (maier)
- Allow loader to parse DNS and write DNS1, DNS2, ... itself (again). (#595388)
  (maier)
- GATEWAY in linuxrc.s390's ifcfg is really IPv4 only (#595388) (maier)
- Handle OPTIONS in ifcfg files transparently in loader (#595388) (maier)
- If only (clumens)
- Catch and display KickstartErrors coming from execute() cleanly (#603059).
  (clumens)
- Forcibly remove packages from deselected groups (#495621). (clumens)
- Default to aes-xts-plain64 for new luks devices. (#600295) (dlehman)
- Put another '/' in the rhinstall-install.img path (#601838). (clumens)
- Fix driver disc repo baseurl (#602343) (msivak)
- or -> and (clumens)
- fix: do not check root devices from hasWindows (#592860). (akozumpl)
- fix: kickstart sshpw command dysfunctional (#602308). (akozumpl)
- Include /sbin/blkid in the initrd.img (dcantrell)
- Correct initrd.img load address on s390 (dcantrell)
- Remove duplicate md handling code from 70-anaconda.rules (#599197)
  (dcantrell)
- Add md arrays to the devicetree with a md# name rather then md/# (hdegoede)
- "Finding" -> "Examining" storage devices (#594804). (clumens)
- In the filter UI, also ignore devices that do not report a size (#594803).
  (clumens)
- translations: scdate can translate timezones better then us. (akozumpl)
- fix: the po path has to be bound for gtk.glade too. (akozumpl)
- translations: don't say context=yes if you don't mean it. (akozumpl)
- translations: loader header files strings missing in anaconda.pot. (akozumpl)
- fix error saving screenshots during package install (#594826). (akozumpl)
- Re-get partedPartition after re-adding failed-to-remove partition. (dlehman)
- Select default and mandatory packages when enabling repos. (dlehman)
- do not import block from isys. not needed. (#601291). (akozumpl)
- removal: gui.InstallKeyWindow. (akozumpl)
- Make minimum shrink size 1 not 0 (#602442) (bcl)
- Initialize Decimal for partition slices (#602376) (bcl)
- Make sure lvm2 gets installed when we are using lvm (#601644) (hdegoede)
- Handle FCoE over vlan properly (#486244) (hdegoede)
- Tell user when nothing can be upgraded (#592605) (bcl)
- netork -> network (clumens)
- Redownload and extract updates.img during anaconda restart. (akozumpl)
- Restarting anaconda. (akozumpl)
- New version. (clumens)

* Fri Jun 04 2010 Chris Lumens <clumens@redhat.com> - 14.7-1
- Assign the trimmed identifier so it gets used in the UI. (clumens)
- Remember disk selections when going back to the text partition UI (#596113).
  (clumens)
- Fix typo in libblkid requires (#599821). (clumens)
- Fix green strips showing up (#582744) (bcl)
- Remember when IPv4 IPADDR has been read from ifcfg file in loader (#595388)
  (maier)
- Don't let loader write HWADDR to ifcfg file on s390. (#595388) (maier)
- Tell which stacks to configure in /etc/sysconfig/network on s390 (#595388)
  (maier)
- Really ignore deprecated parm/conf file options in linuxrc.s390 (#595388)
  (maier)
- Correctly pass netdev name from linuxrc.s390 to loader (#595382) (maier)
- Re-enable usable pdb with vnc on s390x (maier)
- Fix most of what is necessary for install over IPv6 on s390 (#594090)
  (dcantrell)
- Remove long deprecated writing of alias for network in linuxrc.s390 (maier)
- Fix backtrace when a vg starts with freespace (#597925) (hdegoede)
- Only kill init for reboot/halt and then exit linuxrc.s390 (maier)
- Fix a couple small errors found by checkbot. (clumens)
- Retain user's UTC checkbox setting (#591125) (bcl)
- Fix up pylint to work with the new source layout. (clumens)
- Replace the Serial Number column with an Identifier column (#560666).
  (clumens)
- Adjust mdraid size estimates (#587442) (bcl)
- Extra debugging output (#587442) (bcl)
- Set NM_CONTROLLED=no iscsi for storage devices only on system (#598070)
  (rvykydal)
- Improve handling of auto and unknown types in fstab. (#577260) (dlehman)
- Give blkid the final word on device format detection. (#593637) (dlehman)
- Allow ignoredisk to be interactive without the rest of the UI (#596804)
  (pjones)
- memory: check for URL install in loader too (#596993). (akozumpl)
- spec: python-pyblock has to be in BuildRequires too. (akozumpl)
- Ignore errors upon restoring /lib and /usr after unmounting filesystems
  (hdegoede)
- Make sure we still have an elf interpreter after unmounting fs (#598222)
  (hdegoede)
- booty: remove hack city hack (hdegoede)
- Remove booty/checkbootloader hacky raid set handling (hdegoede)
- booty: make getDiskPart deal with devices instead of names (hdegoede)
- booty: move grub specific mangling of partition number to the grub code
  (hdegoede)
- booty make getDiskPart use the devicetree (hdegoede)
- booty: make grubbyPartitionName and grubbydiskName take a device (hdegoede)
- booty: make matchingBootTargets and addMemberMbrs deal with devices instead
  of names (hdegoede)
- booty: make getPhysicalDevices take and return Devices rather then device
  names (hdegoede)
- booty: Make getPhysicalDevices only return physical devices (#593718)
  (hdegoede)
- booty: Don't create device.map entries for devices backing / (hdegoede)
- Add simple firewall unit test (msivak)
- Improve module cleanup in our TestCase class and fix issues in FS mock class.
  (msivak)
- Find tests using python-nose and create make unittest target (msivak)
- Update .gitignore file to account for new directory structure. (dcantrell)
- Update po/Rules-* files to account for new directory structure. (dcantrell)
- Structure the repo layout so it matches final structure better and make isys
  a real Python package. (msivak)
- Add more sanity checks to the mountpoint (#592185) (bcl)
- Make sure the product.img directory is mounted before copying (#587696).
  (clumens)
- Put a missing close brace back into isys.c. (clumens)
- refactoring: put totalMemory() into isys. (akozumpl)

* Wed May 26 2010 Chris Lumens <clumens@redhat.com> - 14.6-1
- Set repository in kickstart harddrive command (#592239) (rvykydal)
- nm-c-e integration: fix some leftovers from patch porting. (rvykydal)
- Add missing logging import to installinterfacebase (hdegoede)
- Give pre-existing mdraid arrays the proper name in the UI (#596227)
  (hdegoede)
- Add nm-c-e translations to stage 2 (#594982) (rvykydal)
- set the resolution with resolution= from the cmdline (#594918). (akozumpl)
- cleanup: gui.py never uses runres for anything, off it goes. (akozumpl)
- Skip the bootloader placement window if we're on UEFI (#582143) (pjones)
- Add some more stuff to .bash_history (pjones)
- Support cio_ignore functionality for zFCP devices (#533492) (dcantrell)
- Add missing newline for 'nfs' line in ks file (#591479) (dcantrell)
- Correct problem with initrd.addrsize generation (#546422) (dcantrell)
- Fix rescue mode startup with kickstart file and without (#515896) (msivak)
- More checkbot fixes. (clumens)
- fix: traceback in check_memory() (#595284). (akozumpl)
- Drop init questions from cmdline.py (hdegoede)
- Move init questions to InstallInterfaceBase (hdegoede)
- Make re-init all inconsistent lvm mean re-init all instead of ignore all
  (hdegoede)
- Read cciss devices correctly from 'multipath -d' output (#559507) (dcantrell)
- On NFS installs, look for product.img and updates.img under images/
  (#594811). (clumens)
- Remove yum cache for anaconda's temporary repos (#593649). (clumens)
- Use correct NM dbus interfaces (#594716) (rvykydal)
- Change the configuration of depmod and link modules to better place (#593941)
  (msivak)
- Make ssid and wepkey in boot params and stage 1 kickstart work (#473803)
  (rvykydal)
- logging: remove addLogger() (akozumpl)
- iutil: execWithCallback() and execWithPulseProgress() return an object.
  (akozumpl)
- logging: simplify stdout logging in execWithCallback(). (akozumpl)
- logging: use stderr parameter in execWithCallback(). (akozumpl)
- logging: remove addSysLogHandler() (akozumpl)
- analog: handle a config file we can't open. (akozumpl)
- clearer error messages for missing iscsi initiator name (hdegoede)
- fedora is part of iSCSI initiator name (#594659) (hdegoede)
- Add default iSCSI initiator name in rescue mode (#594434) (hdegoede)
- Do not allow editing of extended partitions (#593754) (hdegoede)
- Check for sane mountpoint in raid dialog (#592185) (bcl)
- Check for sane mountpoint in lvm dialog (#592185) (bcl)
- Check for sane mountpoint in partition dialog (#592185) (bcl)
- Cleaned up sanityCheckMountPoint (bcl)
- Don't autostep past the end of the install screens (#593556) (bcl)
- Add missing rpm macros file to get rid of the rpm warnings (msivak)
- Add the rpmrc file to the initrd.img (#508242) (mgracik)
- fix: syntax error in gui.py from 9e69c5f36f79410d9df1502fe69f02f4d06173ab.
  (akozumpl)
- Keep track of pvcount for non existing vgs (#593871) (hdegoede)
- Improve module cleanup in our TestCase class and fix issues in FS mock class.
  (msivak)
- Don't drop encryption when re-editing new encrypted partitions. (#582888)
  (dlehman)
- Return disk to prior state following failed partition removal. (#580088)
  (dlehman)
- Display unpartitioned disks in main partitioning gui. (#588637) (dlehman)
- Pick up mountpoint for existing formats on encrypted LVs. (#587002) (dlehman)
- Automatic partitioning should yield no more than one PReP partition.
  (dlehman)
- Pass short type names for PartSpec ctor. (dlehman)
- Setting up lvs should never fail (hdegoede)
- We no longer need to handle lvs which are part of an incomplete vg (hdegoede)
- Don't clear immutable devices (#593642) (hdegoede)
- Store immutable info into the device for easier access (hdegoede)
- Reset vg blacklist when initializing storage (hdegoede)
- Handle vgs with duplicate names (#591469) (hdegoede)
- Delay setting up lvs until other devices are scanned (hdegoede)
- anaconda udev rules should not get lvm info based in volgroup name (hdegoede)
- Move creation of lv devices into its own function (hdegoede)
- livecd: window icon (#583333). (akozumpl)
- FcoeDiskDevice.dracutSetupString(): use the right dracut syntax (#486244)
  (hdegoede)
- improve the memory checking so it reflects better the hungry architectures.
  (akozumpl)
- logging: fix SIGSEGV when trying to log after closeLog() is called.
  (akozumpl)
- Updates to scripts/makebumpver. (dcantrell)
- Suppress failures to tear down /dev/loop devices (#591829) (bcl)
- Fix the order of arguments in archive read callback and archive closing.
  (msivak)
- Use "kernel-modules = version" style for locating rpms providing driver
  updates (msivak)
- Move depmod configuration into new directory structure to get rid of depmod
  warning (#508242) (msivak)
- Fix descriptor leak and iteration progress in driverdisc code (#592225)
  (msivak)
- Add lsof command to initrd.img (mgracik)
- Add hmac file for sshd (#592186) (mgracik)
- Enable fips mode after fips mode installation (#592188) (mgracik)
- Add nslookup to the install.img (#591064) (mgracik)
- Add the chk files for libraries to the install.img (#590701) (mgracik)
- Add the eject command to the install.img (#591070) (mgracik)
- Add hmac file for libgcrypt to install.img (#590701) (mgracik)
- Don't remove *.hmac files when creating install images (mgracik)
- Added clear command to the install.img (#586499) (mgracik)
- Added chvt to the install.img (#575844) (mgracik)
- Only install non-branded anaconda icon on liveinst arches (dcantrell)
- Fix of typo. (rvykydal)
- Fix two minor errors found by checkbot. (clumens)
- Fix bad patches reordering (#473803) (rvykydal)
- scripts/analog: normalize paths before generating the config. (akozumpl)
- gui: "_use anyway" mnemonic. (akozumpl)
- logging: give loglevels for the shortened names. (akozumpl)
- logging: remove references to the 'bootloaderadvanced' step. (akozumpl)
- logging: remove references to some more steps. (akozumpl)
- Move importing of tested modules into setUp methods (msivak)
- Add Mock classes (msivak)
- gui, autopart: don't let a too verbose translation ruin all teh fun
  (#591955). (akozumpl)
- Update po/POTFILES.in for nm-connection-editor integration. (dcantrell)
- Fix typo in loader/nfsinstall.c (dcantrell)
- Add the best package for this arch to the optional package selector
  (#591653). (clumens)
- Swap server and opts on the split() call (#591479) (dcantrell)
- Handle devices that don't have a /dev/disk/by-path/ symlink (#563242)
  (pjones)
- Make sure we write out multipath.conf before discovery (#563242) (pjones)
- Handle >2 way /sbin/multipath output better (#563242) (pjones)
- Look for updates.img and product.img on NFS installs. (clumens)
- And add a menu to the right hand side so you can see the new column.
  (clumens)
- Don't ask if we have ESSID specified by kickstart or stage 1 (#473803)
  (rvykydal)
- Make ks option network --wepkey work in stage 2 (#473803) (rvykydal)
- Add support for wireless configuration using nm-c-e in stage 2 (#473803)
  (rvykydal)
- Write out ifcfg files only when necessary (#520146) (rvykydal)
- Use separate method for copying network configuration to system (#520146).
  (rvykydal)
- Network: remove functions that are not used anymore (#520146) (rvykydal)
- Wait for specific activated network devices (#520146). (rvykydal)
- Set network devices configured in ks to be nm-controlled (#520146).
  (rvykydal)
- Remove no longer needed devices argument from Network.write() (#520146)
  (rvykydal)
- Actually generate contents of 70-persistent-net.rules (#520146) (rvykydal)
- Disable [Configure Network] button if there are no net devs (#520146)
  (rvykydal)
- Add net device description into selection dialog (#520146) (rvykydal)
- Check preselected install network device as nm-controlled (#520146)
  (rvykydal)
- Don't ask when configuring net if we have only one network device (#520146)
  (rvykydal)
- Do not mess value change with line formatting (#520146) (rvykydal)
- Log change of ifcfg files by nm-c-e (#520146) (rvykydal)
- Enable networking in stage 2 using nm-c-e (#520146) (rvykydal)
- Write ifcfg files via NetworkDevice in Network.write() method (#520146)
  (rvykydal)
- Use ifcfg files via NetworkDevice in Network class (#520146) (rvykydal)
- Use proper attribute instead of NetworkDevice 'DESC' hack (#520146)
  (rvykydal)
- Quote values when writing out to ifcfg files (#520146) (rvykydal)
- Network.__str__() little cleanup (#520146) (rvykydal)
- Use IfcfgFile class to back NetworkDevice objects (#520146) (rvykydal)
- Move some consts to module globals for use in other places (#520146)
  (rvykydal)
- Add class for handling ifcfg files (#520146) (rvykydal)
- logging: the ibft message once again. (akozumpl)
- logging: no iBFT is not an error, fix spelling. (akozumpl)
- logging: log loader messages with LOG_LOCAL1 syslog facility. (akozumpl)
- logging: strip the extra newline in FCoE EDD log (akozumpl)
- logging: remove references to "confirminstall" and "confirmupgrade" steps.
  (akozumpl)
- logging: remove all references to the "installtype" step. (akozumpl)
- Determine if an mdmember is biosraid earlier (#586298) (hdegoede)
- Set runlevel 5 based on the presence of both a display manager and X server.
  (#588483) (notting)
- Add "Serial Number" column to the right side of the cleardisks UI. (clumens)
- Set permissions on initrd.addrsize to 0644 (#591455) (dcantrell)
- fix compile error after 7aace0bf0e0557cd914aa93e80a709a9f21f07f8 (akozumpl)
- autoconf: icons/ is missing makefiles (akozumpl)
- new version of report wont start without /etc/report.conf (akozumpl)
- Don't allow creating a new bootloader config in text mode (#580378).
  (clumens)
- Fix verification of DDs, we were looking for wrong path (#508242) (msivak)
- Remove raid clone option and code (#587036) (hdegoede)
- cleanup booty x86 flag.serial handling (#589773) (hdegoede)
- isys/auditd was missing from .gitingore. (akozumpl)
- bootloader timeout default should be None not 0 (jkeating)
- Use iBFT if present and user didn't asked for anything else. (#590719)
  (msivak)
- storage: LUKSDevice takes req_grow after its slave (#589450). (akozumpl)
- Correctly parse system-release (#590407) (lkundrak)
- Offer to ignore unformatted DASDs rather than forcing exit (#580456)
  (dcantrell)
- Make Format and Resize checkboxes mutually exclusive (#589977) (dcantrell)
- Fix usage of deviceNameToDiskByPath in devicetree.py (#589967) (dcantrell)
- Advance line pointer & don't strdup(val) on error in readNetInfo (dcantrell)
- Add non-branded default liveinst icons for anaconda (#588737) (dcantrell)
- Add expanded=False to the base class's detailedMessageWindow as well.
  (clumens)
- Add all possible install class locations to the search path (#587696).
  (clumens)
- Use module reloading in driver disc operations (#590015) (msivak)
- Use gtk consts instead of magic ints. (rvykydal)
- Only initialize logging via a method, not with every import (#584054).
  (akozumpl)
- Remove the check for partitions (#508242) (msivak)
- Close the dir descriptor after usage. (#589580) (msivak)
- Remove partitions after unpartitioned non-partition devices. (#588597)
  (dlehman)
- Work around device node creation issues when creating EFI images. (#589680)
  (pjones)
- Clean up tabs in dispatch.py (bcl)
- Just use /dev/dasdX if we can't get a by-path link (dcantrell)
- Do not prepend /dev/disk/by-path in format DASD window (dcantrell)
- Use udev_device_get_by_path() to get /dev/disk/by-path link (dcantrell)
- Add udev_device_get_by_path() to return /dev/disk/by-path link (dcantrell)
- Expand the details pane when showing unformatted DASDs (#580463) (dcantrell)
- Log problem line if unquoting failed in readNetInfo() (dcantrell)
- Update generic.ins for s390x (#546422) (dcantrell)
- Rename geninitrdsz.c to addrsize.c (#546422) (dcantrell)
- Generate initrd.addrsize file correctly for LPAR booting (#546422)
  (dcantrell)
- Only allow upgrading from one minor release of RHEL to another (#589052).
  (clumens)
- fcoe: use fipvlan instead of fcoemon to bring up fcoe (#486244) (hdegoede)
- memory: increase the RAM limits, check for URL installs (#549653). (akozumpl)
- memory: build auditd as a standalone binary and run it so (#549653).
  (akozumpl)
- gui: don't let metacity display the title right-click menu (#588642).
  (akozumpl)

* Wed May 05 2010 Chris Lumens <clumens@redhat.com> - 14.5-1
- Link /sbin/reboot and /sbin/halt to /sbin/init on s390x (#571370) (dcantrell)
- Don't clear bootloader radio selection on double click (#588771). (clumens)
- Add support to livecd for arbitrarily complex dir structures. (#504986)
  (dlehman)
- Grab everything in $LIBDIR/rsyslog/ (pjones)
- Do not automatically backtrace when telnetd quits (#588964). (clumens)
- Share terminology between the cleardisks text and panel headers (#587879).
  (clumens)
- Allow displaying groups that only contain conditional packages (#475239).
  (clumens)
- Fix hasWindows() to actually work as advertised (hdegoede)
- Revert commit 27a4c7df871744454d1ca8979a576f9f45c67189 (hdegoede)
- Make deviceNameToDiskByPath check udev info instead of sysfs (dcantrell)
- Fix some minor problems in storage/dasd.py (#560702) (dcantrell)
- Read in network settings correctly, as configured by linuxrc.s390 (dcantrell)
- Clean up wording for oversized LVs (#587459) (dcantrell)
- Teach upd-instroot about i686 (jkeating)
- Make the rule for 70-anaconda.rules in updates.img be generic. (pjones)
- Do not use --quiet and --nostart when doing selinux configuration (#568528)
  (msivak)
- Tell dracut it should activate the first swap device (#572771) (hdegoede)
- Remove broken hasWindows function from bootloader.py and its callers
  (hdegoede)
- booty: remove dead code chunk (hdegoede)
- Don't add recovery partitions to the grub boot menu (#534066) (hdegoede)
- Use g_str_has_suffix() to check end of string (dcantrell)
- Find stage2 install.img on local hd installs (dcantrell)
- gui: gray out OK button while adding raid set (#587161). (akozumpl)
- Strip quoting from OPTIONS when composing rd_CCW line (#577193). (dcantrell)
- Default the global grub timeout to 5 for serial (jkeating)
- Print out device sizes in list-harddrives-stub as well (#587395). (clumens)
- Make sure a given path exists before calling os.statvfs on it (#587662).
  (clumens)
- Wait for scsi adapters to be done with scanning their busses (#583143)
  (hdegoede)
- Set CURL_FAILONERROR to catch url download errors (#586925) (dcantrell)
- Bring up network for local hd vnc kickstart installs (#522064) (dcantrell)
- gui: no close buttons etc. in window decoration (#582645) (akozumpl)
- Don't clear BIOS RAID member disks (#587066) (hdegoede)
- Remove devices from libparted's cache when destroying them (#586622)
  (hdegoede)
- Offer to format unformatted DASD devices (#560702) (dcantrell)
- X input configuration has moved to /usr/share (#585621). (clumens)
- Disable button icons on stock GTK buttons (#579701). (akozumpl)
- Remove button icons from the glade files (#579701). (akozumpl)
- Don't traceback on CD-ROM driver in list-harddrives-stub (#586410). (clumens)
- Fetch ks files over NFS when ksdevice is not given (#541873) (dcantrell)
- put liveinst/console.apps/liveinst.h in .gitignore (akozumpl)
- Remove the README files (#583408). (clumens)
- Make it more clear what the purpose of the "Boot" column is (#584811).
  (clumens)
- nfs: off by one error leaves extra slash in a path. (akozumpl)
- removal: umountStage2(). (akozumpl)
- nfs: direct mounting of stage2. (akozumpl)
- loader: strip trailing slash character from stage2= URL. (akozumpl)
- imount: allow bind mounts. (akozumpl)
- Make sure we use 1.0 mdraid metadata when the set is used for boot (#584596)
  (hdegoede)
- Add a preCommitFixup hook to StorageDevice classes (hdegoede)
- Check for not having found any disks after populating the tree (#583906)
  (hdegoede)
- Prune resize and format create/migrate actions if destroying a device.
  (dlehman)
- Schedule actions when removing existing extended partitions. (#568219)
  (dlehman)
- Don't try to zero out extended partitions. (dlehman)
- lvm: check resizing against format's targetSize (#580171). (akozumpl)
- Restore storage.clearPartType after reset when backing out of GUI. (#559233)
  (dlehman)
- Make Cancel button the default for 'Weak Password' dialog (#582660) (bcl)
- Set Create Storage focus to first active radio button (#582676) (bcl)
- BaseInstallClass no longer has a setInstallData method. (clumens)
- livecd.py: set the selected keyboard (#583289). (akozumpl)
- Make rhel.py an installclass that we can inherit from for variants. (notting)
- Don't make all devices on the boot device selector immutable (#583028).
  (clumens)
- Don't allow running as non-root (#583213). (clumens)
- Careful with that WINDOW_TYPE_HINT_DESKTOP, Eugene. (#582998) (akozumpl)
- Introduce flags.preexisting_x11. (akozumpl)
- Fix some HIG problems with the "Write Changes" dialog (#583405). (clumens)
- Fix up some HIG problems with the betanag dialog (#583404). (clumens)
- Fixup P_ usage in questionInitializeDASD (hdegoede)
- Prevent low-level formatting of DASDs in rescue mode (#582638) (hdegoede)
- Move the question about formatting DASD's to the interface class (hdegoede)
- Let the user know if adding a zfcp drive fails (#582632) (hdegoede)
- Fixup P_ usage in installinterfacebase (hdegoede)
- Check for presence of filesystem module in FS.mountable (#580520) (dcantrell)
- Check for fs utils when determining if an fs can be resized (#572431)
  (dcantrell)
- Select "Advanced Storage Devices" by default on s390 (#580433). (clumens)
- Don't sigsegv on stage2= derived from invalid repo= parameter (#574746).
  (rvykydal)
- Removed the tooltips showing glade.gnome.org link (#566773) (mgracik)
- Better filter for commits to ignore for the RPM changelog. (dcantrell)
- In groupListExists, log what groups don't exist. (notting)
- Do not append "rhgb quiet" to s390 boot loader config (#570743) (dcantrell)
- No instdata on master anymore. (anaconda.id -> anaconda) (dlehman)
- Try to get boot reqs onto the selected boot device. (#560387) (dlehman)
- Ensure proper disklabel type on boot disk if CLEARPART_TYPE_ALL. (#570483,
  #530225) (dlehman)
- Add proper support for destruction of disklabels. (dlehman)
- Three small fixes to action sorting. (dlehman)

* Thu Apr 15 2010 Chris Lumens <clumens@redhat.com> - 14.4-1
- There is no rhbz list for non rhel branch builds. (dcantrell)
- pylint up, pychecker down. (clumens)
- Add a script for running pylint on anaconda (hdegoede)
- add_drive_text: Pass interface to iscsi.addTarget (hdegoede)
- Add a questionInitializeDisk method to the rescue interface (#582304)
  (hdegoede)
- Add advanced storage support to rescue mode (#571808) (hdegoede)
- rescue.py: Put our mount / rw, ro, skip question in a loop (hdegoede)
- Move addDriveDialog() and friends to their own class (hdegoede)
- partition_text: Make addDriveDialog() not depend on anaconda.storage
  (hdegoede)
- Fix syntax error in kickstart.py (hdegoede)
- Fix various syntax errors (hdegoede)
- Read ~/.rhbzauth in scripts/makebumpver (dcantrell)
- Simplify HWADDR removal check on s390x (#546005) (dcantrell)
- Set minswap suggestion on s390x to 1 (#466289). (dcantrell)
- Check for and offer to format unformatted DASD devices (#560702). (dcantrell)
- Add /sbin/reboot and /sbin/halt to s390 initrd.img (#571370) (dcantrell)
- Do not append "rhgb quiet" to s390 boot loader config (#570743) (dcantrell)
- Increase ping timeout for gateway/dns server reachability check (#536815)
  (dcantrell)
- Wait on all pids, not just udevd's. (#540923) (pjones)
- Use the new modularized anaconda path in run_test.py. (clumens)
- Fix a mismatched kickstart command as caught by the new test case. (clumens)
- Fix a typo. (clumens)
- Fix "make check" to run the tests against your git checkout of anaconda.
  (clumens)
- Add a test case to verify that kickstart commands use the right handler.
  (clumens)
- filter_gui.py: fixup isProtected changes for biosraid and mpath (hdegoede)
- Write an AUTO ... line to mdadm.conf (#537329) (hdegoede)
- Inherit the ZFCP command from the correct pykickstart class (#581829).
  (clumens)
- Apply yet another translation patch (#573870). (clumens)
- Add bug mapping support to scripts/makebumpver. (dcantrell)
- Makefile.am syntax fixes for the 'bumpver' target. (dcantrell)
- Fix traceback in booty when ppc /boot lives on mdraid (#555272) (hdegoede)
- Call scripts/makebumpver from 'make bumpver' target. (dcantrell)
- Add docs/commit-log.txt explaining git commit log policies. (dcantrell)
- Move 'make bumpver' functionality to scripts/makebumpver (dcantrell)
- Fix some previously difficult-to-translate strings (#573870). (clumens)
- Default to /images/install.img if no dir is given in stage2=hd: (#528809)
  (rvykydal)
- Startup notification in live installer (#530908). (akozumpl)
- init: switch back to tty1 after the installer finishes. (#577380) (akozumpl)
- Don't segfault if proxyUser or proxyPassword are empty (#580226). (clumens)
- yum requires the proxy settings to include a protocol (#576691). (clumens)
- Allow using pre-existing gpt labels for /boot on non EFI x86 (#572488)
  (hdegoede)
- Log successful login to iscsi targets (hdegoede)
- storage/udev.py handle iscsi ID_PATH IPV6 address containing : (#579761)
  (hdegoede)
- Catch errors when downloading the escrow cert (#579992). (clumens)
- fix: mnemonics don't work in the welcome screen until user clicks. (akozumpl)
- refactoring gui.py: setup_window() and setLanguage() are way too similar.
  (akozumpl)
- gui.py: removed unused parameter in setup_window() (akozumpl)

* Tue Apr 06 2010 Chris Lumens <clumens@redhat.com> - 14.3-1
- Sort partition create actions before other unpartitioned devices.
  (#574379) (dlehman)
- Update the partition scheme icons to better looking ones (#579697).
  (clumens)
- Move some kickstart-specific storage init into storageInitialization.
  (clumens)
- Call the right superclass's __init__ method. (clumens)
- Adjust paths that reference things that have moved. (clumens)
- Move compiled things out of /usr/lib/anaconda-runtime. (clumens)
- Move boot files, language data, keymaps, etc. to /usr/share/anaconda/.
  (clumens)
- Move class Anaconda to __init__.py. (clumens)
- Install classes are now under the anaconda module directory. (clumens)
- lang-table and lang-names have moved to /usr/share/anaconda. (clumens)
- upd-instroot no longer needs to explicitly pull in the python parts.
  (clumens)
- Adjust command stubs to use new anaconda module location. (clumens)
- Put /usr/lib*/python?.?/site-packages/pyanaconda at the front of
  PYTHONPATH. (clumens)
- Adjust the Makefiles to install anaconda to /usr/lib{,64}/python?.?.
  (clumens)
- ui: keep the bootloader device dialog always centered (#463489). (akozumpl)
- Reword the filter UI tooltip to be a little more clear (#576144). (clumens)
- Automatically select devices added via the "Add Advanced" button
  (#579051). (clumens)
- Re-Check minimum size of partition after running fsck on it (#578955) (bcl)
- Take the request's format into account when deciding to resize (#578471).
  (clumens)
- Schedule removal actions for any format on a --onpart= device (#576976).
  (clumens)
- Fix early networking log message to correctly assign blame. (pjones)
- Restore xdriver=<driver> functionality (#577312) (msivak)
- loader: con Newt into thinking LANG is always en_US.UTF-8 (#576541).
  (akozumpl)
- network.dracutSetupString(): handle hosts outside the subnet (#577193)
  (hdegoede)
- Copy install.img to install target on http installs. (pjones)
- Make sure the install.img exists before attempting to copy (#578391).
  (clumens)
- Write rd_CCW when root fs is on a network device on s390x (#577193)
  (dcantrell)
- Keep /usr/bin/seq for the initrd.img (#558881). (dcantrell)
- fix: Tackle race condition issues during X startup. (akozumpl)
- Make checksum error message user-friendlier (#578151) (rvykydal)
- Enable network if it is needed when repo is added in UI (#577803).
  (rvykydal)
- Do not try to commit diskLabels on non partitionable devices (#576145)
  (hdegoede)
- Copy install.img and remount no matter how many discs (#577196) (pjones)
- Fix typo in linuxrc.s390. ctm should be ctcm. (dcantrell)
- Remove dasdSetup() from loader. (dcantrell)
- Add new return code check for isomd5sum's mediaCheckFile (#578160).
  (rvykydal)
- Use symbolic constants of libcheckisomd5 (#555107) (rvykydal)
- Adapt for libcheckisomd5 callback abi change (#555107) (rvykydal)
- Include /sbin/*_cio_free commands in s390x initrd.img (#558881).
  (dcantrell)
- Use /sbin/dasd_cio_free to free blacklisted DASDs (#558881) (dcantrell)
- Don't add duplicates to the transaction set (#575878, jantill). (clumens)
- fcoe: sysfs_edd.sh has been renamed to fcoe_edd.sh (hdegoede)
- Fix off-by-one error in string initialization (#577413) (msivak)
- Fix uninitialized variable compile error (#577501) (msivak)
- Do not write OPTIONS=layer2=1 on all architectures (#577005). (dcantrell)
- Show protected devices in the filter UI, but make them immutable
  (#568343). (clumens)
- Turn protected devices into a property on the Anaconda object. (clumens)

* Thu Mar 25 2010 David Lehman <dlehman@redhat.com> - 14.2-1
- Unlock the CD tray door in isys.ejectcdrom() (#569377) (pjones)
- Try to pull in generic libraries as well as optimized ones (#572178)
  (pjones)
- Translate the Back button in glade (#576082) (akozumpl)
- Make the kernel 'sshd' parameter work as expected (#572493) (akozumpl)
- Add originalFormat handling to editLVMLogicalVolume. (#576529) (dlehman)
- Fix a cut&paste error that caused a traceback (#574743) (dlehman)
- Remove isys/str.c, replace calls with glib.h or string.h calls. (dcantrell)
- Only look for extended partitions on partitioned devices (#576628)
  (hdegoede)
- Fix referring to disks by-label, by-uuid, etc (#575855). (clumens)
- fcoe startEDD() add missing return statement (hdegoede)
- Add support for recognizing BIOS EDD configured FCoE drives (#513018)
  (hdegoede)
- Update format of cdrom devices when looking for repos on media (#566269)
  (rvykydal)
- Fix syntax for passing a mapping to a translatable string (#576085).
  (clumens)
- Update filter for translation log entries. (dlehman)

* Mon Mar 22 2010 David Lehman <dlehman@redhat.com> - 14.1-1
- Don't pass size=1 for autopart PVs. Use PartitionDevice's default size.
  (dlehman)
- Update po/POTFILES.in to list all files with strings. (dcantrell)
- platform.py: _diskLabelType is a string itself (hdegoede)
- Make python start with correct default unicode encoding (#539904).
  (akozumpl)
- Add boot= argument to kernel cmdline when in fips mode (#573178) (hdegoede)
- Catch NotImplementedError when scanning for disklabels (#566722) (hdegoede)
- BIOS RAID sets get shown double when adding advanced storage (#574714)
  (hdegoede)
- Filter UI do not start / stop BIOS RAID sets to get there size (#574587)
  (hdegoede)
- Make filter UI honor nodmraid cmdline option (#574684) (hdegoede)
- Properly align the first partition we create (#574220) (hdegoede)
- Move disabling of cylinder alignment to disklabel format (hdegoede)
- put the analog script into the RPM (akozumpl)
- Fix focus, repaint, and stack issues for nm-c-e (#520146) (rvykydal)
- Connect nm-connection-editor to network config button (#520146). (rvykydal)
- Add "Configure Network" button to network UI screen (#520146). (rvykydal)
- Add nm-connection-editor to stage2 (#520146). (rvykydal)
- l10n: Updates to Spanish (Castilian) (es) translation (gguerrer)
- Don't try to set selinux context for read-only mountpoints. (dlehman)
- Derive stage2= from repo=nfsiso: correctly (#565885) (rvykydal)
- Include USB ATA bridge modules in initrd (#531532) (rvykydal)
- Remove hacks that don't apply in present repo setup flow. (rvykydal)
- Reset comps/groups info after editing repo in UI (#555585) (rvykydal)
- Set cache base directory for repos added/edited in UI. (rvykydal)
- Use None, not '', for empty repo proxy attributes (#572460) (rvykydal)
- livecd: show graphical error dialog when memory check fails (#572263)
  (akozumpl)
- l10n: Updates to Sinhala (si) translation (snavin)
- use isSparc not isSPARC (dennis)
- set the bootloader to silo for sparc installs (dennis)
- sparc64 is a lib64 arch (dennis)
- Make sure that SPARC bootdisk Makefile is made (dennis)
- make sure we include sparc boot configs (dennis)
- add function to get the sparc system type (dennis)
- Sparc bootloader config not written to /etc (dennis)
- Fix generation of boot.iso on SPARC (dennis)
- l10n: Updates to Polish (pl) translation (raven)
- Keep the selected device count right when going back to filtering
  (#572882). (clumens)
- Fully qualify _ped.IOException. (dlehman)

* Mon Mar 15 2010 David Lehman <dlehman@redhat.com> - 14.0-1
- Do not crash on .autorelabel when using read only rescue mount (#568367)
  (msivak)
- parted.PartedDisk can throw IOExceptions too (#573539) (hdegoede)
- l10n: fix/updates to hungarian translation (snicore)
- l10n: updated translations (snicore)
- Use the disk name from kickstart in the shouldClear error message.
  (clumens)
- Fix displaying error messages on cleanup/remove callback problems
  (#572893). (clumens)
- Before running shouldClear, make sure a real disk was specified (#572523).
  (clumens)
- Fix: execWithRedirect() unexpectedkeyword argument 'searchPath' (#572853)
  (hdegoede)
- Tell ld.so and friends not to use hardware optimized libs (#572178)
  (pjones)
- By default, libcurl does not appear to follow redirects (#572528).
  (clumens)
- FcoeDiskDevice.dracutSetupString: handle DCB on / off option (hdegoede)
- Redo the 'sshd' flag. (ajax)
- Catch "Exception" when window manager is starting. (akozumpl)
- Preserve encryption setting when re-editing new encrypted LVs. (#568547)
  (dlehman)
- Never pass "<Not applicable>" as mountpoint to format constructors.
  (dlehman)
- Fix up device dialogs' handling of preexisting formatting. (dlehman)
- Set up devices using their original formats for certain action types.
  (#565848) (dlehman)
- Keep a handle to devices' original format instance. (#565848) (dlehman)
- Pick up system's clock settings on upgrade. (#570299) (akozumpl)
- Do not crash when getDevices returns NULL (#567939) (msivak)
- Use new API in libblkid to look for driverdiscs on removable devices
  (#508242) (msivak)
- Use new package structure of firstaidkit (#510346) (msivak)
- Add "crashkernel=auto" to grub.conf for RHEL installs (#561729) (hdegoede)
- Drop iscsi initrd generation hack (hdegoede)
- Fix recognition of partitions on mdraid arrays (#569462) (hdegoede)
- dcbd is being replaced with lldpad (#563790) (hdegoede)
- Use the same cache directory as yum now uses (#568996). (clumens)
- exception.py: switch to tty1 before exit (#569071) (akozumpl)
- Reset conditionals of transaction info too. (#505189) (rvykydal)
- Use '--keyword=P_:1,2' for plural gettext string extraction (#567417).
  (dcantrell)
- make sure the new logging also works when isys is imported as a python
  module. (akozumpl)
- use the new logging approach in imount.c (akozumpl)
- allow logging into program.log and syslog through log.c (akozumpl)
- log.c: factor out common parts from logMessageV() (akozumpl)
- static variable rename in log.c (akozumpl)
- move log.c from loader into isys. (akozumpl)
- Analog, a generator of rsyslog config files to monitor remote installs.
  (akozumpl)
- Remove isys/minifind.c and isys/minifind.h (dcantrell)
- Keep default metacity schema generated for gconf. (#520146) (rvykydal)
- metacity, fix a displaying problem with WaitWindow and ProgressWindow
  (#520146) (akozumpl)
- Nuke addFrame()'s showtitle parameter (#520146). (akozumpl)
- Remove gui code we no longer need when mini-wm is gone (#520146) (akozumpl)
- Remove mini-wm.c. (#520146) (akozumpl)
- Introduces metacity window manager (#520146) (akozumpl)
- fix: do not initialize the install interface whenever is is accessed
  (#565872) (akozumpl)
- Select/Deselect All should only apply to the current tab (#516143,
  #568875). (clumens)
- Don't try to write firewall and auth information twice (#568528). (clumens)
- Fixes bug #569373 - Change udev_trigger block calls to use change action
  (bcl)
- Include the report module and related support files (#562656). (clumens)
- report handles exn saving now, and doesn't require a Filer (#562656).
  (clumens)
- Adapt to using report's UI API (#562656). (clumens)
- Do some editing of package and filter UI strings (#569039). (clumens)

* Thu Mar 04 2010 Chris Lumens <clumens@redhat.com> - 13.33-1
- On live installs, the syslog is /var/log/dmesg. (#568814). (clumens)
- Set up udev environment so anaconda's udev rules run in livecd. (#568460)
  (dlehman)
- Ignore probably-spurious disklabels on unpartitionable devices. (#567832)
  (dlehman)
- The justConfigFile parameter doesn't do anything on x86, either (#568567).
  (clumens)
- Add python-devel's gdbinit, which provides useful debugging macros.
  (pjones)
- Minor style fix (indent "cat" correctly") (pjones)
- doReIPL should return when going back through steps, too (#563862).
  (clumens)
- Skip the filter/cleardisk steps on upgrades, too (#568334). (clumens)

* Thu Feb 25 2010 David Lehman <dlehman@redhat.com> - 13.32-1
- Check for the real device-mapper nodes in /proc/swaps. (#567840) (dlehman)
- It's necessary to give each vfprintf invocation a fresh va_list (#568235)
  (akozumpl)
- Don't unconditionally unskip the partition step on failure (#567889).
  (clumens)
- rpm doesn't always give the callback a tuple (#567878). (clumens)

* Wed Feb 24 2010 David Cantrell <dcantrell@redhat.com> - 13.31-1
- Revert "There is no kernel-PAE package anymore, use kernel for xen
  (#559347)." (dcantrell)
- logging: make loader say 'loader' (#563009). (akozumpl)
- Make loader log into syslog (so remote logging works for it as well)
  (#524980) (akozumpl)

* Tue Feb 23 2010 Chris Lumens <clumens@redhat.com> - 13.30-1
- Revert "Add back hald for Xorg input device queries (#553780)" (clumens)
- No longer remove persistent udev rules files (#566948). (clumens)
- When BUILDARCH==ppc64, set BASEARCH to ppc (#524235). (dcantrell)
- There is no kernel-PAE package anymore, use kernel for xen (#559347).
  (dcantrell)
- Fix a typo, leaving one less string needing translation (#567427).
  (clumens)
- Don't show BIOS RAID and multipath members in the cleardisks UI (#567281).
  (clumens)

* Mon Feb 22 2010 David Cantrell <dcantrell@redhat.com> - 13.29-1
- DiskLabel.status can't be determined so return False. (#563526,#561074)
  (dlehman)
- Remove getDasdDevPort() and getDasdState() from isys.py. (dcantrell)
- Replace calls to isys.getDasdPorts() with calls to new getDasdPorts()
  (dcantrell)
- Add getDasdPorts() to storage/dasd.py. (dcantrell)
- Remove isys/dasd.c, functions no longer needed in isys. (dcantrell)
- Fix creation of encrypted md members and pvs in kickstart. (#567396)
  (dlehman)
- Don't align free space geometries in getFreeRegions. (#565692) (dlehman)
- Align extended partitions like we do other partitions. (dlehman)
- Don't allow the host's LD_LIBRARY_PATH affect get_dso_deps (#565887).
  (clumens)
- Remove a couple redundant network bring up calls. (clumens)
- Reset the resolver cache after bringing up the network (#562209). (clumens)
- Let's have /etc/xorg.conf.d in stage2 (#566396) (akozumpl)
- Add the filter UI screens to the list of translatable files (#567216).
  (clumens)
- Don't traceback when a user tries to put /boot on an LV (#566569)
  (hdegoede)
- RescueInterface should inherit from InstallInterfaceBase too (hdegoede)

* Fri Feb 19 2010 Chris Lumens <clumens@redhat.com> - 13.28-1
- Allow --ignoremissing to work for @base and @core (#566752).
  (clumens)
- Add device node names to the filter UI, hidden by default (#566375).
  (clumens)
- logging: initialize tty3 logging in anaconda_log, along with all other
  basic loggers. (akozumpl)
- logging: introduce stderr logger and use it for critical situations in
  kickstart.py. (akozumpl)
- logging: Loggers live a cosmopolitan life, forget about them after
  created. (akozumpl)
- logging: remove AnacondaLog's unused default parameter. (akozumpl)
- logging, fix: setting remote logging from kicstart (akozumpl)
- logging: addFileHandler does not set autoLevel by default (akozumpl)
- Allow deleting the interface property, too (#566186). (clumens)

* Tue Feb 16 2010 Chris Lumens <clumens@redhat.com> - 13.27-1
- Fix hiding the advanced button on the filter UI (#555769, #565425,
  #560016). (clumens)
- PartitionDevice._setDisk: self.disk can be None. (#565930) (dlehman)
- Add currentSize method to the PartitionDevice class (#565822) (hdegoede)
- Fix instData removal mis merge (hdegoede)
- Require a format to have a mountpoint before testing for RO (#565879).
  (clumens)
- The step is named cleardiskssel, not cleardisksel (#565873). (clumens)
- Use the LUKS UUID, not the filesystem UUID for dracut. (#561373) (dlehman)
- Show the correct device path when formatting as swap or luks. (dlehman)
- Fix ordering of arguments to xfs_admin for writing fs label. (#556546)
  (dlehman)
- Log only the disks' names in PartitionDevice._setDisk. (dlehman)
- Check for the updates directory before using it (#565840). (clumens)
- Fix a handful of simple pychecker errors. (clumens)
- Add the .libs directories to PYTHONPATH so pychecker works again. (clumens)
- Warn when ignoring BIOS RAID members (#560932) (hdegoede)
- Intel BIOS RAID array not recognized (#565458) (hdegoede)
- Fix traceback in filter_gui.py when dealing with RAID10 BIOSRAID (#565444)
  (hdegoede)
- Remove newly added partition from disk if subsequent commit fails.
  (#559907) (dlehman)
- Use property() so we can assign to anaconda.intf (#565639). (clumens)
- Don't always set anaconda.upgrade to be True (#565622). (clumens)
- Re-remove the end of line from pychecker-false-positives. (clumens)
- cryptPassword is not part of any class (#565611). (clumens)
- Fix another missing import (#565599). (clumens)
- Add a missing import (#565592). (clumens)
- createLuserConf is not a part of any class (#565306). (clumens)

* Fri Feb 12 2010 David Lehman <dlehman@redhat.com> - 13.26-1
- Fix return values for dasd_settle_all() in linuxrc.s390 (#558881).
  (dcantrell)
- Don't reset the default package selection on text installs (#564103).
  (clumens)
- Remove rules handled by the device-mapper package's rules. (dlehman)
- Raise default lvm extent size from 4MB to 32MB. (dlehman)
- Add udev_settle after setup of LUKSDevice. (#534043) (dlehman)
- Pass '--force' to vgremove to avoid interactive prompts. (#563873)
  (dlehman)
- Find rsyslog libs in $LIBDIR not /usr/$LIBDIR (jkeating)
- "_Do_ override BASEARCH with BUILDARCH, it does make sense (#524235)"
  (msivak)
- Don't traceback during kickstart if no ignoredisk line is given (#563581).
  (clumens)
- Allow any add-on python module to be updated via an updates.img. (clumens)
- Correct references to lcs and ctcm devices (#561816). (dcantrell)
- Use lsznet.raw from s390utils package (#563548). (dcantrell)
- Revert "Write ARP=no to ifcfg file when VSWITCH=1 is set on s390x
  (#561926)." (dcantrell)
- Use /sys/devices/lcs instead of /sys/devices/cu3088 (#561816). (dcantrell)
- Wait for all DASDs to be online after autodetection (#558881). (dcantrell)
- Prompt user for install method when going back to STEP_METHOD. (dcantrell)
- Set initrd load address to 32MB for s390x (#546422). (dcantrell)
- Only show the error message if there was an error. (dlehman)
- Be even more clear about removing existing linux installations. (#493360)
  (dlehman)
- Improve reboot modes in init.c and shutdown.c. (akozumpl)
- Be more explicit in which libraries we link with. (clumens)
- Do not override BASEARCH with BUILDARCH, it doesn't make sense (#524235)
  (msivak)
- platform.checkBootRequest(): Fix use of map instead of filter (hdegoede)
- Improve platform.checkBootRequest() mdarray handling (hdegoede)
- Fix backtrace when trying to use LV for /boot (#562325) (hdegoede)
- Add lsusb to rescue mode stage2 (#562616) (hdegoede)
- No longer refer to instdata in attrSkipList. (clumens)
- Clarify which storage exceptions are bugs (#557928). (clumens)
- Merge branch 'no-instdata' (clumens)
- Fix partitioning help spelling (#562823). (clumens)
- Keep the end sector aligned when resizing partitions (#560647) (hdegoede)
- Write ARP=no to ifcfg file when VSWITCH=1 is set on s390x (#561926).
  (dcantrell)
- Don't return the passphrase from hasKey. Should return a boolean. (dlehman)
- Fix splitting of error strings from program.log. (dlehman)
- Take advantage of default size for new partitions. (dlehman)
- Add a default size of 500MB for new partition requests. (dlehman)
- Remove check for MD_DEVNAME from udev_device_is_md. (#562024) (dlehman)
- Don't try to specify bitmap for RAID0 since mdadm doesn't allow it.
  (#562023) (dlehman)
- Use 0 for a default max_req_size instead of None. (dlehman)
- Add missing methods to RescueInterface (pjones)
- Clean up imports in __main__. (clumens)
- Nothing uses InstallData anymore, so it can completely be removed.
  (clumens)
- Last attribute out of InstallData, please turn out the lights. (clumens)
- Move firstboot into the Anaconda object. (clumens)
- Move bootloader into the Anaconda object. (clumens)
- Move escrowCertificates into the Storage object. (clumens)
- Move storage into the Anaconda class. (clumens)
- Move desktop to the Anaconda object. (clumens)
- Move timezone to the Anaconda object. (clumens)
- Move firewall into Anaconda. (clumens)
- Move users and security to the Anaconda object. (clumens)
- Move network to the Anaconda object. (clumens)
- Move keyboard to the Anaconda object. (clumens)
- Move instLanguage to the Anaconda object. (clumens)
- Move the writeKS and write methods from InstallData to Anaconda. (clumens)
- Move upgrade-related data to the Anaconda object. (clumens)
- Make a bunch of Anaconda attributes into properties. (clumens)
- Move instProgress to be an attribute on the InstallInterface. (clumens)
- Finally remove the x_already_set hack. (clumens)
- Move instClass to be an attribute on Anaconda. (clumens)
- Use anaconda.ksdata instead of anaconda.isKickstart. (clumens)
- Move ksdata to be an attribute on Anaconda. (clumens)
- Remove backend and other pointless attributes from InstallData. (clumens)
- Move the isHeadless attribute onto the Anaconda class. (clumens)
- Set displayMode on the anaconda object, then refer to that everywhere.
  (clumens)
- Sort the attributes on class Anaconda for my future reference. (clumens)
- Install classes may no longer force text mode. (clumens)
- Add a Requires: for tigervnc-server (#561498). (clumens)

* Wed Feb 03 2010 David Lehman <dlehman@redhat.com> - 13.25-1
- Fix keymaps-override-ppc pickup in mk-images (#524235) (msivak)
- Fix typo in action sorting. Disklabels before partitions. (#560017)
  (dlehman)
- Display ID_PATH for zFCP devices instead of looking for a WWID. (clumens)
- Fix a variety of filtering UI problems caused by switching models around.
  (clumens)
- Add ID_SERIAL in as a backup in case there's no ID_SERIAL_SHORT. (clumens)
- Display ID_PATH instead of WWID for DASDs as well. (clumens)
- Rename the WWID column to Identifier. (clumens)
- Enforce maximum partition sizes. (#528276) (dlehman)
- Log commands as a string instead of as a list of strings. (dlehman)
- Strip off the timestamp from error output pulled from program.log.
  (dlehman)
- Fix: execWithRedirect() logging stderr at wrong loglevel. (akozumpl)
- Fix: execWithCallback() not logging stderr. (akozumpl)
- Fix:  ArithmeticError: Could not align to closest sector (#561278)
  (hdegoede)
- Fixed parsing of strings with multiple values in pyudev (mgracik)
- On text kickstart installs, doBasePackageSelect still needs to run
  (#559593). (clumens)
- Remove unused udev_parse_block_entry() function (hdegoede)
- Fixed the problem with string to list properties (#560262) (mgracik)

* Mon Feb 01 2010 Chris Lumens <clumens@redhat.com> - 13.24-1
- Don't log the size of what we're unpacking anymore. (clumens)
- Fixup partition aligning (#560586) (hdegoede)
- Fix backtrace when adding mdraid arrays (#560360) (hdegoede)
- pyudev: explicitly specify all return value and argument types (#559394)
  (hdegoede)
- Correctly add found multipath devices to our dict (#560029). (clumens)
- gtk.TreeStores are iterable, so use indices instead of iterators. (clumens)
- Build sorted models on top of filtered models to make column sorting work.
  (clumens)
- Skip the filtering UI if there's only one disk in the machine. (clumens)
- Allow getScreen methods to indicate the screen should be skipped. (clumens)
- rename constants and a variable in anconda_log.py so the names make more
  sense. (akozumpl)
- anaconda, storage and yum: log to tty3 in the same format as we log into
  tty4 (akozumpl)
- Remove /sys prefix in udev_enumerate_devices() (hdegoede)
- Use libudev's enumerate_devices function (#559394) (mgracik)
- Update =~ regexps in lsznet.raw for bash-4.1 (#558537). (dcantrell)
- Startup iscsi / fcoe / zfcp before listing drives in the filter UI
  (hdegoede)
- cleardisk_gui: Fix going back to the cleardisks gui (hdegoede)
- cleardisk_gui: Base autoselection of bootdev on detected BIOS order
  (hdegoede)
- Fix typo in partition_ui_helpers_gui.py (hdegoede)
- Remove no longer used isys EDD code (hdegoede)
- Hookup new python EDD code (#478996) (hdegoede)
- Add pure python EDD code parsing and compareDrives substitute (#478996)
  (hdegoede)
- Include /etc/netconfig in the initrd for NFS (#557704). (clumens)
- Log system messages to /tmp/syslog instead of /tmp/messages.log. (clumens)
- Make sure we always check /lib64 and /lib in find_library (#555669).
  (dcantrell)
- Make sure we get required nss-softokn libs in the images. (dcantrell)
- Add 5 second ping delay for gateway and dns test on s390x (#536815).
  (dcantrell)
- Update =~ regexps in linuxrc.s390 for bash-4.1 (#558537). (dcantrell)
- Add strace to the stage2 image and initrd. (clumens)
- multipath gives us CCISS devices names with ! in them, but we expect /.
  (clumens)
- Fix visibility counting on filter notebook pages. (clumens)
- Fix thinko in displaying the first filter notebook page that disks.
  (pjones)
- DMRaidArrayDevice don't pass major/minor to DMDevice.__init__ (#558440)
  (hdegoede)
- Filter UI: don't show cciss controllers without sets (hdegoede)
- Filter UI: give BIOS RAID sets a usable model string and display that
  (hdegoede)
- Make MDRaidArray description the same as DMRaidArray (hdegoede)
- Add DMRaidArrayDevice description and model properties (#558440) (hdegoede)
- DMRaidArrayDevices exist when created (#558440) (hdegoede)
- Clarify syslinux menu text (#557774) (hdegoede)
- Use description property for MDRaidArrayDevice model (hdegoede)
- MDRaidArrayDevice: Get rid of the ugly self.devices[0].type checking
  (hdegoede)
- Make storage.unusedMDFoo also check mdcontainer members (hdegoede)
- Remove MDRaidArrayDevice biosraid property (hdegoede)
- Give MD BIOS RAID arrays there own type (hdegoede)
- Check for devices with no media present in filter_gui.py (#558177)
  (hdegoede)
- multipath requires libaio.so (pjones)
- init, fixes a bug in getSyslog() causing a SEGV (akozumpl)

* Fri Jan 22 2010 Chris Lumens <clumens@redhat.com> - 13.23-1
- Only /boot needs to be on one of the bootFSTypes. (#557718) (dlehman)
- nss files moved around again, NM needs more (#557702) (dcantrell)
- Fix broken log message. (pjones)
- MDRaidMember.__str__ add biosraid attribute to the returned string
  (hdegoede)
- Remove setting of _isDisk and _partitionable from iscsi and fcoe disk code
  (hdegoede)
- Add isDisk property to MDRaidArrayDevice (hdegoede)
- Make isDisk a property (hdegoede)
- Remove DMRaidDevice.mediaPresent method (hdegoede)
- Honor clearPartDisks when clearing whole disk formatting formatted disks
  (hdegoede)
- Fixup MDRaidArrayDevice.biosraid (hdegoede)
- Update exclusiveDisks when handling mdraid BIOSRAID in isIgnored (hdegoede)
- MDRaidDevice does not have serial, vendor or bus arguments (hdegoede)
- Don't traceback on devices without a serial (hdegoede)
- Make addUdevPartitionDevice add lvm filters for ignored partitions
  (hdegoede)
- Remove BIOSRAID see if ignored again code from addUdevPartitionDevice
  (hdegoede)
- Remove special partition handling from isIgnored (hdegoede)
- Fix MDRaidArrayDevice mediaPresent to not depend on paritioned state
  (hdegoede)
- Special handling for mdraid BIOS RAID sets in exclusive disks (hdegoede)
- 2 small mdraid related storage/udev.py changes (hdegoede)
- Fix an infinite loop by properly iterating over the disks store (#557856).
  (clumens)
- Prevent init from telling us its story if the shutdown was planned.
  (akozumpl)
- Add a description attribute to MDRaidArrayDevice (hdegoede)
- Don't do exclusiveDisks checking for BIOS RAID members (hdegoede)
- Fix a syntax error in filter_gui.py (hdegoede)
- Make multipath support use device-mapper-multipath to setup mpaths.
  (pjones)
- Make PartitionDevice have its own teardown() when used with mpath. (pjones)
- Create multipath.conf (pjones)
- Make sure MultipathDevice is setup correctly. (pjones)
- List biosraids w/ disks and don't include them w/ md arrays in partgui.
  (dlehman)
- Add biosraid property and use it in MDRaidArrayDevice.partitionable.
  (dlehman)
- Make partitionable a property of StorageDevice instead of a plain attr.
  (dlehman)
- Remove the multipath name generator, it is no longer used. (pjones)
- Set StorageDevice.exists before calling Device.__init__ (pjones)
- Add another command to .bash_history. (pjones)
- Introducing a proper syslog daemon allows us to remove the syslogd stub we
  have. (akozumpl)
- Merge branch 'forward_all' (akozumpl)
- Python logging is talking to the syslog daemon. (akozumpl)
- make dracut only activate the root LV (#553295) (hdegoede)

* Wed Jan 20 2010 David Cantrell <dcantrell@redhat.com> - 13.22-1
- Add mpath device to selection instead of its constituents. (pjones)
- Make all StorageDevice-s support .vendor and .model (pjones)
- Add a parser for 'multipath -d' output. (pjones)
- Multipath members should not be added to the ignored disk list. (pjones)
- Add udev accessor for ID_MODEL_FROM_DATABASE/ID_MODEL. (pjones)
- Add udev_device_get_multipath_name(). (pjones)
- Use mpath names instead of serials to group them. (pjones)
- Add an exception to use when multipath fails. (pjones)
- Add missing log_method_call()s. (pjones)
- Introduces rsylogd to anaconda (part of #524980) (akozumpl)
- Fix compile problem from 65a3c05. (akozumpl)
- Remove unnecessary free from the rpmextract error handler (msivak)
- Fix SIGSEGV in dlabel feature (#556390) (msivak)
- Support ignore all/reinit all on the disk reinitialization question
  (#512011). (clumens)
- Handle reboot better on s390 (#533198) (dcantrell)
- Reset network setting input counters for IPv4 and IPv6 (#553761).
  (dcantrell)
- Fix reading dasd status sysfs attribute (#536803). (dcantrell)
- Fix whitespace error that was introduced. (pjones)
- setStage2LocFromCmdline() shouldn't strdup so much. (pjones)
- s390 CHPID types must be treated in hex for lookup table to work (#552844)
  (maier)
- Fixed the setting of LD_LIBRARY_PATH in rescue (mgracik)
- Use StorageError insead of enumerating all the different storage errors.
  (pjones)
- Get rid of "stage2param" in parseCmdLineFlags(); it is unused. (pjones)
- Make clearDisksWindow use device.model not device.partedDevice.model
  (pjones)
- Include device-mapper-multipath in stage2.img (pjones)
- Load all scsi_dh_* modules, since they can't be modprobe by aliases...
  (pjones)
- Display the first filter notebook page that has any disks on it. (clumens)
- The firmware and additional-web-server groups no longer exist (#555609).
  (clumens)
- Fix a traceback adding RAID devices to the filtering UI. (clumens)
- reIPL code cleanup in loader (dcantrell)
- Show call depth with spaces in log_method_call() (pjones)
- iutil.execWithRedirect() hasn't used searchPath= since 2006.  Take it out.
  (pjones)
- Look for the SSH config file in /etc/ssh on s390 as well (#555691).
  (clumens)
- Changed the architecture check from __ppc64__ to __powerpc64__ (#555669)
  (mgracik)
- Fix the blkid infinite loop. (#555601) (msivak)
- Testing mode was removed. (rvykydal)
- There's no reason to keep bits of mkinitrd in upd-instroot. (pjones)
- Support the new excludedGroupList in pykickstart (#554717). (clumens)
- Use passed in anaconda parameter instead of relying on handler (hdegoede)
- kickstart.py: Fix stdoutLog not being defined (hdegoede)
- pylint error fixes round 2 (hdegoede)
- Fixup various errors detected by pylint (hdegoede)
- mdraid: various changes to options for new mdraid array creation (hdegoede)
- Emit a dracut setup string for the root device itself (hdegoede)
- Fix path mistakes in dasd_settle() in loader/linuxrc.s390 (dcantrell)
- Do not write HWADDR to ifcfg file on s390x for OSA Layer 2 (#546005)
  (dcantrell)
- Poll DASD status for 'online' or 'unformatted' (#536803) (dcantrell)
- Add back hald for Xorg input device queries (#553780) (dcantrell)
- Support moving multiple rows at once in the cleardisks UI. (clumens)
- Allow disks in the filter and cleardisks UIs to be selected via
  double-click. (clumens)
- Don't log the big parted.Partition string every time we do a flag op.
  (dlehman)
- Check for disklabels on unpartitionable devices. (#539482) (dlehman)
- Make partitioned attr depend on whether the device is partitionable.
  (dlehman)
- Make sure to clear partitions before destroying a disklabel. (dlehman)
- Raise an exception when /etc/fstab contradicts detected fs type (#536906)
  (dlehman)
- Don't include read-only filesystems in fsFreeSpace. (#540525) (dlehman)
- NTFS filesystems are not really modifiable in any real sense. Admit it.
  (dlehman)

* Tue Jan 12 2010 Chris Lumens <clumens@redhat.com> - 13.21-1
- Fix implicit declaration of things in sys/stat.h. (clumens)

* Tue Jan 12 2010 Chris Lumens <clumens@redhat.com> - 13.20-1
- devicetree.devices is a list, not a dict (#554455). (clumens)
- Try to copy the correct traceback file, not anacdump.txt. (clumens)
- Make sure /tmp/DD exists before trying to copy it. (clumens)

* Fri Jan 08 2010 David Cantrell <dcantrell@redhat.com> - 13.19-1
- st_size is off64_t on i386, off_t on others. (dcantrell)

* Fri Jan 08 2010 David Cantrell <dcantrell@redhat.com> - 13.18-1
- RPM version check correction. (dcantrell)

* Fri Jan 08 2010 David Cantrell <dcantrell@redhat.com> - 13.17-1
- fstat->st_size is a long unsigned int, not a long long unsigned int.
  (dcantrell)
- Use libarchive and rpm pkg-config files during build. (dcantrell)
- Take ignoredDisks into account on the filter screen as well. (clumens)
- Don't wait on the filtertype screen on kickstart installs. (clumens)
- Our overridden AutoPart class must be mentioned in commandMap. (clumens)
- Reword filter UI introductory text to be less confusing. (clumens)
- Install the driver discs according to what was loaded in stage1 (msivak)
- Use the updated DriverDisc code in loader (msivak)
- Backport the RHEL5 DriverDisc functionality (msivak)
- Include depmod in stage1 and set it to prefer the DD directory (msivak)
- Add a function to get paths to loaded modules (msivak)
- Add rpm extraction routines (use librpm and libarchive) (msivak)
- Add DriverDisc v3 documentation (msivak)
- When displaying the filter UI, check devices that are in exclusiveDisks.
  (clumens)
- get rid of global import of anaconda_log (akozumpl)
- introduce loglevel flag and use it in yum's tty3 logging (akozumpl)
- Remove LoggerClass but maintain loglevel= functionality (akozumpl)
- Do not duplicate exclusiveDisks when going back to filtering UI. (rvykydal)
- Fixes problems in the manual network configuration screen in loader with
  IPv6. (akozumpl)
- Bring back missing IPv6 pieces that were lost in time. (dcantrell)
- Add configuration option to enable/disable IPv6 support. (dcantrell)
- Ask about LVM inconsistencies only in storageinit step. (rvykydal)
- Ask about disk initialization only in storageinit step. (rvykydal)
- Fix partition request sorting based on number of allowed disks. (#540869)
  (dlehman)

* Wed Jan 06 2010 Chris Lumens <clumens@redhat.com> - 13.16-1
- Add libblkid as a BuildRequires. (clumens)

* Wed Jan 06 2010 Chris Lumens <clumens@redhat.com> - 13.15-1
- Also remove requirement for libbdevid (hdegoede).
- Update the python-pyblock version requirement, too. (clumens)
- Bump the required version numbers on a couple of components. (clumens)
- ID_BUS is not always defined (on virt, for instance) so handle that.
  (clumens)
- opts should always be treated as a list inside isys.mount(). (clumens)

* Mon Jan 04 2010 Chris Lumens <clumens@redhat.com> - 13.14-1
- Include fontconfig files needed for scaling of Meera fonts (#531742,
  #551363). (clumens)
- Don't write dracut kernel cmdline paramters to anaconda-ks.cfg (hdegoede)
- Write dracut rd_NO_foo options to grub.conf (hdegoede)
- Add dracutSetupString methods to all relevant device classes (hdegoede)
- Avoid duplicate kernel cmdline options and cleanup booty dracut code
  (hdegoede)

* Wed Dec 23 2009 Chris Lumens <clumens@redhat.com> - 13.13-1
- lsreipl from s390-utils uses incorrect path (hamzy).
- fix for a bug in 05ce88b2 that split one line over several in program.log
  (akozumpl)
- Dump the initial and final state of the system's storage devices. (dlehman)
- Add a "dict" attribute to Device and DeviceFormat classes. (dlehman)
- Sort Storage.devices by name (not path) for consistency. (dlehman)
- Put fsprofile support back in. (dlehman)
- Fix reset of lvm filtering (#527711) (rvykydal)
- Fix bootloader driveorder dialog. (rvykydal)
- Fix selection of default boot target in UI (#548695) (rvykydal)
- 'cleardiskssel' typos that made it impossible to run text install.
  (akozumpl)

* Fri Dec 18 2009 David Cantrell <dcantrell@redhat.com> - 13.12-1
- Use the per-disk flag to disable cylinder alignment for msdos disklabels.
  (dlehman)
- Don't include advanced devices in the total count on the basic filter UI.
  (clumens)
- For iSCSI devices, put the path into the UI instead of a WWID. (clumens)
- Add udev_device_get_path. (clumens)
- Make Callbacks._update_size_label callable from outside the object.
  (clumens)
- Do not show the "Add Advanced" button on the basic filtering screen.
  (clumens)
- Log into program.log through the standard python logging (part of
  #524980). (akozumpl)
- Fix typo from commit 13022cc2. (dlehman)
- Restore accidentally removed line in backend.py (hdegoede)
- yuminstall: Fix indentation error (hdegoede)
- No need to special case ignoring of dmraid sets (hdegoede)

* Wed Dec 16 2009 Chris Lumens <clumens@redhat.com> - 13.11-1
- Clean up setting paths on preupgrade (jvonau). (clumens)
- And call freetmp, too. (Jerry)
- Add a method to remove /tmp/install.img on low memory conditions (jvonau).
  (clumens)
- Make sure /mnt/stage2 is mounted before trying to unmount. (Jerry)
- Skip the mediaDevice check before attempting to mount the install.img.
  (Jerry)
- Remove install.img from /boot during preupgrade. (Jerry)
- Add __str__ methods to the DeviceFormat classes. (dlehman)
- Expand PartitionDevice.__str__ to include partition geometry and flags.
  (dlehman)
- Hide biosraid member devices that contain MDRaidMember formats. (dlehman)
- Move disklabel handling into handleUdevDeviceFormat with the others.
  (dlehman)
- DiskDevice.__init__ expects an "exists" parameter, so add it. (clumens)
- Fix multipath filtering. (clumens)
- Log error messages before displaying dialogs. (clumens)
- Include error messages when logging selinux context get/set failures.
  (dlehman)
- Catch failures to set selinux contexts so it doesn't cause a crash.
  (dlehman)
- Fix typo logging failure to get default file context. (dlehman)
- Use DiskLabel.alignment instead of getDiskAlignment. (dlehman)
- Add an alignment property to DiskLabel. (dlehman)
- iscsi.py: Do not translate log messages (hdegoede)
- Make iscsi,etc startup use the iscsi,etc Singletons (hdegoede)
- kickstart: Move onlining of fcoe/iscsi/zfcp devices to parse phase
  (hdegoede)
- Make the fcoe, iscsi and zfcp classes singletons (hdegoede)
- Remove call to no longer existing isys DriveDict method (hdegoede)
- Use the correct yum configuration file when searching for the -logos
  package (kanarip)
- Fix two missing closing parens in previous commits. (clumens)
- Add an interface to select the fancy filtering UI vs. the regular one.
  (clumens)
- Add a step to prompt for the cleardisks UI. (clumens)
- Add a dialog to configure advanced storage devices. (clumens)
- Add an early user interface for filtering storage devices. (clumens)
- Rework the upgrade vs. install screen a bit to make it look nicer.
  (clumens)
- Add the updated and simplified parttype screen. (clumens)
- Add a method to determine whether a device is a CCISS RAID device.
  (clumens)
- Move identifyMultipaths from DeviceTree to devicelibs. (clumens)
- Add a method to return a device's WWID. (clumens)
- Add a method to get the bus/interconnect from udev and store it on
  devices. (clumens)
- Add a vendor getting udev method, though udev doesn't always know it.
  (clumens)
- Add the serial number to all DiskDevices and subclasses. (clumens)
- Put less space between rows and allow text to be longer before wrapping.
  (clumens)
- Allow InstallInterfaces to modify the installation steps. (clumens)
- Default /boot to 500 MB. (clumens)
- Some iscsi cleanups (hdegoede)
- Bring auto discovered drives online before parsing the ks file (hdegoede)
- Make a better effort at tearing down everything before action processing.
  (dlehman)
- Tighten restrictions on the type of disklabel on x86 and EFI boot disks.
  (dlehman)
- Use string instead of parted.diskType for disklabel types. (dlehman)
- A couple of cleanups to warnings about formatting preexisting devices.
  (dlehman)
- Rework udev_settle timeout handling (#544177) (hdegoede)
- Remove smp.c from the Makefile.am, too. (clumens)
- Nothing has a kernel-smp anymore so none of this code is useful. (clumens)
- Get rid of the goofy nested try statements. (clumens)
- update reIPL messages (hamzy)
- Change btrfs command line option (josef)

* Wed Dec 09 2009 Chris Lumens <clumens@redhat.com> - 13.10-1
- Kickstart support for unpartitioned disks. (dlehman)
- Skip disklabel handling for biosraid and multipath members. (dlehman)
- Improve disklabel's name attr so we don't have to hide them anymore.
  (dlehman)
- Hide devices with certain formatting in the main partitioning UI. (dlehman)
- Automatic partitioning support for whole-disk formatting. (dlehman)
- Add support for whole-disk formatting. (dlehman)
- Add per-row control over sensitive property for CheckList and
  WideCheckList. (dlehman)
- Use a function to add a device to the partition gui. (dlehman)
- Don't crash if there's no intf passed to getLUKSPassphrase. (dlehman)
- Remove unused selinux file context functions from isys. (dlehman)
- Use selinux python module for file context operations. (dlehman)
- Obtain device alignment information from parted. (#529051) (dlehman)
- Handle roots with or without trailing "/" in FileDevice.path. (#541473)
  (dlehman)
- sundries.h is no longer used. (clumens)
- Kill yet another unused lodaer flag. (clumens)
- stage1 (init): Make /tmp tmpfs large enough to hold install.img (#540146)
  (hdegoede)
- With flags.setupFilesystems gone, justConfig can be removed from booty.
  (clumens)
- Nothing sets flags.setupFilesystems anymore, so it can go too. (clumens)
- Remove test mode from the loader, too. (clumens)
- Complain if we're started in test or rootPath mode instead of aborting.
  (clumens)
- Remove test mode. (clumens)
- Remove rootPath mode. (clumens)
- Enable method/repo nfs options in stage2. (rvykydal)
- Accept "nfs:" prefix in ks repo --baseurl setting beside "nfs://".
  (rvykydal)
- Display url having invalid prefix in repo editing dialog. (rvykydal)
- Do not traceback on invalid ks repo --baseurl values (#543003) (rvykydal)
- Remove /etc/localtime before trying to copy into it (#533240). (akozumpl)
- Whenever storage code tries to log a method call, do so into the
  'tmp/storage.log' file. (a part of #524980) (akozumpl)
- Make loader log time with milliseconds (part of #524980). (akozumpl)
- Log storage in the same format as the main anaconda log (a part of
  #524980) (akozumpl)

* Tue Dec 01 2009 Chris Lumens <clumens@redhat.com> - 13.9-1
- Improve text mode fcoe interface (hdegoede)
- Fix udev rule to test whether we're in anaconda. (dlehman)
- Fix devicelibs.dm.device_is_multipath support for new udev rules. (pjones)
- Display progress or wait window when creating devices. (dlehman)
- Display progress or wait window when formatting devices. (dlehman)
- Add optional progress windows to devicelibs create functions. (dlehman)
- Force mkswap to do its job. (dlehman)
- Don't try to get dm node or update sysfs path for lvm vgs. (dlehman)
- Log upon leaving installer steps as well as entering (a part of #524980).
  (akozumpl)
- An unitialized variable in iw/partition_gui.py and a typo in kickstart.py
  (akozumpl)
- Add DCB option to text mode FCoE setup (#513011) (hdegoede)
- Add DCB option to GUI FCoE setup (#513011) (hdegoede)
- Add DCB option to kickstart FCoE code (#513011) (hdegoede)
- Add support for DCB to fcoe.py (#513011) (hdegoede)
- Include fcoemon and dcbd in install.img for FCoE DCB support (#513011)
  (hdegoede)
- Add RAID4 support (#541433) (oliva)
- Clear a partition's BOOT flag when formatting it (hdegoede)
- Do not set boot flag when there is already a partition with the flag
  (#533658) (hdegoede)
- Fixes a syntax error in commit b495db2cd56c881a7e661ac55bd31069510cf662.
  (akozumpl)
- If /boot is too small to preupgrade, don't allow going back (#499321).
  (clumens)
- One reference to earlyKS somehow survived.  Kill it. (clumens)
- Quote backticks when writing out the .bash_history file, and add another
  cmd. (clumens)
- Set the default keyboard based on language before showing the UI
  (#532843). (clumens)
- Don't attempt to get the size of a filesystem unless it's supported
  (#540598). (clumens)
- Require /boot to be on a GPT or MSDOS disk label on x86 (#540588).
  (clumens)
- Fix killall -USR2 anaconda writing out a traceback file. (clumens)
- Only check for DEVICE_DASD in S390.diskLabelType, not for all platforms.
  (clumens)
- Use installclass to make the bootloader timeout 5 seconds on RHEL. (pjones)
- Make sure we get tcp_wrappers-libs installed for stage 2 (pjones)
- Mount usbfs before installing packages (#532397) (mmatsuya)
- Use fs with largest amount of freespace to store install.img (hdegoede)
- Always update booty drivelist before filling bootstore (#533335) (hdegoede)
- Enhance drive specification for clearpart, ignoredisk, and partition.
  (clumens)
- Add a function that determines which devices match a given shell glob.
  (clumens)
- Extend udev_resolve_devspec to allow specifying devices in more ways.
  (clumens)
- Name log files something that doesn't conflict with the system (#539542).
  (clumens)
- Adds interactive install support for NFS options (#537764) (akozumpl)
- Introduces check_asprintf macro that checks asprintfs return value and
  terminates program in OOM scenarios. (akozumpl)
- Sleep if the kickstart file read fails (#537361) (akozumpl)
- Move libcurl initialization to urlinstTransfer() (#537870). (dcantrell)
- Replace all popt use with glib's option parsing code. (dcantrell)
- Clean up initProductInfo() in loader.c. (dcantrell)
- Use glib string parsing functions in driverselect.c. (dcantrell)
- If a package has %%pre/%%post scriptlet errors, abort the install
  (#531599). (clumens)
- If a package has a dependency problem, offer to continue/abort (#511801).
  (clumens)
- Generate more complete device.map grub file when upgrading grub. (#533621)
  (rvykydal)
- Added the libudev python bindings (mgracik)
- If the kickstart log file's path doesn't exist, make it. (clumens)
- Don't make chown or lsetfilecon errors fatal (#529940). (clumens)
- Get correct boot device in reIPL code for s390 (#537390). (hamzy)
- Expand the proxy table a little bit to reduce clutter (#537878). (clumens)
- Use glib data structures in loader's module handling code. (dcantrell)
- Various improvements to kickstart scriptlet reporting (#510636). (clumens)

* Thu Nov 12 2009 David Cantrell <dcantrell@redhat.com> - 13.8-1
- Ignore merge commit messages when generating the rpm changelog. (dcantrell)
- Remove last references to hal. (dcantrell)
- Log calls to DiskLabel's commit and commitToDisk methods. (dlehman)
- Fix DiskLabel.status so it returns True, not self.partedDisk, when active.
  (dlehman)
- Write /etc/dasd.conf to target system on s390 (#533833). (dcantrell)
- Latest dracut has new syntax for rd_DASD. (dcantrell)
- Handle case of not enough space in VG more gracefully. (#533797) (dlehman)
- Make sure partitioning-related drive lists are sorted properly. (#534065)
  (dlehman)
- Remove the early kickstart processing pass (#532453). (clumens)
- Move all the important stuff out of the KickstartCommand.parse methods.
  (clumens)
- These changes require a later version of pykickstart. (clumens)
- commandMap and dataMap are now updates to the existing dict. (clumens)
- Set a reference to the kickstart handler on BaseData objects. (clumens)
- Move exception setup to right after instdata is populated. (clumens)
- Leave one free logical block before each logical partition. (dlehman)
- Use Chunk's geometry attr to access the parted Geometry. (dlehman)
- Fix sorting of requests by mountpoint. It was backwards. (dlehman)
- Align logical partitions' start sector up one logical block for metadata.
  (dlehman)
- Use parted.Device's sectorSize attr instead of physicalSectorSize.
  (dlehman)
- Select partition layout based on potential for growth. (dlehman)
- Reimplement partition growing. (dlehman)
- Create and use a function to obtain a parted alignment for a disk.
  (dlehman)
- Create and use a new function to create and add new partitions to disk.
  (dlehman)
- Make and use a new function to remove non-existent partitions. (dlehman)
- Disable parted's cylinder alignment code. (dlehman)
- Use new functions for conversion between size and sector count. (dlehman)
- Consider whether a partition is growable when choosing free space.
  (dlehman)
- Allocate fixed-size requests before growable requests. (dlehman)
- For the catch-all case, put the message into the UI, not the exn
  (#536854). (clumens)
- Add a missing binary to KEEPFILES (#533237) (msivak)
- Set boot flag for /boot on mdraid 1 array too (#533533). (rvykydal)
- Report no media present for cpqarray controllers with no disks attached
  (hdegoede)
- Honor existing RUNKS conf file variable on s390 (#513951). (dcantrell)
- Add "Hipersockets" to qeth NETTYPE description (#511962). (dcantrell)
- Set custom_icon to error for advanced storage dialog errors (hdegoede)
- When creating a new md array check we have enough members (#533027)
  (hdegoede)
- Convert string.find calls into something modern (jkeating)
- rescue: Don't copy install.ing to /tmp when not enough RAM (#531304,
  #529392) (jvonau)
- isys: remove stray debug printf (#533597) (hdegoede)
- Don't activate / de-activate dmraid sets on setup / teardown (hdegoede)
- Remove previous mdadm bug 523334 workaorund (hdegoede)
- Don't stop mdraid containers or their arrays (#532971) (hdegoede)
- Include the command line to put anaconda into debugger mode in history.
  (pjones)
- Allow remote(ish) debugging. (pjones)
- Make sure /var/log/lastlog is there so we don't have ugly logs. (pjones)
- Correct modopts initialization in loader (take 2) (#531932). (dcantrell)
- Get rid of dead code, and fix gettimespecofday's math. (pjones)
- Don't exec without forking first when calling udevadm. (pjones)
- If init or loader exit unexpectedly, traceback. (pjones)
- Fix the vim magic in this file to work. (pjones)
- Add handling for sshpw command. (pjones)
- Improve createLuserConf behavior and chroot behavior in users.* (pjones)
- Improve logging of ssh-keygen. (pjones)
- Remove tabs in "anaconda" (pjones)
- pidof is a symlink to killall5, so we need that as well. (pjones)
- Correctly initialize modopts in loader (#531932). (dcantrell)
- Increase the size of /boot a little bit (#530555). (clumens)
- Modify autopart requests to include a separate /home (#150670). (clumens)
- Take the spec's requiredSpace into account when creating LVs. (clumens)
- Add the PartSpec.__str__ method for debugging. (clumens)
- Trim the inital / off the mountpoint before making an LV name from it.
  (clumens)
- Remove "anaconda" from attributes to skip (#532612, #532737). (clumens)
- Fix status for and consolidate handling of '-' in vg/lv names. (#527302)
  (dlehman)
- Rename "setupShellEnvironment" to "setupSshd".  That's all it does.
  (pjones)
- Put "killall -USR2 anaconda" in a pre-populated history. (pjones)
- Only try to split proxy commands out if there's actually one specified.
  (pjones)
- Consolidate the parsing of nfs: locations for ks= and stage2= (#529197)
  (stijn)
- Copy cio_ignore kernel parameter to zipl.conf on s390 (#475675).
  (dcantrell)
- Do not modify /etc/hosts from setup package (#530343). (dcantrell)
- In execWithCallback(), support disabling stdout echo (#528386) (dcantrell)
- Select drives in partition dialog, preserving settings. (#529931) (dlehman)
- Clear pot and po updates after a 'make release' or 'make archive'.
  (dcantrell)
- Use the new anaconda image in fedora-logos (#529267). (jkeating)
- Call udev_trigger with a "change" action and don't filter out dm devices.
  (dlehman)
- Remove unused attr_nomatch keyword argument from baseudev.udev_trigger.
  (dlehman)
- Fix logging of isys mount/umount into program.log. (rvykydal)
- Fix "resize failed: 1" errors for ext2/ext3/ext4 (#517491). (dcantrell)
- Log why we're exiting the installer in storage.DASD.startup() (dcantrell)
- Improve detailedMessageWindow() in text.py. (dcantrell)
- Use 'zerombr' kickstart command for DASDs needing dasdfmt (#528386).
  (dcantrell)
- Add 'zerombr' to list of early kickstart commands we look for. (dcantrell)

* Thu Oct 29 2009 Chris Lumens <clumens@redhat.com> - 13.7-1
- TypeError: '_ped.DiskType' object is not callable (#531730) (hdegoede)
- Fix upgrade of GRUB with md raid boot for versions F11 and earlier.
  (rvykydal)
- Remove another code duplication in grub upgrade code. (rvykydal)
- Remove code duplication, use fixed code from writeGrub. (rvykydal)
- Remove target parameter from grub installation code - it is no more
  needed. (rvykydal)
- Remove support for IUCV networking devices on s390. (#531494) (dcantrell)
- Find and format any unformatted DASD devices (#528386). (dcantrell)
- Improve detailedMessageWindow() in text.py. (dcantrell)
- Create execWithCallback() function in iutil. (dcantrell)
- preexist -> onPart (#531407). (clumens)
- Add sshd support for non-s390 platforms. (pjones)
- When doing initlabel on a dasd disk create a dasd disklabel (#531209)
  (hdegoede)
- Rename platform.diskType to platform.diskLabelType (hdegoede)
- Fix arrow key cycling in the Edit Partition dialog (#519641). (clumens)
- Provide a single checkbox for a minimal install (#523839). (clumens)
- Fix DASD and zFCP device discovery (#530287). (dcantrell)
- Clarify the shrink target message (#530789). (clumens)
- Re-enable running udevadm. (clumens)
- max_logical -> max_logicals (#530786). (clumens)
- Filter out device-mapper devices when doing a udev_trigger. (dlehman)
- Expand udev_trigger to allow attr filtering and action specification.
  (dlehman)
- More udev fixups for device-mapper and cryptsetup temp devices. (#526699)
  (dlehman)
- Add the bcm5974 kernel module needed for some touchpads (#474225).
  (clumens)
- /boot is already being checked by the superclass, so don't check again.
  (clumens)
- Allow /boot to be on a variety of filesystems during kickstart (#529846).
  (clumens)
- Platform.bootloaderPackage -> Platform.packages (clumens)
- Bootloader choice strings were marked with N_, but never translated
  (#530017). (clumens)
- Handle more than x.y version numbers in 'make bumpver'. (dcantrell)
- Mark live device as protected instead of ignoring it. (#517260) (dlehman)
- Don't force logical with a free primary slot and an extended. (#527952)
  (dlehman)
- Use rpm to determine how to set bootloader args and default runlevel
  (#527520). (clumens)
- Improve message given to user for fsck failures (#527626). (dcantrell)
- 'Packages completed' string should use P_() instead of N_(). (dcantrell)
- Reintegrate reipl to trigger reboot/halt on s390x correctly. (#528380)
  (maier)
- Put the icon back on the Back button on livecd installs (#526925).
  (clumens)
- Make LOADER_FLAGS_NOSHELL default also for s390x not just s390 (#527063)
  (maier)
- Adapt standalone shutdown to nokill changes so s390x can use it. (#528380)
  (maier)
- Add dracutSetupData() method to DASDDevice (#526354). (dcantrell)
- Collect DASD kernel parameter information during device tree scan
  (#526354). (dcantrell)
- Add dracutSetupString() method to ZFCPDiskDevice (#526354). (dcantrell)
- Write LAYER2 and PORTNO correctly as parts of OPTIONS to ifcfg for s390x
  (maier)
- Don't set unnecessary multipath defaults. (pjones)
- Add a "File Bug" button to all possibilitys in turnOnFilesystems
  (#528006). (clumens)
- For cmdline mode, add the long text to what messageWindow will print
  (#528006). (clumens)
- Use /dev/mapper/live-osimg-min instead of the old device node name
  (#526789). (clumens)
- Remove double slash from nfs:// ks repo value for use in UI. (rvykydal)
- Make bootLoaderInfo new-style class, so that its properties work
  correctly. (rvykydal)
- liveinst: deactivate mdraid arrays before running liveinst (#528235)
  (hdegoede)
- Set parted filesystemtype for swap partitions (hdegoede)

* Tue Oct 13 2009 David Cantrell <dcantrell@redhat.com> - 13.6-1
- BR system-config-keyboard (dcantrell)

* Tue Oct 13 2009 David Cantrell <dcantrell@redhat.com> - 13.5-1
- Remove extra echo in 'make rpmlog'. (dcantrell)
- Do not traceback if network device doesn't have HwAddress property
  (#506013). (rvykydal)
- Fix liveinst to (1) not unmount /dev/pts, (2) unmount in order (509632).
  (clumens)
- Do not read DASD data from /tmp/install.cfg in booty (#526354). (dcantrell)
- Merge branch 'master' of ssh://git.fedoraproject.org/git/anaconda (notting)
- Support upgrading when the language isn't in lang-table (#528317).
  (clumens)
- Fix task selection when tasks contain the same group. (#528193) (notting)
- Update drivelist with bootloader --driveorder ks option instead of
  replacing it (#506073). (rvykydal)
- Use ID_SERIAL to write multipath.conf, but ID_SERIAL_SHORT for UI. (pjones)
- Don't run 70-anaconda.rules on an installed system (#527781). (clumens)
- Handle Installation Repo (base repo) as any other in repo edit UI.
  (rvykydal)
- Fix methodstr editing dialog. (rvykydal)
- Store methodstr url of repo (#502208, #526022). (rvykydal)
- Show user of which repository he edits the url (methodstr editing).
  (rvykydal)
- Don't traceback with malformed repo= nfs: parameter. (rvykydal)

* Mon Oct 12 2009 David Cantrell <dcantrell@redhat.com> - 13.4-1
- Missing volume_key shouldn't break LUKS support completely. (#526899)
  (dlehman)
- Write multipathd.conf in anaconda so that dracut can find it. (pjones)
- We moved from dialog to newt.. (#528497) (msivak)
- Fix a segfault when stage2= boot parameter and kickstart url method is
  used (#524417). (rvykydal)
- Fix parsing of optional portnr in iscsi target IP (#525118) (hdegoede)

* Fri Oct 09 2009 David Cantrell <dcantrell@redhat.com> - 13.3-1
- Reset PartitionDevice attributes after failed edit. (#498026) (dlehman)
- Add MultipathDevice.getDMNode(), because .updateSysfsPath() needs it.
  (pjones)
- Add MultipathDevice.updateSysfsPath() (pjones)
- Run implantisomd5 on boot.iso on x86. (bz#526902) (pjones)
- Consider encryption when checking for duplicate mountpoint. (#526697)
  (dlehman)
- Fix grub stage1 installation for /boot on md raid1. (rvykydal)
- Do not show the VNC-over-text question, when there is not enough memory
  for GUI (#527979) (msivak)
- Fix filtering out of 'Sending translation for' log messages in bumpver.
  (rvykydal)
- Use addUdevPartitionDevice() for adding dmraid / multipath partitions
  (#527785) (hdegoede)
- Set partedPartition system to the correct FS when creating an FS (hdegoede)
- Reset parted flags in createFormat not destroyFormat (hdegoede)
- Default to mbr bootloader target for mdraid 1 boot device too (#526822).
  (rvykydal)
- Clear out state before calling XkbGetState. (clumens)

* Thu Oct 08 2009 Radek Vykydal <rvykydal@redhat.com> - 13.2-1
- Override fstabSpec in PartitionDevice for by-path DASD (#526364). (dcantrell)
- Create DASDDevice objects for DASD devices when building devicetree.
  (dcantrell)
- Add udev_device_is_dasd() to detect DASD devices. (dcantrell)
- Change existing call to deviceNameToDiskByPath(). (dcantrell)
- Make storage.devices.deviceNameToDiskByPath() more robust. (dcantrell)
- Do not copy over 70-persistent.rules if instPath is '' (#527707) (dcantrell)
- Filter out 'Sending translation for' log messages in bumpver. (dcantrell)
- Don't copy _raidSet, but merely pass around a reference (hdegoede)
- Action...Format setup device before modifying the partition table (hdegoede)
- map() -> filter() in storage.writeEscrowPackets() (dcantrell)
- lokkit has moved to a subpackage, so require that (#523709). (clumens)
- Stop trying to run xrandr (#527678). (clumens)
- Only initialize escrow packet code if there's devices that need it (#527668).
  (clumens)
- On lookup of a PartedDevice also check for _ped.DeviceException (#527699)
  (hdegoede)
- Set related ayum attributes if media is found when editing methodstr
  (#515441). (rvykydal)
- In repo editing UI do not use object we are creating (#515441). (rvykydal)

* Tue Oct 06 2009 David Cantrell <dcantrell@redhat.com> - 13.1-1
- Tell udev to ignore temporary cryptsetup devices. (#526699) (dlehman)
- Have redhat.exec reference generic.prm, not redhat.parm (dcantrell)
- Bring back cio_ignore=all, !0.0.0009 for generic.prm on s390x (#463544)
  (dcantrell)
- Take 70-persistent-net.rules generated at installation (#526322)
  (dcantrell)
- Use $LIBDIR to find the boot-wrapper file. (jkeating)
- formatByDefault: Don't traceback when mountpoint is None (#522609)
  (hdegoede)
- Don't warn /usr should be formatted when "Format as:" is already selected
  (hdegoede)
- Bring up network interface before trying to use it for FCoE (hdegoede)
- DMRaidArray: Don't report no media present when in teared down state
  (hdegoede)
- Wait for udev to settle before trying to find dmraid sets in udev DB
  (hdegoede)
- Implement the double click for free space on the bar view (jgranado)
- Pass only cCB and dcCB to the StripeGraph classes. (jgranado)
- React to a double click on a "free row" in the tree view. (jgranado)
- Create getCurrentDeviceParent function. (jgranado)
- Make sure we don't exceed the 80 character threshold (jgranado)
- Display an LVM graph on the bar view when we click on the VG's free space
  (jgranado)
- Add a free row in the LVM tree view when necessary. (jgranado)
- Reorganize the tree view related to lvm. (jgranado)
- Remove unneeded variable (jgranado)

* Mon Oct 05 2009 David Cantrell <dcantrell@redhat.com> - 13.0-1
- Remove an errant popd. Probably cut/paste error. (jkeating)
- Only add the .img file to .treeinfo if it exists. (jkeating)
- Make the netboot dir before trying to use it (jkeating)
- Only write network --netmask if one has been defined (#527083). (clumens)
- Add --label to anaconda-ks.cfg if needed (#526223). (clumens)
- Fix existing size calculation for NTFS (#520627) (dcantrell)
- Write label to filesystem if we have one set (#526226, #526242) (dcantrell)
- Add wget to the initrd, which is required for rhts. (clumens)
- Fix the check for no /boot request on PPC yet again (#526843). (clumens)
- Surround the stage2= parameter in quotes for RHEL (#526863). (clumens)
- Correct makeupdates script to work with deleted files. (jgranado)
- Stop dragging mkinitrd into the install (hdegoede)
- Add --keyword=P_ to xgettext command arguments. (dcantrell)
- Use named parameters for translatable strings with multiple params.
  (dcantrell)
- Change 'support' to 'supported' in UnknownSwapError dialog (#526549)
  (dcantrell)
- Force interface up before checking link status (#525071). (dcantrell)
- Only ignore partitions <1MB that are freespace. (#526445) (dlehman)
- Try to include error messages in lvm/mdadm exceptions. (dlehman)
- Add the create LV option. (jgranado)
- Give the proper orientation to the gtk objects. (jgranado)
- Show the information message when user hits a non-bar element. (jgranado)
- Control the sensitivity of the "delete" and "create" buttons (jgranado)
- Respond to double click on a VG, LV and RAID device. (jgranado)
- Remove the "Hide RAID/LVM" checkbox. (jgranado)
- Display a message in the bar view when user has no selected items.
  (jgranado)
- Cosmetic changes. (jgranado)
- The StripeGraph class does not need tree nor editCB (jgranado)
- Restrain from outputing any digits after the decimal point. (jgranado)
- Add a slice when the extended partition contains "free space" (jgranado)
- Reduce message size in clone screen. (jgranado)
- Add Slice size to the bar view (jgranado)
- Select the device in the treeview when its selected in the barview.
  (jgranado)
- Make canvas a class method. (jgranado)
- Incorporate all the Graph types in the custom screen. (jgranado)
- Add the Volume Group and md RAID array Graph classes (jgranado)
- Make the Bar View Code generic. (jgranado)
- Pass the device instead of the name to the add funciton. (jgranado)
- Display the device path with a smaller font and different color. (jgranado)
- Display bar view for the selected device only. (jgranado)
- Fix indentation in editCB (jgranado)
- Organize the creation of the custom screen into sections. (jgranado)
- Use a checkmark from a PNG image instead of a string. (jgranado)
- Put the size after the device name in the storage tree. (jgranado)
- Add the warning message for an invalid create. (jgranado)
- Reorganize the Customization screen a little. (jgranado)
- Remove unneeded functions & add the about messages for LVM and RAID.
  (jgranado)
- Have an intermediary screen for the "Create" action. (jgranado)
- New screen for "Create" action. (jgranado)
- New function to tell us if there is free space for a new partition.
  (jgranado)
- Edit LVM LV when user has a LV selected. (jgranado)
- Don't fail to commit partitions due to active lvm/md. (dlehman)
- Create and use DiskLabelCommitError for failure to commit. (dlehman)
- Work around partition renumbering in processActions. (dlehman)
- Re-get preexisting partitions using their original path. (dlehman)
- Don't store a copy of ActionDestroyFormat's device attr. (dlehman)
- Don't retry commiting partition table to disk (hdegoede)
- Stop /lib/udev/rules.d/65-md-incremental.rules from messing with mdraid
  sets (hdegoede)
- Don't try to do format handling on drives without media (#523467)
  (hdegoede)
- Wait for mdraid arrays to become clean before reboot / halt (hdegoede)
- Add repo --proxy= support to kickstart. (clumens)
- Pass the proxy config information to stage2. (clumens)
- Add support for proxies to the command line. (clumens)
- Add proxy support to kickstart in the loader. (clumens)
- Add a function to split up a proxy parameter into its parts. (clumens)
- libcurl supports https in addition to http, so change our tests. (clumens)
- getHostAndPath is only used by the nfs code, so move it. (clumens)
- Add initial loader UI support for proxies (#125917, #484788, #499085).
  (clumens)
- We no longer need our own FTP/HTTP protocol support code. (clumens)
- Get rid of the convertURL/UI functions, make iurlinfo just store a string.
  (clumens)
- Convert urlinstall.c to using the new urlinstTransfer function. (clumens)
- Add proxy support to urlinstTransfer by setting more curl options.
  (clumens)
- Add the urlinstTransfer function, which replaces urlinst*Transfer.
  (clumens)
- Add a function to construct an array of HTTP headers and cache the result.
  (clumens)
- Add a CURL instance to the loader data. (clumens)
- Add checks for libcurl into the makefile process. (clumens)
- Add the packages needed to support libcurl. (clumens)

* Tue Sep 29 2009 David Cantrell <dcantrell@redhat.com> - 12.32-1
- Improve loader messages in parseCmdLineFlags when passing vnc (#526350).
  (maier)
- Update po/anaconda.pot during a 'bumpver' run. (dcantrell)
- Add 'make release' as a synonym for 'make archive'. (dcantrell)
- Whitespace cleanup in loader/net.c. (dcantrell)
- Clean up getHostandPath() debugging messages for host & file. (dcantrell)
- Need an extra  on the PS1 line in /.profile (dcantrell)
- Korean font package name changed (#525597) (dcantrell)
- We can't prompt for new network info in cmdline mode (#526262). (clumens)
- yaboot supports /boot on ext4 (#526219). (clumens)
- bootloader --append= should append, not set the args list (#524004).
  (clumens)
- Don't check if /boot is under the 4MB mark on i/p Series (#526200).
  (clumens)
- "minimal" has been renamed to "core" (#526191). (clumens)
- Remove some unused isys methods. (clumens)
- Make sure the disk holding /boot is setup before setting boot flag
  (#526063) (hdegoede)
- Use temporary repo id for edited object to prevent Duplicate Repo error
  (#524599). (rvykydal)
- Do not delete repo twice or when it had not been added actually (#524599).
  (rvykydal)
- Disable repo before deleting it (#524599). (rvykydal)
- Log more, repo editing UI. (rvykydal)
- Make _enableRepo a little more readable. (rvykydal)

* Fri Sep 25 2009 David Cantrell <dcantrell@redhat.com> - 12.31-1
- Move S390MODS to inside makeBootImages(), remove libiscsi_tcp. (dcantrell)
- Require the latest and greatest python-meh. (clumens)
- Add a stub enableNetwork method for cmdline mode (#525779). (clumens)
- Adapt to python-meh passing a bug description around. (clumens)
- Return None for next part type if all primary slots full. (#524859)
  (dlehman)
- Make sure the Minimal group is selected by default on RHEL installs
  (#524561). (clumens)

* Thu Sep 24 2009 Chris Lumens <clumens@redhat.com> - 12.30-1
- Simplify s390x module list generation. (dcantrell)
- Read cmsfs* commands from $IMGPATH/usr/sbin in mk-images (dcantrell)
- Use correct kernel-bootwrapper on ppc64. (dcantrell)
- Anaconda no longer requires hal. (notting)

* Tue Sep 22 2009 David Cantrell <dcantrell@redhat.com> - 12.29-1
- Updated po/anaconda.pot (dcantrell)
- Remove ui/instkey.glade.h from po/POTFILES.in (dcantrell)

* Tue Sep 22 2009 David Cantrell <dcantrell@redhat.com> - 12.28-1
- Preserve whitespace in $CDLABEL in mk-images.x86 (dcantrell)
- Modify rhel.py installclass for current RHEL development efforts.
  (dcantrell)
- Add --brand switch support to buildinstall script. (dcantrell)
- Remove the installation number screen. (clumens)
- Remove kickstart-docs.txt, since it comes with pykickstart (#515168).
  (clumens)
- ybin, mkofboot, and ofpath moved from /usr/sbin to /sbin (#524608).
  (clumens)
- Honor ignoredisk --only-use. (#514353) (dlehman)
- Make sure user-selected mountpoint is not already in use. (#524584)
  (dlehman)
- Do not raise UI dialog in stage2 if network is set in ks (#487503).
  (rvykydal)
- Use whiptail instead of dialog in rescue mode, supports serial line better
  and looks nicer (msivak)

* Mon Sep 21 2009 David Cantrell <dcantrell@redhat.com> - 12.27-1
- Require at least system-config-keyboard 1.3.1 or higher. (dcantrell)
- Fixes for rhel installclass. (dcantrell)
- Start with all modules from kernel/drivers/s390 on s390x (#524566)
  (dcantrell)
- Do not require dhcpv6-client, package is now obsolete. (dcantrell)
- Take into account snapshots and mirrored volumes in lvm dialogs. (dlehman)
- Add handling for snapshot and mirrored logical volumes to DeviceTree.
  (dlehman)
- Add attrs to LVMLogicalVolumeDevice class for snapshots and mirrored lvs.
  (dlehman)
- Add function lvorigin to determine the name of a snapshot's origin lv.
  (dlehman)
- Add function udev_device_get_lv_attr to retrieve lv attribute strings.
  (dlehman)
- Include hidden volumes and lv attributes in udev db. (dlehman)
- Add 'install' user to start anaconda on s390x. (dcantrell)
- Set a default shell prompt for s390x installs. (dcantrell)
- Do not assume we found a module in addOption() in loader/modules.c
  (dcantrell)
- Do not try to load floppy, edd, pcspkr, or iscsi_ibft on s390x. (dcantrell)
- Handle Esc keypress in (some more) dialogs as Cancel - (#520110).
  (rvykydal)
- All the nss libraries have moved from /lib to /usr/lib (#524410). (clumens)
- Add python-nss as a requirement (#524307, #524313). (clumens)
- Call $LDSO --verify for the binary file -inside- the chroot. This fixes
  building x86 boot images on a x86_64 host system. (thomas.jarosch)
- Just grab everything in a /usr/share/fonts/lohit* directory (#523906).
  (clumens)
- Don't write an empty mdadm.conf (hdegoede)
- Write mdraid arrays to mdadm.conf in sorted order (hdegoede)
- containers and their sets must only have a UUID= parameter in mdamd.conf
  (hdegoede)
- Updated anaconda.pot file. (dcantrell)

* Thu Sep 17 2009 David Cantrell <dcantrell@redhat.com> - 12.26-1
- NetworkManagerSystemSettings.service no longer exists. (jkeating)
- udevsettle is no longer used (udevadm settle is called instead) so don't
  put it in images. (jkeating)
- nm-system-settings is no longer shipped. (jkeating)
- Port from PolicyKit to polkit (jkeating)
- Keep po/anaconda.pot in the source tree (#522072) (dcantrell)
- Do not show Unknown as filesystem type for free space. (dcantrell)
- Catch failures from write(2) in utils/snarffont.c (dcantrell)
- Don't leak fds (#520154) (jgranado)
- Initialize the opts variable. (jgranado)
- Add the help messages for the new options of makeupdates script. (jgranado)
- Revert "The Madan font should no longer be used (apparently).  (#523906)."
  (clumens)
- Fix going back from hd install UI when stage2 is given as boot param
  (#519206). (rvykydal)
- The Madan font should no longer be used (apparently).  (#523906). (clumens)
- Update the pykickstart requirement to reflect the escrow stuff. (clumens)
- add requires for sparc arches on elftoaout and piggyback we need them to
  make the tftp image (dennis)
- copy the sparc boot loader on all sparc arches (dennis)
- make sure we include sparc boot loaders on all sparc arches (dennis)
- make sure we get the sparc64 kernel on sparc (dennis)
- Check whatever contains /boot on PPC as well as the bootable part
  (#523747). (clumens)
- make a call to rpmutils to get the basearch works on all arches that dont
  have anaconda built on the basearch (dennis)
- s-c-keyboard is now provided on all architectures (#523445). (clumens)

* Tue Sep 15 2009 David Cantrell <dcantrell@redhat.com> - 12.25-1
- Use pyblock for device-mapper devices' status. (dlehman)
- load_policy has moved from /usr/sbin to /sbin (#523506). (clumens)
- Collect all modules from modules.{ccwmap|networking} on s390x (#522519)
  (dcantrell)
- Copy cmsfscat from /usr/sbin, not /usr/bin. (dcantrell)
- Remove duplicate search_cu() in linuxrc.s390 (dcantrell)
- Try harder to stop mdraid arrays (hdegoede)
- Log when we are skipping disks without media (hdegoede)
- Don't scan stopped md devices (hdegoede)
- Make udev_get_block_device() return None on failure (hdegoede)
- Do not pass --update=super-minor to mdadm for containers and sets there in
  (hdegoede)
- Write mdadm.conf lines for mdraid container formats (imsm) (hdegoede)
- Really put appended kernel cmdline arguments at the end (hdegoede)
- Install dracut-network when using network storage (hdegoede)
- Make recreateInitrd() generate a dracut initrd (hdegoede)
- Use type of device rather than name in booty target selection. (hdegoede)
- write netroot=fcoe:... to kernel cmdline in grub.conf for dracut (hdegoede)
- write ifname=eth#:MAC to kernel cmdline in grub.conf for dracut (hdegoede)
- write iscsi initiator name to kernel cmdline in grub.conf for dracut
  (hdegoede)
- Make iswmd the default (hdegoede)
- Use new icons in anaconda so we don't look so dated (#515601). (clumens)
- Prevent infinite loop in doClearPartitionedDevice. (dlehman)
- Rename doDeleteDependentDevices to doClearPartitionedDevice for clarity.
  (dlehman)
- Handle Esc keypress in dialogs as Cancel (#520110). (rvykydal)
- Don't use baseurl containing space in yum repo object (#516042). (rvykydal)
- Add escrow support (mitr)
- Add python-{nss,volume_key} to stage2, volume_key to rescue (mitr)
- Update for pykickstart with escrow support (mitr)
- Fix --encrypted when creating volumes in kickstart (mitr)
- Remove the "Remove dmraid Device" button, which isn't even hooked up.
  (clumens)
- Require the right version of system-config-date (#523107). (clumens)
- Fix setting of "Add repository" dialog title. (rvykydal)
- Update state and name of repository in list after editing. (rvykydal)
- Fix busy cursor in repo editing (#518529) (rvykydal)
- Fix busy cursor stack popping when creating formats (#518529). (rvykydal)
- Remove partitions in reverse order when clearing disks. (dlehman)
- Improve the info provided to DeviceAction.__str__. (dlehman)
- Include device id in log lines since partitions can get renumbered.
  (dlehman)
- Don't try to preserve old format attrs when reinitializing pvs. (dlehman)
- remove the no longer used initcb and initlabel DiskDevice.__init__
  arguments (hdegoede)

* Thu Sep 10 2009 Chris Lumens <clumens@redhat.com> - 12.24-1
- dmidecode is in /usr/sbin, not /usr/bin. (clumens)
- Add cmsfscat to the initrd on s390 as well (#522535). (clumens)
- Fix the gawk/awk symlink mess in the initrd (#522535). (clumens)
- No longer use /usr/bin/env (#521337). (clumens)
- It's controlunits, not controlunits.sh. (clumens)
- Get DMRaidArrayDevice's a DiskLabel format when they are added to the tree
  (hdegoede)
- Fix askmethod + stage2= (#516973, #519288, #518194) (rvykydal)

* Wed Sep 09 2009 David Cantrell <dcantrell@redhat.com> - 12.23-1
- initrd-generic.img -> initramfs.img (hdegoede)

* Wed Sep 09 2009 David Cantrell <dcantrell@redhat.com> - 12.22-1
- No longer require xfsdump, since anaconda doesn't use it anywhere
  (#522180). (clumens)
- The zonetab module has moved (#521986). (clumens)
- No longer copy over the CD/DVD repodata or repo config file (#521358).
  (clumens)
- language dracut kernel cmdline should be space seperated (#521113)
  (hdegoede)

* Mon Sep 07 2009 David Cantrell <dcantrell@redhat.com> - 12.21-1
- Require python-meh (#521661) (dcantrell)
- Handle UnknownSwapError when turning on existing swap volumes. (dcantrell)
- Check for a valid interface in swapErrorDialog, exit without one.
  (dcantrell)
- On SuspendError, allow users to skip/format/exit like OldSwapError.
  (dcantrell)
- Raise exception if detected swap volumes are not Linux v1 swap space.
  (dcantrell)
- Handle OldSwapError (#510817) (dcantrell)
- Support a force=True argument on SwapSpace.create() (dcantrell)
- Skip all Makefiles and the liveinst subdirectory in 'make updates'
  (dcantrell)
- Make anaconda know its version number (#520061) (dcantrell)
- Add top back to the stage2 image. (clumens)
- Do not put device node path, but the fs UUID in fstab for mdraid:
  (#519337) (hdegoede)
- Expose common fsset methods and properties in class Storage. (dcantrell)
- Don't display the warning about not enough memory on a VNC install
  (#521109). (clumens)
- The vtoc.h header has moved from the kernel to s390utils (karsten,
  #520830). (clumens)

* Wed Sep 02 2009 David Cantrell <dcantrell@redhat.com> - 12.20-1
- Rename mostlyclean-glade to mostlyclean-liveinst. (dcantrell)
- Handle rootPath referencing a chroot value or actual path (#519665)
  (dcantrell)
- We convert cmdline args to longs in several places, so reduce to a
  function. (clumens)
- Support rootpath overrides in fsset.rootDevice (#519665) (dcantrell)
- Pass anaconda.rootPath to FSSet() (dcantrell)
- Include ui, liveinst, and lang-table strings in po updates (#515411)
  (dcantrell)
- Add some silent make support for sed, mkctype, and other commands.
  (dcantrell)
- Recheck if a partition should be ignored after getting its disk (#518971)
  (hdegoede)
- Fix traceback when editing a pre-existing logical volume (hdegoede)
- Do not traceback on an usb cardreader with no card present (hdegoede)
- Don't identify multi lun usb card readers as multipath (#517603) (hdegoede)
- Device class does not have a format member (hdegoede)
- Device class does not have a path member (hdegoede)
- Simplify language.py to two basic settings, and a lot of support
  (#517569). (clumens)
- clobber is a method of PartedDevice not PartedDisk (hdegoede)
- Remove unused fsFromConfig method (hdegoede)
- allocatePartitions: PartitionCount is a member of PartedDisk not
  DiskDevice (hdegoede)
- New version. (clumens)
- Fix storage/__init__.py:1857: non-keyword arg after keyword arg (hdegoede)
- Remove a bunch of unnecessary semicolons (hdegoede)
- pylint does not like )
- Fix 55:udev_resolve_devspec: Using possibly undefined loop variable 'dev'
  (hdegoede)
- MDRaidArrayDevice.totalDevices is a read only property so don't write it
  (hdegoede)
- storage/__init__.py:471:Storage.exceptionDisks: Undefined variable 'udev'
  (hdegoede)

* Tue Sep 01 2009 Chris Lumens <clumens@redhat.com> - 12.19-1
- NetworkManager changed *again*, use libnm-glib.pc now. (dcantrell)
- Save duplicates from /etc/fstab and don't traceback (#517498). (clumens)
- Update fstab header to reference blkid instead of vol_id. (dlehman)
- Sort fstab entries by mountpoint. (#498354) (dlehman)
- Don't hardcode path to tune2fs. (dlehman)

* Fri Aug 28 2009 David Cantrell <dcantrell@redhat.com> - 12.18-1
- Append s390x packages to PACKAGES list, exclude /sbin/qetharp-2.4
  (dcantrell)
- On kickstart installs, you can't select a different parttype
  (#519137, #520058). (clumens)
- Don't try to create a primary partition if all slots are taken. (#519784)
  (dlehman)
- Fix handling of locked preexisting LUKS devices. (#502310) (dlehman)
- Fix up handling of preexisting partitions. (dlehman)
- Pick up mountpoint set for protected partitions. (#498591) (dlehman)
- Ignore partitions belonging to disks we've reinitialized. (dlehman)
- Handle newly initialized disklabels whether via ks or prompt. (#519235)
  (dlehman)
- Fix some indentation in the disklabel initialization block. (dlehman)
- Use commitToDisk() instead of commit() when only changing flags (hdegoede)
- Update PartitionDevice's partedPartition when the PartedDisks get reset
  (hdegoede)
- Add --localscripts option to buildinstall. (dcantrell)
- Add missing dependencies for linuxrc.s390 and lsznet in mk-images
  (dcantrell)
- Re-enable login of root user in initrd.img (dcantrell)
- Less log clutter with fixing ld64.so.1 symlink in instbin on s390x
  (dcantrell)
- Fix typo in get_dso_deps() for searching /lib on s390x (dcantrell)
- Add hfsplus and netconsole kernel modules (#519756, #519785). (clumens)
- Adapt expandLangs to work with three character base lang names (#517770).
  (clumens)
- Prevent resizes that would go past the end of the disk (#495520)
  (dcantrell)

* Wed Aug 26 2009 Chris Lumens <clumens@redhat.com> - 12.17-1
- dracut has initrd-generic-<version> instead of initrd-<version> (#519185)
  (hdegoede)
- Do not try to commit disks changes to the os while partitions are in use
  (hdegoede)
- disklabel.commit(): DeviceError -> DeviceFormatError (hdegoede)
- A "partition" having no partedPartition shouldn't be a traceback
  (#519128). (clumens)
- Add some debugging code so we know what's going on for #504986 (katzj)
- Fix going back in "Inst. Method" and "Configure TCP/IP" screens in stage 1
  (#515450) (rvykydal)
- Fix going back from stage1 nfs/url setup dialog. (rvykydal)
- When bringing up network in UI, update only ifcfg file of selected device
  (#507084). (rvykydal)
- Update Optional packages button via popup menu too (#515912). (rvykydal)
- Remove the firstadkit-plugin-grub from non-grub archs (msivak)
- Use the path instead of the name for the questionInitialize function.
  (#517926) (jgranado)
- Only add "rhgb quiet" to boot args for non-serial installs (#506508,
  #510523). (clumens)
- On rpm unpack errors, display a fatal error message (#452724). (clumens)
- Use tee thread to ensure line buffered output to screen and log file at
  the same moment... (#506664) (msivak)
- Ensure libraries are copied to initrd.img for xauth (#516369) (maier)
- Import shutil for upgrades (#519011). (clumens)
- Fix focus grabbing on both the password and hostname screens. (clumens)
- x86 and EFI platforms can now have /boot on ext4. (clumens)
- Use the Platform's idea of what filesystem /boot can be on. (clumens)
- zz-liveinst.sh: Restore the #! line (ajax)
- Import _ped so it can be used for _ped.DiskLabelException. (pjones)
- Make sure LV and VG names fit within LVM limits (#517483) (dcantrell)
- Fix updates target to honor KEEP variable correctly. (dcantrell)
- Add support for the reiserfs filesystem (#504401) (dcantrell)
- Update instructions on how to generate source archive. (dcantrell)
- Use disk.description instead of trying to access parted attrs. (#518212)
  (dlehman)
- Fix disk.partedDisk -> disk.format.partedDisk. (dlehman)
- Fix a stupid typo in the logging. (clumens)
- If modifying a repo fails, do not delete it (#516053). (clumens)
- If repo setup fails, also make sure to delete it from yum. (clumens)
- Allow configuring additional NFS repositories, not just the base. (clumens)
- Consolidate "base repo" setup into an extra function. (clumens)
- Allocate memory for login and password and do not meddle with host pointer
  so we can correctly free it (#483818) (msivak)
- Run make in silent mode by default. (jgranado)
- Allow creation of an updates image from a tag offset. (jgranado)

* Tue Aug 18 2009 David Cantrell <dcantrell@redhat.com> - 12.16-1
- correctly deactivate zFCP LUN on s390 (maier)
- correctly activate zFCP LUN on s390 (maier)
- prevent getting started up or shutdown again while already in such state
  (maier)
- Remove unused reipl code in linuxrc.s390 (maier)
- Fix copying of shutdown to initrd.img in mk-images for s390x (#517888)
  (maier)
- 64 bit sparc linux does not define __sparc64__ we need to use
  "(defined(__sparc__) && defined(__arch64__))" fixes building 64 bit sparc
  (dennis)
- make tftp images as small as possible. we have a 10mb hardware limitation
  on there size (dennis)
- make sure we correctly make the sparc tftp image (dennis)
- make sure we have glibc.sparcv9 installed in sparc installers not
  glibc.sparcv9v (dennis)
- add the sparc screen font (dennis)
- add the files for sparc boot config setup configure.ac to define IS_SPARC
  (dennis)
-  add mk-images.sparc script (dennis)
- add support for making sparc images (dennis)
- sparc no longer needs and special keyboard handling.  it uses the standard
  api's interfaces (dennis)
- setup termcap for sparc (dennis)
- Close %%packages with a %%end (#518063) (katzj)
- Call udev_settle from DiskLabel.commit to ensure it happens. (dlehman)
- Fix traceback in text mode upgrade. (#505435) (dlehman)
- Don't traceback if Delete button is hit when no device is selected.
  (dlehman)
- Clean up management of extended partitions we create. (#497293) (dlehman)
- Don't use StorageDevice for partitions w/ biosraid formatting. (#504002)
  (dlehman)
- Don't try to get the size of fstypes w/ no infofsProg defined. (dlehman)
- Change all disklabel manipulations to use the DiskLabel format class.
  (dlehman)
- Create a DiskLabel format class for partition tables. (dlehman)
- Add support for specifying a tag to makeupdates. (dlehman)
- Include changed files from the top level in the updates. (dlehman)
- If asked, put the system SN (as given by dmidecode) into an HTTP header.
  (clumens)
- Add dmidecode to the initrd. (clumens)
- Add the kssendsn parameter and corresponding flag. (clumens)
- Don't keep testing if we're doing URL_METHOD_HTTP. (clumens)
- Later pyparted will define DEVICE_DM, so change the test to use it.
  (clumens)
- Use the new GTK Tooltip API (#517389). (clumens)
- Fix a typo in a kickstart error string (#517760). (clumens)
- Be sure we have a sorted list of mountpoints for live mangling (#504986)
  (katzj)
- Fix askmethod to work with stage= being specified (#516973) (katzj)
- Fix ordering on device list returned from identifyMultipaths() (pjones)
- Fix typo in mpath support. (pjones)

* Wed Aug 12 2009 David Cantrell <dcantrell@redhat.com> - 12.15-1
- Make sure we have the ca cert to handle https repo connections. (517171)
  (jkeating)

* Wed Aug 12 2009 David Cantrell <dcantrell@redhat.com> - 12.14-1
- Correctly inform the user once about obsolete parm/conf file options on
  s390 (maier)
- Handle activation of DASDs in linuxrc.s390 since loader no longer works
  (maier)
- make IPv4 configuration in linuxrc.s390 compatible with NM in loader
  (maier)
- suggest disabled X11-forwarding for ssh login in linuxrc.s390 (maier)
- Fix an erroneous "!" in the test for doKill, and make reboot explicit.
  (pjones)

* Mon Aug 10 2009 David Cantrell <dcantrell@redhat.com> - 12.13-1
- Fix syntax error in identifyMultipaths() (dcantrell)

* Mon Aug 10 2009 David Cantrell <dcantrell@redhat.com> - 12.12-1
- Honor network config boot params for CD-booted ks installs (#433214)
  (dcantrell)
- Include ipcalc command in all initrd.img files, not just s390 (#516084)
  (dcantrell)
- Don't to unmount /mnt/source unless something's mounted there (#516304).
  (clumens)
- Honor nodmraid commandline option (#499733) (hdegoede)
- Don't try to multipath CD devices. (#516362) (pjones)
- booty: Do not strip the trailing p from a devicename like
  mapper/isw_Vol0_tmp (hdegoede)
- booty: isw_Vol0_Stripe is not a disk isw_Vol0_Stri with an e part
  (#505205) (hdegoede)

* Fri Aug 07 2009 Chris Lumens <clumens@redhat.com> - 12.11-1
- upd-instroot: Inspect gtkrc for cursor theme (ajax)
- Support NFS repos in kickstart (#495620, #507093). (clumens)
- upd-instroot: xorg-x11-auth -> xorg-x11-xauth (ajax)
- Check to see if the arch string starts with ppc64. (#516144) (jgranado)
- vtActivate doesn't work on some ppc64 machines, so don't traceback
  (#516206). (clumens)
- Make all sysfs path's be _without_ /sys prefix (#516168) (hdegoede)
- Do not go interactive if timezone in ks is not valid (#473647) (rvykydal)
- Fix going back from "NFS Setup" screen in stage 1 (#507064) (rvykydal)

* Thu Aug 06 2009 David Cantrell <dcantrell@redhat.com> - 12.10-1
- Add missing 'i' in loader/loader.c for non-s390 arches. (dcantrell)

* Thu Aug 06 2009 David Cantrell <dcantrell@redhat.com> - 12.9-1
- Avoid finding the word 'engine' in comments. (jkeating)
- Don't try to get dso deps of statically linked files. (jkeating)
- Call shutDown() correctly for s390 (karsten)
- Remove unused variable from loader/loader.c (karsten)
- Delete unpackaged files on non-livearches. (karsten)
- Do not set parted.PARTITION_BOOTABLE on s390. (root)
- Complete udev setup in linuxrc.s390 for automatic module loading (root)
- Recognize mpath devices when we see them. (pjones)
- Make DiskDevice.partedDisk a property. (pjones)
- Make questionInitializeDisk() somewhat less ugly. (pjones)
- Add a description to DiskDevice, and use it in the UI. (pjones)
- Get rid of Device.description, it is unused. (pjones)
- Close the opened file descriptors when necessary. (#499854) (jgranado)
- Add the glade files to the install image so save-to-bugzilla works
  (#515444). (clumens)
- New system-config-keyboard has a different version then I expected
  (hdegoede)

* Wed Aug 05 2009 Chris Lumens <clumens@redhat.com> - 12.8-1
- Don't try to unmount the CD before we later unmount the CD (#515564).
  (clumens)
- Do not offer going back when ugrade root for ks upgrade is not found
  (#499321) (rvykydal)
- Rebuild .pot file and update translations. (clumens)
- Import the logging stuff (#515564). (clumens)
- Add keyboard kernel cmdline options to grub.conf for dracut (hdegoede)
- Fix backtrace in network.dracutSetupString in the static ip case (hdegoede)
- Write dracut i18n cmdline options to grub.conf (hdegoede)
- Pass InstalltData to booty __init__ as it needs access to many of its
  members (hdegoede)
- Fix ctrl-alt-deleter behavior /before/ end of install. (pjones)
- Merge branch 'master' of ssh://git.fedoraproject.org/git/anaconda (notting)
- No longer use HAL in list-harddrives. (clumens)
- The names of a couple basic udev methods has changed. (clumens)
- Move basic udev methods out of the storage module (#514592). (clumens)
- We do not actually require gtkhtml2 or the python bindings for it.
  (notting)
- Fix some typos in rescue mode (#515091) (msivak)
- Add a dracutSetupString method to network.py (hdegoede)
- Fix backtrace due to iscsi.getNode() not finding the iscsi node (hdegoede)
- Use dracutSetupString() method to add the kernel parameters needed for
  dracut (hdegoede)
- Add a dracutSetupString method to devices.py classes (hdegoede)
- Differentiate between ibft discovered and manually added iscsi disks
  (hdegoede)
- Store iscsi node pointer in iScsiDiskDevice objects (hdegoede)
- When checking logical partition dependcies, make sure the are one the same
  disk (hdegoede)
- Only set iscsi nodes to autostart when none of the LUN's contain /
  (hdegoede)
- Add functions to go from an iScsiDiskDevice to an libiscsi node (hdegoede)

* Fri Jul 31 2009 Chris Lumens <clumens@redhat.com> - 12.7-1
- Fix up udev sillies (related to #514501) (katzj)
- Log when we unmount filesystems so we have a match for mount messages.
  (clumens)
- Let's not exit from buildinstall.functions, say, ever (katzj)
- Rework shutDown() to better accomidate "nokill" better. (pjones)
- Make upgradeany boot option work again (#513227) (rvykydal)
- Update device.map when upgrading (#513393) (rvykydal)
- Catch None devs (katzj)

* Wed Jul 29 2009 Chris Lumens <clumens@redhat.com> - 12.6-1
- Fix CDLABEL substitution in syslinux.cfg for x86 boot.iso (katzj)
- And finish off the removal of rhpl (katzj)
- Use keyboard bits from system-config-keyboard now (katzj)
- Use python-meh instead of our own exception handling now (clumens)
- NM no longer exposes information through HAL (#514501). (clumens)
- Put mkdir into /sbin on the initrd, too. (clumens)
- Make sure controlunits.sh is installed to initrd on s390 (dcantrell)
- Remove ChangeLog (#512502) (dcantrell)
- Add s390utils-cmsfs in upd-instroot for s390 (dcantrell)
- Make sure s390 gets /lib/ld64.so.1 (dcantrell)
- Skip writeDisabledNetInfo() when loader starts on s390 (dcantrell)
- Fix part --onpart= to print the device name instead of the __str__.
  (clumens)
- Just pull in all python modules for stage2 (katzj)
- Trim PACKAGES list in upd-instroot. (dcantrell)
- Update linuxrc.s390 and friends to reflect review comments. (maier)
- Log non-upgradable upgrade candidate roots. (rvykydal)
- unmountFilesystems -> umountFilesystems (#510970). (clumens)
- Disable devel repos on release (#503798) (katzj)
- Work around problems with live installs and dpi other than 96 (#506512)
  (katzj)
- Fix obvious typo in font name (katzj)

* Wed Jul 22 2009 David Cantrell <dcantrell@redhat.com> - 12.5-1
- New build because koji hates me.

* Wed Jul 22 2009 David Cantrell <dcantrell@redhat.com> - 12.4-1
- Add scripts/makeupdates to generate updates.img files. (dcantrell)
- Add python-decorator to the stage2 image for pyparted (#513175). (clumens)
- Set stage2= on x86 boot.iso (katzj)
- Try to auto-find the CD even if stage2= is specified (katzj)
- Make sure we have a device before check if it's protected. (#510033)
  (dlehman)
- Remove unresolvable file devices from the devicetree. (#503830) (dlehman)
- Support multiple fstab entries of a single nodev fstype. (#505969)
  (dlehman)
- Refer to nodev devices as "none", not "nodev". (dlehman)
- Change DeviceTree.devices from a dict to a list. (dlehman)
- Show locked LUKS devices as "Encrypted (LUKS)", not "LUKS". (dlehman)
- Allow creation of four primary partitions on a disk. (#505269) (dlehman)
- Add a bunch more stuff to the initrd needed for networking. (clumens)
- Add more things to /sbin on the initrd that udev requires. (clumens)
- Add dmesg to the images. (clumens)

* Mon Jul 20 2009 David Cantrell <dcantrell@redhat.com> - 12.3-1
- Set GECOS field for new user accounts specific in ks files (dcantrell)
- Show MAC address of network device in text mode too. (rvykydal)
- Fix selection of alternative iface in UI after fail (#507084). (rvykydal)
- Stop the cdrom device before ejecting (#505067) (msivak)
- Add hipersockets to NETTYPE description (bhinson, #511962). (clumens)
- Don't show formatting progress bar after mkfs has exited. (eric_kerin)
- Run firstaidkit-qs script instead of the shell (shows rescue menu)
  (#508512) Add dialog package required for firstaidkit Create /etc/fstab in
  ramdisk to make mount commands easier (#440327) (msivak)
- When ignoring partitions make sure lvm also ignores them (hdegoede)
- 70-anaconda.rules: pass --ignorelockingfailure to lvm invocation (hdegoede)
- Call mdadm -I with --no-degraded for all disks but the last (hdegoede)
- There is no /bin on the initrd so sleep needs to go into /sbin. (clumens)
- Add deviceNameToDiskByPath(). (dcantrell)
- Display drive model and size in MB in partitioning UI (#460697) (dcantrell)
- Lots of small grammar and wording changes. (pjones)
- Edit user-visible dialogs for style. (pjones)
- Get rid of sloppy elipses usage. (pjones)
- Don't write optical devices to /etc/fstab (#505697). (clumens)
- error messages of zFCP on s390: log or pass to the UI (maier)
- correctly delete a SCSI device provided by a zFCP LUN on s390 (maier)
- All other teardown methods take a "recursive" argument (#506166). (clumens)
- Clean yum caches following preupgrade, too (#503096). (clumens)

* Thu Jul 09 2009 David Cantrell <dcantrell@redhat.com> - 12.2-1
- mdmon added to install.img (Jacek.Danecki)
- Remove some unnecessary code. (clumens)
- Use a method yum provides, rather than inventing our own. (clumens)
- Remove _catchallCategory.  yum handles this for us now. (clumens)
- Write out NM_CONTROLLED=no for NICs used for FCoE (hdegoede)
- Add support for biosraid using mdadm (hdegoede)
- Reverse: "Support for MD containers" (hdegoede)
- When all udev_is-foo() checks fail return instead of backtracing (hdegoede)
- 70-anaconda.rules: always import blkid output (hdegoede)
- Make sure to have "self" as an argument. (clumens)
- Add kickstart fcoe command (hdegoede)
- Use the yum preconf object to do $releasever substitution. (clumens)
- Indicate LV status according to lv_attr active bit (#491754) (dcantrell)
- Include lv_attr in lvm.lvs() return value. (dcantrell)
- Fix list of 64-bit arches. (notting)
- We also need -DUSESELINUX if we want to call matchPathContext. (clumens)
- Clean up some arch code. (notting)
- Update /etc/hosts with hostname for loopback IP address (#506384)
  (rvykydal)
- Add missing LAYER2 and PORTNO handling for s390x. (dcantrell)
- Ignore configure.ac when generating updates.img (dcantrell)
- AC_ARG_WITH -> AC_ARG_ENABLE (dcantrell)
- dhclient now reads config files from /etc/dhcp (dcantrell)
- no "rhgb quiet" on s390 to enable visible boot progress and system
  automation (#509881) (maier)
- fix backtrace in s390 reipl support due to missing anaconda.id.fsset
  (#509877) (maier)
- Put sleep in /bin on the initrd (#505639). (clumens)
- Also include the grep programs. (clumens)
- Add programs from vim-minimal, coreutils, and util-linux-ng. (clumens)
- Move programs that aren't s390-specific into the main image. (clumens)
- Look for /bin/sh, not /sbin/busybox. (clumens)
- No longer symlink binaries to busybox. (clumens)
- No longer require busybox. (clumens)

* Mon Jul 06 2009 Chris Lumens <clumens@redhat.com> - 12.1-1
- Include the rest of the libs isys needs to link against (#509572).
  (clumens)
- Add FCoE disks to the devicetree with a type of FcoeDiskDevice (hdegoede)
- Add FcoeDiskDevice class to storage/devices.py (hdegoede)
- Add FCoE support to storage/udev.py (hdegoede)
- Write out configuration of FCoE to installed system (hdegoede)
- Initial FCoE support (hdegoede)

* Thu Jul 02 2009 Chris Lumens <clumens@redhat.com> - 12.0-1
- network --bootproto no longer implies DHCP. (clumens)
- Don't unconditionally skip the network config screen in kickstart. (clumens)
- Allow creating new groups through kickstart. (clumens)
- Set focus on hostname entry in network UI screen (#494135) (rvykydal)
- Fix upgrade selected in UI after storage reset (#503302) (rvykydal)
- Add support for specifying upgrade partition in ks (#471232) (rvykydal)
- Add missing liveinst/* files. (dcantrell)
- Update code that checks for devices that contain install media. (dlehman)
- Rework tracking of devices containing installation media. (#497087) (dlehman)
- Add function storage.udev.udev_resolve_devspec. (dlehman)
- Prevent false positives in devtree's device lookup methods. (dlehman)
- Skip exceptionDisks if exn originated in devtree.populate. (#497240) (dlehman)
- Stop using rhpl.arch in writeRpmPlatform() (katzj)
- Move simpleconfig (back) into anaconda from rhpl (katzj)
- Use iutil arch specifiers rather than rhpl (katzj)
- Remove unused rhpl imports (katzj)
- Switch to using iutil.isS390 instead of rhpl.getArch (katzj)
- Stop using rhpl.translate (katzj)
- Default to /boot on ext4 (katzj)
- Allow /boot on ext4 now that we have a grub that allows it (katzj)
- Make sure the library directory is always set (notting)
- Write out "MAILADDR root" into mdadm.conf (#508321) (rvykydal)
- Do not install grub more times than needed. (rvykydal)
- Ensure we set the SELinux context correctly on symlinks (#505054) (katzj)
- udev dropped vol_id (#506360) (katzj)
- Handle installing multilib into the installer intramfs correctly. (notting)
- Set LIBDIR appropriately on PPC64. (notting)
- Fix grub upgrade (#505966) (rvykydal)
- Include yum.log in anacdump.txt too. (rvykydal)
- Access format options property instead of mountopts attr. (#506219) (dlehman)
- Be more careful about identifying NFS fstab entries. (dlehman)
- Don't add leading directory for files twice. (#503830) (dlehman)
- booty changes for iswmd (Jacek.Danecki)
- Support for MD containers. (Jacek.Danecki)
- New iswmd parameter for kernel cmdline (Jacek.Danecki)
- New udev rule for using mdadm for isw_raid_member (Jacek.Danecki)
- Use isohybrid to make boot.iso a hybrid image (katzj)
- Log yum messages. (rvykydal)
- Tell booty to rescan for bootable drivers when an extra disks get
  added (hdegoede)
- Do not encourage VNC when doing kickstart text installs (#506534) (dcantrell)
- Rename bootstrap to autogen.sh (dcantrell)
- Include the contents of /proc/cmdline in exception reports (katzj)
- Include libwrap library for sshd and telnet in s390 installs (jgranado)
- Enforcing matching rootfs type on LVs as well as for partitions
  (#504743) (katzj)
- Remove problem packages before attempting a re-download (#501887). (clumens)
- Be more explicit about what's lacking on EFI systems (#501341). (clumens)
- If not enough memory is installed, enforce swap partition creation
  (#498742). (clumens)
- Convert to using automake/autoconf. (dcantrell)
- Convert po/ subdirectory to GNU gettext template system. (dcantrell)
- Restructure liveinst/ for the new build system. (dcantrell)
- Add m4/ subdirectory with autoconf macros. (dcantrell)
- Removed py-compile script. (dcantrell)
- Rename anaconda.spec to anaconda.spec.in (dcantrell)
- Ignore autoconf and automake files in the tree. (dcantrell)
- Removed toplevel Makefile and Makefile.inc (dcantrell)
- Show MAC address of network device in combo box (#504216) (dcantrell)
- Remove loader/tr/.cvsignore (dcantrell)
- Increase max NIC identification duration to 5 minutes (#473747). (dcantrell)
- Use /sbin/ipcalc for IP address validation (#460579) (dcantrell)
- Fix an obvious traceback when doing part --ondisk= (#504687). (clumens)
- Catch errors from bootloader installation (#502210). (clumens)
- Remove umask temporarily so device permissions are correct
  (#383531, wmealing).
- Remove the name check on driver disk packages (#472951). (clumens)
- Make the installation key text more descriptive (#474375). (clumens)
- Fix discovery of existing raid/lvm for ks install without clearpart
  (#503310, #503681) (rvykydal)
- Use the F12 version of the bootloader command. (clumens)
- It's /sbin/fsadm, not /sbin/e2fsadm (#504043). (clumens)
- Remove the bootloader --lba32 option. (clumens)
- Use gettext.ldngettext when necessary (#467603) (dcantrell)
- Test NM_CONTROLLED setting correctly in network.py (#502466) (dcantrell)
- Show unknown partitions as "Unknown" in partition editor. (dcantrell)
- Add a type hint on popup windows (rstrode). (clumens)
- Use the F12 version of the driverdisk command. (clumens)
- Remove driverdisk --type, since mount can figure that out. (clumens)
- Fix an error when editing an unreachable repo (#503454). (clumens)
- If /etc/rpm/platform is found, move it out of the way. (clumens)
- We no longer write out /etc/rpm/platform, so don't offer to upgrade
  it. (clumens)
- Remove locals containing "passphrase" or "password" from exns
  (#503442). (clumens)
- Make progress bars modal (#493263, #498553, rstrode). (clumens)
- Make sure to import os.path if we are going to use it. (jgranado)
- ipcalc is copied to /usr/lib. (jgranado)
- Limit the trigger to block type devices. (jgranado)
- We need ipcalc for new s390 installation script. (jgranado)
- Fix off-by-one errors in read. (notting)
- sysconfig file changed names for system-config-firewall (katzj)
- Don't write out firewall settings if they already exist (#502479) (katzj)
- Make sure that the devices are correctly detected (#491700) (jgranado)
- Make the save-to-bugzilla dupe detection smarter. (clumens)
- If network --device=MAC is given, translate to device name
  (#185522). (clumens)
- Add a function to convert MAC addresses to device names. (clumens)
- Move /boot checks from sanityCheck into Platform.checkBootRequest. (clumens)
- Return translated strings from checkBootRequest. (clumens)
- Check that /boot is on a Mac disk label for PPC installs (#497745). (clumens)
- Call checkBootRequest from sanityCheck. (clumens)
- Put some space in that big scary warning. (clumens)
- fond -> found (clumens)
- Use powers of two in swapSuggestion (#463885). (clumens)
- Trim "mapper/" off device names in the bootloader UI (#501057). (clumens)
- Make the weak password dialog comply with the HIG (#487435). (clumens)
- Add a newline to a cmdline mode string (#497575). (clumens)

* Tue Jun 02 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.59-1
- Do not show disabled repos such as rawhide during the install (#503798).
  (jkeating)

* Sun May 31 2009 David Lehman <dlehman@redhat.com> - 11.5.0.58-1
- Pass --force to lvresize so it doesn't ask for confirmation. (dlehman)
- Fix a typo in action sorting for resize actions (fs vs. device). (#501000)
  (dlehman)
- Sending translation for French (mrtom)

* Thu May 28 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.57-1
- Create and use unique ids for Device instances. (#500808) (dlehman)
- Adjust remaining PartitionDevices' names after removing a partition.
  (dlehman)

* Tue May 26 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.56-1
- Ensure matching rootfs type to live type with autopart (#501876) (katzj)

* Tue May 26 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.55-1
- Fix blank network device descriptions in the loader. (#501757) (notting)
- Make sure the right _isMigratable gets used for Ext3FS (#501585). (clumens)

* Tue May 19 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.54-1
- We are not guaranteed to have a partedDisk in the udev code (#501556,
  #501428). (clumens)
- The location of the options wiki page has changed. (clumens)
- Disable BETANAG. (clumens)
- Install a en_US.UTF-8 locale in the first stage image. (notting)
- Reset font when changing language. (notting)
- Set locale to en_US.UTF-8 when initializing the console. (notting)

* Mon May 18 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.53-1
- LVMVolumeGroupDevice stores pesize in MB, kickstart expects it in KB.
  (dlehman)
- Don't schedule a format resize if reformat scheduled. (#500991) (dlehman)
- Deactivate md arrays regardless of state if the device is present.
  (#496441) (dlehman)
- Lame hack to make sure --size= is never 0 (#500905). (clumens)
- Don't filter out partitions that haven't been allocated (#500932).
  (clumens)
- Write out PE size as an integer, since that's what anaconda wants
  (#501049). (clumens)
- Set clearPartType to None on preupgrade too (#499321). (clumens)
- Fix indentation of line to remove cancelled actions from the list.
  (#500932) (dlehman)
- Consider active-idle state of md device as accepatable status of device
  (#497407) (rvykydal)
- Fix detection of cciss disks (#499408) (dchapman)
- Get existing fs size for xfs. (dcantrell)
- Get existing fs size for ntfs. (dcantrell)
- Get existing fs size for jfs. (dcantrell)
- Get existing fs size for ext2, ext3, and ext4. (dcantrell)
- Compute existing filesystem size using fs info utility. (dcantrell)
- Do not allow users to migrate ext4 to ext4. (dcantrell)
- Correct handling of formats on encrypted preexisting LVs. (#499828)
  (dlehman)
- Ignore unrecognized device-mapper devices we find. (#499967) (dlehman)
- loader: Mount /tmp as tmpfs not ramfs so we can swap it out (ajax)
- format.mountpoint -> lvd.mountpoint (#500913). (clumens)
- Treat the loop labels as devices without a label.(#493219) (jgranado)
- Add the partition table partition after initializing (#498602). (clumens)

* Wed May 13 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.52-1
- Add a Mac OS boot line to yaboot.conf (#499964). (clumens)
- Catch IOError when enabling repos (#500439). (clumens)
- Use a newer version of the kickstart Partition command. (clumens)
- Fix a traceback when installing over previous installs on PPC (#499963).
  (clumens)
- Fix a typo when probing exception disks. (clumens)
- Add support for --noformat too. (clumens)
- Add support for --onpart, --ondrive, and --useexisting. (clumens)
- Make the storage.writeKS method useful and called from instdata (#493703).
  (clumens)
- Add writeKS methods to the device objects. (clumens)
- Add writeKS methods to all the format objects. (clumens)
- upd-instroot: Add gdbserver (ajax)
- Remove text-mode syslinux help (katzj)
- If clearPartType is None, don't attempt to clear a device (#499321).
  (clumens)
- Only set clearpart data if the command was provided in the kickstart file.
  (clumens)
- Override previously defined mountpoints in kickstart (#499746). (clumens)
- Yet another font package name has changed (#499322). (clumens)
- Set new mountpoint correctly for existing encrypted LVs. (#496363)
  (dlehman)
- Once a partition is part of another device it cannot be modified.
  (#496760) (dlehman)
- Maintain request sort order by using req_disks instead of parents.
  (dlehman)
- Do not set a parent on the /mnt/sysimage/dev bind mount object (#499724).
  (clumens)
- Skip .pyc files in subdirectories when running make updates. (clumens)
- Remove 'lowres' option. (ajax)
- Run tune2fs on newly formatted ext[34] filesystems. (#495476) (dlehman)

* Thu May 07 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.51-1
- Don't clear the first partition on any disk with a Mac disk label
  (#492154). (clumens)
- Add detailedMessageWindow to the cmdline class (#499700). (clumens)
- Don't traceback when a freespace partition is present (#499662). (clumens)
- Do nomodeset when doing xdriver=vesa (ajax)
- Fix calculation of smallest PV's size in the lvm dialog. (#493753)
  (dlehman)
- Fix KeyError when partition numbers change during allocation. (#497911)
  (dlehman)
- Update EFI CD booting code in mk-images (pjones)

* Wed May 06 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.50-1
- Use storage objects throughout the partition editing UI code (#491806,
  #496002). (clumens)
- Verify filesystems after the live resize (katzj)
- Verify with fsck after resizing filesystems (katzj)
- IBM improvements to linuxrc.s390 (#475350) (dcantrell)
- Write out correct hostname during LiveCD installs (#492515) (dcantrell)
- Enter in hostname entry field advances to next screen (#494135) (dcantrell)
- Check if we'll clear a partition after setting its format attr. (#499251)
  (dlehman)
- Don't pass the default clearPartType value to the device tree. (dlehman)
- Fix some logic errors in storage.partitioning.shouldClear. (dlehman)
- Forward port various iscsi fixes from 5.4 iscsi work (hdegoede)
- Avoid writing out NAME= in ifcfg files (#497485) (dcantrell)
- Retry network configuration in loader (#492009) (dcantrell)
- Make sure /boot ends up on the same disk as Apple Bootstrap (#497390).
  (clumens)
- Handle that the default bootloader entry can sometimes be None (#496618).
  (clumens)
- The PS3 bootloader allows booting from ext4 filesystems (#498539).
  (clumens)
- Support LVM PE sizes > 128MB (#497733) (cristian.ciupitu)
- Set ANACONDAVERSION on most livecd installs. (clumens)
- getDependentDevices is in devicetree, not storage (#499144). (clumens)

* Mon May 04 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.49-1
- Collect network interfaces from NetworkManager (#493995) (dcantrell)
- Handle fstab entries whose filesystem we don't recognize.(#498120)
  (dlehman)
- Add an error signifying an unrecognized entry in /etc/fstab. (dlehman)
- Don't drop discovered format with unknown devices when parsing fstab.
  (dlehman)
- Fix display of paths for device-mapper device in bootloader widget.
  (dlehman)
- Don't call udevDeviceFormat if we're just going to clear the device
  (#497323). (clumens)
- Pass clearPartType to the devicetree as well. (clumens)
- Break the complex should-clear logic out of clearPartitions. (clumens)
- Handle clearpart in the early kickstart pass too. (clumens)
- Correct setting the SELinux context on mountpoints (#494995). (clumens)
- make resetFileContext return the context set (wwoods)
- Allow editing of the hdiso source partition so it can be mounted
  (#498591). (clumens)
- Add a ignoreProtected= parameter to deviceImmutable that does the obvious.
  (clumens)
- Be more aggressive unmounting before install starts (#498260) (katzj)
- Add %%{?dist} to the release number in the spec file. (dcantrell)
- Configure network in kickstartNetworkUp() iff NM is not connected
  (#490518) (dcantrell)
- Don't segfault with "ks someotherparam" (#498307). (clumens)
- Fix the arch upgrade check in yuminstall.py, too (#498280). (clumens)
- Move _resetRpmDb into iutil so we can access it everywhere. (clumens)
- Don't mount bind mounts last, that makes /dev break. (pjones)
- Pass anaconda to storage.FSSet.turnOnSwap. (dlehman)
- Ignore spurious formatting on partitioned devices. (dlehman)
- Revert "DeviceError only returns a message, not (message, device) tuple
  (#496343)." (dlehman)
- Fix action sorting for partitions on the same disk. (#498064) (dlehman)
- Fix traceback in second editing of existing raid dev (#497234). (rvykydal)
- Allow existing LVs with filesystems to be resized (#490913) (dcantrell)
- Rate limit pulse() calls to ProgressWindow. (pjones)
- Don't populate flags.cmdline with "True" values when no = is used. (pjones)
- Add "nomodeset" to the list of command line arguments copied to grub.conf
  (pjones)
- Use device.format.mountType insead of device.format.type for fstab.
  (pjones)
- Initialize x86 class variables before efiBootloaderInfo.__init__() (pjones)
- Fix a segfault on nfs+kickstart (pjones)
- Fix an error when raising FormatCreateException. (clumens)
- Add more windows to the rescue interface class (#498014). (clumens)
- Remove requirement for EFI machines to be x86, since IA64 is too
  (#497934). (clumens)
- Fix the kernel package selection on ppc64 machines (#497264). (clumens)
- Include fsck.ext4 and mkfs.ext4 in the images (#497996). (clumens)
- Properly restore SIGCHLD if X startup fails (wwoods)
- Fix kickstart PV references handling for lvm on raid (#497352). (rvykydal)

* Fri Apr 24 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.48-1
- Fix handling of swap files. (#496529) (dlehman)
- Pass anaconda to turnOnSwap so we can use swap files. (dlehman)
- Fix incorrect attribute name use for retrofit flag. (dlehman)
- Use slightly better checks when testing for 0 size (#493656, #497186,
  #497389). (clumens)
- If the LV has no child, don't attempt to grab its format (#497239).
  (clumens)
- Apply the global passphrase when doing kickstart autopart (#497533).
  (clumens)
- Add support for encryption passphrase retrofits. (dlehman)
- Bring luks_add_key and luks_remove_key back into devicelibs.crypto.
  (dlehman)
- Don't let lvremove failures from incomplete vgs crash the install.
  (#497401) (dlehman)
- Allow setting a mountpoint w/o formatting an encrypted partition.
  (#495417) (dlehman)
- Remove encryption from preexisting device if "Encrypt" is deactivated.
  (dlehman)
- Fix indentation of preexisting partition handling block. (dlehman)
- The device passed to the luks passphrase dialogs is a string. (#492123)
  (dlehman)
- Protect against tracebacks from the partition isFoo properties. (dlehman)
- Fix handling of bind mounts. (#496406) (dlehman)
- Add more filesystem checks. (clumens)
- Support vfat filesystems in the partitioning UI (#496351). (clumens)
- Remove devices in leaves first order (#496630) (hdegoede)
- Don't remove an inconsistent lvm partition from the devicetree (#496638)
  (hdegoede)
- Move isEfi to be a property on Platform instead of on X86 (#497394).
  (clumens)
- Support --encrypted --useexisting on kickstart installs (#497147).
  (clumens)
- When making a RAID device, require that some members be selected
  (#491932). (clumens)
- When catching an OSError, handle it as an object instead of a tuple
  (#497374). (clumens)
- Enforce the fstype that holds /boot on kickstart installs (#497238).
  (clumens)
- Fix ps3 platform support (#497203) (katzj)
- Clean up rpmdb locks at the end of the install (#496961) (katzj)
- Don't allow /boot to be on an encrypted device (#496866). (clumens)
- Use the correct unmount method (#496764). (clumens)

* Tue Apr 21 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.47-1
- Fix adding of fifth partition in UI (#496930). (rvykydal)
- Define the fd variable before it can ever be referenced (#496930).
  (clumens)
- Fix preservation of format attrs for preexisting luks partitions. (dlehman)
- Set md member devices' uuids after creating an array. (dlehman)
- Don't try to get size for nodev and bind filesystems. (dlehman)
- Include the device path in DeviceError exceptions. (dlehman)
- Mdadm's incremental mode ignores the auto option, so don't use it.
  (dlehman)
- Use incremental mode for all md member addition during probing. (dlehman)
- Try to name existing md arrays based on their preferred minor. (dlehman)
- Reimplement mdexamine using a more easily parseable output format.
  (dlehman)
- Fix position of "--run" option to mdadm assemble. (dlehman)
- Handle passphrase prompts without a traceback in cmdline mode. (#492123)
  (dlehman)
- Fix another device vs. string problem in EFI bootloader config (#496669).
  (clumens)
- Add the device's name to mdadm.conf (#496390). (clumens)
- Show normal cursor during passphrase entry (#496534) (msivak)
- Fix traceback in cmdline mode after exception handling cleanup (#496644)
  (katzj)
- DeviceError only returns a message, not (message, device) tuple (#496343).
  (clumens)

* Fri Apr 17 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.46-1
- Clean up argument list after changing from rhpl to iutil for
  execWithRedirect (jkeating)
- Fix NameError traceback setting up bootloader in EFI installs (wwoods)
- No longer force ISOs to be on ext2, ext3, or vfat partitions. (clumens)
- Sending translation for German (ckpinguin)
- Split text mode exn saving into multiple screren (#469380). (clumens)
- Copy /tmp/program.log to /mnt/sysimage/var/log/. (clumens)
- Fix member preselection in raid UI. (rvykydal)
- Fix editing of raid device (persistence of level choice) (#496159)
  (rvykydal)
- Fix ks --useexisting and --noformat options of logvol and volgroup
  (rvykydal)
- Make sure inconsistencies dont screw us up. (jgranado)
- Re-implement the inconsistency functionality. (jgranado)
- Allow the use of "-" in the lvm names. (495329) (jgranado)
- Make sure we "insist" on mdadm commands. (491729) (jgranado)
- [PATCH] Possible fix for some encryption related bugs during the Custom
  Layout editation (#495848) (msivak)

* Thu Apr 16 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.45-1
- Touch /.autorelabel when running under rescue mode (#491747). (clumens)
- Add support for fingerprint-based logins (#481273). (clumens)
- Add a "File Bug" button to the catch-all partitioning exception handler.
  (clumens)
- Remove the early catch-all exception handler (#495933). (clumens)
- Implement the save to USB using devicetree devices. (jgranado)
- Use size instead of currentSize when comparing lv sizes (hdegoede)
- Make sure all pv's of an lv's vg are setup before resizing an lv (hdegoede)
- Do not try to teardown a non existing format (hdegoede)
- Center the bootloader configuration dialog (#495802). (clumens)
- Destroy (potential) stale metadata when creating a new partition (hdegoede)
- use partition req_base_size instead of size in partitionCompare()
  (hdegoede)
- Fix changing size of newly created partitions (hdegoede)
- Don't traceback on invalid filesystem detection (#495156) (dcantrell)
- Check to see if formatcb is None. (jgranado)
- Use the PV name when logging error messages. (jgranado)
- Don't set up the device to obtain minSize anymore. (dlehman)
- Improve estimate of md arrays' size. (dlehman)
- Determine minimum size for filesystems once, from constructor. (dlehman)
- Fix estimate of LUKS header size for newly encrypted devices. (#493575)
  (dlehman)
- Fix two syntax problems with generated mdadm.conf entries. (#495552)
  (dlehman)
- Default to AES-XTS cipher mode with 512 bit key for new LUKS devices.
  (dlehman)
- When going back from a failed shrink, reset the device action set.
  (clumens)
- If we can't communicate while logging in to bugzilla, error (#492470).
  (clumens)
- Make save to usb work. (jgranado)
- We don't always have a formatcb either (#495665). (clumens)
- The entry is named lvsizeentry now. (jgranado)

* Mon Apr 13 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.44-1
- Default to SHA512 password encoding algorithm. (dcantrell)
- Handle format combo box not existing (#495288) (dcantrell)

* Mon Apr 13 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.43-1
- Run programs with LC_ALL=C in case we're parsing output (#492549).
  (clumens)
- A volume group device has a "peSize" attribute (not "pesize"). (dlehman)
- Remove uncommitted new lv from dict on cancel. (dlehman)
- Use the correct value when setting new extent size. (#493753) (dlehman)
- Fix image generation so all ELF binaries have their deps included
  (#495231). (clumens)
- Clean up the code in editLogicalVolume function. (jgranado)
- Setup the disks before partitioning as the nodes are needed. (jgranado)
- Rescan the devices when we are saving a traceback. (jgranado)
- Close file descriptors when an error occurs. (jgranado)
- Aesthetic changes to "editLogicalVolume" function. (jgranado)
- When deallocating a partition also set its disk attribute to None
  (hdegoede)
- Check self.partedPartition not being None before using it (#495077)
  (hdegoede)
- growPartitions: Change op_func (back to) add when an iteration succeeds
  (hdegoede)
- partedPartition can be None while growing partitions (#495076) (hdegoede)

* Thu Apr 09 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.42-1
- Fix display of format type for devices. (dlehman)
- Fix handling of priority option from swap fstab entries. (#494992)
  (dlehman)
- Some fs types cannot be passed to programs (#495061, #493075). (clumens)
- When a new module is loaded, update the kernel_filesystems list. (clumens)
- Add more Indic fonts (#494261, pnemade).
- Remove the message saying you can make your own layout (#495015). (clumens)
- Put e100 (and other) firmware in its own directory if needed (#494778).
  (clumens)
- Run /bin/umount instead of calling umount(2) in _isys.umount (#493333)
  (dcantrell)
- Add doPwUmount() and mountCommandWrapper() to isys (#493333) (dcantrell)
- Preserve symlinks and only collect deps on ELF executables. (dcantrell)
- Use $(ARCHIVE_TAG) throughout the updates target. (dcantrell)
- partedUtils doesn't exist anymore (katzj)
- Revert "Show the header in certain non-lowres cases" (#493153) (katzj)
- Pre-existing partitions names may change (#494833) (hdegoede)
- Use getDeviceNodeName() instead of basename of device node. (hdegoede)
- Fix ks raid --useexisting and --noformat (rvykydal)
- Fix processing of --level and --device options of ks raid commands.
  (rvykydal)
- Don't start pdb immediately in debug mode (katzj)
- Fix EDD BIOS disk order detection in general and make it work with dmraid
  (hdegoede)
- Update extended partition geometry when we change it (hdegoede)

* Tue Apr 07 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.41-1
- Make sure we have a clean lvm ignore list when we initialize. (jgranado)
- We need to search by name without the "mapper" prefix. (jgranado)
- Create a min_max constraint to avoid alignments issues. (jgranado)
- Don't exit the installer from filesystem errors. (dlehman)
- Try not to raise exceptions from minSize calculators. (dlehman)
- Don't traceback when PVs are encrypted or are not partitions. (dlehman)
- Adjust device dependencies when backing out device encryption. (#493257)
  (dlehman)
- Include filesystem type in mount log message. (dlehman)
- Load filesystem modules on demand (#490795, #494108). (clumens)
- Use existing partitions when --onpart is used for PVs or raid members
  (#493065) (rvykydal)
- Raise message, not exception when size set in LV dialog is too big.
  (rvykydal)
- Raise an error when remofing an extended part with logical parts.
  (jgranado)
- Esthetic changes to storage/partitioning.py. (jgranado)
- dmraid.py is no longer being used by anything, so remove it. (clumens)
- Remove partedUtils.py. (clumens)
- This is the only place isEfiSystemPartition is used, so pull it in.
  (clumens)
- getReleaseString now lives in the storage module. (clumens)
- Stop lying about our support for dmraid and multipath in kickstart.
  (clumens)
- Remove some old, unused code that also uses biosGeometry. (clumens)
- For very small disks, don't try to display a stripe in the graph
  (#480484). (clumens)
- Fix reading the console= parameter from the cmdline (#490731). (clumens)
- For dmraid partititons device node name != name (hdegoede)
- When a partition request gets unallocated, set the name back to req#
  (hdegoede)
- Do not use getPartitionByPath() in allocatePartitions() (hdegoede)
- Remove no longer used iscsi_get_node_record function (hdegoede)
- Try to handle devices which live in a subdir of /dev properly (hdegoede)
- Split DeviceTree.addUdevDevice into several smaller methods. (dlehman)
- Don't traceback from failure finding minimum fs size. (#494070) (dlehman)
- udev_settle after format teardown to avoid EBUSY on device teardown.
  (#492670) (dlehman)
- Add a parted.Device attribute to all existing StorageDevices. (dlehman)
- If no partitioning commands are given, apply the UI selections (#490880).
  (clumens)
- Update font package names for ml_IN, si_LK, etc. (#493792, #493794).
  (clumens)
- Fix a typo in the city name for Nepali (#493803). (clumens)
- Fix writing out the partition= line on PPC (#492732). (clumens)
- Do not check size when adding LV to growing VG (bug #492264) (rvykydal)

* Thu Apr 02 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.40-1
- Don't let device names affect action order in general case. (dlehman)
- Round up when aligning to pesize for space used. (#493656) (dlehman)
- Improve handling for various nodev filesystems in fstab. (#493685,
  #493202) (dlehman)
- Present the correct max lv size in the dialog. (dlehman)
- Use the head of the current branch, not master, for scratch archives.
  (dlehman)
- Make a top level StorageError that all others are based on. (dlehman)
- Remove unused PRePDevice class. (dlehman)
- Make the disk model an attribute of DiskDevice. (dlehman)
- Handle format actions in cancelAction() (dcantrell)
- Fix format check box for pre-existing partitions (#491675) (dcantrell)
- Remove temporary directory used in _getExistingSize() (dcantrell)
- Activate storage before looking up the hdiso source drive (#491781).
  (clumens)
- Remove isys.getDeviceByToken since it is no longer used. (clumens)
- Don't allow the rootfs on live installs to not match (#493206, #492727)
  (katzj)
- Create setup and teardown functs for dmraid devs. (jgranado)
- put xfs back where it belongs (sandeen)
- Fix up the other caller of unmountCD to pass in a device (#493537).
  (clumens)

* Wed Apr 01 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.39-1
- Prevent sensitive information in kickstart files from ending up in
  tracebacks. (clumens)
- It's 2009, let's ignore floppy drives now (#493338, #493377). (clumens)
- Remove DmRaidArrayDevice level attribute (#493293) (hdegoede)
- get_containing_device takes two arguments (#493266). (clumens)
- Fix the check for if there's enough space available on / and /usr
  (#492614). (clumens)
- Fix testing if a PPC partition is bootable (#492726). (clumens)
- Look for a PReP "partition" by examining the format, not the flags
  (#492426). (clumens)
- Fix a few more pylint warnings and errors in storage/* (hdegoede)
- Fix some pylint warnings in iw/*.py (hdegoede)
- Don't start our audit daemon with the livecd installer (katzj)
- If there's a problem finding removable disks, disable save-to-disk.
  (clumens)
- Move %%pre processing to much earlier in the install process. (clumens)
- If there are no installs to rescue via kickstart, display an error.
  (clumens)
- Add an early kickstart processing pass. (clumens)
- Fixes of errors shown by pylint that didn't get into the beta build.
  (mgracik)
- Adjust the dmraid ignoring logic. (jgranado)
- Reference the format by type, not name.(#492596) (jgranado)
- Sending translation for Chinese (Simplified) (leahliu)
- Increase udev_settle timeout in udev_get_block_devices. (#492049) (dlehman)
- Fix check for fully defined md array when raidlevel is 0. (#491796)
  (dlehman)
- Fix a typo ('isEFI' should be 'isEfi'). (dlehman)
- Make sure the pvs are set up before doing lvremove or vgremove. (dlehman)
- Don't write out md member devices to a config file for assemble. (dlehman)
- Fix the supported property of filesystems and prepboot format. (dlehman)
- Return early from doAutoPartition if partition allocation fails. (dlehman)
- Reset storage instance if autopart fails. (#492158) (dlehman)
- Assign weights to partition requests when doing manual or kickstart
  installs. (clumens)
- Refresh windows immediately to make sure they appear. (clumens)
- Fix problem with format and migrate combo box activation. (dcantrell)
- Fix typo in upgrade.py (dcantrell)
- Move _scheduleLVs and growLVM calls to be inside try/except (dcantrell)
- Correct bounds checking problems in 'Shrink current system' (dcantrell)
- Require libselinux-python (#489107) (dcantrell)
- Do not prompt for NIC selection in cmdline mode (#492586) (dcantrell)
- Do not write /etc/hosts since setup owns that now (#491808) (dcantrell)
- Remove unused self._resize variable. (dcantrell)
- Having 2 raidsets in the same group of devs is possible. (jgranado)
- getDevice returns a string.  Use that to look up the device object
  (#492465). (clumens)
- Take into account i386->i586 when warning on upgrade arch mismatch.
  (clumens)
- Remove unused getVG{Free,Used}Space methods. (clumens)
- We can no longer display Russian correctly in text mode (#491394).
  (clumens)
- Clean up the reinitialize LVM warning message (#491888). (clumens)
- Update translation files (#484784). (clumens)
- Include the storage directory when building the .po files. (clumens)
- Merge commit 'origin/anaconda-storage-branch' (clumens)
- Keep VG size property non-negative (rvykydal)
- Grow LVs for kickstart requests too (rvykydal)
- Handle not finding the upgrade root gracefully. (jgranado)
- Use self.name to report that we could not eject cd. (jgranado)
- Fix ppoll() timeout=infinity usage in auditd (#484721). (pjones)
- Use correct parse method for the upgrade command (#471232) (wwoods)
- Rename /etc/modprobe.d/anaconda to /etc/modprobe.d/anaconda.conf (clumens)
- Handle FTP servers that both want and don't want PASS after USER
  (#490350). (clumens)
- Only select the Core group in text mode (#488754). (clumens)
- Add created user to default group created for the user. (rvykydal)

* Wed Mar 25 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.38-1
- Fix pylint errors in iw/*.py (hdegoede)
- Rework CryptTab.parse (dlehman).
- Code fixes of errors shown by pylint (mgracik).
- Don't underflow on the busy cursor stack. (clumens)
- "vg" is not valide inside this if. (jgranado)
- Device is sometimes None. (jgranado)
- Fix typo. (#492042) (dlehman)

* Tue Mar 24 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.37-1
- Start with a basic /etc/hosts file (#491634) (dcantrell)
- Do not flag every existing partition for resize (#491803) (dcantrell)
- Remove unused noformatCB() function. (dcantrell)
- Remove unnecessary istruefalse() function. (dcantrell)
- Build new _isys.so for updates.img if needed. (dcantrell)
- Get the UUID of each md array we create. (#491796) (dlehman)
- Call udev_settle after committing changes to a disk (#491529) (hdegoede)
- Be a little bit smarter about allocating space to grow parts. (#491761)
  (dlehman)
- Check that partition is on the disk before trying to remove it. (#491997)
  (dlehman)
- Work around a bug in mdadm incremental assembly. (dlehman)
- Use the same units (MB) for extent size that we do for everything else.
  (dlehman)
- Put line breaks in between crypttab entries. (#491938) (dlehman)
- Register the NoDevFS class. (clumens)
- fslabels -> labels. (clumens)
- NFSDevice does not take exists= as a parameter. (clumens)
- Override _setDevice and _getDevice in NFS. (clumens)
- Move resolveDevice into the DeviceTree class. (clumens)
- Move most of the parseFSTab logic into its own function. (clumens)
- We don't even use partedUtils in this module. (clumens)
- PReP formats can never be active. (#491865) (dlehman)
- Move protectedPartition setup into storageInitialize (#491781). (clumens)
- Use the mount and unmount methods on OpticalDevice.format now. (clumens)
- Add a format for ISO9660 filesystems. (clumens)
- getDeviceByName does not expect the CD device to start with "/dev/"
  (#491768). (clumens)
- Write the same arch to .discinfo as iutil.getArch() gives us (#490977).
  (clumens)
- Don't remove partitions twice. (jgranado)

* Mon Mar 23 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.36-1
- Add EFI, Apple Bootstrap, and PPC PReP Boot formats. (dlehman)
- Remove all implicit calls to self.format.destroy from Device classes.
  (dlehman)
- Pop the busy cursor when we're done with the wait window (#491736).
  (clumens)
- If the new size and old size are the same, treat as a no-op (#491496).
  (clumens)
- Let mountFilesystems handling bind mounting /dev (#490772). (clumens)
- Not all FileDevices have parents, so don't assume. (clumens)
- Bind mount formats are mountable. (clumens)
- If a filesystem is already mounted, don't raise an error. (clumens)
- Fix a typo calling the superclass's constructor. (clumens)
- Add a fake device for bind mounting /dev. (clumens)
- If there was an exception leading to the urlgrabber error, log it.
  (clumens)
- Fix the import of checkbootloader (#491574). (clumens)
- Add a missing import (#491605). (clumens)

* Fri Mar 20 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.35-1
- Fix traceback in FSSet.crypttab. (#491160) (dlehman)
- Fix traceback on upgrade. (#491446) (dlehman)
- Do not include .h and .sh files in updates.img (dcantrell)
- Make PartitionDevice resize work. (dcantrell)
- Reset mouse pointer if we find an unreadable disk. (dcantrell)
- Use label attr instead of non-existent fslabel attr. (#491120) (dlehman)
- Need to notify the kernel of changes before udev settle (katzj)
- Revert "mount and umount commands are in /sbin now, remove from /usr/sbin"
  (dcantrell)
- Make some fixes to the rescue mode system selection UI (#489973, #489977).
  (clumens)
- Fix text mode autopartitioning (#491282). (clumens)
- Do not use _rnetdev as fstab option for network based / (hdegoede)
- Make root= line in grub.conf and path spec in fstab consistent (hdegoede)
- Fix a reference to the partitions list (#491335). (clumens)
- Do not traceback at the very beginning of rescue mode (msivak)
- Fix traceback when editing encrypted mdraid device in UI. (rvykydal)

* Thu Mar 19 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.34-1
- Catch FSError when detecting storage, prevent user from continuing.
  (dcantrell)
- If we have no error string, place None in the tuple. (dcantrell)
- Move OUTPUT_TERMINAL definition to isys.h (dcantrell)
- mount and umount commands are in /sbin now, remove from /usr/sbin
  (dcantrell)
- Avoid SIGSEGV in doPwMount() when NULL is last parameter (#491192)
  (dcantrell)
- Attempt disk commits 5 times before raising an exception. (dcantrell)
- Add boot partition size limit properties and size validation method.
  (dlehman)
- Make sure boot flag gets set. (#491170) (dlehman)
- Make bootable a property of PartitionDevice. (dlehman)
- After setting up our random UUID, inform the storage layer (katzj)
- Handle system crappyness. (jgranado)
- Fix up checking for live image backing (katzj)
- Let's not remove our mountpoints (katzj)
- Fix writing the default= line in grub.conf (#490756). (clumens)
- Revert "Fix pruning of destroy actions for preexisting devices." (dlehman)
- Add more blacklisting (katzj)
- Blacklist the live image backing device (katzj)
- Move blockdev blacklisting to be a function (katzj)
- Inhibit devkit-disks during a live install (katzj)
- try to unmount everything from /media on live installs (katzj)
- Fix live installs to not traceback (katzj)
- Fix New partition in UI (rvykydal)

* Thu Mar 19 2009 David Lehman <dlehman@redhat.com> - 11.5.0.33-1
- Rework the lvm dialog. (#490301,#490966,#490681,#489870) (dlehman)
- Improve chances of uniqueness from Storage.createSuggestedLVName. (dlehman)
- Fix pruning of destroy actions for preexisting devices. (dlehman)
- Devices should not be resizable unless they exist. (dlehman)
- Try to activate an existing md array after adding each member. (dlehman)
- Indicate filesystem is mountable if we have a mount command. (dcantrell)
- Mount existing filesystems read-only when getting size. (dcantrell)
- Fix some errors in the updates target. (dcantrell)
- Place all mount.* commands in /sbin (dcantrell)
- Fix error message reading and writing in doPwMount() (dcantrell)
- Use booleans in isys.mount() and isys.umount() (dcantrell)
- Add a FIXME comment for setting uuid in VG / LV create (hdegoede)
- Do not traceback when writing anaconda.ks with iscsi with auth info.
  (hdegoede)
- Do not write LV uuid to grub.conf, but the filesystem uuid (hdegoede)
- If a mountpoint depends on a network disk at _netdev to its fstab options
  (hdegoede)
- Do not hang when creating raid array with member having filesystem
  detected (#490891) (rvykydal)
- Destroy and create luks child of raid array too when editing in UI.
  (rvykydal)
- Editing non-existent raid device by destroying and creating actions
  (rvykydal)
- actionDestroyFormat call takes device, not format (rvykydal)
- Fix getChildren call in partition UI (rvykydal)
- Fix removing of devices with the same name from	tree when adding
  create action. (rvykydal)
- Do not duplicate requested minor number in edit raid UI list. (rvykydal)
- Offer available partitions when editing non-preexisting raid request.
  (rvykydal)
- Don't try to fit the whole StorageDevice.__str__ output into the UI
  (#490406). (clumens)
- Make PartitionDevice handle both normal and dmraid partitions (hdegoede)
- Stop overriding __init__ in DMRaidPartitionDevice (hdegoede)
- Set format UUID after creating a format (hdegoede)
- Fix result of updateSysfsPath to be consistent with initial sysfsPath
  values (hdegoede)
- Use getDevicesByInstance() for storage.partitions (hdegoede)
- We no longer use iscsiadm anywhere (hdegoede)

* Tue Mar 17 2009 Jesse Keating <jkeating@redhat.com> - 11.5.0.32-1
- Typo fix. (clumens)
- Make platform.checkBootRequest work better and not use diskset anymore. (clumens)
- Fix a traceback when looking for PS3 boot partitions (#490738). (clumens)
- FormatArgs -> FormatOptions (#490737). (clumens)
- Fix ppoll() timeout=infinity usage in auditd (#484721). (pjones)
- Simplify kernel package selection. (clumens)
- Look at CPU flags instead of /proc/iomem to determine PAE-ness (#484941). (clumens)
- Tell NM not to touch interfaces when / is on a network disk (hdegoede)
- Get iscsi going with the new storage code (hdegoede)
- Use minihal instead of isys.hardDriveDict in list-harddrives (#488122). (clumens)
- storage.disks never includes disks without media present. (clumens)
- Changed the getDevicebyLabel() to getDeviceByLabel() in devicetree.py (mgracik)

* Mon Mar 16 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.31-1
- Don't use disk.maximizePartition anymore. (dlehman)
- Only schedule implicit format destruction if there is formatting to
  destroy. (dlehman)
- Reset encryptionPassphrase when we reset the rest of storage. (dlehman)
- Do not create a LUKSDevice if we do not have a way to map the device.
  (dlehman)
- Fix handling of new extended partitions during partition allocation.
  (dlehman)
- Fix bug in dependency list for partitions. (dlehman)
- Fix inconsistency in variable use in search for free space. (dlehman)
- Check for disk name being in disk.name not in clearPartDisks (dcantrell)
- Create a Makefile target to generate updates.img automatically. (dcantrell)
- When creating free space, handle cases other than clearpart --drives=
  (clumens)
- Ignore loop and ram devices (hdegoede)
- devicetree: fix slave addition of incomplete dm / md devices (hdegoede)
- Catch LVMErrors too when tearing down devices (hdegoede)
- Install udev rules in /lib/udev/rules.d instead of in runtime dir
  (hdegoede)
- Ignore disk devices with missing media (#488800). (clumens)
- Use correct parse method for the upgrade command (#471232) (wwoods)
- Fix creation of fs options for preexisting encrypted devices. (dlehman)
- Fix lots of buggy behavior in the partition dialog. (dlehman)
- Handle FTP servers that both want and don't want PASS after USER
  (#490350). (clumens)
- Fixed the names of the variables for lvm.py functions. (mgracik)
- editPartitionRequest -> editPartition in iw/partition_gui.py (#490384).
  (clumens)
- clampPVSize -> clampSize in lvm.py (#490295). (clumens)
- Fix the obvious and stupid typo (#490296). (clumens)
- isys.umount removes mount directory by default (rvykydal)
- Fix tempfile.mkdtemp call. (rvykydal)
- Initialize attribute _mountpoint before using it (rvykydal)
- devicetree.py has _ignoredDisks instead of ignoredDisks. (jgranado)
- Create separate resize actions for formats and devices. (dcantrell)
- Use os.statvfs() to get existing filesystem size. (dcantrell)
- Add resizeArgs for Ext2FS and fix it for BtrFS. (dcantrell)
- Report when we cannot find any free space partitions. (dcantrell)
- Improve resizeDialog text. (dcantrell)
- Raise FSResizeError if filesystem cannot be resized. (dcantrell)
- Handle resizing when setting targetSize for PartitionDevice (dcantrell)
- Let users set the size property of StorageDevices. (dcantrell)
- Add support for kickstart's '--initlabel' option to clearpart. (dlehman)
- Fix display of LV format type for encrypted LVs. (dlehman)
- Make paths somewhat flexible so we'll work in normal environments.
  (dlehman)

* Fri Mar 13 2009 David Lehman <dlehman@redhat.com> - 11.5.0.30-1
- Fix supportable attribute for cmdline-enabled fstypes. (dlehman)
- Access private attribute for luks dict. (dlehman)
- Schedule format create for newly encrypted preexisting partition. (dlehman)
- Don't traceback if vg.teardown fails in recursive teardown. (dlehman)
- Schedule format create action for newly encrypted preexisting LV. (dlehman)
- Make sure we return something other than None for new requests. (dlehman)
- Add __str__ methods to Device objects. (clumens)
- Add mediaPresent and eject to the OpticalDevice class. (clumens)
- Use the right import path for checkbootloader (#490049). (clumens)
- Rename /etc/modprobe.d/anaconda to /etc/modprobe.d/anaconda.conf (clumens)
- Don't clear partitions containing the install media. (dlehman)
- Wait til everyone knows the format/fs is no longer active. (dlehman)
- Save a copy of the device stack so we can destroy the format. (#489975)
  (dlehman)
- Add a deep copy method to Device since we can't just use copy.deepcopy.
  (dlehman)
- Fix infinite loops in partition screen populate. (#490051) (dlehman)
- Default to a name based on the uuid for existing luks mappings. (dlehman)
- Use the correct keyword for luks map names ('name', not 'mapName').
  (dlehman)
- Fix getting of number of total devices of sw raid. (rvykydal)
- Only select the Core group in text mode (#488754). (clumens)
- Added test case for devicelib mdraid.py. (mgracik)
- Add created user to default group created for the user. (rvykydal)
- Fix editing of existing logical volume. (rvykydal)
- Add a list that lvm should ignore. (jgranado)

* Thu Mar 12 2009 David Lehman <dlehman@redhat.com> - 11.5.0.29-1
- Don't create a PartitionDevice for devices that do not exist (#489122).
  (clumens)
- A getter doesn't usually take a parameter (#489965). (clumens)
- Do not write "Running..." to stdout, as that could be tty1. (clumens)
- Call storage.exceptionDisks, not diskset.exceptionDisks. (#489615)
  (dlehman)
- Fix typo. (jgranado)
- Fix typo. (dlehman)
- Add udev rules for handling for mdraid arrays. (dlehman)
- Honor the zerombr kickstart directive. (dlehman)
- currentSize is expected to be a float, so convert it to one (#489882).
  (clumens)
- It's clearPartDisks, not clearPartDrives. (clumens)
- Get rid of the mappings and ksID as well. (clumens)
- Make sure the device has a diskType before attempting to check what it is.
  (clumens)
- Update the volgroup command to work with the new storage code. (clumens)
- Update the raid command to work with the new storage code. (clumens)
- Update the part command to work with the new storage code. (clumens)
- Update the logvol command to work with the new storage code. (clumens)
- addPartRequest is no longer needed. (clumens)
- Don't set default partitioning in every kickstart case. (clumens)
- Clear partitions before scheduling requests. (clumens)
- Always go through doAutoPart. (clumens)
- Format modules import fix (mgracik)
- Fixed the format modules import (mgracik)
- Allow overriding the anaconda udev rules from an updates.img (hdegoede)
- If a pv somehow does not contain a vg_name, do not try to get other vg
  info (hdegoede)

* Wed Mar 11 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.28-1
- Fix a few bugs in the lvm dialog. (#489022) (dlehman)
- Modify livecd.py to work with new storage backend. (dlehman)
- Be explicit about resetting Disks' partedDisk attribute. (#489678)
  (dlehman)
- Deactivate devices after we've finished scanning them. (dlehman)
- Handle the case of removing an unallocated partition from the tree.
  (dlehman)
- Try again to set up LVs when we've just added a new PV to the VG. (dlehman)
- Set partition flags in format create/destroy execute methods. (dlehman)
- Make sure we use the newly committed parted.Partition after create.
  (dlehman)
- Make device teardown methods more resilient. (dlehman)
- Initialize storage in rescue mode so we can find roots (#488984). (clumens)
- We also need to pack up the extra args tuple, too. (clumens)
- doLoggingSetup keeps growing new arguments, so put them into a dict
  (#489709). (clumens)
- Fix anaconda udev rules to not require pre-existing device nodes (hdegoede)
- Hook up 'Shrink current system' dialog to new storage code. (dcantrell)
- Fix _getCheckArgs() in class FS. (dcantrell)

* Tue Mar 10 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.27-1
- Fix action pruning to handle more complex scenarios. (dlehman)
- Schedule destruction of any existing formatting along with the device.
  (dlehman)
- Add a size attribute to mdraid arrays. (dlehman)
- Speed up partitioning screen redraws by trimming workload where possible.
  (dlehman)
- Create partitions with exactly the geometry we calculate. (dlehman)
- Fix name collision between formats.mdraid and devicelibs.mdraid. (dlehman)
- Destruction of the member device formatting will be handled elsewhere.
  (dlehman)
- Fix a typo (jkeating)
- Fix pruning between two destroy actions on the same device (rvykydal)
- Use the pyblock functions when possible. (jgranado)
- We are searching a list, not a dict now (rvykydal)

* Mon Mar 09 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.26-1
- Move the recursive teardown of all devices out of processActions. (dlehman)
- Clean up handling of /proc, /sys, /dev/pts, /dev/shm entries. (dlehman)
- Fix several minor bugs preventing upgrade/rescue mount. (#488946) (dlehman)
- Only populate the device tree on demand. (dlehman)
- Prune actions by device based on path, not object-id. (dlehman)
- Rewrite action sort so it works correctly. (dlehman)
- Do a separate disk.commit for each partition add/remove. (dlehman)
- Fix bug keeping track of best free region/type/disk info. (dlehman)
- Return early if doAutoPart is False, but clearpart first if kickstart.
  (dlehman)
- Recognize PS3 as a valid machine type (#489263). (clumens)
- Move the mdRaidBootArches logic into the platform module. (clumens)
- stdout and stderr may also need to be created. (clumens)
- Fix booty for dmraid (hdegoede)
- It's self.origrequest, not self.origreqest (#489036). (clumens)
- Added crypto.py unittest; Updated devicelibs tests baseclass.py and lvm.py
  (mgracik)
- Start storage before parsing the kickstart file. (clumens)
- Make sure autopart without any clearpart command will fail. (clumens)
- Update storage flag on ks autopart (rvykydal)
- Use correct storage attribute for ks clearpart (rvykydal)
- Catch the new _ped.DiskLabelException for unrecognized disklabels.
  (dlehman)
- Catch all failures from making parted objects in exceptionDisks. (dlehman)
- various dmraid fixes. (jgranado)
- Implement the format disk question as a callback. (jgranado)
- Add dmraid functionality to new storage code. (jgranado)
- Do not pass None values into nonmandatory arguments, you are screwing the
  default values.. (msivak)

* Thu Mar 05 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.25-1
- Schedule device destroy actions for partitions last. (dlehman)
- Pass storage.disks, not storage, to createAllowed.... (#488860) (dlehman)
- Nodev filesystems always exist. And the device is arbitrary. (dlehman)
- Include proc, &c filesystems in fstab and FSSet.{mount/umount}Filesystems.
  (dlehman)
- Remove FSSet.writeFSTab. That job is handled elsewhere. (dlehman)
- Add properties to FSSet to provide the nodev entries. (dlehman)
- Fix incomplete format in Storage.deviceImmutable. (dlehman)
- Make sure we use the same disk the free space is on. (#488807) (dlehman)
- Prevent clobbering of name 'mdraid' by qualifying it. (dlehman)
- Handle unformatted disks and cdroms in Storage.exceptionDisks. (dlehman)
- Add resizeArgs property for resizable filesystems. (dcantrell)
- Fill out class NTFS a bit more. (dcantrell)
- Add fsckProg property to class FS. (dcantrell)
- Ext2FS.migratable(self) -> Ext2FS.migratable (dcantrell)
- Fix StorageDevice.minSize() and PartitionDevice.maxSize() (dcantrell)
- Center resize window on the screen. (dcantrell)
- Do not raise DeviceError if not bootable device is found. (dcantrell)
- Do an even more thorough job of ignoring disks libparted doesn't like.
  (clumens)
- Fix a couple problems on the "Change device" bootloader dialog. (clumens)
- Fix a typo when writing out the mdadm config file. (clumens)
- Remove all uses of isys.cdromList, which no longer exists. (clumens)
- Check to see if we're on S390 on the congrats screen (#488747). (clumens)
- Handle non-fatal errors more gracefully in addUdevDevice. (dlehman)
- partRequests no longer exists, so don't try to import it (#488743).
  (clumens)
- When building the exceptionDisks list, skip devices libparted doesn't
  like. (clumens)
- Iterate over devicetree.devices.values, not devicetree. (dlehman)
- Add a get() method to Flags, since it pretends to be a dictionary.
  (clumens)
- Stop with the fsset usage. (dlehman)
- Format message string after translation not before (msivak)
- We need newer python-cryptsetup because of the default values for cipher
  and keysize for luskFormat (msivak)
- If a drive is not initialized, offer reinitialization or ignoring the
  drive to the user (msivak)
- More syntax errors / traceback fixes (hdegoede)
- Fix syntax errors (rvykydal)
- Implement Storage.sanityCheck, mostly from old partitions code. (dlehman)

* Thu Mar  5 2009 Dave Lehman <dlehman@redhat.com> - 11.5.0.24-3
- Fix booty's desire to import fsset.
- Fix attempt to set read-only attr "removable" in DiskDevice.__init__

* Thu Mar 05 2009 Peter Jones <pjones@redhat.com> - 11.5.0.24-2
- Add EFI boot.iso generation.

* Wed Mar  4 2009 Dave Lehman <dlehman@redhat.com> - 11.5.0.24-1
- Storage test day.

* Fri Feb 20 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.23-1
- Remove old content from utils/ (dcantrell)
- Ensure request.drive is always a list (#485622) (dcantrell)
- Pick up pyblock if it exists in block/ on an updates.img. (dcantrell)
- Don't check for a swapfs on things that aren't partitions (#485977).
  (clumens)
- Perform ext3->ext4 filesystem migration if ext4migrate is given (#484330).
  (clumens)
- Translate i?86 into i386 as a base arch. (jkeating)
- Teach upd-instroot about i586 arch, for sake of glibc.i586/openssl.i586
  (jkeating)
- Fix the obvious typo. (clumens)
- filer.login raises an exception with it can't login, not returns None
  (#486454). (clumens)
- Take into account that a parted.Partition's _fileSystem can be None
  (#485644). (clumens)

* Thu Feb 19 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.22-1
- Updated Romanian translation (alexxed)
- Remove the qla2xxx line from mk-images again (wwoods).
- Fix broken shell syntax from 3bdcd64d2 (jkeating)
- The VLGothic-fonts package has changed name and location (#486080).
  (clumens)

* Tue Feb 17 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.21-1
- Building for i586 only now in Fedora. (dcantrell)

* Tue Feb 17 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.20-1
- Fix indentation on upd-instroot (kanarip)
- Fix the indentation in mk-images (kanarip)
- Remove unused iface_netmask2prefix() function. (dcantrell)
- A parted.Disk has no attribute named "dev".  It's named "device"
  (#486007). (clumens)
- Use brandpkgname for the efi art too (katzj)
- Let's use the product string for a brandpackage name. (kanarip)
- Fix indentation in mk-images.efi (kanarip)
- Fix indentation in buildinstall script (kanarip)
- It's part.active, not part.is_active(). (clumens)
- File the basic traceback as the first comment instead of a generic
  message. (clumens)
- Encode our upgrade policy in productMatches/versionMatches and enforce it.
  (clumens)
- If we'd show package selection on kickstart installs, also show tasksel.
  (clumens)

* Fri Feb 13 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.19-1
- Fix build errors in the new net.c code. (clumens)

* Fri Feb 13 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.18-1
- Require pyparted >= 2.0.0 (dcantrell)
- Update to use the new pyparted. (dcantrell, clumens)
- Replace non UTF-8 char for hiding password chars with UTF-8 (#485218)
  (hdegoede)
- Use a better test for when we're in text mode (#484881). (clumens)
- Add iBFT support to loader (msivak)
- Hardlink the initrd.img since we're linking the vmlinuz as well. (jkeating)
- Check if ld-linux.so.2 is a link already, before removing it (dcantrell)

* Wed Feb 11 2009 Hans de Goede <hdegoede@redhat.com> - 11.5.0.17-1
- Revert broken German translation fixes so that we will build again
- Sync up module list (#484984) (katzj)

* Wed Feb 11 2009 Hans de Goede <hdegoede@redhat.com> - 11.5.0.16-1
- Rewrite iscsi support using libiscsi (hdegoede)

* Mon Feb 09 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.15-1
- Fix gptsync/lib.c for gcc strict aliasing rules. (dcantrell)
- Fix gcc warning for gptsync memset() usage. (dcantrell)

* Mon Feb 09 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.14-1
- Rewrite mdio_read() in linkdetect.c for strict aliasing rules. (dcantrell)

* Mon Feb 09 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.13-1
- Check that required kickstart commands are present early on (#483048).
  (clumens)
- Simplify the text mode interface. (clumens)
- Fix truncated translation string for livecd installs (#484430). (clumens)
- Calcutta -> Kolkata (#484638). (clumens)
- Fix runpychecker.sh to find zonetab module (hdegoede)
- Strip invalid characters from automatically made VG/LV names (#483571).
  (clumens)
- Fix systemtime setting during installation (#6175, #461526). (rvykydal)
- Workaround MMC block devs showing up not as disks from hal (#481431)
  (katzj)
- Add some new false positives to pychecker false positives filtering
  (hdegoede)
- Make kickstart timezone value check consistent with system-config-date
  (#483094) (rvykydal)
- Make ext4 default in UI filesystem selection (bug #481112) (rvykydal)
- Redirect iscsiadm's stderr away from the console. (clumens)
- Pay attention to the stderr parameter to execWithCapture. (clumens)
- For python2.6, our showwarnings function must take a line= parameter.
  (clumens)
- If ext4dev is seen in the /etc/fstab, treat it as ext4 instead (#474484).
  (clumens)
- Make sure to call _getConfig from our YumSorter subclass. (clumens)
- Set proper text mode font for Greeks (#470589) (msivak)
- Lots of translation updates.

* Thu Jan 29 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.12-1
- If ks=nfs:... is given, don't try to find the file via boot options
  (#480210). (clumens)
- Fix cdrom install on machines with no network devices (wwoods)
- updated fuzzy strings (jsingh)
- Use modinfo to find out what firmware we need in initrd (wwoods)
- Use the preconf object for yum configuration now (jantill). (clumens)
- Updated Dutch translation adn only 1 -fuzzy- string left (zuma)
- Add a boot target for the xdriver=vesa parameter and document it. (clumens)
- repo.proxy is now a property, so check before setting it (#481342).
  (clumens)

* Wed Jan 21 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.11-1
- Fix a logic problem with network file write outs. (480769) (jkeating)
- Only run selectBestKernel, selectBootloader, etc. for new installs.
  (wwoods)

* Mon Jan 19 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.10-1
- btrfs install support (sandeen)
- Default / to be ext4 (katzj)
- Allow live installs to use ext4 as root and make the error message clearer
  (katzj)
- Add support for Maithili and Nepali (#473209). (clumens)

* Fri Jan 16 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.9-1
- Cracklib moved locations, account for this in our keepfiles. (jkeating)
- Look in the right path for kernel module lists. (jkeating)
- Fix more problems in expandModuleSet, based on a patch from markmc
  (#480307). (clumens)
- Allow ext4 without magic argument (keep a flag for migrate) (katzj)
- Fix pulling in network modules (katzj)
- Support mounting NTFS filesystems (#430084) (katzj)
- dejavu fonts changed package names, pick up new names. (jkeating)
- TightVNC is now the default VNC server in Fedora (#480308). (clumens)
- Only skip (over)writing netconfig if we have an actual instPath (jkeating)
- The sets module is deprecated, so no longer use it. (clumens)

* Wed Jan 14 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.8-1
- Fix D-Bus usage in get_connection in loader (jkeating)

* Wed Jan 14 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.7-1
- How to get raw pages from the wiki has changed again. (clumens)
- Make sure the 'anaconda' file gets the right detected type (alsadi,
  #479574).
- Include the missing import. (clumens)

* Thu Jan 08 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.6-1
- Collect DSO deps for NetworkManager plugins. (dcantrell)

* Thu Jan 08 2009 Chris Lumens <clumens@redhat.com> - 11.5.0.5-1
- NetworkManager system settings plugins were renamed, change mk-images.
  (dcantrell)
- Add a message to install.log when package installation is done (#476953).
  (clumens)
- Add support for specifying which partition to upgrade (atodorov, #471232).
  (clumens)
- pykickstart has a new version of the upgrade command. (clumens)
- Log all calls to mount to /tmp/program.log as well. (clumens)
- Log everything from execWithRedirect or execWithCapture (#467690).
  (clumens)
- Update partedUtils.py:findExistingRootPartitions to return UUID
  (atodorov). (clumens)
- Don't skip the method screen when going back and forth (#477991). (clumens)
- Die on errors from upd-instroot/mk-images rather than continuing on (katzj)
- The FTP USER command does not need to be followed by a PASS (#477536).
  (clumens)

* Mon Jan 05 2009 David Cantrell <dcantrell@redhat.com> - 11.5.0.4-1
- Workaround compile error due to (# 478663) (hdegoede)
- Various packaging fixed from review (#225246) (hdegoede)
- Show the header in certain non-lowres cases (#478765, alsadi AT
  ojuba.org). (clumens)
- Remove doMultiMount. (clumens)
- Use mount -t auto instead of passing a list of valid fstypes (#477328).
  (clumens)
- Fix case sensitivity when searching for headers (kanarip)
- Fix a traceback in checking for network install (ricky AT
  fedoraproject.org). (clumens)

* Tue Dec 23 2008 David Cantrell <dcantrell@redhat.com> - 11.5.0.3-1
- Initialize domainname to None (#477831) (dcantrell)
- Do not import unused modules. (dcantrell)
- Call '/sbin/udevadm settle' instead of /sbin/udevsettle (dcantrell)

* Tue Dec 23 2008 David Cantrell <dcantrell@redhat.com> - 11.5.0.2-1
- Require latest pykickstart for repo command (clumens)
- Remove libdhcp* from scripts/upd-instroot (dcantrell)
- methodstr -> self.methodstr (dcantrell)
- Rewrite iface_ip2str() to use libnm-glib (dcantrell)
- Fix a few syntax error caugh by pychecker (hdegoede)
- Remove isys.e2fslabel() and isys.getraidsb() (dcantrell)

* Thu Dec 18 2008 David Cantrell <dcantrell@redhat.com> - 11.5.0.1-1
- Remove plural forms from po/tg.mo (katzj)

* Thu Dec 18 2008 David Cantrell <dcantrell@redhat.com> - 11.5.0.0-1
- Reduce direct D-Bus calls in isys/iface.c. (dcantrell)
- Allow 'ks' to function as it once did (#471812) (dcantrell)
- Fix telnet install support (#471082) (dcantrell)
- Call 'udevadm settle' instead of 'udevsettle'. (dcantrell)
- When using anaconda with kickstart file with UI mode - do not show the VNC
  question (#476548) (msivak)
- Check error from asprintf() correctly for dhcpclass handling. (dcantrell)
- Use libnm_glib in net.c:get_connection() (dcantrell)
- Add libnm_glib CFLAGS and LIBS to loader's Makefile. (dcantrell)
- BR NetworkManager-glib-devel. (dcantrell)
- Only write the short hostname to the localhost line (#474086) (dcantrell)
- Updated Tajik Translation - Victor Ibragimov (victor.ibragimov)
- Copy /etc/dhclient-DEV.conf file to target system (#476364) (dcantrell)
- Use macros for D-Bus paths (dcantrell)
- Let X tell us when it's launched rather than just sleeping. (ajax)
- When there's no baseurl, set a default of [] instead of [''] (#476208).
  (clumens)
- cracklib now raises exceptions on bad passwords (rzhou, #476312). (clumens)
- Make sure ssh doesn't get duplicated in the open port list (#474937).
  (clumens)
- mdraid1: default to putting grub on partition instead of mbr (#217176)
  (hdegoede)
- Don't install the games group as part of office/productivity (#472324).
  (clumens)
- Don't dump encryption passphrases. (dlehman)
- Write anacdump.txt upon receipt of SIGUSR2 (from clumens). (dlehman)
- Use stacks instead of tracebacks in traceback handlers. (dlehman)
- Unmount swap devices when migrating filesystems, then reactivate
  (#473260). (clumens)
- Handle both /dev/sr0 and sr0, since that's what cdromList gives (#475083).
  (clumens)
- In iface_ip2str(), make sure to advance to next item before continue.
  (dcantrell)
- We already have _GNU_SOURCE defined in Makefile.inc (dcantrell)
- Remove XXX comment in net.c about GATEWAY (dcantrell)
- Use strverscmp() from glibc in place of rpmvercmp() (dcantrell)
- Remove readLine() function from loader/loadermisc.c (dcantrell)
- Do not write SEARCH line to ifcfg-DEVICE file (#474858) (dcantrell)
- Preserve existing network configuration files during install (#461550)
  (dcantrell)
- Send unique vendor class identifier unless user specifies one. (dcantrell)
- Avoid tracebacks when filling in static network config fields (#474275)
  (dcantrell)
- Prevent network install when no network devices are found (#470144)
  (dcantrell)
- Remove markup from text before printing it in cmdline mode (#470253).
  (clumens)
- Move strip_markup() into iutil. (clumens)
- Fix up plural forms header so that python doesn't blow up for us (katzj)
- Change text to reflect Jesse's comments (katzj)
- Add support for the Tajik language (#455963). (clumens)
- Add a button to the UI to ignore all missing packages. (clumens)
- First small eu.po transtation, just to be sure that the system is set up
  OK. (mikel.paskual)
- mini-wm: Turn on automatic window redirection. (ajax)
- Better naming for LVM volume groups and logical volumes (#461682)
  (dcantrell)
- Partition requests can be None when populating the tree. (#474284)
  (dlehman)
- Say we are unable to configure the network interface (#467960) (dcantrell)
- Match textw/network_text.py strings to iw/network_gui.py (#470145)
  (dcantrell)
- In addSnap(), check snapshots for data key before continuing (#433824)
  (dcantrell)
- Load FCP modules early for CD/DVD install (#184648) (dcantrell)
- Update mk-s390-cdboot.c to work with large kernel images (#184648)
  (dcantrell)
- Make sure fstype exists before we try to test it (#473498). (clumens)
- Updated a small correction in kn locale (svenkate)
- Use modules.* files for finding modules of a type rather than modinfo
  (katzj)
- Make complete text mention updates (#244431) (katzj)
- Make text for autopartitioning types clearer (#441350) (katzj)
- Allow installing grub on the MBR if /boot is on mdraid (#217176) (hdegoede)
- Fix some spelling errors in German translation (fabian)
- Make the required media dialog less wordy (#469557). (clumens)
- returnNewestByName now raises an error instead of returning [] (#472462).
  (clumens)
- Fix death on login of an OLPC on a live image (katzj)
- Fix ld-*.so globbing for glibc-2.9 . (pjones)
- Do not bring up network for non-remote kickstart locations (#471658)
  (dcantrell)
- Resolve dm-X devices returned by pvdisplay. (#448129) (dlehman)
- More shell script syntax fixing (katzj)
- Only bring up the network dialog on package failures if required
  (#471502). (clumens)

* Wed Nov 12 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.58-1
- Add comps groups for new repos that are added (#470653) (katzj)
- Support upgrades of systems whose rootfs is on an LV. (#471288) (dlehman)
- Use hasPassphrase() instead of directly accessing passphrase member.
  (dlehman)
- Don't dump private class members (those with leading "__") (dlehman)
- Explicitly close the CD drive after the user hits "continue" (#375011)
  (pjones)
- Fix shell syntax error (#471090) (ivazqueznet)
- Save the /etc/fstab before overwriting it on upgrades (#452768, #470392).
  (clumens)

* Tue Nov 11 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.57-1
- Fix more UnicodeDecodeErrors, hopefully for good this time (#470733).
  (clumens)
- iscsi do missing value check only once (hdegoede)
- Don't try to label XFS filesystems on livecd installs (#470951). (clumens)
- Include cracklib .mo files and look up strings in the right domain.
  (clumens)
- Bugzilla has changed its return values for a couple queries. (clumens)
- Set the default keyboard based on the language (#470446). (clumens)
- Prevent traceback for vnc installs on KVM guests (#470559) (dcantrell)
- Bring up networking early enough for syslog= param (#470513) (dcantrell)
- Sleep a bit before calling udevsettle in iscsiTarget.login (#470073,
  #466661) (hdegoede)
- kickstart, iscsi do not call iscsi.startup after startIBFT has been called
  (hdegoede)
- Do not stop and restart iscsid when rescanning disks/partitions (#470223)
  (hdegoede)
- iscsi.startup should not login to targets as we are already logged in
  (#470230) (hdegoede)
- Remove obsolete normally never reached code from _stopIscsiDaemon
  (#470229) (hdegoede)
- The function getEncryptedDevice gets called correctly expect when we are
  in (jgranado)
- More translations

* Thu Nov 06 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.56-1
- Don't have the key icon take up so much space on the LUKS dialog
  (#470338). (clumens)
- Avoid getting linux-base in the kernel list (katzj)
- Deselect groups when we reset things also (#469854) (katzj)
- make iscsi login code wait for udev to create the devices (#466661,
  #470073) (hdegoede)
- Set the correct path when using the directory chooser. (clumens)
- We always need a wait window, not just when the repo has a name. (clumens)
- Set initial state of IP configuration fields in text mode (#469933)
  (dcantrell)
- Prevent traceback when there are no network devices (#469339) (dcantrell)
- Indentation fix. (pjones)
- Let users edit net settings on network failure in stage 1 (#465887)
  (dcantrell)
- Move startNewt later to avoid printing extra messages on the screen
  (#469687). (clumens)

* Mon Nov 03 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.55-1
- Revert "Make sure dialog deletions take effect sooner (#455676)." (clumens)
- Don't set up the launcher for the installer on XO (katzj)
- Whitespace cleanups for timezone.py (dcantrell)
- Do not store mount options in loaderData->instRepo (#467760) (dcantrell)
- Make sure we look up the IP address for the correct device (#469439)
  (dcantrell)
- Remove unused bool() function. (dcantrell)
- Check for required space for / on live installs (#468867) (katzj)
- Add a basic method for checking the minimal size needed for a backend
  (katzj)
- Fix typo that somehow snuck in (katzj)
- If there's no language selected, don't traceback (#469578). (clumens)
- Improve filtering of non-available groups (#469438) (katzj)
- filer.py: set defaultProduct in __init__ (hdegoede)
- Fix indentation error in filer.py (again) (hdegoede)
- Rebuild keymaps to get rid of trq.map (#469433). (clumens)
- Provide sample punch card reader script for s390x (#462953) (dcantrell)
- Fix a typo that shouldn't have even gotten though. (clumens)
- Check that the platform and product are also correct (#469367). (clumens)
- Remove cio_ignore functionality for s390x (dcantrell)
- Remove bootdisk/s390 (dcantrell)
- If method=nfs: is given, check if it's really an NFSISO install (#468885).
  (clumens)
- Get the right list elements for the iscsi text interface (#466902).
  (clumens)
- Don't traceback when displaying error messages (#469372). (clumens)
- Make sure we differentiate locked luks devs from deleted ones. (dlehman)
- Fix a typo that breaks kickstart with encryption. (#469318) (dlehman)

* Thu Oct 30 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.54-1
- Call startNewt earlier than network bring up (#469171). (clumens)
- Write out the path to the repo, not anaconda-ks.cfg (#467753). (clumens)
- Allow specifying devices by path if they're files (#468504) (katzj)
- Fix the last pychecker warnings in master (hdegoede)
- Add --strict option to runpychecker.sh (hdegoede)

* Wed Oct 29 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.53-1
- Don't sleep(5) after xrandr (ajax)
- Force DPI to 96 even harder (#458738) (ajax)
- Don't try to switch VT to the one that X is on (ajax)
- Only copy /etc/resolv.conf if instPath != '/' (dcantrell)
- 'is not' -> '!=' (dcantrell)
- Write --dhcpclass instead of --class to the anaconda ks file. (jgranado)
- Fix 2 issues in pyparted found by pychecker (hdegoede)
- Add a bit of documentation to the top of runpychecker.sh (hdegoede)
- Add runpychecker.sh script and pychecker-false-positives file (hdegoede)
- Fix saving tracebacks via scp while in text mode. (clumens)
- Search for the hash in the whiteboard, not as the entire whiteboard.
  (clumens)
- Fix various syntax errors caught by PyChecker (hdegoede)
- Wouldn't it be nice to have some real documentation in filer.py? (clumens)
- Make sure the productVersion given by .treeinfo exists in bugzilla
  (#468657). (clumens)

* Mon Oct 27 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.52-1
- Let DNS lookups work from %%post scripts (#468132) (dcantrell)
- Do not use /.tmp for temporary files (#468720) (dcantrell)
- Don't treat encrypted PVs as available if we don't have the key. (#465240)
  (dlehman)
- Do all new device passphrase prompting from partitioningComplete. (dlehman)
- Fix the obviously stupid typo. (clumens)
- There's a new version of the firewall command for F10 (#467753). (clumens)
- Another fix for printing package summaries in text mode (#468283).
  (clumens)
- Fix traceback in network.bringUp() (#468651) (dcantrell)
- lvresize requires a --force arg now (#468478) (katzj)
- Include return code on resize failure error message (#468479) (katzj)

* Fri Oct 24 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.51-1
- Catch UnicodeDecodeError so traceback messages display anyway. (dcantrell)
- Do not write NM_CONTROLLED=yes to ifcfg files (#468028) (dcantrell)
- Log D-Bus messages at ERROR or INFO level. (dcantrell)
- Write dhcpclass to the dhclient conf file for the device (#468436)
  (dcantrell)
- Tell NetworkManager not to touch network interfaces when / is a netfs
  (hans)
- Catch more X failures and fallback to text (#467158). (clumens)
- Fix a typo when using network --gateway (#468364). (clumens)
- Fix icon (#468273) (katzj)
- Remove extra debug info. (pjones)
- Fix the damn spinner in the progress bar. (pjones)
- Fix whitespace. (pjones)
- Fix "looking for installation images" when there's no disc at all. (pjones)
- Make sure dialog deletions take effect sooner (#455676). (clumens)
- Make cdrom drive door status messages be INFO not DEBUG. (pjones)
- Don't switch to tty6 on vnc installs. (clumens)
- Update font list (#462295). (clumens)
- Don't display the entire lengthy device description (#467825). (clumens)
- Fix ext4 detection on existing partitions (#467047) (rvykydal)
- Make sure we handle the /tmp/method file for FTP correctly (#467753).
  (clumens)
- Do not write NM_CONTROLLED=yes to ifcfg files (#468028) (dcantrell)
- Revert "dhclient-script not needed for NetworkManager" (clumens)
- Skip Installation Repo when writing out repo kickstart lines. (clumens)
- Correct media check docs (#468061). (clumens)
- Many translation updates

* Fri Oct 17 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.50-1
- Update several font package names that we were missing. (clumens)
- Only bring up the netconfig dialog if the repo requires networking.
  (clumens)
- cmdline.py: Fix a small typo in a message (rh 467338) (hansg)
- Enable CCW devices used for installation (#253075) (dcantrell)
- I don't know what trq.map.trq-map is, but let's not include it. (clumens)
- If networking is needed for yum repos, bring it up before fetching
  repodata. (clumens)
- Force DPI to 96 when launching X. (#458738) (ajax)
- Lots of translation updates.

* Tue Oct 14 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.49-1
- Make kickstart installs work again (#374271, #392021, #448096, #466340,
  #466304) (dcantrell)
- Let users go Back when loading updates. (dcantrell)
- Write ifcfg files to /etc/sysconfig/network-scripts instead of /.tmp
  (dcantrell)
- Handle unknown hosts in getDefaultHostname (#466775) (dcantrell)
- Try to look up the hostname by the IP address NM reports (#466775)
  (dcantrell)
- NM no longer provides the hostname as a property (#466775). (clumens)
- ext4dev -> ext4 (esandeen). (clumens)
- Move persistent network udev rule to under /etc (#464844). (clumens)
- Update keymaps to include latest Romanian settings (#466117). (clumens)
- Take ip= parameter values by not resetting ipinfo_set. (dcantrell)

* Fri Oct 10 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.48-1
- Remove unnecessary STEP_IP code. (dcantrell)
- Fix how configureTCPIP() returns. (dcantrell)
- Write new sysconfig data to a tmpdir first, then move in place. (dcantrell)
- Write NM_CONTROLLED=yes rather than NM_CONTROLLED= (dcantrell)
- Get rid of some iface flags that were not doing anything anymore.
  (dcantrell)
- Generate new config files in /.tmp in writeEnabledNetInfo() (dcantrell)
- Remove unused variables from configureTCPIP() (dcantrell)
- Do not call get_connection() twice for DHCP. (dcantrell)
- Ask for language and keyboard in rescue mode (#466525). (clumens)
- Fix bringing up the network in rescue mode (#466523). (clumens)
- If we don't have a translation for a lang name, just use the English
  (#466515) (katzj)
- Disable some more IPv6 checks. (clumens)
- Fix a typo (second part of #466374) (katzj)

* Thu Oct 09 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.47-1
- Tag problems in pkgcvs.  Wish we still had force-tag

* Thu Oct 09 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.46-1
- Pull in static network settings from the boot: line (#465270) (dcantrell)
- Do not segfault when going back to select a new interface (#465887)
  (dcantrell)
- Do not test for DNS settings in mountNfsImage() (dcantrell)
- Populate struct iface correctly in setupIfaceStruct() (dcantrell)

* Thu Oct 09 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.45-1
- Fix sorting of repos so we always return an integer value (#466174).
  (clumens)
- Change the upgrade progress bar to pulse (#466053). (clumens)
- Mark iscsi disks not used for / as autostart (rh461840) (hans)
- Always display the wait window when fetching repo information. (clumens)
- Lazily unmount everything before killing NetworkManager (#463959).
  (clumens)
- lang-names really does need to depend on subdirs (katzj)
- Reset targetLang on language change (#465981) (katzj)
- Honor static net parameters with NM (#465270) (dcantrell)

* Mon Oct 06 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.44-1
- Do not rely on loaderData->noDns to tell if we have DNS configured.
  (dcantrell)
- Skip askmethod dialog if user passes repo= and stage2= (dcantrell)
- Reset resolver in get_connection() (dcantrell)
- Fix problems dealing with PXE boot and the ksdevice= parameter. (dcantrell)
- Disable more IPv6 code in loader for now. (dcantrell)
- Write BOOTPROTO=static for manual IPv4 config. (dcantrell)
- Disable IPv6 widgets for F-10. (dcantrell)
- Add iwlagn driver firmware (#465508). (clumens)
- Move starting HAL to after we've probed for hardware. (clumens)
- Don't try to load a couple modules that no longer exist. (clumens)
- The Chinese font package has changed names (#465290). (clumens)
- Fix a traceback when there's no ksdevice given (#465638). (clumens)
- Fix traceback in post install configuration (hans)

* Fri Oct 03 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.43-1
- Disable IPv6 interface widgets in loader for now. (dcantrell)
- Start NetworkManager earlier (#462083) (hans)
- Work around gtk2 bug (#465541) (hans)
- Move our yum.conf out of /etc (#465160) (katzj)
- Correctly display the IP address a vnc viewer should connect to (#465353).
  (clumens)
- lohit-fonts-malayam has been replaced by smc-fonts-meera (#456449).
  (clumens)
- Fix a typo in cleaning up repos. (clumens)
- Fix the mount error reading for real this time (pjones, #465250). (clumens)
- Support ksdevice=link when booting from boot.iso. (dcantrell)
- Automatically select NIC based on ksdevice= boot parameter. (dcantrell)

* Wed Oct 01 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.42-1
- Revert "Finally controlled the plural issue at #508  in Japanese"
  (dcantrell)

* Wed Oct 01 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.41-1
- Fix text inconsistency (#465165). (clumens)
- If there's an error running Xvnc, also print it to the console. (clumens)
- Set the installation repo when using the askmethod UI (#463472). (clumens)
- Fix a segfault when the wrong HDISO repo parameter is given. (clumens)
- Remove the 'Installation Repo' cache directory after install (#464853).
  (clumens)
- If there aren't any usable NICs, don't write out a config (#465127).
  (clumens)
- It helps to specify what the method string should be split on (#464855).
  (clumens)
- Gateway and nameserver are optional for static network configuration.
  (dcantrell)
- Store nameserver in NetworkDevice object. (dcantrell)
- Fix a traceback calling enableNetwork (#464849). (clumens)
- Enable groups when creating new repos since yum doesn't do that now.
  (clumens)
- Update FQDN patch to fix a couple tracebacks (#464191). (clumens)
- Fix static network configuration from boot.iso installs. (dcantrell)
- Use all caps naming for the netdev keys. (dcantrell)
- Left justify text in ui/netconfig.glade interface. (dcantrell)
- Use the right attribute for repo URLs. (clumens)
- Use fullscreen for small screens (#444943) (katzj)
- Another try at fixing up reading errors from mount. (clumens)
- Don't traceback if no baseurl has been set yet. (clumens)
- Allow users to enter a hostname or FQDN during installation (#464191)
  (dcantrell)
- Whitespace cleanups. (dcantrell)
- Fix mk-s390-cdboot on s390x (#184648) (dcantrell)
- Run all text through unicode() before putting it into the TextBuffer.
  (clumens)
- Add reverse chap iscsi bits for kickstart (hans)
- Properly center the passphrase entry dialog. (clumens)
- Fix test for an empty hostname. (clumens)
- Support installs to SD via MMC (#461884) (katzj)
- Set ANACONDA_PRODUCTNAME, etc from /etc/system-release (#464120) (alsadi)
- Reduce code duplication by moving methods into backend (katzj)
- Select packages after repos are set up (#457583) (katzj)
- Add a basic reset method (katzj)
- Cleanups and simplifications to repo setup (clumens) (katzj)
- Revert "Revert "lang-names should really only depend on lang-table""
  (katzj)
- Fix lang-name generation + fix traceback with LANG=C (katzj)
- Allow going back to the method selection screen on error (#463473).
  (clumens)
- Make the boot loader device dialog less ugly (#463489). (clumens)
- Look in images/ for install.img on HDISO (#463474). (clumens)
- Sort Installation Repo to the top of the repo list. (clumens)
- Fuzzy string to fix translation build (katzj)

* Wed Sep 24 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.40-1
- Fix network interface bring up in text mode (#463861, #462592) (dcantrell)
- Bring back isys.resetResolv() and fix NetworkManager polling in
  network.py. (dcantrell)
- Poll 'State' property from NetworkManager in network.bringUp() (dcantrell)
- Log error in rescue mode is network.bringUp() fails. (dcantrell)
- Set the first network device in the list to active. (dcantrell)
- Get rid of firstnetdevice in Network (dcantrell)
- Do not write /lib/udev.d rules if instPath is '' (dcantrell)
- Fix problems with bringDeviceUp() calls (#463512) (dcantrell)

* Mon Sep 22 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.39-1
- Fix a traceback when getting the interface settings (#462592). (clumens)
- self.anaconda -> anaconda (clumens)

* Sat Sep 20 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.38-1
- Restore old lang-names generation method (dcantrell)
- Remount /mnt/sysimage/dev after migrating filesystems. (clumens)
- Use the instroot parameter like we should be doing. (clumens)

* Fri Sep 19 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.37-1
- Set the filename on the traceback when we upload it (wwoods).
- Don't worry about errors looking up protected partitions on upgrades.
  (clumens)
- Fix test for allowing the installation source to be on the root fs
  (#462769). (clumens)
- lang-names should really only depend on lang-table (katzj)
- Don't make the .desktop file unless we actually need to (katzj)
- Fix lang-name generation (katzj)
- Look for xrandr in the search path. (clumens)
- Make the textw network screen match the iw interface by only prompting for
  hostname (#462592) (dcantrell)
- Pick up hostname if we have it, otherwise use localhost.localdomain
  (#461933) (dcantrell)
- dhclient-script not needed for NetworkManager (dcantrell)
- Add getDefaultHostname() to network.py (dcantrel)
- Write out NETMASK and BROADCAST correctly in loader. (dcantrel)
- Fix problems with manual network configuration in loader. (dcantrel)
- anaconda-yum-plugins is now in its own source repo. (clumens)
- Remove most of the network configuration from text mode as well (#462691).
  (clumens)
- Add an extra newline to the empty partition table message. (clumens)
- Fixup DiskSet._askForLabelPermission() (markmc)

* Mon Sep 15 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.36-1
- Remove invalid i18n stuff to let anaconda build. (dcantrell)
- Remove doConfigNetDevice() prototype. (dcantrell)

* Mon Sep 15 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.35-1
- Call network.bringDeviceUp() instead of old isys functions. (dcantrell)
- Pass device name to network.setDNS() and network.setGateway(). (dcantrell)
- NetworkManager fixes in network.py (dcantrell)
- Remove code from isys not needed for NetworkManager. (dcantrell)
- Avoid writing out NM_CONTROLLED more than once. (dcantrell)
- Write out final ifcfg-DEVICE files correctly. (dcantrell)
- Use POSIX and LSB hostname length limit. (dcantrell)
- Consistent whitespace usage in network.py (dcantrell)
- Do not try to start hald or dbus-daemon from anaconda. (dcantrell)
- On HDISO installs, mark LABEL= and UUID= partitions as protected. (clumens)
- Do encrypted device passphrase retrofits while activating partitioning.
  (dlehman)
- Use one passphrase for all new LUKS devices and offer retrofit to old
  ones. (dlehman)
- There's only one passphrase member (encryptionPassphrase) in Partitions.
  (dlehman)
- Only add LUKSDevice instances to PV requests as needed. (dlehman)
- New device passphrase is now always global w/ option to retrofit. (dlehman)
- Don't prompt for a passphrase when creating encrypted devices. (dlehman)
- Define a method to add a passphrase to an existing LUKS device. (dlehman)
- Fix a traceback when starting a shell in rescue mode (#462148). (clumens)
- md, lock_nolock, and dm_emc kernel modules no longer exist. (clumens)
- Fix iscsi disk detection with newer kernels (rh 461839, 461841) (hans)
- Fix the crash reported in bug 454135 (hans)
- Make iBFT reading explicit from a higher level (hans)
- Add ibft flag to ease in testing. (hans)
- Support iSCSI CHAP and Reverse CHAP authentication (rhbz#402431,
  rhbz#432819) (hans)
- Don't set iscsi devices to autostart (rhbz#437891) (hans)
- Add full CHAP support to iSCSI. (rhbz#432819) (hans)
- Do not try to initialize iSCSI, when no portal (#435173) (hans)
- Fix wrong function names for iscsi login/start (rhbz#295154) (hans)
- Set an attribute when iscsid is started (#431904). (hans)
- Better fixes for iscsi probing (patch from jlaska) (hans)
- Make sure ISCSIADM and such are defined (rhbz#431924) (hans)
- Fix iscsi so that mkinitrd can actually talk to the running daemon (hans)
- Make iscsi/ibft work (hans)
- Add mk-images changes forgotten in previous commit (hans)
- Add support for iSCSI iBFT table (#307761) (hans)

* Thu Sep 11 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.34-1
- Always start NM so we can talk to it in the boot.iso case (#461071).
  (clumens)
- Use the device path to identify LUKS devs in /etc/fstab. (#460700)
  (dlehman)
- Use the LUKS UUID instead of device nodes in all references. (#460700)
  (dlehman)
- LUKSDevice.getScheme() no longer cares if the dev has a passphrase.
  (#461203) (dlehman)
- Correct translation to fix the build. (clumens)
- Add the method string back into anaconda-ks.cfg. (clumens)
- Let's try pulling libsqlite into the initrd one more time. (clumens)
- Don't traceback at the end of live installs (katzj)
- Correct the message telling you to use a VNC password. (clumens)
- Remove unused TIMEZONES= crud. (clumens)
- print doesn't yet support the file= syntax in our version of python.
  (clumens)
- Catch errors from using the wrong bugzilla field and display them.
  (clumens)
- Fix line wrapping on part type screen (jlaska, #461759).
- rep_platform has been renamed to platform. (clumens)

* Tue Sep 09 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.33-1
- Include NetworkManager and dbus libraries on 64-bit arches (#461632).
  (clumens)
- We need libsqlite3.so in upd-instroot before it can be in the initrd.
  (clumens)
- Fix partitions growing (backport of rhbz #442628) (rvykydal)
- Kickstart timezone validity check fixed (#461526) (rvykydal)
- Add more kernel crypto modules (#443545). (clumens)
- Make the progress bar move when downloading the install.img (#461182).
  (clumens)
- Add overrideDHCPhostname as an attribute. (clumens)
- Fix saving to remote hosts (#461500). (clumens)
- short_desc is now summary. (clumens)
- Use print() as a function. (pjones)

* Sat Sep 06 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.32-1
- Use struct audit_reply instead of struct auditd_reply_list (dcantrell)

* Sat Sep 06 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.31-1
- Use --service=NAME in firewall.py when calling lokkit (dcantrell)
- Make NM work for the DHCP case, at least (dcbw) (#461071). (clumens)
- Sleep a little after dbus to give it time before HAL connects. (clumens)
- Add libsqlite to the initrd, which is needed by NSS libs. (clumens)
- Add more dlopen()ed libraries to the initrd. (clumens)
- Fix various problems with the exn saving UI (#461129). (clumens)
- Fail gracefully if we can't talk to NetworkManager over DBus. (dcantrell)
- Reword text for easy of translating plurals (#460728). (clumens)
- Make sure /bin/sh is linked to /bin/bash (dcantrell)
- Do not include /usr/lib/gconv in install.img (dcantrell)
- Add /etc/NetworkManager/dispatcher.d to the install.img. (clumens)
- Remove last vestiges of rhpxl and pirut. (clumens)
- Only one list of packages in upd-instroot, thanks. (clumens)
- Add xrandr back into the install.img (#458738). (clumens)
- Add a couple more directories to search paths. (clumens)
- Do repo setup and sack setup as separate steps. (clumens)
- Fix a typo that was causing repos in the kickstart file to be skipped
  (#451020). (clumens)

* Fri Aug 29 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.30-1
- Fix a traceback with unencrypted autopart. (dlehman)
- doLoggingSetup has grown some new arguments (#460654). (clumens)
- Updated German translation (fabian)
- Remove references to isConfigured in network.py (dcantrell)
- Define the NM_STATE_* constants in isys.py (dcantrell)
- Rewrite NetworkWindow to only prompt for hostname. (dcantrell)
- Pad the icon more in network.glade (dcantrell)
- Removed iface_dns_lookup() (dcantrell)
- Don't pass NULL to dbus_message_unref() (dcantrell)
- New network configuration screen for GTK+ UI. (dcantrell)
- Pass family to iface_ip2str() call (dcantrell)
- Rewrite iface_ip2str() to talk to NetworkManager over D-Bus (dcantrell)
- New translation (besnik)
- Pull in the gtkrc file so we can find the theme. (clumens)
- Use signed git tags (katzj)
- Skip networkDeviceCheck in dispatch.py (dcantrell)
- Do not call has_key() on NetworkDevice, use isys.NM_* (dcantrell)
- Separate lines per BR. (dcantrell)
- Remove invalid line iw/autopart_type.py (dcantrell)
- Fix syntax error in yuminstall.py, fix pychecker warnings. (dcantrell)
- Updated Hungarian translation (sulyokpeti)
- Add missing () to function definitions. (dcantrell)
- Fix err handling in doMultiMount() (dcantrell)
- Revert "Pass --follow to git-log" (dcantrell)
- Remove references to /tmp/netinfo (dcantrell)
- Gather network settings from NetworkManager and ifcfg files. (dcantrell)
- Update the pot file and refresh the pos (katzj)
- For all HTTP/FTP repos, keep the cached repodata (#173441). (clumens)
- Fix a traceback when trying to set the status whiteboard on a bug.
  (clumens)
- When the wrong filesystem type is used, raise a more explicit error.
  (clumens)
- Don't copy the install.img over in single media cases (#216167). (clumens)
- Remove isys.getopt() (dcantrell)
- Remove code not used in net.c (dcantrell)
- Write to /etc/sysconfig/network-scripts/ifcfg-INTERFACE (dcantrell)
- mystrstr() -> strstr() (dcantrell)
- Expand getDeviceProperties to return all devices. (dcantrell)
- Pass --follow to git-log (dcantrell)
- Support accessing preexisting LUKS devs using LRW or XTS ciphers.
  (#455063) (dlehman)
- Use yum's handling of optional/default/mandatory package selection
  (#448172). (clumens)
- List iSCSI multipath devices in the installer UI. (dcantrell)
- Fix text wrap width on the partition type combo, for real this time
  (#221791) (dlehman)
- For /dev/hvc0 terminals, set TERM to vt320 (#219556). (dcantrell)
- The Timer class is no longer used. (clumens)
- Handle preexisting swraid w/ encrypted member disks/partitions. (dlehman)
- Don't try to close a dm-crypt mapping that is not open. (dlehman)
- Remove unused silo code that wouldn't even build if it were used. (clumens)
- Remove some really old, really unused code. (clumens)
- Add another mount function that takes a list of fstypes to try. (clumens)
- Download progress indicator for FTP and HTTP in stage 1. (dcantrell)
- Make sure we wait for NetworkManager. (dcantrell)
- Renamed loader2 subdirectory to loader (hooray for git) (dcantrell)
- Do not include wireless.h or call is_wireless_device() (dcantrell)
- Add getDeviceProperties() and rewrite getMacAddress() (dcantrell)
- Do not include wireless.h (dcantrell)
- Rewrite isys.isWireless() to use D-Bus and NetworkManager (dcantrell)
- Rewrite isys.getIPAddress() to use D-Bus and NetworkManager. (dcantrell)
- Include ../isys/ethtool.h instead of ../isys/net.h. (dcantrell)
- Rename isys/net.h to isys/ethtool.h, removed unnecessary typedefs.
  (dcantrell)
- Removed waitForLink() function in loader. (dcantrell)
- Remove initLoopback() function in loader (dcantrell)
- Use D-Bus properties to get current NM state. (dcantrell)
- Use dbus in hasActiveNetDev() and _anyUsing() (dcantrell)
- Use NetworkManager instead of libdhcp. (#458183) (dcantrell)
- When mount fails, pass the error message up to the UI layer. (clumens)
- Bring askmethod back to prompt for the location of install.img. (clumens)

* Fri Aug 22 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.29-1
- Enable yum plugins. (clumens)
- In the preupgrade case, repo=hd: means an exploded tree on the hard drive.
  (clumens)
- Remove preupgrade-specific hacks. (clumens)
- Add conf files for our yum plugins so they can be enabled. (clumens)
- Create a subpackage containing the yum plugins. (clumens)
- Add the new blacklist and whiteout yum plugins. (clumens)
- Allow retrying if the ISO images aren't found (for the USB case). (clumens)
- Include "--encrypted" in anaconda-ks.cfg partitioning as needed. (#459430)
  (dlehman)
- Support establishing a global passphrase when creating encrypted devices.
  (dlehman)
- Display the lock icon for encrypted RAID members. (#459123) (dlehman)
- More descriptive drive message when warning on format. (dcantrell)
- Need to import rhpl for things like switching to pdb. (clumens)
- Fix traceback in passphrase handling code for encrypted RAID requests.
  (#459121) (dlehman)
- Copy the install.img to /tmp on HD installs. (clumens)
- Fix a typo (dcantrell).
- Expert mode was disabled in 2004.  Remove it now. (clumens)
- Remove an extra "Local disk" option (#459128). (clumens)
- Clear up error reporting on upgrades when devices are listed by UUID.
  (clumens)
- If the UI was used to specify a repo, construct a repo param (#458899).
  (clumens)
- Fix a traceback calling createMapping. (clumens)
- First crack at upgrade of systems with encrypted block devices. (#437604)
  (dlehman)
- In kickstart, prompt for new LUKS dev passphrase if not specified.
  (#446930) (dlehman)
- Remove passphrase check hack from LUKSDevice.getScheme. (dlehman)
- Allow specification of a device string for display in passphrase dialog.
  (dlehman)
- Add encrypted device passphrase dialog for text mode. (dlehman)
- Fix PartitionDevice.getDevice to take asBoot into account. (dlehman)
- Make passphrase dialogs appear in the center of the screen. (#458114)
  (dlehman)
- Consider clearpart and ignoredisk when scanning for encrypted partitions.
  (dlehman)
- Correctly handle typos in the stage2 location when inferred from repo=.
  (clumens)
- Fix the loader UI when prompting for stage2.img on HDISO. (clumens)
- Rename stage2.img to install.img (dcantrell)
- Bring up the network before saving a bug via scp. (clumens)
- Make it more explicit we want the stage2.img URL, not the repo URL.
  (clumens)
- Add the match type so we don't find all bugs. (clumens)
- Make upd-updates create the updates.img you specify if it doesn't already
  exist. (pjones)
- Don't base mpath/dmraid/raid startup/stopping based on if lvm is activated
  yet, (pjones)
- Add diskset.devicesOpen boolean, so we can tell if devices should be
  started (pjones)
- Add dirCleanup back in so we don't leave install metadata behind. (clumens)
- Move betanag to after keyboard and language are setup. (clumens)
- Add module dependencies of qeth.ko (#431922). (clumens)
- Copy the changes from RHEL5 for the linuxrc.s390 over. (clumens)
- Disable SCSI devices so we can safely remove a LUN (bhinson, #249341).
  (dcantrell)

* Tue Aug 12 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.28-1
- More fixes to include udev rules in the initrd (#458570). (clumens)
- Catch the first non-generic-logo package that provides system-logos.
  (clumens)
- Remove extra ')' in install-buildrequires (dcantrell)

* Mon Aug 11 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.27-1
- Handle 'rescue' and %%post in rescue mode (atodorov)
- Delay the duplicate label error until the label is actually used
  (#458505). (clumens)
- Enable wireless modules again for now as a test (#443545). (clumens)
- udev rules have changed location (#458570). (clumens)
- Add install-buildrequires target. (dcantrell)

* Fri Aug 08 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.26-1
- Remove a bunch of cachedir setting code that is no longer needed. (clumens)
- Fix segfaults on interactive NFS installs (#458416). (clumens)
- Fix LVM error handling so the exceptions actually get into the namespace.
  (pjones)
- yuminstall: don't look for kernel-xen anymore (markmc)
- console: kill the /proc/xen hack (markmc)
- yuminstall: don't ever stop people installing the virt group (markmc)
- lang: kill xen keymap hack (markmc)
- bootloader: remove old kernel-xen-{guest, hypervisor} handling (markmc)
- Preserve baseurl/mirrorlist and mirrorlist checkbox settings across loads.
  (clumens)
- It's BETANAG, not betanag. (clumens)
- Various string fixes (clumens).
- Wrap spec file changelog lines. (dcantrell)
- mk-images: replace kernel-xen with pv_ops kernel (markmc)
- Use a temporary location for yum cache data (#457632). (clumens)
- Remove extra newtPopWindow() call that was causing a crash (#260621).
  (dcantrell)
- Add /sbin/sfdisk (#224297). (dcantrell)
- Do not call _isys.vtActivate() on s390 or s390x platforms (#217563).
  (dcantrell)
- Change the maximum recommended swap size to "2000 + (current
  ram)".(#447372) (jgranado)
- Make it >= not > for the memory size comparison (#207573) (pjones)
- Allow float comparison between nic names in isys.py. (#246135) (joel)
- Fix formatting on disk sizes >1TB (pjones)
- Don't traceback when trying to remove /mnt/sysimage (#227650). (dcantrell)
- If we're booting off the boot.iso, don't prompt for lang or kbd (#457595).
  (clumens)
- Don't mention images/diskboot.img anymore (#441092). (clumens)
- Remove iSeries image generation (#456878) (dcantrell)
- Display capslock status correctly (#442258) (dcantrell)

* Mon Aug 04 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.25-1
- Eject the CD/DVD if we booted off a boot.iso as well (#442088). (clumens)
- Fix a GTK warning that only appears with s-c-ks running from a
  shell (#431844). (clumens)
- Break a few functions out of yuminstall.py into their own file. (clumens)
- We're not actually activating new filesystems quite yet. (clumens)
- Fix a typo in the initial partitioning screen. (clumens)
- Use system-logos instead of hardcoding fedora-logos (#457378). (clumens)
- anaconda can no longer be None when we create a DiskSet instance. (clumens)
- Remove LabelFactory since we now rely on UUIDs for everything. (clumens)
- Filter out repos that aren't enabled when running in betanag mode. (clumens)
- Close the transaction between CDs (#457126). (clumens)
- Split media fixes. (clumens)
- Handling (ask user) of invalid timezone value in kickstart added
  (#404323) (rvykydal)

* Thu Jul 31 2008 Jeremy Katz <katzj@redhat.com> - 11.4.1.24-1
- Don't try to use self.tree as the mode to open .discinfo. (clumens)
- Remove all the RPM lock files before creating a new
  transaction (#456949). (clumens)
- Support VDSK devices on s390x (#264061) (dcantrell)

* Wed Jul 30 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.23-1
- Fix mke2fs argument passing (#457285). (clumens)
- Disable logging in the firmware loader, since it clobbers other
  log messages. (pjones)

* Wed Jul 30 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.22-1
- udevsettle takes forever, so display a waitWindow. (clumens)
- Leave anaconda-runtime around for mk-images run. (dcantrell)

* Tue Jul 29 2008 Jeremy Katz <katzj@redhat.com> - 11.4.1.21-1
- Remove an instance of NEEDGR still existing to fix graphical
  isolinux (#457144) (katzj)
- use newer mke2fs arguments for different filesystems (sandeen)
- Use attributes to tell us whether filesystems are
  bootable (#457037). (clumens)
- Make sure we drag in gzip, used by the image creation stuff. (jkeating)

* Fri Jul 25 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.20-1
- Clean up some mistakes in the minstg2 removal. (dcantrell)
- Fix passing the language to anaconda (katzj)

* Thu Jul 24 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.19-1
- Fix another NFS kickstart segfault (#456461). (clumens)
- Remove support for generating a minstg2.img image. (dcantrell)
- If the xconfig command is given, do something with it (#455938). (clumens)
- METHOD_CDROM is now supported on s390 (jgranado). (clumens)
- Fix test for if we could access stage2.img on the CD (wwoods).
- Look for updates.img and product.img on the boot.iso. (clumens)
- Suspend the curses interface before calling scripts and resume afterwards
  (#435314) (msivak)

* Wed Jul 23 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.18-1
- MD_NEW_SIZE_BLOCKS no longer exists in newer kernel headers. (clumens)

* Wed Jul 23 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.17-1
- Add support for filing bugs straight into bugzilla. (clumens)
- Running git-tag -f from a makefile rule is a bad idea (katzj)
- A text message in rescue.py is not gettext-ized (atodorov)
- Code cleanup - handling of --serial (atodorov)
- Offer physical NIC identification in stage 1 (#261101) (dcantrell)
- Specify a default cio_ignore parameter for s390x (#253075) (dcantrell)
- Fix getting the stage2 image when doing kickstart installs. (clumens)
- Convert package names to unicode before displaying the error message
  (#446826). (clumens)
- When there is text mode specified in the kickstart file, disable the vnc
  question (#455612) (msivak)
- We no longer add the fstype to the hd: method in loader. (clumens)
- Check DHCP by default on the text network configurator screen. (clumens)
- Support booting from FCP-attached CD/DVD drive on s390 (#184648) (dcantrell)

* Thu Jul 17 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.16-1
- Support xdriver= again (katzj)
- Fix loadkeys on serial console (niels.devos)
- don't change from cmdline to textmode on lowmem systems (niels.devos)
- Update the VNC over text mode patch, so it correctly passes the password
  to VNC server (#455612) (msivak)
- Set interface MTU if user specified mtu= param (#435874) (dcantrell)
- Bring up the network before attempting to mount the NFSISO source. (clumens)
- Catch mount errors when adding NFS repos (#455645). (clumens)
- Fix a traceback when trying to save exceptiona via scp. (clumens)
- Give a progress bar when cleaning up after upgrades (#208725). (clumens)
- Look for repo config files in /etc/anaconda.repos.d. (clumens)
- baseurl should be a list, mirrorlist should not. (clumens)
- It's called crypto_blkcipher.ko these days. (clumens)

* Tue Jul 15 2008 David Cantrell <dcantrell@redhat.com> - 11.4.1.15-1
- Add a text-mode network config dialog so default installs can work. (clumens)
- Use the right format for the NFS methodstr, but harder this time. (clumens)
- Ask the user if he wants to use VNC instead of text mode (#453551) (msivak)
- Fix a segfault when displaying the wrong CD message. (clumens)
- Use the right format for the NFS methodstr. (clumens)
- Use correct path for FAK plugins in upd-instroot (jgranado)

* Fri Jul 11 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.14-1
- Remove an extra tab that was causing problems with the Iloko
  translation. (clumens)
- Use the right stage2.img path for kickstart URL installs (#452140). (clumens)
- Convert package errors to unicode before displaying them (#441200). (clumens)
- Display a status message while waiting for the CD to become ready. (clumens)
- Fix window title to be the same as all others. (clumens)
- In cmdline mode, give some feedback when transferring loader files. (clumens)
- If network config info isn't provided for cmdline, abort. (clumens)
- If we're not given a method in cmdline mode, we have to quit. (clumens)
- In cmdline mode, set language to the default if none is provided. (clumens)
- Don't stop on the method screen if stage2= is provided. (clumens)
- Add support for NFS to the repo editor (#443733). (clumens)
- Fix whitespace silliness. (pjones)
- Fix closing the drive door so that if the kernel happens to start giving us
  the right error code, we'll handle it correctly... (pjones)
- Fix the mysterious Error: OK message. (clumens)
- The return value from mediaCheckCdrom is totally useless. (clumens)
- Add better error handling when initializing yum (#453695). (clumens)
- Add functions for creating repos as well. (clumens)
- Don't handle all possible exceptions as if they were repo errors. (clumens)
- Reorganize to make it easier to reset the "base" repository. (clumens)
- Remove the pkgSack when a repo is disabled. (clumens)
- Use the new method of calling the NetworkConfigurator. (clumens)
- Add an updated repo editor. (clumens)
- Don't suggest text mode to the poor, poor user. (pjones)

* Wed Jul 09 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.13-1
- Filter out source and debuginfo repos from the UI. (clumens)
- Add the MD5 sum to the boot.iso to avoid errors in loader
  (#453698). (clumens)
- Don't strip too much off the NFS directory path. (clumens)
- Log stage2 url better. (pjones)
- Fix minor whitespace nits. (pjones)
- Use %%m rather than strerror() where appropriate. (pjones)
- Make setupCdrom() actually return the path to the stage2 image it
  found. (pjones)
- Don't unconditionally pass --lang for live installs (#454101) (katzj)
- Set up rhgb for plymouth on live.  And conditionalize rhgb + runlevel 5 (katzj)
- Set up rhgb if plymouth is installed as well as rhgb (katzj)
- Get the math right on how many usec per second... (pjones)
- Import missing module "network". (pjones)
- Wait up to 45 seconds for "No medium found" to stop happening (pjones)

* Thu Jul 03 2008 Peter Jones <pjones@redhat.com> - 11.4.1.12-1
- Add dmraid-libs to PACKAGES so new dmraid won't break installs.

* Thu Jul 03 2008 Peter Jones <pjones@redhat.com> - 11.4.1.11-1
- Fix double free in setupCdrom
- Fix missing psudo->pseudo spelling fix (katzj, #453843)
- Include missing X libraries in stage2.img

* Tue Jul 01 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.10-1
- Remove old livecd flag (katzj)
- Explicitly setup livecd install by passing --liveinst to anaconda (katzj)
- Check return value of asprintf() consistently (dcantrell)
- Per strtol(3) man page, set errno=0 before call. (dcantrell)
- Rescue mode no longer needs access to a methodstr (#453044). (clumens)
- Use strtol() instead of atoi() (dcantrell)
- Spell pseudo correctly. (pjones)

* Wed Jun 25 2008 Chris Lumens <clumens@redhat.com> 11.4.1.9-1
- Query for anaconda rather than anaconda-runtime in buildinstall (jkeating).

* Mon Jun 23 2008 Jeremy Katz <katzj@redhat.com> - 11.4.1.8-1
- Remove from being installed too (katzj)
- Remove anaconda-runtime as a separate subpackage (katzj)
- Remove the stuff we're not calling. (pjones)
- Remove this since we don't use it anymore (katzj)
- Don't continue on using the base installclass if we can't find one (katzj)
- Get rid of wlite and unicode-lite; these were necessary to support (pjones)
- Remove pkgorder and splittree; these should be in pungi (katzj)
- Add the .treeinfo file into the exception report. (clumens)
- Fix a typo (#452140). (clumens)

* Fri Jun 20 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.7-1
- Remove ancient block of code to upgrade Netscape Communicator. (clumens)
- Move enableNetwork into the interface.  Bring network up for scp. (clumens)
- If we can't mount for some reason, don't traceback (#452159). (clumens)
- Fix the upgrade button traceback (#374891). (clumens)

* Wed Jun 18 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.6-1
- Enable media check again, and let it check the boot.iso. (clumens)
- Substitute the version from buildstamp for $releasever if needed. (clumens)
- Remove the askmethod cmdline option. (clumens)
- Lots of work to make loader only look for stage2.img, and stage2 do
  all the install method configuration. (clumens)
- Add the --stage2= and --repo= options, deprecate --method=. (clumens)
- Fix pkgorder to include deps of kernel early. (pjones)
- Deal with udev losing udevcontrol/udevtrigger (katzj)
- Boot in graphical mode if /usr/bin/kdm exists. (clumens)
- bootProto isn't a global variable (#451689). (clumens)

* Fri Jun 13 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.5-1
- Add a mirrorlist option. (jkeating)
- Don't display garbage when prompting for the updates device. (clumens)
- Don't write out yum repo config files in kickstart.py. (clumens)
- It doesn't make sense to insert a disk into a partition, so don't
  ask. (clumens)
- Unmount /mnt/sysimage/dev manually since it doesn't get an entry. (clumens)
- Link ld-linux.so.2 to ld-*.*.*.so (dcantrell)
- Quote the repo name in anaconda-ks.cfg in case it includes spaces. (clumens)
- Move all the exception classes into a single file. (clumens)
- And import iutil a the end as well. (clumens)
- Don't display obsoleted packages in the UI. (clumens)

* Thu Jun 05 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.4-1
- Fix text mode button translations (#450176). (clumens)
- Remove a rogue call to textdomain. (clumens)
- Make "upd-updates /tmp/updates.img" update everything newer in the
  current (pjones)
- _xmltrans is undefined.  Try xmltrans instead. (clumens)
- Fix reference to cost vs. priority (#450168). (clumens)
- Don't do the "exec shell on tty1" thing in vnc if we've got virtual
  terminals. (pjones)
- Import N_ (#450163). (clumens)
- raise "NotImplementedError", not "NotImplemented" (pjones)
- Need to import iutil before we use it. (clumens)
- Don't reference PartitioningError.value . (pjones)

* Wed Jun 04 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.3-1
- Can't reference iutil.whatever from inside iutil.py. (clumens)
- When using the boot.iso and URL installs, download the .treeinfo
  file. (clumens)
- Fix a couple typos in the getArch commit. (clumens)
- Be consistent with data type. (dcantrell)
- Replace rhpl.getArch() calls with iutil calls. (dcantrell)
- Expand iutil.isX86() and added iutil.getArch() (dcantrell)
- Add isAlpha() test function to iutil. (dcantrell)
- Create architecture test functions in iutil (dcantrell)
- Removed mystrstr() function in loader2/init.c (dcantrell)
- Don't support Arabic in text mode installs since we don't even do
  RTL. (clumens)
- Removed old strace debugging in loader2/init (dcantrell)
- Keep only one copy of this code for group sorting/display around (katzj)
- Stop using rhpl.translate and use gettext directly (katzj)
- Add a descriptive comment to the top of /etc/fstab (#448966). (clumens)
- Use "message" instead of "value" on errors, and stringify on the front
  side. (pjones)
- Translate package descriptions (#449455). (clumens)
- Translate password error messages (#439981). (clumens)
- Fix traceback starting vnc (#449295) (katzj)
- Add Hewbrew to lang-table (oron)
- Fix errors in python string formatting (#449130). (clumens)

* Thu May 29 2008 Chris Lumens <clumens@redhat.com> - 11.4.1.2-1
- Allow ext4 migration again for testing at least (katzj)
- Remount filesystems after migration (#440055) (katzj)
- Add blkid to the keepfiles list so jkeating will whine less (pjones)
- Don't allow vfat /boot (katzj)
- Use the base yum doConfigSetup method. (clumens)
- Include the yum repo files from fedora-release in stage2. (clumens)
- No longer maintain our own list of extra repos. (clumens)
- Sort the repos in the UI. (clumens)
- Add cost, includepkgs, and excludepkgs to the ks repo
  objects (#448501). (clumens)
- Stop pretending to support Greek text mode (#208841) (katzj)
- Make it clear you need to reboot to use the installed
  system (#238297) (katzj)
- Activate LVM for when we do meta-resizing (#441706) (katzj)
- List Norweigian as Bokmål (#437355) (katzj)
- Simplify the install classes. (clumens)
- Don't show the EFI filesystem unless we're on an EFI platform (katzj)
- Add nfsv4 so that we don't nuke them on upgrades (#448145) (katzj)
- When there are errors reading the live CD, offer a retry. (clumens)
- Can't recover from buildTransaction errors on a per-repo
  basis (#447796). (clumens)
- Set default partition size to 200 MB in the custom partitioning
  UI. (clumens)
- Limit the size of things in exception dumps to 1k. (clumens)
- Catch IOErrors one place they seem to happen most. (clumens)
- Add a unique user agent for anaconda's grabbing in stage2 (katzj)
- Remove text mode help support as well. (clumens)
- Check for all the non-mkfs utilities required for each filesystem
  type. (clumens)
- More partitioning error handling fixes (#446453). (clumens)
- Require cracklib-python for the rootpassword screen. (notting)
- Use pykickstart's deprecated versions of the xconfig and monitor
  classes. (clumens)
- Fix tyop in upgrade migrate screen (#446363) (katzj)

* Tue May 13 2008 Jeremy Katz <katzj@redhat.com> - 11.4.1.1-1
- Just call the XStartupCB() function directly and randr to the
  desired resolution (katzj)
- Stop writing out an xorg.conf (katzj)
- Make the "dump to removable device" option work in anaconda. (jgranado)

* Mon May 12 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.79-1
- Stop neutering DRI (notting)
- make scripts/buildinstall take multiple repos (wwoods)
- Don't worry about telling people that interactive text mode is in
  wrong lang (katzj)
- Allow cpio updates.img in the tree for URL installs. (dlehman)
- Declare unpackCpioBall for use from within urlinstall.c. (dlehman)
- Don't unlink an image we retrieved but could not mount as it
  could be .cgz. (dlehman)
- Don't run lspci with an explicit path (katzj)
- Include lspci on all images (#445974) (katzj)
- Add support for attaching gdbserver to the loader early on. (clumens)
- Add virtio max partition count (markmc)
- Sort virtio devices first (markmc)
- Merge branch 'master' of ssh://git.fedorahosted.org/git/anaconda (andrewm)
- 2008-05-08  Andrew Martynov <andrewm)
- Look in the right place when ISO images are in a
  subdirectory (#443580). (clumens)
- And run in the root (#374921) (katzj)
- Don't crash when given URLs of the form ftp://user)
- Use 'yum clean all' when cleaning up after an upgrade, not
  preupgrade (#374921) (katzj)
- Kickstart flag is backwards (katzj)
- If we're given a language, don't warn about console fonts (#444258) (katzj)
- And actually include the bash binary too (#443700) (katzj)
- Search path rather than hard-coding path to mdadm (#444843) (katzj)
- Fix incorrect command name in error message. (clumens)
- Specify which protocol is used for remote saving (#440214). (clumens)
- Use bash for minstg2 shell (#443700) (katzj)
- Revert PS1 and PATH changes as they don't work with busybox as used
  in minstg2 (katzj)

* Mon Apr 28 2008 David Cantrell <dcantrell@redhat.com> - 11.4.0.78-1
- Write per-interface DNS info to ifcfg files (#443244) (dcantrell)
- Clean up sanityCheckHostname() in network.py (dcantrell)
- Activate autorepeat for GUI installs. (jgranado)

* Fri Apr 25 2008 David Cantrell <dcantrell@redhat.com> - 11.4.0.77-1
- Preserve 'set the hostname' setting when going Next/Back (#443414) (dcantrell)
- Avoid traceback on network configuration screen (#444184) (dcantrell)
- Add missing backslashes for the .profile here document. (dcantrell)
- Label the efi boot filesystem on ia64 as well. (pjones)
- Don't use size to determine if a partition is an EFI system
  partition; instead, (pjones)
- Handle the DVD having a disknumber of ALL. (443291) (jkeating)
- Make the LUKS passphrase prompt fit on an 80x25 screen. (#442100) (dlehman)
- Don't dd the image from /dev/zero _and_ use
  "mkdosfs -C <image> <blockcount>" (pjones)
- label the filesystem in efidisk.img so that HAL and such won't try to
  mount it. (pjones)
- fix testiso Makefile target - boot.iso, not netinst.iso (wwoods)

* Thu Apr 24 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.76-1
- Use the execWithCapture wrapper to be consistent. (jgranado)
- Call the mdadm with full path. (jgranado)
- Use the correct ls(1) alias. (dcantrell)
- Set PS1 and ls(1) alias for tty2 shell. (dcantrell)
- Lookinig for the capabilities file in xen is valid in more cases. (jgranado)
- Avoid putting virtualization option when in Xen or VMware.
  (#443373) (jgranado)
- If the stage2 image is on a CD, don't bother copying it (#441336). (clumens)
- Once we've found the stage2 media on CD, always use it (#443736). (clumens)
- Change mount point for CD to /mnt/stage2 when looking for stage2
  (#443755). (clumens)
- Switch to using 'yum clean all' to clean up after preupgrade
  (#374921) (katzj)
- Handle .utf8 vs .UTF-8 (#443408) (katzj)
- Avoid dividing by zero (#439160) (katzj)
- Changes related to BZ #230949 (dcantrell)
- $XORGDRIVERS no longer exists (markmc)
- Bump version. (katzj)
- Write IPv6 values to /etc/sysconfig/... correctly (#433290) (dcantrell)
- Use the right base class for autopart handler. (clumens)

* Fri Apr 18 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.75-1
- Listing the directories before expiring yum caches helps (katzj)

* Fri Apr 18 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.74-1
- Don't look for .discinfo on the rescue CD (#442098). (clumens)
- Use /var/cache/yum as the cachedir since /tmp might be
  too small (#443083). (clumens)
- Revert "Don't look for a .discinfo file in rescue
  mode (jvonau, #442098)." (clumens)
- Revert "Fix figuring out that the CD has stage2 on it and should
  be mounted." (clumens)
- We've always expected devices to be strings, not unicode (#443040) (katzj)
- Resizing lvs on top of RAID fails, make the error not a traceback (katzj)
- Don't put an extra slash on the error message (jgranado)
- Kernel changed howw the uevent API works for firmware
  loading *AGAIN*. (pjones)
- Expose the log file descriptors so fwloader can avoid closing
  them (pjones)
- Minor UI tweaks to passphrase dialogs (katzj)
- Nuke preupgrade cache once we're done (#442832) (katzj)
- Support bringing up the network if needed with preupgrade (#442610) (katzj)
- Use a real GtkDialog instead of some crazy hacked up dialog (katzj)
- Fix handling of pre-existing raids for the upgrade/rescue
  case (#441770) (katzj)
- Add missing / (Doug Chapman, #442751) (katzj)

* Wed Apr 16 2008 David Cantrell <dcantrell@redhat.com> - 11.4.0.73-1
- Fix figuring out that the CD has stage2 on it and should be mounted. (clumens)
- Don't copy the stage2 image on NFS installs (#438377). (clumens)

* Tue Apr 15 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.72-1
- Don't use megabytes for the livecd size for copying. (notting)
- find moved (katzj)
- Fix up silly syntax error that crept in to this commit (katzj)
- Back to using the raw version of the docs (#442540) (katzj)
- Expire yum caches on upgrade (#374921) (katzj)
- Include KERNEL== in udev rules (#440568) (dwmw2)
- Don't look for a .discinfo file in rescue
  mode (jvonau, #442098). (clumens)
- Slower machines may take more than five seconds for hal
  to start (#442113) (katzj)
- Pass the full device path (notting)
- Only include the parts of grub that will work without
  crazy tricks (#429785) (katzj)

* Thu Apr 10 2008 Peter Jones <pjones@redhat.com> - 11.4.0.71-1
- Fix destdir handling in upd-kernel (markmc)
- Get rid of module ball remnants in mk-images (markmc)
- Make upd-kernel handle version numbers the way we do them now (markmc)
- Fix ia64 kernel path problems (katzj, #441846)
- Don't tag more than one partRequest with mountpoint=/boot/efi (pjones)
- Don't treat tiny disks as EFI System Partitions during autopart (pjones)

* Thu Apr 10 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.70-1
- ide-cd_mod, not ide-cd_rom (thanks to jwb) (katzj)

* Wed Apr 09 2008 Peter Jones <pjones@redhat.com> - 11.4.0.69-1
- Ignore some warnings copying into /etc and /var (clumens)
- Try to mount the NFS source in the loader to verify it is correct (clumens)
- Be as clean as possible when looking for files/directories (jgranado, #431392)
- More ia64 kernel finding fixage (katzj, #441708)
- Fix read permissions on efidisk.img (pjones)
- Use the mount flags passed to isys.mount() (pjones)

* Wed Apr 09 2008 Peter Jones <pjones@redhat.com> - 11.4.0.68-2
- Fix device-mapper dep.

* Tue Apr 08 2008 Peter Jones <pjones@redhat.com> - 11.4.0.68-1
- Handle EFI partitions somewhat better (pjones)
- Fix typo in mk-images.efi's parted usage (pjones)

* Tue Apr 08 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.67-1
- Set the initial state of the auto-encrypt checkbutton (#441018) (katzj)
- Don't treat RAID devices as "disks" to avoid lots of odd
  behavior (#438358) (katzj)
- Log a message if we disable selinux on upgrade (katzj)
- Build efiboot.img on x86_64 and i386 . (pjones)
- When splitting srpms, only link srpms, nothing else. (jkeating)
- Don't cause the text to flicker between installed packages. (clumens)
- Don't cause the screen to jump up and down between
  packages (#441160). (clumens)
- Fix zooming and centering in the timezone screen (#439832). (clumens)
- Handle ia64 kernel path (katzj)
- And add nas to the list (#439255) (katzj)
- Set parent so that the dialog centers (#441361) (katzj)
- Don't show the label column (#441352) (katzj)
- Do string substitution after we've translated (#441053) (katzj)
- Set domain on glade file so translations show up (#441053) (katzj)
- fix compression of modules (notting)
- More build fixing due to translation breakage. (katzj)
- Add code to create efiboot.img on i386 and x86_64 (pjones)
- Remove gnome-panel too, it's no longer multilib. (jkeating)
- Fix raising new NoSuchGroup exception. (clumens)
- remove debugging print (notting)
- Support encrypted RAID member devices. (#429600) (dlehman)
- No longer require Amiga partitions on Pegasos (dwmw2)
- Don't copy the stage2 image every time or on the way back. (clumens)
- Make lukscb.get_data("encrypt") always return a valid value. (pjones)
- Set the scrollbar color so it doesn't surprise me the same way in
  the future. (pjones)
- Translation updates.

* Sun Apr 06 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.66-1
- Another day, another broken translation commit to fix. (katzj)
- Work around GL crashes in anaconda X by disabling them. (jkeating)
- Clean up "finishing upgrade" wait window (katzj)
- Stop refreshing like mad in text-mode on WaitWindow.refresh() (katzj)
- Avoid progress bars going off the end and making newt unhappy (katzj)
- Brute force hack to avoid the number of packages
  overflowing (#436588) (katzj)
- Revert "Change the default level in /etc/sysconfig/init now
  (#440058)." (notting)
- Add gnome-applets to the upgrade blacklist, fix kmymoney2 typo. (jkeating)
- Don't enable encryption by default (katzj)
- Print our mount commands to /dev/tty5 for easier debugging. (clumens)
- Change the default level in /etc/sysconfig/init now (#440058). (clumens)
- Make the Back button work when asking for tcp/ip information in
  loader.c. (#233655) (jgranado)
- Have <F12> work in the network configuration stage (#250982) (jgranado)
- Use a better test to see if a package group doesn't exist (#439922). (clumens)
- avoid behavior in (#208970) (jgranado)
- Correctly label the xen images in the .treeinfo file (jgranado)
- Translation updates

* Wed Apr 02 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.65-1
- Only do verbose hal logging if loglevel=debug (katzj)
- Avoid AttributeError in HardDriveDict (#432362) (pjones)
- Don't use %%n with gettext to avoid segfaults (#439861) (katzj)
- Require live installs to be to an ext2 or ext3 filesystem (#397871) (katzj)
- Don't allow migrations to ext4 for now (katzj)
- Change ext4 parameter to ext4, not iamanext4developer (katzj)
- Bootable requests can not be on logical volumes (#439270). (clumens)
- Don't allow /boot to be migrated to ext4 (#439944) (katzj)
- Fix for ia64 (#439876) (katzj)
- Update pkgorder group listings to match current Fedora defaults. (jkeating)
- Lame attempt to try to avoid race condition with udev creating device
  nodes (katzj)
- Don't traceback if stdout is an fd either (katzj)
- iutil doesn't need isys anymore (katzj)
- Free memory only after we're done using it (#439642). (clumens)
- Fix a segfault freeing memory on boot.iso+hdiso installs. (clumens)

* Mon Mar 31 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.64-1
- Fix my tyop (katzj)
- Fuzzy broken string again (katzj)

* Sun Mar 30 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.63-1
- Fix broken translations.  Again. (katzj)

* Sun Mar 30 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.62-1
- Translation updates
- Allow GPT disk labels on ppc/ppc64. (dcantrell)
- Tear down the right loopback device before going to stage2. (clumens)
- Don't pass None as stdout or stderr. (clumens)
- Make sure there's a stdout to write to. (clumens)
- Handle fstype munging in isys.readFSType instead of in various
  other places. (dlehman)
- Fix a typo in new encrypted LV code. (dlehman)
- Partitioning UI for handling of preexisting encrypted devices. (dlehman)
- Support discovery of preexisting rootfs on LV. (dlehman)
- Improve handling of logical volume device names when encrypted. (dlehman)
- Add support for discovery of preexisting LUKS encrypted devices. (dlehman)
- Add support for retrieving LUKS UUIDs. (dlehman)
- Refresh po files (katzj)
- Mark for translation based on feedback from translators (katzj)
- Just relabel all of /etc/sysconfig (#439315) (katzj)
- When dhcp is selected ensure that bootproto is set to
  dhcp (RPL-2301) (elliot)
- Fix for test mode repo bits (katzj)
- Try to make the size flow a little more for weird resolution
  screens (#439297) (katzj)
- Add kmymoney to upgrade remove list (#439255) (katzj)

* Thu Mar 27 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.61-1
- Fix broken translation. (clumens)

* Thu Mar 27 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.60-1
- Have a fallback empty description for devices (#432362) (katzj)
- os.path.join does not work the way we think it should. (clumens)
- Remove the stage2 in all cases now that we're copying it basically
  all the time (katzj)
- Add support for saving the exception to a local directory for live
  installs (katzj)
- Catch errors on resize and present a dialog to the user (katzj)
- Save resize output to a file (/tmp/resize.out) so that it's more
  useful (katzj)
- Make sure we give the command that's run on stdout so that it's
  logged (katzj)
- more mouse-related removals (notting)
- Fix up autopart resizing for the multiple partitions to resize case (katzj)
- Fix up the case where both method= and stage2= are given (katzj)
- Remove mouse screens that haven't been used in 4 years (katzj)

* Wed Mar 26 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.59-1
- Only remove duplicate slashes from the front of the prefix. (clumens)
- Ensure that we take into account new repos (katzj)
- Handle kernel variants a little better at install time too (katzj)
- Make a little bit more future proof for kernel version changing (katzj)
- Add confirmation of closing the installer window (#437772) (katzj)
- Fix SIGSEGV on all mounts without options (katzj)
- Add support for encrypted logical volumes in kickstart. (clumens)
- Add support for encrypted LVs. (dlehman)
- Put in some handling for redundant method calls and devices containing '/'.
  (dlehman)

* Tue Mar 25 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.58-1
- Fuzzy broken string (katzj)

* Tue Mar 25 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.57-1
- Use anaconda-upgrade dir in the preupgrade case (katzj)
- Have 'preupgrade' key doing an upgrade (katzj)
- Fix what we expect to be the message from ntfsprogs (katzj)
- Fix up compile error for new newt (katzj)
- Don't traceback if we have little freespace partitions (#438696) (katzj)
- Translation updates (ko, ru)

* Mon Mar 24 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.56-1
- Translation updates (hi, fr, kn, de, ml, es, mr, ko, te)
- Fix up more unicode shenanigans (#437993) (katzj)
- Move /tmp/stage2.img to /mnt/sysimage to free up some
  memory (#438377). (clumens)
- Be a little smarter about downloading repo metadata (#437972). (clumens)
- Make sure that devices are set up before using them. (#437858) (dlehman)
- Don't prepend /dev/ on bind mounts either. (clumens)
- Use the repo name instead of id in the group file error
  message (#437972). (clumens)
- Handle /dev being on hard drive devices in the second stage (katzj)
- Fix the build (katzj)
- The units for /sys/block/foo/size aren't bytes.  Fixes finding some
  disks (katzj)
- Remove the check for .discinfo on URL installs. (clumens)
- Always unmount /mnt/source on hdiso installs before starting
  stage2. (clumens)
- Always unmount /mnt/source on nfsiso installs before starting
  stage2. (clumens)
- Make sure the first disc image is mounted before setting up repos. (clumens)
- Fix $UPDATES for real (katzj)
- Avoid piling up slashes in the UI when retrying (#437516). (clumens)
- Require comps-extras now that we don't require pirut bringing it in (notting)
- Put "ide-cd_mod" in the list of modules to pull in. (pjones)

* Tue Mar 18 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.55-1
- Fix format of method=hd: parameter (#438075). (clumens)
- Work on support for NFSISO installs when using boot.iso. (clumens)
- If a file doesn't exist, don't continue trying to loopback mount
  it. (clumens)
- Make loopback mount error messages more useful. (clumens)
- Focus root password entry box (#436885). (dcantrell)
- Fix a traceback writing out the method string for hdiso installs. (clumens)
- Fix use of sizeof on a malloc()'d char ** (pjones)
- Fix up ppc boot check (#438005) (katzj)
- Support reading the UUID from the disk like we do with labels. (clumens)
- If the protected partition is not yet mounted, mount it now. (clumens)
- Don't add /dev/ to LABEL= or UUID= devices either. (clumens)
- Use arch instead of the name again in package nevra. (clumens)
- Fix traceback with preexisting LUKS partitions in setFromDisk.
  (part of #437858) (dlehman)

* Mon Mar 17 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.54-1
- Translation updates (de, fi, it, gu, ta, pa)
- Fix a typo. (clumens)
- Fix the build. (clumens)
- Make sure we return the same kind of exception in all cases. (clumens)
- Filter so we don't show LVM and RAID components when adding
  boot entry (#437501) (katzj)
- Only print the filename we're fetching, as newt doesn't like
  long names. (clumens)
- Fix off by one error reading .buildstamp (pjones)
- Use the right path when trying to fetch .discinfo. (clumens)
- Don't prepend /dev/ onto nfs devices.  Also log mount
  errors to tty5. (pjones)

* Sun Mar 16 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.53-1
- Update translations (pl, de)
- Use i586 kernel (#437641) (katzj)
- Give indication of success or failure for mediacheck (#437577) (katzj)
- Ensure the UUID for the rootfs is random and not the same for every
  live image (katzj)
- Make migration from ext3 -> ext4 saner on upgrade (#437567) (katzj)
- Force filesystem mount options on /boot/efi . (pjones)
- On HDISO installs, look for the stage2.img file in the right
  directory. (clumens)
- Accept devices with or without a leading /dev/. (clumens)
- .buildstamp no longer contains productPath, so change
  the default (#437509). (clumens)
- Remove references to an uninitialized variable. (clumens)
- Use shortname=winnt instead of shortname=win95 when
  mounting /boot/efi (pjones)
- Do not strip leading or trailing whiltespace from
  passphrases. (#437499) (dlehman)
- Set methodstr for nfsiso installs (#437541). (clumens)
- Create and check /boot/efi correctly, and use preexisting
  one if available. (pjones)
- Handle /boot/efi and /boot both as bootrequests (pjones)
- Emit "efi" as /boot/efi's filesystem type (pjones)
- Add EFI handling to the bootloader setup choices. (pjones)
- Add efi to the ignoreable filesystem list. (pjones)
- Add EFIFileSystem, and getMountName() to hide that it's really vfat. (pjones)
- Add isEfiSystemPartition(), and use it where appropriate (pjones)
- Call getAutoPartitionBoot with our partition list as an arg. (pjones)
- Don't show the epoch in package selection either (#437502). (clumens)
- Fix some errors on reporting which files are being downloaded. (clumens)
- Revert "Handle /boot and /boot/efi separately, plus fixes" (pjones)
- Handle /boot and /boot/efi separately, plus fixes (pjones)
- Get rid of unused >1024 cylindar check, fix text of boot
  check exceptions. (pjones)
- Make bootRequestCheck() check /each/ boot partition like it's
  supposed to, (pjones)
- Fix shell quoting on numbers > 9, and fix an error message. (pjones)
- Don't show the epoch in the progress bar (#437502). (clumens)
- Include efibootmgr in the instroot (pjones)

* Thu Mar 13 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.52-1
- Don't unmount NFS source so NFSISO will work. (clumens)
- Fix the format of the method=hd: parameter. (clumens)
- Fix creating new users in kickstart. (clumens)
- "gtk-edit" isn't valid in text mode. (clumens)
- Ignore LUKS headers on partitions containing RAID signatures.
  (#437051) (dlehman)
- The xconfig command with no X running doesn't make sense. (clumens)

* Wed Mar 12 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.51-1
- yum.remove removes installed packages, not to be installed
  packages (#436226) (katzj)
- Make the /tmp/updates vs RHupdates code at least a little readable. (pjones)
- Allow vfat update images. (pjones)
- Fix syntax error (pjones)
- Add a progress bar for when we're downloading headers (#186789). (clumens)
- mount will set up the loopback device if we let it. (clumens)
- Fix mounting problems with NFSISO images. (clumens)
- Simplify the logic for the upgrade arch check (katzj)
- Add a fallback method for determining the architecture of installed
  system during an upgrade (#430115) (msivak)
- Avoid a traceback (#436826) (katzj)
- Make sure host lookups work for manual net config (#435574). (dcantrell)

* Tue Mar 11 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.50-1
- Focus root password entry box (#436885). (dcantrell)
- Make sure default is SHA-512 for libuser.conf. (dcantrell)
- Fix detection of ISO images on a hard drive partition. (clumens)
- Devices names aren't prefixed with /dev/. (clumens)
- Filter out /dev/ram* devices from the list of hdiso partitions. (clumens)
- But make sure that we've activated the keymap now that X
  follows its defaults (katzj)
- Don't set a keyboard in the X config, we should just do this
  at runtime (katzj)
- Writing out the nfs method line is a lot simpler now. (clumens)
- Use /mnt/sysimage/tmp/cache for the yum cache, instead of the
  ramdisk. (clumens)
- Translation updates (nl, gu, ml, mr, pa)

* Mon Mar 10 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.49-1
- Use the full path to the .discinfo file (#436855). (clumens)
- List netinst.iso/boot.iso in .treeinfo (#436089) (katzj)
- Convinced to change the name back to boot.iso (katzj)
- Only pass the file path to {ftp,http}GetFileDesc. (clumens)
- Pass the correct NFS method parameter to stage2 (#436360). (clumens)
- Fix logging messages to not display the hostname twice. (clumens)
- Fix traceback with text mode adding iscsi (#436480) (katzj)

* Thu Mar 06 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.48-1
- Don't use the bits from $UPDATES unless $UPDATES exists (katzj)
- Fix horkage with busybox stuff.  There's now start-stop-daemon (katzj)
- Require new enough version of yum-utils (katzj)
- Pass the --archlist option to yumdownloader (jkeating)
- Update pt_BR translation

* Wed Mar 05 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.47-1
- Fix the build again (katzj)

* Wed Mar 05 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.46-1
- Don't require some things which we fall back gracefully when not there (katzj)
- Check for filesystem utilities to see if a filesystem is supported (katzj)
- Write out keyboard settings before installing packages. (related
  to #429358) (dlehman)
- Update pl translation
- Make sure http:// or ftp:// is specified (#436089) (katzj)
- Fix segfault when port is specified (#435219) (katzj)
- Use ntfsresize -m to get minimum size (#431124) (katzj)
- Use the right path to the .discinfo file when validating a tree. (clumens)

* Tue Mar 04 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.45-1
- Fix the build.

* Tue Mar 04 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.44-1
- Add --archlist to repoquery call. (jkeating)
- Translation updates (pl, nl, ja)
- Handle efibootmgr and grub.efi in upd-instroot. (pjones)
- Merge in branch to implement stage2= parameter. (clumens)
- Revert the memtest86 bits for EFI, since this gets run on
  multiple arches. (pjones)
- Use iutil.isEfi() instead of testing for ia64-ness. (pjones)
- Only do gptsync if we're not using EFI. (pjones)
- Don't do gptsync if we're using EFI. (pjones)
- Use gpt on all efi platforms. (pjones)
- Rework isEfi() to be slightly more conservative. (pjones)
- Test for using efi rather than arch==ia64 (pjones)
- Don't copy memtest86 in on EFI since it won't work. (pjones)
- Add comment regarding usage of elilo (pjones)
- Free some variables so we can http GET twice if needed. (clumens)
- Change the method config prompts. (clumens)
- Support stage2= for CD installs in loader. (clumens)
- Support stage2= for HD installs. (clumens)
- Support stage2= for NFS installs. (clumens)
- Support stage2= for URL installs. (clumens)
- Update the method string handling for NFS and URL installs. (clumens)
- mountStage2 now needs to take an extra argument for updates. (clumens)
- If stage2= is given, it overrides the check for a CD stage2 image. (clumens)
- Support the stage2= parameter, and add a flag for it. (clumens)

* Mon Mar 03 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.43-1
- Only use UUID= for devices we would have labeled.  Related to #435228 (katzj)
- If we don't find a kernel package, then give a better error (katzj)
- Translation updates (cs, de)

* Sun Mar 02 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.42-1
- Fix a traceback when we have an error.  Related to #433658 (katzj)
- Add virtio_pci in hopes of getting virtio working (katzj)
- Pull in the bits of pirut that we use so that we don't depend on pirut (katzj)
- Default to RAID1 instead of RAID0 (#435579) (katzj)
- Refresh po (katzj)
- Fix traceback leaving task selection screen (#435556) (katzj)
- More ext4 vs ext4dev nonsense.  (#435517) (katzj)
- Fix reverse name lookup. (pjones)

* Thu Feb 28 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.41-1
- Don't write out /etc/rpm/platform anymore. (katzj)
- anaconda-runtime now needs yum-utils (katzj)
- Add 'testiso' target (katzj)
- Remove rescue cd creation scripts (katzj)
- Take --updates with location of additional updates beyond the package
  set used (katzj)
- Change the ISOs we build (katzj)
- Take advantage of yum repos being available (katzj)
- Allow recovery from some missing repodata conditions. (clumens)
- Rework the repo editor screen to be more modular. (clumens)
- Move doPostImages to be run after the second stage build (katzj)
- Ensure that group info for txmbrs is accurate after we reset (katzj)
- Fix backwards logic for yum verbosity (katzj)
- No more arc (#435175) (katzj)
- Remove an unused method. (clumens)

* Tue Feb 26 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.40-1
- Use non-deprecated HAL properties. (notting)
- More crud to deal with the fact that rawhide trees are composed weird (katzj)
- Gtk does not have the error type, use custom with proper
  icons. (#224636) (msivak)

* Mon Feb 25 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.39-1
- Fix up symlinks that could be broken with our movement here (#434882) (wwoods)
- pvops xen uses hvc as its console (#434763) (katzj)
- Follow symlinks when looking for the anaconda-runtime package. (jkeating)

* Sun Feb 24 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.38-1
- Write out UUID in the fstab (#364441) (katzj)
- Add support for getting UUID using libblkid (katzj)
- Fix calculation of sizes of LVs when resizing (#433024) (katzj)
- Add back some bits for text mode (katzj)
- Remove advanced bootloader bits (katzj)
- Add support for actually changing where the boot loader gets
  installed as well (katzj)
- Less text. (katzj)
- Reorder things a little, clean up spacing (katzj)
- Use a tooltip instead of a long bit of text that most people
  don't read (katzj)
- Remove advanced checkbox (katzj)
- Switch the grub installation radio to be a checkbutton.  Cleanups for
  grub only (katzj)
- Lets redirect to /dev/null to ensure that what we get in DIR is the
  result of pwd. (jgranado)
- Catch the error emmited by lvm tools during logical volume
  creation process (#224636). (msivak)
- Don't try to lock /etc/mtab, fix error detection when mount fails. (clumens)
- Don't append (null) to the NFS mount options. (clumens)
- There's no need to wait if the last download retry failed. (clumens)
- the '-o' is appended to the mount command in imount.c (jgranado)
- Use full path to device for mount in findExistingRootPartitions. (dlehman)
- Map preexisting encrypted devs before mounting everything
  in mountRootPartition. (dlehman)
- Fix traceback on test mount in findExistingRootPartitions. (dlehman)
- Use SHA-512 by default for password encryption. (dcantrell)
- Clean up root password user interfaces. (dcantrell)

* Tue Feb 19 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.37-1
- Default to the right timezone when language is changed (#432158). (clumens)
- Fix another text mode network config traceback (#433475). (clumens)
- More scripts cleanups. (jgranado)
- Remove more references to ARC (#433229). (clumens)
- Mount flags should be an optional argument (#433279, #433280). (clumens)
- We don't need productpath anymore, so stop taking it as an option (katzj)
- Set yum output level based on whether or not we've passed --debug or
  not (katzj)
- Clean up invocation of mk-images from buildinstall (katzj)
- Clean up invocation of upd-instroot from buildinstall (katzj)
- Remove some legacy stuff that's no longer relevant from
  .discinfo/.treeinfo (katzj)
- Don't depend on product path for finding the anaconda-runtime
  package (katzj)
- Make buildinstall a little clearer (katzj)
- Use $LIBDIR instead of lib globbing to avoid problems with chroots (katzj)
- Add some error handling around populateTs. (clumens)

* Thu Feb 14 2008 David Cantrell <dcantrell@redhat.com> - 11.4.0.36-1
- Fix up firmware inclusion.  This didn't actually ever work. (katzj)
- Fix up the groff related stuff for man pages to be done in the correct
  place (katzj)
- remove yumcache (katzj)
- Don't do fixmtimes anymore (katzj)
- Don't compress translations (katzj)
- Don't manually duplicate things from package %%post scripts (katzj)
- Remove some unused options (--discs and --buildinstdir) (katzj)
- Keep /etc/nsswitch.conf and /etc/shells (katzj)
- Stop forcing passive mode for FTP by patching urllib (katzj)
- We don't use timezones.gz anymore anywhere (katzj)
- We shouldn't need to remove files that are only in -devel packages (katzj)
- Remove some obsolete files from the list to clean up noise in the
  output (katzj)
- We want nss bits on all arches these days (katzj)
- Just use default /etc/nsswitch.conf and /etc/shells (katzj)
- alpha should have translations probably (katzj)
- Remove some things that aren't used anymore (katzj)
- Don't run pkgorder as a part of buildinstall anymore (katzj)
- Remove duplicate file from the file lists (katzj)
- Don't use the static versions of these anymore as they're likely to go
  away (katzj)
- Remove weird s390 hack that shouldn't be needed any more (katzj)
- Make makebootfat less noisy (katzj)
- Get rid of dangling fobpath stuff; now that we're not mounting to
  create (katzj)
- Ignore .bak files created by glade (katzj)
- Get rid of duplication for yaboot stuff to make scripts less noisy (katzj)
- Correct internationalization of exception handler text (msw)
- More fixing of mount paths (#432720) (katzj)
- securitylevel -> firewall in the spec file. (clumens)
- Include util-linux-ng, which contains mount (#432720). (clumens)
- When mounting stage2 on loopback, add -o loop to mount opts. (clumens)

* Tue Feb 12 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.35-1
- Fix the build (katzj)

* Tue Feb 12 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.34-1
- Handle modules with more than one description (#432414) (katzj)
- Finish HDISO installs, at least for DVDs (#431132). (clumens)
- Move migration to before mounting filesystems (katzj)
- Fix silly thinko in Eric's patch (katzj)
- Allow ext3->ext4 upgrades (sandeen)
- Do the man pages in rescue mode the right way. (jgranado)
- Merge branch 'master' of ssh://git.fedorahosted.org/git/anaconda (notting)
- Use /etc/adjtime as the configuration file for UTC/not-UTC. (notting)
- Remove all our own mount code. (clumens)
- Use the mount program instead of our own code. (clumens)
- Add the real mount programs to stage1. (clumens)
- Use the correct variables to get the ipv6 info. (#432035) (jgranado)
- Update error messages to match function names. (dcantrell)
- Rename nl.c to iface.c and functions to iface_* (dcantrell)
- In rescue mode, show interface configuration (#429953) (dcantrell)
- Add qla2xxx firmware (#377921) (katzj)
- Rename base repo (#430806). (clumens)
- Remove dep on anaconda from pkgorder (katzj)
- Remove no longer used dumphdrlist script (katzj)

* Thu Feb 07 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.33-1
- Fix error message on continuing after changing cds with mediacheck (katzj)
- Fix the progress bar during mediacheck (#431138) (katzj)
- Ensure we disable SELinux if the live image isn't using it (#417601) (katzj)
- Correct nl_ip2str() cache iteration. (dcantrell)
- Check the fstype of the live image (katzj)
- Check for device existence rather than starting with /dev (katzj)
- The FL_TEXT flag has no reason to be here. (#207657) (jgranado)
- Don't traceback when getLabels is called with DiskSet.anaconda set
  to None. (dlehman)
- Pass arguments correctly to anaconda (katzj)
- Cancel on escape being pressed with autopart resizing (katzj)

* Wed Feb 06 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.32-1
- Make passwordEntry appear on the exn saving screen. (clumens)
- Don't allow disabling default repositories. (clumens)
- Make loopback device purposes line up with what stage2 expects. (clumens)
- Fix methodstr handling for hdiso installs (#431132). (clumens)
- Remove our own DNS functions, since glibc's are available now. (clumens)

* Tue Feb 05 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.31-1
- Copy over repodata from media after the install is done (#381721) (katzj)
- Add resizing support in autopartitioning (katzj)
- Fix test mode with python-fedora installed (katzj)
- Add support for encrypted devices in rescue mode (dlehman).
- Allow creation of LUKSDevice with no passphrase. (dlehman)
- Fix hdiso installs in loader and in methodstr (#431132). (clumens)
- Avoid infinite loop in nl_ip2str(). (dcantrell)
- Force users to set a hostname (#408921) (dcantrell)
- Forward-port RHEL-5 fixes for s390x issues. (dcantrell)
- fsset.py tweaks for ext4dev & xfs (sandeen)
- When editing the raid partitions show raid memebers. (#352721) (jgranado)
- mdadm to create the mdadm.conf (#395881) (jgranado)

* Wed Jan 30 2008 David Cantrell <dcantrell@redhat.com> - 11.4.0.30-1
- Initialize int in doConfigNetDevice() to fix compiler warnings. (dcantrell)

* Wed Jan 30 2008 David Cantrell <dcantrell@redhat.com> - 11.4.0.29-1
- Handle putting updates ahead of anaconda in the updates= case too. (clumens)
- Make sure the device name starts with /dev (#430811). (clumens)
- Revert "Initial support for network --bootproto=ask (#401531)." (clumens)
- (#186439)  handle lv names with "-" when doing kickstart. (jgranado)
- Remove the last references to makeDevInode (#430784). (clumens)
- Don't traceback trying to raise an exception when making
  users (#430772). (clumens)

* Mon Jan 28 2008 David Cantrell <dcantrell@redhat.com> - 11.4.0.28-1
- Go back to the method screen if back is hit on nfs config (#430477). (clumens)
- Fix dmidecode dependency (#430394, Josh Boyer <jwboyer)

* Fri Jan 25 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.27-1
- Fix generation of stage1 images. (notting)
- Fix a typo in mk-images. (clumens)
- Allow removing packages by glob now that yum supports it. (clumens)

* Thu Jan 24 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.26-1
- Fix a traceback on the driver selection screen (#428810). (clumens)
- Map 'nousb', 'nofirewire', etc. to be proper module blacklists. (notting)
- Clean off leading and trailing whitespace from descriptions. (notting)
- Write out /etc/rpm/platform on livecd installs. (clumens)

* Wed Jan 23 2008 David Cantrell <dcantrell@redhat.com> - 11.4.0.25-1
- Include new firstboot module. (clumens)
- Conditionalize ntfsprogs as not all arches include it. (clumens)
- Remove kudzu-probe-stub. (clumens)
- Remove rogue references to kudzu. (clumens)
- Add dogtail support (#172891, #239024). (clumens)
- Fix some error reporting tracebacks. (clumens)

* Tue Jan 22 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.24-1
- Avoid possible SIGSEGV from empty loaderData values. (dcantrell)
- Do not require glib2-devel for building. (dcantrell)
- Use libnl to get interface MAC and IP addresses (dcantrell)
- Don't refer to the libuser.conf when creating users (#428891). (clumens)
- pcspkr works (or isn't even present), per testing on #fedora-devel (notting)
- Inline spufs loading for ppc. (notting)
- Load iscsi_tcp, so that iSCSI actually works (notting)
- inline ipv6 module loading (notting)
- If we execWith a program, require the package containing it. (clumens)
- Add a repository editor. (clumens)
- Add the default repo to the UI so it can be edited later. (clumens)
- Fix non-latin-1 locale display in the loader. (notting)
- Make sure anaconda has precedence in the search path (#331091). (clumens)
- When starting RAID arrays, the device node may not already exist. (notting)
- Fix a typo that's breaking kickstart network installs. (clumens)
- Don't allow backing up to partitioning (#429618). (clumens)
- Update font paths. (clumens)

* Mon Jan 21 2008 David Cantrell <dcantrell@redhat.com> - 11.4.0.23-1
- Try to fix a problem creating users via kickstart (#428891, clumens)
- Fix a loader segfault doing kickstart nfs installs (clumens)
- Move more interactive steps ahead of partitioning (clumens)
- If we can't possibly add advanced devices, don't offer it (#429210, clumens)
- Don't flush after rescanning so recently attached disks are
  available (clumens)
- If bootproto is dhcp, unset any static settings (#218489, dcantrell)
- Add some groups to pkgorder to make the CDs come out right (pjones)
- Fix traceback when using non-encrypted RAID (notting)
- Complete the patch for dhcptimeout (#198147, #254032, msivak)

* Wed Jan 16 2008 David L. Cantrell Jr. <dcantrell@redhat.com> - 11.4.0.22-1
- Require the latest libdhcp (dcantrell)
- Don't set currentMedia when we're on a network install (#428927, clumens)
- Don't offer two reboot options (clumens)
- Remove fsopts that are already defaults (#429039, clumens)
- Remove isofs module to get rid of a FATAL message (clumens)
- Add the crc32c kernel module for iscsi (#405911, clumens)
- Add MAC address to the network device selection screen (#428229, clumens)
- Initial support for network --bootproto=ask (#401531, clumens)
- Remove an extra newline (clumens)
- Add firstaidkit to the rescue image (jgranado)
- Fix the progress bar to hit 100%% on the last package (#428790, clumens)
- Add some output so the startup delay doesn't seem quite so long (clumens)
- Initial kickstart support for encrypted partitions (clumens)

* Mon Jan 14 2008 David Cantrell <dcantrell@redhat.com> - 11.4.0.21-1
- Inherit from the right versions of pykickstart classes (clumens)
- Update for nss files moving to /lib (clumens)
- Remove unneeded arguments from detectHardware function (notting)
- Symlink all udev support binaries to udevadm (notting)
- /sbin/restorecon on /etc/modprobe.d (notting)
- Add the kickstart syntax version to the kickstart file (clumens)
- Require latest libdhcp to fix x86_64 SIGABRT problems

* Sun Jan 13 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.20-1
- Install new udev paths so HAL can talk to it (notting)
- Also get DSO deps for setuid binaries (like X). (clumens)
- Fix a bunch of pychecker errors. (clumens)

* Fri Jan 11 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.19-1
- Make sure the arch is listedat the top of all loader screens. (clumens)
- Add the version number really early in the log file too. (clumens)
- Require latest libdhcp (dcantrell)
- Add nicdelay parameter to loader, so we can wait before sending DHCP
  requests. (msivak)
- Add dhcpdelay to loader so we can modify the default dhcp timeout
  (#198147, #254032). (msivak)
- Fix the selected device when disabling entries in Add advanced drive
  dialog. (#248447) (msivak)
- Include mkfs.gfs2 (#356661). (clumens)
- Use the new default Japanese font (#428070). (clumens)
- More urlinstall loader fixes. (clumens)

* Wed Jan 09 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.18-1
- Fix encrypted autopart traceback. (dlehman)
- Allow for better recovery if the CD/DVD is bad. (clumens)
- If downloading the updates image fails, prompt for a new location. (clumens)
- X now relies on libpciaccess, so add it to our list. (clumens)
- Erase temporary packages after installing them on all methods. (clumens)

* Mon Jan 07 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.17-1
- Make text mode root password dialog default match GUI. (clumens)
- Fix a segfault in making the URL dialog box. (clumens)

* Sun Jan 06 2008 Chris Lumens <clumens@redhat.com> - 11.4.0.16-1
- Fix checking the timestamps on split media installs. (clumens)
- Fix reference to isodir to avoid a post-install traceback. (clumens)
- Use a better test when populating the URL panel in loader. (clumens)
- Don't use error messages from dosfslabel as the label (#427457). (clumens)
- No longer require kudzu (#427680). (clumens)

* Thu Jan 03 2008 David Cantrell <dcantrell@redhat.com> - 11.4.0.15-1
- Require latest libdhcp (#378641) (dcantrell)

* Thu Jan 03 2008 David Cantrell <dcantrell@redhat.com> - 11.4.0.14-1
- Precreate /etc/modprobe.d in installroot (jkeating)
- 'import sets' in image.py (jkeating)
- Fix traceback when displaying required media (clumens)

* Tue Jan 01 2008 Jeremy Katz <katzj@redhat.com> - 11.4.0.13-1
- Make it obvious which partitions are being formatted and encrypted (katzj)
- Set initial sensitivity of encrypt button correctly (katzj)
- Fix traceback on invalid passphrase (#426887) (katzj)
- Use mkstemp() instead of tempnam() (katzj)
- Don't resize filesystems which are being formatted (#426466) (katzj)
- Add cracklib-dicts (#426444) (katzj)
- Fix build (notting)
