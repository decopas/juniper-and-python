
datafile='/var/db/scripts/op/BasicShows'

with open(datafile,'r') as mydata:
  for line in mydata:
   print(">>>" + line)
   print("\n\n")
