##############################
ParcellationTerminologyVersion
##############################

:Semantic name: https://openminds.om-i.org/types/ParcellationTerminologyVersion

:Display as: Parcellation terminology version


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
   :instructions: Add the location of all files in which this parcellation terminology version is stored.

`BACK TO TOP <ParcellationTerminologyVersion_>`_

------------

.. _hasEntity_heading:

*********
hasEntity
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/hasEntity
   :value type: | linked object array \(1-N\) of type
                | `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add all parcellation entity versions which belong to this parcellation terminology version.

`BACK TO TOP <ParcellationTerminologyVersion_>`_

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
   :instructions: Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this parcellation terminology version.

`BACK TO TOP <ParcellationTerminologyVersion_>`_

------------

