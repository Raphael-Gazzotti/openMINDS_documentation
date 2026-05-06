######
Strain
######

:Semantic name: https://openminds.om-i.org/types/Strain

:Display as: Strain


------------

------------

Properties
##########

:Required: `geneticStrainType <geneticStrainType_heading_>`_, `name <name_heading_>`_, `species <species_heading_>`_
:Optional: `alternateIdentifier <alternateIdentifier_heading_>`_, `backgroundStrain <backgroundStrain_heading_>`_, `breedingType <breedingType_heading_>`_, `description <description_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `diseaseModel <diseaseModel_heading_>`_, `laboratoryCode <laboratoryCode_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_, `phenotype <phenotype_heading_>`_, `stockNumber <stockNumber_heading_>`_, `synonym <synonym_heading_>`_

------------

.. _alternateIdentifier_heading:

*******************
alternateIdentifier
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/alternateIdentifier
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter all identifiers for this strain, excluding its ontological identifiers or RRID (e.g., identifiers from the Mouse Genome Informatics (MGI) database or Rat Genome Database (RGD)).

`BACK TO TOP <Strain_>`_

------------

.. _backgroundStrain_heading:

****************
backgroundStrain
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/backgroundStrain
   :value type: | linked object array \(1-2\) of type
                | `Strain <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/strain.html>`_
   :instructions: Add the background strain that explains the majority of the genetic background and/or causes the majority of the prominent traits. If two strains contributed equally, state both.

`BACK TO TOP <Strain_>`_

------------

.. _breedingType_heading:

************
breedingType
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/breedingType
   :value type: | linked object of type
                | `BreedingType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/breedingType.html>`_
   :instructions: Add the breeding type for this strain.

`BACK TO TOP <Strain_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/description
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a short text describing this strain.

`BACK TO TOP <Strain_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/digitalIdentifier
   :value type: | linked object of type
                | `RRID <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/RRID.html>`_
   :instructions: Add the 'Research Resource Identifier' (RRID) of this strain.

`BACK TO TOP <Strain_>`_

------------

.. _diseaseModel_heading:

************
diseaseModel
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/diseaseModel
   :value type: | linked object array \(1-N\) of type
                | `Disease <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/disease.html>`_ or `DiseaseModel <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/diseaseModel.html>`_
   :instructions: Add all (human) diseases and/or conditions that this strain is a model for.

`BACK TO TOP <Strain_>`_

------------

.. _geneticStrainType_heading:

*****************
geneticStrainType
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/geneticStrainType
   :value type: | linked object of type
                | `GeneticStrainType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/geneticStrainType.html>`_
   :instructions: Add the genetic background type of this strain.

`BACK TO TOP <Strain_>`_

------------

.. _laboratoryCode_heading:

**************
laboratoryCode
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/laboratoryCode
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the laboratory code assigned by the Institute of Laboratory Animal Research (ILAR) for the investigator or organization that has created this strain following the defined pattern (e.g., Aaa).

`BACK TO TOP <Strain_>`_

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name of this strain.

`BACK TO TOP <Strain_>`_

------------

.. _ontologyIdentifier_heading:

******************
ontologyIdentifier
******************

Term or code used to identify something or someone registered within a particular ontology.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/ontologyIdentifier
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this strain.

`BACK TO TOP <Strain_>`_

------------

.. _phenotype_heading:

*********
phenotype
*********

Physical expression of one or more genes of an organism.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/phenotype
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short description for the phenotype of this strain.

`BACK TO TOP <Strain_>`_

------------

.. _species_heading:

*******
species
*******

Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/species
   :value type: | linked object of type
                | `Species <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/species.html>`_
   :instructions: Add the species of this strain.

`BACK TO TOP <Strain_>`_

------------

.. _stockNumber_heading:

***********
stockNumber
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/stockNumber
   :value type: | embedded object of type
                | `StockNumber <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/stockNumber.html>`_
   :instructions: Add the stock number from the vendor the strain was supplied from/is in stock at.

`BACK TO TOP <Strain_>`_

------------

.. _synonym_heading:

*******
synonym
*******

Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/synonym
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter any synonyms (including abbreviations) of this strain.

`BACK TO TOP <Strain_>`_

------------

