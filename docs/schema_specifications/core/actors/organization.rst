############
Organization
############

:Semantic name: https://openminds.ebrains.eu/core/Organization

:Display as: Organization

An entity comprised of one or more natural persons with a particular purpose. [adapted from Wikipedia](https://en.wikipedia.org/wiki/Organization)


------------

------------

Properties
##########

:Required: `fullName <fullName_heading_>`_
:Optional: `digitalIdentifier <digitalIdentifier_heading_>`_, `hasParent <hasParent_heading_>`_, `homepage <homepage_heading_>`_, `shortName <shortName_heading_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object array \(1-N\) of type
                | `GRIDID <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/GRIDID.html>`_ or `RORID <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/RORID.html>`_
   :instructions: Add one or several globally unique and persistent digital identifier for this organization.

`BACK TO TOP <Organization_>`_

------------

.. _fullName_heading:

********
fullName
********

Whole, non-abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the full name of the organization.

`BACK TO TOP <Organization_>`_

------------

.. _hasParent_heading:

*********
hasParent
*********

Reference to a parent object or legal person.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasParent
   :value type: | linked object of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/actors/organization.html>`_
   :instructions: Add a parent organization to this organization.

`BACK TO TOP <Organization_>`_

------------

.. _homepage_heading:

********
homepage
********

Main website of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/homepage
   :value type: | linked object of type
                | `URL <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/URL.html>`_
   :instructions: Add the uniform resource locator (URL) to the homepage of this organization.

`BACK TO TOP <Organization_>`_

------------

.. _shortName_heading:

*********
shortName
*********

Shortened or fully abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the short name of this organization.

`BACK TO TOP <Organization_>`_

------------

