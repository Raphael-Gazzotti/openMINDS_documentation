###############
ChemicalMixture
###############

:Semantic name: https://openminds.ebrains.eu/chemicals/ChemicalMixture

:Display as: Chemical mixture

Structured information about a mixture of chemical substances.


------------

------------

Properties
##########

:Required: `hasPart <hasPart_heading_>`_, `type <type_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `name <name_heading_>`_, `productSource <productSource_heading_>`_

------------

.. _additionalRemarks_heading:

*****************
additionalRemarks
*****************

Mention of what deserves additional attention or notice.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/additionalRemarks
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter any additional remarks concerning this chemical mixture.

`BACK TO TOP <ChemicalMixture_>`_

------------

.. _hasPart_heading:

*******
hasPart
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasPart
   :value type: | embedded object array \(2-N\) of type
                | `AmountOfChemical <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/chemicals/amountOfChemical.html>`_
   :instructions: Enter all components, including other mixtures, that are part of this chemical mixture.

`BACK TO TOP <ChemicalMixture_>`_

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name of this chemical mixture.

`BACK TO TOP <ChemicalMixture_>`_

------------

.. _productSource_heading:

*************
productSource
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/productSource
   :value type: | linked object of type
                | `ProductSource <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/chemicals/productSource.html>`_
   :instructions: Add the source of this chemical mixture.

`BACK TO TOP <ChemicalMixture_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/type
   :value type: | linked object of type
                | `ChemicalMixtureType <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/controlledTerms/chemicalMixtureType.html>`_
   :instructions: Add the type of this mixture.

`BACK TO TOP <ChemicalMixture_>`_

------------

