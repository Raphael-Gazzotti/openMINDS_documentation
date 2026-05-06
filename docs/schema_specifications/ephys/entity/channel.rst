#######
Channel
#######

:Semantic name: https://openminds.om-i.org/types/Channel

:Display as: Channel


------------

------------

Properties
##########

:Required: `internalIdentifier <internalIdentifier_heading_>`_, `unit <unit_heading_>`_
:Optional:

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
   :instructions: Enter the identifier (or label) of this channel that is used within the corresponding data files to identify this channel.

`BACK TO TOP <Channel_>`_

------------

.. _unit_heading:

****
unit
****

Determinate quantity adopted as a standard of measurement.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/unit
   :value type: | linked object of type
                | `UnitOfMeasurement <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/unitOfMeasurement.html>`_
   :instructions: Add the unit of measurement for this channel.

`BACK TO TOP <Channel_>`_

------------

