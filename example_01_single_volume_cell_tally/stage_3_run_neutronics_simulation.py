# makes use of the previously created neutronics geometry (h5m file) and assigns
# actual materials to the material tags. Sets simulation intensity and specifies
# the neutronics results to record (know as tallies).

import openmc
import openmc_dagmc_wrapper

# defines a simple point source
my_source = openmc.Source()
my_source.space = openmc.stats.Point((0, 0, 0))
my_source.angle = openmc.stats.Isotropic()
my_source.energy = openmc.stats.Discrete([14e6], [1])

neutronics_model = openmc_dagmc_wrapper.NeutronicsModel(
    h5m_filename='stage_2_output/dagmc.h5m',
    source=my_source,
    materials={"mat1": "eurofer"},
    cell_tallies=["flux"]
)

neutronics_model.simulate(
    simulation_batches=5,
    simulation_particles_per_batch=1e4,
)

results = neutronics_model.process_results()

print(results)
