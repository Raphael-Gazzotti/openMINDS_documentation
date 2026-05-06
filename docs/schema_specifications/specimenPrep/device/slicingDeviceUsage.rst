##################
SlicingDeviceUsage
##################

:Semantic name: https://openminds.om-i.org/types/SlicingDeviceUsage

:Display as: Slicing device usage


------------

------------

Properties
##########

:Required: `device <device_heading_>`_, `sliceThickness <sliceThickness_heading_>`_, `slicingPlane <slicingPlane_heading_>`_
:Optional: `lookupLabel <lookupLabel_heading_>`_, `metadataLocation <metadataLocation_heading_>`_, `oscillationAmplitude <oscillationAmplitude_heading_>`_, `slicingAngle <slicingAngle_heading_>`_, `slicingSpeed <slicingSpeed_heading_>`_, `usedSpecimen <usedSpecimen_heading_>`_, `vibrationFrequency <vibrationFrequency_heading_>`_

------------

.. _device_heading:

******
device
******

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/device
   :value type: | linked object of type
                | `SlicingDevice <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/specimenPrep/device/slicingDevice.html>`_
   :instructions: Add the slicing device used.

`BACK TO TOP <SlicingDeviceUsage_>`_

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

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _metadataLocation_heading:

****************
metadataLocation
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/metadataLocation
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/file.html>`_ or `FileBundle <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/fileBundle.html>`_
   :instructions: Add all files or file bundles containing additional information about the usage of this device.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _oscillationAmplitude_heading:

********************
oscillationAmplitude
********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/oscillationAmplitude
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the oscillation amplitude of the blade from the slicing device during its use.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _sliceThickness_heading:

**************
sliceThickness
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/sliceThickness
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the defined slice thickness during the use of this slicing device.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _slicingAngle_heading:

************
slicingAngle
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/slicingAngle
   :value type: | embedded object array \(1-2\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `NumericalProperty <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/numericalProperty.html>`_
   :instructions: Enter all slicing angles (intentional or unintentional) in relation to the slicing plane used during this activity.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _slicingPlane_heading:

************
slicingPlane
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/slicingPlane
   :value type: | linked object of type
                | `AnatomicalPlane <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/anatomicalPlane.html>`_
   :instructions: Add the anatomical plane that best describes the slicing direction of the tissue sample(s) during the use of this slicing device.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _slicingSpeed_heading:

************
slicingSpeed
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/slicingSpeed
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the defined slicing speed during the use of this slicing device.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _usedSpecimen_heading:

************
usedSpecimen
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/usedSpecimen
   :value type: | linked object of type
                | `SubjectState <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/subjectState.html>`_ or `TissueSampleState <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/tissueSampleState.html>`_
   :instructions: Add the state of the tissue sample or subject that this device was used on.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _vibrationFrequency_heading:

******************
vibrationFrequency
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/vibrationFrequency
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the defined vibration frequency during the use of this slicing device.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

