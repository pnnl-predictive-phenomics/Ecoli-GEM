import cobra
import pathlib

path = pathlib.Path(__file__).parent

ecoli = cobra.io.read_sbml_model(
    path.joinpath( 'iML1515.xml').__str__()
)