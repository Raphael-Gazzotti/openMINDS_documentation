######################
CustomAnatomicalEntity
######################

:Semantic name: https://openminds.om-i.org/types/CustomAnatomicalEntity

:Display as: Custom anatomical entity


------------

------------

Properties
##########

:Required: `name <name_heading_>`_
:Optional: `hasAnnotation <hasAnnotation_heading_>`_, `relatedInterspeciesAnatomy <relatedInterspeciesAnatomy_heading_>`_, `relationAssessment <relationAssessment_heading_>`_

------------

.. _hasAnnotation_heading:

*************
hasAnnotation
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/hasAnnotation
   :value type: | embedded object array \(1-N\) of type
                | `CustomAnnotation <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/non-atlas/customAnnotation.html>`_
   :instructions: Add all custom annotations which define this custom anatomical entity.

`BACK TO TOP <CustomAnatomicalEntity_>`_

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
   :instructions: Enter a descriptive name for this custom anatomical entity.

`BACK TO TOP <CustomAnatomicalEntity_>`_

------------

.. _relatedInterspeciesAnatomy_heading:

**************************
relatedInterspeciesAnatomy
**************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/relatedInterspeciesAnatomy
   :value type: | linked object of type
                | `AnatomicalCavity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/anatomicalCavity.html>`_, `ExternalBodyRegion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/externalBodyRegion.html>`_, `MuscularStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/muscularStructure.html>`_, `NervousSystemStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/nervousSystemStructure.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organ.html>`_, `OrganSystemStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organSystemStructure.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organismSubstance.html>`_, `OrganismSystem <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organismSystem.html>`_, `SkeletalStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/skeletalStructure.html>`_, `TissueStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/tissueStructure.html>`_ or `VascularStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/vascularStructure.html>`_
   :instructions: Add the corresponding cross-species anatomical entity from the UBERON-derived terminologies that represents the generic anatomical concept underlying the custom anatomical entity.

`BACK TO TOP <CustomAnatomicalEntity_>`_

------------

.. _relationAssessment_heading:

******************
relationAssessment
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/relationAssessment
   :value type: | embedded object array \(1-N\) of type
                | `QualitativeRelationAssessment <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/miscellaneous/qualitativeRelationAssessment.html>`_ or `QuantitativeRelationAssessment <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/miscellaneous/quantitativeRelationAssessment.html>`_
   :instructions: Add all relations (qualitative or quantitative) of this custom anatomical entity to other anatomical entities.

`BACK TO TOP <CustomAnatomicalEntity_>`_

------------

