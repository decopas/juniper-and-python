from jnpr.junos import Device

datafile='/var/db/scripts/op/BasicShows'

with open(datafile,'r') as mydata:
 with Device() as dev:
  for line in mydata:
   print(">>>" + line)
   print(dev.cli(line, warning=False))
   print("\n\n")

