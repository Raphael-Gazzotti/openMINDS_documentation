######
Person
######

:Semantic name: https://openminds.om-i.org/types/Person

:Display as: Person

Structured information on a person.


------------

------------

Properties
##########

:Required: `preferredName <preferredName_heading_>`_
:Optional: `alternateName <alternateName_heading_>`_, `associatedAccount <associatedAccount_heading_>`_, `contactInformation <contactInformation_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `familyName <familyName_heading_>`_, `givenName <givenName_heading_>`_

------------

.. _alternateName_heading:

*************
alternateName
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/alternateName
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter any other known full name of this person.

`BACK TO TOP <Person_>`_

------------

.. _associatedAccount_heading:

*****************
associatedAccount
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/associatedAccount
   :value type: | linked object array \(1-N\) of type
                | `AccountInformation <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/actors/accountInformation.html>`_
   :instructions: Add the information about web service accounts held by this person.

`BACK TO TOP <Person_>`_

------------

.. _contactInformation_heading:

******************
contactInformation
******************

Any available way used to contact a person or business (e.g., address, phone number, email address, etc.).

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contactInformation
   :value type: | linked object of type
                | `ContactInformation <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/actors/contactInformation.html>`_
   :instructions: Add the contact information of this person.

`BACK TO TOP <Person_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/digitalIdentifier
   :value type: | linked object array \(1-N\) of type
                | `GenericIdentifier <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/digitalIdentifier/genericIdentifier.html>`_ or `ORCID <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/digitalIdentifier/ORCID.html>`_
   :instructions: Add all globally unique and persistent digital identifier of this person.

`BACK TO TOP <Person_>`_

------------

.. _familyName_heading:

**********
familyName
**********

Name borne in common by members of a family.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/familyName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the family name, surname, or equivalent of this person.

`BACK TO TOP <Person_>`_

------------

.. _givenName_heading:

*********
givenName
*********

Name given to a person, including all potential middle names, but excluding the family name.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/givenName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the given name(s) of this person, or a name chosen in place of the given name. At least one of the names should be spelled out in full; initials may be used for the others.

`BACK TO TOP <Person_>`_

------------

.. _preferredName_heading:

*************
preferredName
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/preferredName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the person’s preferred way to write their name in a professional context. It is recommended to place given before family name separated by space.

`BACK TO TOP <Person_>`_

------------

