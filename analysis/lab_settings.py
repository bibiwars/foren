########################### import settings
import os

#paths
python_path = "/usr/bin/python"
vol_path = os.path.join(os.path.dirname(__file__), "../volatility", "vol.py")
cap_path = os.path.join(os.path.dirname(__file__), "../CapTipper", "CapTipper.py")

#vol_path = "/usr/bin/volatility"
###########################################
supported_plugins = ['envars', 'pslist', 'pstree', 'autoruns', 'netscan', 'filescan', 'iehistory', 'chromehistory', 'firefoxhistory', 'cmdscan', 'cmdline','screenshot', 'malfind', 'yarascan', 'hashdump', 'mimikatz']
#supported_plugins = ['envars', 'pslist', 'pstree', 'netscan', 'filescan', 'iehistory', 'chromehistory', 'firefoxhistory', 'cmdscan', 'cmdline','screenshot', 'malfind', 'yarascan', 'hashdump', 'mimikatz']

supported_json_plugins = ['pslist', 'autoruns', 'netscan', 'filescan', 'envars', 'malfind', 'hashdump', 'cmdscan', 'cmdline']
