   for each point in shape.path:
       if meets_condition(point):
           mirrored_point = mirror_function(point)
           add mirrored_point to new_shape.path
       else:
           add point to new_shape.path
   