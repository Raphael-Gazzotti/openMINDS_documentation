#####################
LivePaperResourceItem
#####################

:Semantic name: https://openminds.om-i.org/types/LivePaperResourceItem

:Display as: Live paper resource item


------------

------------

Properties
##########

:Required: `IRI <IRI_heading_>`_, `hostedBy <hostedBy_heading_>`_, `isPartOf <isPartOf_heading_>`_, `name <name_heading_>`_
:Optional:

------------

.. _IRI_heading:

***
IRI
***

Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/IRI
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to this live paper resource item.

`BACK TO TOP <LivePaperResourceItem_>`_

------------

.. _hostedBy_heading:

********
hostedBy
********

Reference to an organization that provides facilities and services for something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/hostedBy
   :value type: | linked object of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/organization.html>`_
   :instructions: Add the host organization of this live paper resource item.

`BACK TO TOP <LivePaperResourceItem_>`_

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/isPartOf
   :value type: | linked object of type
                | `LivePaperSection <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/publications/livePaperSection.html>`_
   :instructions: Add the live paper section this live paper resource item is part of.

`BACK TO TOP <LivePaperResourceItem_>`_

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
   :instructions: Enter a descriptive name for this live paper resource item.

`BACK TO TOP <LivePaperResourceItem_>`_

------------

