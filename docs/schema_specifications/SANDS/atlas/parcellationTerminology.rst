#######################
ParcellationTerminology
#######################

:Semantic name: https://openminds.om-i.org/types/ParcellationTerminology

:Display as: Parcellation terminology


------------

------------

Properties
##########

:Required: `hasEntity <hasEntity_heading_>`_
:Optional: `dataLocation <dataLocation_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_

------------

.. _dataLocation_heading:

************
dataLocation
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/dataLocation
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/file.html>`_
   :instructions: Add the location of all files in which this parcellation terminology is stored.

`BACK TO TOP <ParcellationTerminology_>`_

------------

.. _hasEntity_heading:

*********
hasEntity
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/hasEntity
   :value type: | linked object array \(1-N\) of type
                | `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntity.html>`_
   :instructions: Add all parcellation entities which belong to this parcellation terminology.

`BACK TO TOP <ParcellationTerminology_>`_

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
   :instructions: Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this parcellation terminology.

`BACK TO TOP <ParcellationTerminology_>`_

------------

