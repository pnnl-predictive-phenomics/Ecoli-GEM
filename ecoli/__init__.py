import cobra
import pathlib

path = pathlib.Path(__file__).parent

ecoli = cobra.io.read_sbml_model(
    path.joinpath( 'iML1515.xml').__str__()
)
ecoli_1533 = cobra.io.read_sbml_model(
    path.joinpath( 'iHM1533.xml').__str__()
)
