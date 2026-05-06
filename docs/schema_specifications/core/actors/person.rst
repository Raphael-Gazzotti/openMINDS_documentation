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

:Required: `givenName <givenName_heading_>`_
:Optional: `affiliation <affiliation_heading_>`_, `alternateName <alternateName_heading_>`_, `associatedAccount <associatedAccount_heading_>`_, `contactInformation <contactInformation_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `familyName <familyName_heading_>`_

------------

.. _affiliation_heading:

***********
affiliation
***********

Declaration of a person being closely associated to an organization.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/affiliation
   :value type: | embedded object array \(1-N\) of type
                | `Affiliation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/affiliation.html>`_
   :instructions: Enter all current and, if desired, past affiliations of this person.

`BACK TO TOP <Person_>`_

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
                | `AccountInformation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/accountInformation.html>`_
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
                | `ContactInformation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/contactInformation.html>`_
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
                | `ORCID <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/ORCID.html>`_
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
   :instructions: Enter the family name of this person.

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
   :instructions: Enter the given name of this person.

`BACK TO TOP <Person_>`_

------------

