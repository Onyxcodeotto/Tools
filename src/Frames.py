
class ChemicalProduct:
    """Frame to store the general data of a chemical product
    Attributes
    
    name:str
    CAS_Number: str
    synonyms: str
    formula: str
    concentration_low_threshold: float
    concentration_high_threshold (low and high threshold are equal iff it mentions specific concentration. Also named as purity):float
    company: Company
    
    # storage:
    # handling:
    # disposal:
    """


class ComplexChemicalProduct(ChemicalProduct):
    """Frame to store more of a compound chemical product. (Ex. H2S, CHCl)
    Attributes
    
    {ChemicalProduct attributes}
    composition: [ChemicalProduct]
    """


class Company:
    """ Frame to store company data
    name: str
    address: str
    telephone: str
    fax: str
    website: str
    """


    
#     """




# class Properties:

# class EmergencyInformation:
    
# class FirstAid:

# class FireFight:
    