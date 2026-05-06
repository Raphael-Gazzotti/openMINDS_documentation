############
MRICoilUsage
############

:Semantic name: https://openminds.om-i.org/types/MRICoilUsage

:Display as: Mricoil usage


------------

------------

Properties
##########

:Required: `device <device_heading_>`_, `signalDirectionality <signalDirectionality_heading_>`_
:Optional: `activeElement <activeElement_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `metadataLocation <metadataLocation_heading_>`_, `mountingLocation <mountingLocation_heading_>`_, `usedSpecimen <usedSpecimen_heading_>`_

------------

.. _activeElement_heading:

*************
activeElement
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/activeElement
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Only applicable to radiofrequency (RF) coils! Enter the active coil element identifier(s) corresponding to the transmitting and/or receiving elements that were electrically active during this acquisition; the number of identifiers typically matches the number of physical elements in the selected RF coil and may be fewer if some elements were disabled.

`BACK TO TOP <MRICoilUsage_>`_

------------

.. _device_heading:

******
device
******

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/device
   :value type: | linked object of type
                | `MRICoil <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/neuroimaging/device/MRICoil.html>`_
   :instructions: Add the MRI Coil used.

`BACK TO TOP <MRICoilUsage_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this device usage that may help you to find this instance more easily.

`BACK TO TOP <MRICoilUsage_>`_

------------

.. _metadataLocation_heading:

****************
metadataLocation
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/metadataLocation
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/file.html>`_ or `FileBundle <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/fileBundle.html>`_
   :instructions: Add all files or file bundles containing additional information about the usage of this device.

`BACK TO TOP <MRICoilUsage_>`_

------------

.. _mountingLocation_heading:

****************
mountingLocation
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/mountingLocation
   :value type: | linked object of type
                | `ExternalBodyRegion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/externalBodyRegion.html>`_
   :instructions: Add the anatomical mounting location of the coil, indicating where the coil was positioned on or around the subject (for example, head, neck, knee, or torso). This information is typically applicable to radiofrequency (RF) coils and may be omitted for gradient or shim systems.

`BACK TO TOP <MRICoilUsage_>`_

------------

.. _signalDirectionality_heading:

********************
signalDirectionality
********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/signalDirectionality
   :value type: | linked object of type
                | `SignalDirectionality <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/signalDirectionality.html>`_
   :instructions: Add the signal directionality of the coil, indicating whether it was used for signal transmission, reception, or both. This information is typically defined in the system configuration and can be retrieved from the DICOM header or scanner hardware metadata.

`BACK TO TOP <MRICoilUsage_>`_

------------

.. _usedSpecimen_heading:

************
usedSpecimen
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/usedSpecimen
   :value type: | linked object of type
                | `SubjectState <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/research/subjectState.html>`_ or `TissueSampleState <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/research/tissueSampleState.html>`_
   :instructions: Add the state of the tissue sample or subject that this device was used on.

`BACK TO TOP <MRICoilUsage_>`_

------------

