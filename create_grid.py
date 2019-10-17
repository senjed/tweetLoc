sample_coor = [39.808631, -83.2102799, 40.1572719, -82.7713781]
grid_size = 100 
lat_diff =  abs(sample_coor[2] - sample_coor[1]) / float(grid_size)
lon_diff = abs(sample_coor[1] - sample_coor[3] /float(grid_size)
min_lat_init = sample_coor[0]
min_lon_init = sample_coor[1]

count = 0
for i in range(0, grid_size):
    min_lon = min_lon_init +  (i * lon_diff) 
    for j in range(0, grid_size):
         count +=1
         min_lat = min_lat_init + (j * lat_diff)  
         print str(count) + " " + str(min_lat) + " " + str(min_lon) + " " + str(min_lat + lat_diff) + " " + str(min_lon +  lon_diff) 
    
