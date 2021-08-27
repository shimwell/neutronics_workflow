
# This minimal example makes a 3D volume and exports the shape to a stp file
# A surrounding volume called a graveyard is needed for neutronics simulations

import paramak

my_shape = paramak.ExtrudeStraightShape(
    points=[
        (400, 100),
        (400, 200),
        (600, 200),
        (600, 100)
        ],
    distance = 180,
)

my_shape.export_stp('stage_1_output/steel.stp')
my_shape.export_graveyard('stage_1_output/graveyard.stp')
