##########
GridVolume
##########

:Semantic name: https://openminds.om-i.org/types/GridVolume

:Display as: Grid volume


------------

------------

Properties
##########

:Required: `dataLocation <dataLocation_heading_>`_, `dimension <dimension_heading_>`_, `voxelSize <voxelSize_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `coordinateFramework <coordinateFramework_heading_>`_, `name <name_heading_>`_, `numberOfPlanes <numberOfPlanes_heading_>`_, `obtainedWith <obtainedWith_heading_>`_

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
   :instructions: Enter any additional remarks concerning this grid volume.

`BACK TO TOP <GridVolume_>`_

------------

.. _coordinateFramework_heading:

*******************
coordinateFramework
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/coordinateFramework
   :value type: | linked object of type
                | `CommonCoordinateFrameworkVersion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/atlas/commonCoordinateFrameworkVersion.html>`_ or `CustomCoordinateFramework <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/non-atlas/customCoordinateFramework.html>`_
   :instructions: Add the coordinate space in which this grid volume exists.

`BACK TO TOP <GridVolume_>`_

------------

.. _dataLocation_heading:

************
dataLocation
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/dataLocation
   :value type: | linked object of type
                | `File <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/file.html>`_ or `FileBundle <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/fileBundle.html>`_
   :instructions: Add a reference to the file to which this grid volume information applies. If the information applies uniformly to a grid volume file series, a reference to the corresponding file bundle may be provided instead.

`BACK TO TOP <GridVolume_>`_

------------

.. _dimension_heading:

*********
dimension
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/dimension
   :value type: integer array \(3-3\)
   :instructions: Enter the dimension of this grid volume.

`BACK TO TOP <GridVolume_>`_

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
   :instructions: Enter a descriptive name of this grid volume preferably matching the filename.

`BACK TO TOP <GridVolume_>`_

------------

.. _numberOfPlanes_heading:

**************
numberOfPlanes
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/numberOfPlanes
   :value type: integer
   :instructions: Enter number of planes in this grid volume.

`BACK TO TOP <GridVolume_>`_

------------

.. _obtainedWith_heading:

************
obtainedWith
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/obtainedWith
   :value type: | linked object of type
                | `ElectrodeArrayUsage <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/ephys/device/electrodeArrayUsage.html>`_, `ElectrodeUsage <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/ephys/device/electrodeUsage.html>`_, `PipetteUsage <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/ephys/device/pipetteUsage.html>`_, `MRICoilUsage <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/neuroimaging/device/MRICoilUsage.html>`_, `MRIScannerUsage <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/neuroimaging/device/MRIScannerUsage.html>`_ or `SlicingDeviceUsage <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/specimenPrep/device/slicingDeviceUsage.html>`_
   :instructions: Add the used device for obtaining this grid volume.

`BACK TO TOP <GridVolume_>`_

------------

.. _voxelSize_heading:

*********
voxelSize
*********

Extent of the discrete elements comprising a three-dimensional entity.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/voxelSize
   :value type: | embedded object array \(3-3\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the physical voxel size for this grid volume (in x,y,z order).

`BACK TO TOP <GridVolume_>`_

------------

