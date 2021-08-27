
# This script converts the CAD stp files generated into h5m files that can be
# used in DAGMC enabled codes. h5m files created in this way are imprinted,
# merged, faceted and ready for use in OpenMC. One of the key aspects of this
# is the asssignment of materials to the volumes present in the CAD files.

from cad_to_h5m import cad_to_h5m

cad_to_h5m(
    files_with_tags=[
        {'cad_filename':'stage_1_output/steel.stp', 'material_tag':'mat1'},
        {'cad_filename':'stage_1_output/graveyard.stp', 'material_tag':'graveyard'},
    ],
    h5m_filename='stage_2_output/dagmc.h5m',
    cubit_path='/opt/Coreform-Cubit-2021.5/bin/'
)

