###########
WebResource
###########

:Semantic name: https://openminds.om-i.org/types/WebResource

:Display as: Web resource


------------

------------

Properties
##########

:Required: `IRI <IRI_heading_>`_
:Optional: `contentDescription <contentDescription_heading_>`_, `format <format_heading_>`_

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
   :instructions: Enter the internationalized resource identifier (IRI) to this web resource.

`BACK TO TOP <WebResource_>`_

------------

.. _contentDescription_heading:

******************
contentDescription
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contentDescription
   :value type: | string
                | formatting: text/plain; multiline
   :instructions: Enter a short content description for this web resource.

`BACK TO TOP <WebResource_>`_

------------

.. _format_heading:

******
format
******

Method of digitally organizing and structuring data or information.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/format
   :value type: | linked object of type
                | `ContentType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/contentType.html>`_
   :instructions: Add the expected content type of the document at this web resource.

`BACK TO TOP <WebResource_>`_

------------

