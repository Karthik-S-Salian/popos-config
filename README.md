# popos-config



## Performance Switch script setup
```bash
sudo nano /etc/udev/rules.d/99-auto-power-profile.rules

```

Paste this there
```
SUBSYSTEM=="power_supply", ACTION=="change", RUN+="<absolute path to script>"
```

Save & exit.

Reload udev:

```
sudo udevadm control --reload
sudo udevadm trigger
```