#########
Recording
#########

:Semantic name: https://openminds.om-i.org/types/Recording

:Display as: Recording


------------

------------

Properties
##########

:Required: `channel <channel_heading_>`_, `dataLocation <dataLocation_heading_>`_, `recordedWith <recordedWith_heading_>`_, `samplingFrequency <samplingFrequency_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `name <name_heading_>`_, `previousRecording <previousRecording_heading_>`_

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
   :instructions: Enter any additional remarks concerning this recording.

`BACK TO TOP <Recording_>`_

------------

.. _channel_heading:

*******
channel
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/channel
   :value type: | embedded object array \(1-N\) of type
                | `Channel <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/entity/channel.html>`_
   :instructions: Enter all channels used for this recording.

`BACK TO TOP <Recording_>`_

------------

.. _dataLocation_heading:

************
dataLocation
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/dataLocation
   :value type: | linked object of type
                | `File <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/file.html>`_ or `FileBundle <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/fileBundle.html>`_
   :instructions: Add the location of the file or file bundle in which the recorded data is stored.

`BACK TO TOP <Recording_>`_

------------

.. _internalIdentifier_heading:

******************
internalIdentifier
******************

Term or code that identifies someone or something within a particular product.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/internalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (or label) of this recording that is used within the corresponding data files to identify this recording.

`BACK TO TOP <Recording_>`_

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
   :instructions: Enter a descriptive name for this recording.

`BACK TO TOP <Recording_>`_

------------

.. _previousRecording_heading:

*****************
previousRecording
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/previousRecording
   :value type: | linked object of type
                | `Recording <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/entity/recording.html>`_
   :instructions: If this recording is part of a sequence of recordings (e.g., multiple repetitions or sweeps), add the recording preceding this recording.

`BACK TO TOP <Recording_>`_

------------

.. _recordedWith_heading:

************
recordedWith
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/recordedWith
   :value type: | linked object of type
                | `ElectrodeArrayUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/electrodeArrayUsage.html>`_, `ElectrodeUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/electrodeUsage.html>`_, `PipetteUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/pipetteUsage.html>`_ or `SlicingDeviceUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/specimenPrep/device/slicingDeviceUsage.html>`_
   :instructions: Add the device used to generate this recording.

`BACK TO TOP <Recording_>`_

------------

.. _samplingFrequency_heading:

*****************
samplingFrequency
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/samplingFrequency
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the sampling frequency of this recording.

`BACK TO TOP <Recording_>`_

------------

