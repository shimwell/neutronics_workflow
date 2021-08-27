This is a minimal example that creates a single volume CAD file in stp file format, then converts the file to a DAGMC neutronics model, then runs an OpenMC simulation to get a tally.

Run the files in this order

```bash
python stage_1_create_cad.py
python stage_2_convert_cad_to_neutronics.py
python stage_3_run_neutronics_simulation.py
```
