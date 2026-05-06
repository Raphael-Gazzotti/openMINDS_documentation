###########
Measurement
###########

:Semantic name: https://openminds.om-i.org/types/Measurement

:Display as: Measurement

Structured information about a measurement performed during a scientific experiment.


------------

------------

Properties
##########

:Required: `measuredQuantity <measuredQuantity_heading_>`_, `value <value_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `measuredWith <measuredWith_heading_>`_, `timestamp <timestamp_heading_>`_

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
   :instructions: Enter any additional remarks concerning this measurement.

`BACK TO TOP <Measurement_>`_

------------

.. _measuredQuantity_heading:

****************
measuredQuantity
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/measuredQuantity
   :value type: | linked object of type
                | `MeasuredQuantity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/measuredQuantity.html>`_
   :instructions: Add the quantity that was measured during this measurement.

`BACK TO TOP <Measurement_>`_

------------

.. _measuredWith_heading:

************
measuredWith
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/measuredWith
   :value type: | linked object of type
                | `ElectrodeArrayUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/electrodeArrayUsage.html>`_, `ElectrodeUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/electrodeUsage.html>`_, `PipetteUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/pipetteUsage.html>`_ or `SlicingDeviceUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/specimenPrep/device/slicingDeviceUsage.html>`_
   :instructions: Add the device that was used during this measurement.

`BACK TO TOP <Measurement_>`_

------------

.. _timestamp_heading:

*********
timestamp
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/timestamp
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date and time on which this measurement was made, formatted as '2023-02-07T16:00:00+00:00'.

`BACK TO TOP <Measurement_>`_

------------

.. _value_heading:

*****
value
*****

Entry for a property.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/value
   :value type: | embedded object array \(1-N\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter all values that were measured at the same time and are of the same measured quantity.

`BACK TO TOP <Measurement_>`_

------------

