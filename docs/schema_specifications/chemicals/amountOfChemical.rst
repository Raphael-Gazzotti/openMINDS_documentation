################
AmountOfChemical
################

:Semantic name: https://openminds.om-i.org/types/AmountOfChemical

:Display as: Amount of chemical

Structured information about the amount of a given chemical that was used.


------------

------------

Properties
##########

:Required: `chemicalProduct <chemicalProduct_heading_>`_
:Optional: `amount <amount_heading_>`_

------------

.. _amount_heading:

******
amount
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/amount
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: When used in a mixture, enter the amount of the substance within the mixture (e.g., as concentration or as ratio). When used in its pure state, enter the used amount of the substance.

`BACK TO TOP <AmountOfChemical_>`_

------------

.. _chemicalProduct_heading:

***************
chemicalProduct
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/chemicalProduct
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/chemicals/chemicalMixture.html>`_, `ChemicalSubstance <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/chemicals/chemicalSubstance.html>`_ or `MolecularEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/molecularEntity.html>`_
   :instructions: Add the chemical product that was used.

`BACK TO TOP <AmountOfChemical_>`_

------------

