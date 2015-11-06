# brocade_zoning

Example:

`python zoning.py example/zonedata.json`
```
cfgclear
alicreate SRV_P0, 00:00:00:00:00:00:00:01
alicreate SRV_P1, 00:00:00:00:00:00:00:02
alicreate CLI_PA, 00:00:00:00:00:00:00:03
alicreate CLI_PB, 00:00:00:00:00:00:00:04
zonecreate SRV_CLI1, "SRV_P0; CLI_PA"
zonecreate SRV_CLI2, "SRV_P1; CLI_PB"
cfgcreate FABRIC_1, SRV_CLI1
cfgadd FABRIC_1, SRV_CLI2
cfgenable FABRIC_1
```
