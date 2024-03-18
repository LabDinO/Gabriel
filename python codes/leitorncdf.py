import netCDF4 as nc

netcdf_file = 'Gabriel/finaltcc/grid_compl_casan_juntando_10_topo_alti_net.nc'

conteudo = nc.Dataset(netcdf_file, 'r')

nodes = conteudo['mesh2d_nNodes']


print(conteudo)

print(nodes)