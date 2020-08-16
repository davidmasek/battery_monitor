# battery_monitor

Display notifications on low battery power.

## Requirements

- Python 3
- Tkinter (possibly already bundled with Python)

## Using Crontab

Run:
```bash
crontab -e
```

and add following line (replace `PATH_TO_PYTHON` and `PATH_TO_MONITOR` by actual paths):
```bash
*/5 * * * * PATH_TO_PYTHON PATH_TO_MONITOR/battery_monitor.py
```

You can get `PATH_TO_PYTHON` by running:
```bash
> which python
/usr/bin/python # example output
```

`PATH_TO_MONITOR` is the folder where you place `battery_monitor.py` (for example `/home/yourname/battery_monitor`).

## Tested on:

- Xubuntu 20.04

Program should run on various linux distributions but may need minor tweaking of settings.

## Settings

You can modify various settings inside of `battery_monitor.py`. Especially note `LEVEL_WARN` variable which sets below what percentage of power to display warning message.
