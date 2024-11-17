import bpy
import csv
#selected object in scene gets chosen
obj = bpy.context.active_object

#clears all keyframe data
obj.animation_data_clear()

#changes the scale of the animation
scale = 20
#CSV file to import
file_yukawa = 'Yukawa_potential_data.csv'
frame_rate = 30

with open(file_yukawa, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        #for each row we are setting the X and Y position of the object
        obj.location = (scale*float(row['x']),scale*float(row['y']),0)
        #we also set the keyframe data
        obj.keyframe_insert(data_path="location",frame=frame_rate*float(row['time']))