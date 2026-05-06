#############
EphysStimulus
#############

:Semantic name: https://openminds.om-i.org/types/EphysStimulus

:Display as: Ephys stimulus


------------

------------

Properties
##########

:Required: `internalIdentifier <internalIdentifier_heading_>`_
:Optional: `deliveredBy <deliveredBy_heading_>`_, `description <description_heading_>`_, `epoch <epoch_heading_>`_, `generatedBy <generatedBy_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `specification <specification_heading_>`_, `type <type_heading_>`_

------------

.. _deliveredBy_heading:

***********
deliveredBy
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/deliveredBy
   :value type: | linked object of type
                | `ElectrodeArrayUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/electrodeArrayUsage.html>`_, `ElectrodeUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/electrodeUsage.html>`_, `PipetteUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/pipetteUsage.html>`_ or `SlicingDeviceUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/specimenPrep/device/slicingDeviceUsage.html>`_
   :instructions: Add the device used to deliver this stimulus.

`BACK TO TOP <EphysStimulus_>`_

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
   :instructions: Enter a short text describing this stimulus.

`BACK TO TOP <EphysStimulus_>`_

------------

.. _epoch_heading:

*****
epoch
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/epoch
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the total epoch length of this stimulus.

`BACK TO TOP <EphysStimulus_>`_

------------

.. _generatedBy_heading:

***********
generatedBy
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/generatedBy
   :value type: | linked object of type
                | `ElectrodeArrayUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/electrodeArrayUsage.html>`_, `ElectrodeUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/electrodeUsage.html>`_, `PipetteUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/pipetteUsage.html>`_ or `SlicingDeviceUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/specimenPrep/device/slicingDeviceUsage.html>`_
   :instructions: Add the device used to generate this stimulus.

`BACK TO TOP <EphysStimulus_>`_

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
   :instructions: Enter the identifier (or label) of this stimulus that is used within the corresponding data files to identify this stimulus.

`BACK TO TOP <EphysStimulus_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this stimulus that may help you to find this instance more easily.

`BACK TO TOP <EphysStimulus_>`_

------------

.. _specification_heading:

*************
specification
*************

Detailed and precise presentation of, or proposal for something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/specification
   :value type: | linked object array \(1-N\) of type
                | `Configuration <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/configuration.html>`_, `File <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/file.html>`_, `FileBundle <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/fileBundle.html>`_ or `PropertyValueList <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/propertyValueList.html>`_
   :instructions: Add the specification information for this stimulus.

`BACK TO TOP <EphysStimulus_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/type
   :value type: | linked object of type
                | `ElectricalStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/electricalStimulusType.html>`_
   :instructions: Add the type that describe this electrical stimulus.

`BACK TO TOP <EphysStimulus_>`_

------------

