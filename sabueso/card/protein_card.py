from .protein_databases_card import ProteinDataBasesCard

class ProteinCard():

    """ProteinCard()

    Protein card.

    Aquí va un parrafo...

    Attributes
    ----------
    
    full_name : string
        Descripcion
    short_name : string
        Descripcion
    alternative_names : list
        Descripcion
    sequence : string
        Descripcion
    length : float
        Descripcion
    mass : float
        Descripcion
                




    Examples
    --------

    See Also
    --------


    Notes
    -----

    """

    def __init__(self):

        """convert(item, to_form='molsysmt.MolSys', selection='all', structure_indices='all', syntax='MolSysMT', **kwargs)
    
        Convert a molecular model into other form.
    
        A molecular model in a given accepted form can be converted into any other supported form
        by MolSysMt. The list of supported forms can be found in the section 'XXX'.
    
        Parameters
        ----------
    
        molecular_system: molecular model
            Molecular model in any supported form by MolSysMT (see: XXX).
    
        selection: str, list, tuple or np.ndarray, defaul='all'
           Atoms selection over which this method applies. The selection can be given by a
           list, tuple or numpy array of integers (0-based), or by means of a string following any of
           the selection syntax parsable by MolSysMT (see: :func:`molsysmt.select`).
    
        to_form: str, default='molsysmt.MolSys'
            The output object will take the form specified here. This form supported form by MolSysMt
            for the output object.
    
        syntax: str, default='MolSysMT'
           Syntaxis used in the argument `selection` (in case it is a string). The
           current options supported by MolSysMt can be found in section XXX (see: :func:`molsysmt.select`).
    
        Returns
        -------
    
           item: molecular model
    
           A new object is returned with the form specified by the argument `to_form`.
    
        Examples
        --------
    
        See Also
        --------
    
        :func:`molsysmt.load`, :func:`molsysmt.select`
    
        Notes
        -----
    
        """


        self.full_name = None
        self.short_name = None
        self.alternative_names = []

        self.sequence = None
        self.length = None
        self.mass = None

        self.residues = {}

        self.isoforms = {}



        self.binding_sites = {}
        self.interfaces = {}
        self.ligands = {}
        self.interactants = {}


        self.database = ProteinDataBasesCard()

        self.references = []


