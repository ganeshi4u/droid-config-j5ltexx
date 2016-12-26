# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device j5ltexx
%define vendor samsung
%define vendor_pretty Samsung
%define device_pretty Galaxy J5
%define dcd_path ./

# Community HW adaptations need this
%define community_adaptation 1

# Adjust this for your device
%define pixel_ratio 1.25
# We assume most devices will
%define have_modem 1
%include droid-configs-device/droid-configs.inc
