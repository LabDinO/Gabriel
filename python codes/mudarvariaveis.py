import netCDF4 as netcdf

dados = netcdf.Dataset("D:\Petrobrás/roms_cenpes/bry/sse112_bry_2008.nc")

tempo= dados.variables
print('------------------------------------------------------------')
print(tempo.keys())

var = dados.variables['ocean_time']
print('------------------------------------------------------------')
print(var)
print('------------------------------------------------------------')

#var2 = dados.variables['hc']
#print(var2)
#print('------------------------------------------------------------')


netcdf_file.close()
