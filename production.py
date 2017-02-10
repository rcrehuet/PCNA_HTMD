from htmd.protocols.production_v4 import Production
from htmd import LocalGPUQueue
md = Production()
md.runtime = 300
md.timeunits = 'ns'
md.temperature  = 300
#md.acemd.bincoordinates = 'output.coor'
#md.acemd.extendedsystem  = 'output.xsc'
md.write('equil','prod')

local = LocalGPUQueue()
local.submit('./prod/')
local.wait()
