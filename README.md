# brocade_zoning

Example:

`python zoning.py example/zonedata.json`
```
cfgclear
alicreate SRV_P0, "00:00:00:00:00:00:00:01" 
alicreate SRV_P1, "00:00:00:00:00:00:00:02" 
alicreate CLI_PA, "00:00:00:00:00:00:00:03" 
alicreate CLI_PB, "00:00:00:00:00:00:00:04" 
alicreate STOR2, "00:00:00:00:00:01:00:05;00:00:00:00:00:02:00:05" 
zonecreate "SRV_CLI1", "SRV_P0;CLI_PA" 
zonecreate "SRV_CLI2", "SRV_P1;CLI_PB" 
zonecreate "SRV_P0_STOR2", "SRV_P0;STOR2" 
zonecreate "SRV_P1_STOR2", "SRV_P1;STOR2" 
cfgcreate FABRIC_1, SRV_CLI1
cfgadd FABRIC_1, SRV_CLI2
cfgadd FABRIC_1, SRV_P0_STOR2
cfgadd FABRIC_1, SRV_P1_STOR2
cfgenable FABRIC_1

```
