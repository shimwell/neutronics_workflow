
# This minimal example makes a 3D volume and exports the shape to a stp file
# A surrounding volume called a graveyard is needed for neutronics simulations

import paramak

my_shape = paramak.ExtrudeStraightShape(
    points=[
        (200, 10),
        (200, 20),
        (250, 20),
        (250, 10)
        ],
    distance = 5,
)

my_shape.export_stp('stage_1_output/steel.stp')
my_shape.export_graveyard('stage_1_output/graveyard.stp')
