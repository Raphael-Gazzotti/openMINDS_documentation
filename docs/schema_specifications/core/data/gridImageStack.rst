##############
GridImageStack
##############

:Semantic name: https://openminds.om-i.org/types/GridImageStack

:Display as: Grid image stack


------------

------------

Properties
##########

:Required: `dataLocation <dataLocation_heading_>`_, `dimension <dimension_heading_>`_, `pixelSize <pixelSize_heading_>`_, `z-stepSize <z-stepSize_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `coordinateFramework <coordinateFramework_heading_>`_, `name <name_heading_>`_, `numberOfImages <numberOfImages_heading_>`_, `obtainedWith <obtainedWith_heading_>`_

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
   :instructions: Enter any additional remarks concerning this grid image stack.

`BACK TO TOP <GridImageStack_>`_

------------

.. _coordinateFramework_heading:

*******************
coordinateFramework
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/coordinateFramework
   :value type: | linked object of type
                | `CommonCoordinateFrameworkVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/commonCoordinateFrameworkVersion.html>`_ or `CustomCoordinateFramework <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/non-atlas/customCoordinateFramework.html>`_
   :instructions: Add the coordinate space in which this grid image stack exists.

`BACK TO TOP <GridImageStack_>`_

------------

.. _dataLocation_heading:

************
dataLocation
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/dataLocation
   :value type: | linked object of type
                | `File <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/file.html>`_ or `FileBundle <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/fileBundle.html>`_
   :instructions: Add a reference to the file to which this grid image stack information applies. If the information applies uniformly to a grid image stack file series, a reference to the corresponding file bundle may be provided instead.

`BACK TO TOP <GridImageStack_>`_

------------

.. _dimension_heading:

*********
dimension
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/dimension
   :value type: integer array \(2-2\)
   :instructions: Enter the common dimension of the consecutive grid image planes (optical sections) in pixels.

`BACK TO TOP <GridImageStack_>`_

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
   :instructions: Enter a descriptive name of this grid image stack preferably matching the filename.

`BACK TO TOP <GridImageStack_>`_

------------

.. _numberOfImages_heading:

**************
numberOfImages
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/numberOfImages
   :value type: integer
   :instructions: Enter the total number of consecutive grid image planes (optical sections) in this stack (at least two).

`BACK TO TOP <GridImageStack_>`_

------------

.. _obtainedWith_heading:

************
obtainedWith
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/obtainedWith
   :value type: | linked object of type
                | `ElectrodeArrayUsage <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/ephys/device/electrodeArrayUsage.html>`_, `ElectrodeUsage <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/ephys/device/electrodeUsage.html>`_, `PipetteUsage <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/ephys/device/pipetteUsage.html>`_, `MRICoilUsage <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/neuroimaging/device/MRICoilUsage.html>`_, `MRIScannerUsage <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/neuroimaging/device/MRIScannerUsage.html>`_ or `SlicingDeviceUsage <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/specimenPrep/device/slicingDeviceUsage.html>`_
   :instructions: Add the used device for obtaining this grid image stack.

`BACK TO TOP <GridImageStack_>`_

------------

.. _pixelSize_heading:

*********
pixelSize
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/pixelSize
   :value type: | embedded object array \(2-2\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the common physical pixel size for the consecutive grid image planes (optical sections) (in x,y order).

`BACK TO TOP <GridImageStack_>`_

------------

.. _z-stepSize_heading:

**********
z-stepSize
**********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/z-stepSize
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the physical axial distance between consecutive image planes (optical sections) within this grid image stack.

`BACK TO TOP <GridImageStack_>`_

------------

