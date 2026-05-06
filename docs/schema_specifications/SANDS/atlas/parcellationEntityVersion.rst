#########################
ParcellationEntityVersion
#########################

:Semantic name: https://openminds.om-i.org/types/ParcellationEntityVersion

:Display as: Parcellation entity version


For this schema openMINDS provides a `library of instances <https://openminds-documentation.readthedocs.io/en/v4.0/instance_libraries/parcellationEntityVersions.html>`_.

------------

------------

Properties
##########

:Required: `name <name_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_
:Optional: `abbreviation <abbreviation_heading_>`_, `additionalRemarks <additionalRemarks_heading_>`_, `alternateName <alternateName_heading_>`_, `correctedName <correctedName_heading_>`_, `hasAnnotation <hasAnnotation_heading_>`_, `hasParent <hasParent_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_, `relationAssessment <relationAssessment_heading_>`_, `versionInnovation <versionInnovation_heading_>`_

------------

.. _abbreviation_heading:

************
abbreviation
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/abbreviation
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the official abbreviation of this parcellation entity version.

`BACK TO TOP <ParcellationEntityVersion_>`_

------------

.. _additionalRemarks_heading:

*****************
additionalRemarks
*****************

Mention of what deserves additional attention or notice.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/additionalRemarks
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter any additional remarks concerning this parcellation entity version.

`BACK TO TOP <ParcellationEntityVersion_>`_

------------

.. _alternateName_heading:

*************
alternateName
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/alternateName
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter any alternate names, including any alternative abbreviations, for this parcellation entity version.

`BACK TO TOP <ParcellationEntityVersion_>`_

------------

.. _correctedName_heading:

*************
correctedName
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/correctedName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the refined or corrected name of this parcellation entity version.

`BACK TO TOP <ParcellationEntityVersion_>`_

------------

.. _hasAnnotation_heading:

*************
hasAnnotation
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/hasAnnotation
   :value type: | embedded object array \(1-N\) of type
                | `AtlasAnnotation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/atlasAnnotation.html>`_
   :instructions: Add all atlas annotations which define this parcellation entity version.

`BACK TO TOP <ParcellationEntityVersion_>`_

------------

.. _hasParent_heading:

*********
hasParent
*********

Reference to a parent object or legal person.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/hasParent
   :value type: | linked object array \(1-N\) of type
                | `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add all anatomical parent structures (or version of the structures) for this parcellation entity as defined within corresponding brain atlas version.

`BACK TO TOP <ParcellationEntityVersion_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this parcellation entity version that may help you to find this instance more easily.

`BACK TO TOP <ParcellationEntityVersion_>`_

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
   :instructions: Enter the name of this parcellation entity version.

`BACK TO TOP <ParcellationEntityVersion_>`_

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
   :instructions: Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this parcellation entity version.

`BACK TO TOP <ParcellationEntityVersion_>`_

------------

.. _relationAssessment_heading:

******************
relationAssessment
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/relationAssessment
   :value type: | embedded object array \(1-N\) of type
                | `QualitativeRelationAssessment <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/miscellaneous/qualitativeRelationAssessment.html>`_ or `QuantitativeRelationAssessment <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/miscellaneous/quantitativeRelationAssessment.html>`_
   :instructions: Add all relations (qualitative or quantitative) of this parcellation entity version to other anatomical entities.

`BACK TO TOP <ParcellationEntityVersion_>`_

------------

.. _versionIdentifier_heading:

*****************
versionIdentifier
*****************

Term or code used to identify the version of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/versionIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the version identifier of this parcellation entity version.

`BACK TO TOP <ParcellationEntityVersion_>`_

------------

.. _versionInnovation_heading:

*****************
versionInnovation
*****************

Documentation on what changed in comparison to a previously published form of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/versionInnovation
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a short description (or summary) of the novelties/peculiarities of this parcellation entity version in comparison to its preceding versions. If this parcellation entity version is the first version, leave blank.

`BACK TO TOP <ParcellationEntityVersion_>`_

------------

