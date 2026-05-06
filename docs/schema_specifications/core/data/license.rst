#######
License
#######

:Semantic name: https://openminds.om-i.org/types/License

:Display as: License

Structured information on a used license.


For this schema openMINDS provides a `library of instances <https://openminds-documentation.readthedocs.io/en/v4.0/instance_libraries/licenses.html>`_.

------------

------------

Properties
##########

:Required: `fullName <fullName_heading_>`_, `legalCode <legalCode_heading_>`_, `shortName <shortName_heading_>`_
:Optional: `webpage <webpage_heading_>`_

------------

.. _fullName_heading:

********
fullName
********

Whole, non-abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the full name of this license.

`BACK TO TOP <License_>`_

------------

.. _legalCode_heading:

*********
legalCode
*********

Type of legislation that claims to cover the law system (complete or parts) as it existed at the time the code was enacted.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/legalCode
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the legal code of this license.

`BACK TO TOP <License_>`_

------------

.. _shortName_heading:

*********
shortName
*********

Shortened or fully abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short name (or alias) for this license that could be used as a shortened display title (e.g., for web services with too little space to display the full name).

`BACK TO TOP <License_>`_

------------

.. _webpage_heading:

*******
webpage
*******

Hypertext document (block of information) found on the World Wide Web.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/webpage
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifiers (IRIs) to webpages related to this license (e.g., a homepage).

`BACK TO TOP <License_>`_

------------

