# makes use of the previously created neutronics geometry (h5m file) and assigns
# actual materials to the material tags. Sets simulation intensity and specifies
# the neutronics results to record (know as tallies).

import openmc
import openmc_dagmc_wrapper

# defines a simple point source
# my_source = openmc.Source()
# my_source.space = openmc.stats.Point((300, 0, 0))
# my_source.angle = openmc.stats.Isotropic()
# my_source.energy = openmc.stats.Discrete([14e6], [1])


# initialises a new source object
my_source = openmc.Source()

# the distribution of radius is just a single value
radius = openmc.stats.Discrete([300], [1])

# the distribution of source z values is just a single value
z_values = openmc.stats.Discrete([0], [1])

# the distribution of source azimuthal angles values is a uniform distribution between 0 and 2 Pi
angle = openmc.stats.Uniform(a=0., b=2*3.14159265359)

# this makes the ring source using the three distributions and a radius
my_source.space = openmc.stats.CylindricalIndependent(r=radius, phi=angle, z=z_values, origin=(0.0, 0.0, 0.0))

# sets the direction to isotropic
my_source.angle = openmc.stats.Isotropic()

# sets the energy distribution to a Muir distribution neutrons
my_source.energy = openmc.stats.Muir(e0=14080000.0, m_rat=5.0, kt=20000.0)

neutronics_model = openmc_dagmc_wrapper.NeutronicsModel(
    h5m_filename='stage_2_output/dagmc.h5m',
    tet_mesh_filename='stage_2_output/unstructured_mesh.h5m',
    source=my_source,
    materials={
        'inboard_tf_coils_mat': 'copper',
        'center_column_shield_mat': 'WC',
        'divertor_mat': 'eurofer',
        'firstwall_mat': 'eurofer',
        'blanket_mat': 'Li4SiO4',
        'blanket_rear_wall_mat': 'eurofer'},
    mesh_tally_tet=['heating']  # , '(n,Xa)'
)

results = neutronics_model.simulate(
    simulation_batches=3,
    simulation_particles_per_batch=1e4,
)
print(results)
