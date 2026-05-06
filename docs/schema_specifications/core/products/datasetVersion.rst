##############
DatasetVersion
##############

:Semantic name: https://openminds.om-i.org/types/DatasetVersion

:Display as: Dataset version

Structured information on data originating from human/animal studies or simulations (version level).


------------

------------

Properties
##########

:Required: `accessibility <accessibility_heading_>`_, `contribution <contribution_heading_>`_, `dataType <dataType_heading_>`_, `description <description_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `documentation <documentation_heading_>`_, `ethicsJurisdiction <ethicsJurisdiction_heading_>`_, `experimentalApproach <experimentalApproach_heading_>`_, `fullName <fullName_heading_>`_, `isVersionOf <isVersionOf_heading_>`_, `releaseDate <releaseDate_heading_>`_, `shortName <shortName_heading_>`_, `technique <technique_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_, `versionSpecification <versionSpecification_heading_>`_
:Optional: `contributorAffiliation <contributorAffiliation_heading_>`_, `copyright <copyright_heading_>`_, `funding <funding_heading_>`_, `homepage <homepage_heading_>`_, `howToCite <howToCite_heading_>`_, `inputData <inputData_heading_>`_, `isPrecededBy <isPrecededBy_heading_>`_, `isVariantOf <isVariantOf_heading_>`_, `keyword <keyword_heading_>`_, `preparationType <preparationType_heading_>`_, `protocol <protocol_heading_>`_, `publicationStatus <publicationStatus_heading_>`_, `relatedPublication <relatedPublication_heading_>`_, `repository <repository_heading_>`_, `studiedSpecimen <studiedSpecimen_heading_>`_, `studyTarget <studyTarget_heading_>`_, `supportChannel <supportChannel_heading_>`_, `usageCondition <usageCondition_heading_>`_

------------

.. _accessibility_heading:

*************
accessibility
*************

Level to which something is accessible to someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/accessibility
   :value type: | linked object of type
                | `Accessibility <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/accessibility.html>`_
   :instructions: Add the accessibility of the data for this research product version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _contribution_heading:

************
contribution
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contribution
   :value type: | embedded object array \(1-N\) of type
                | `Contribution <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/contribution.html>`_
   :instructions: Add all individual, organisational, or consortial contributions to this research product version. These values override the inherited values from the version-independent product.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _contributorAffiliation_heading:

**********************
contributorAffiliation
**********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contributorAffiliation
   :value type: | embedded object array \(1-N\) of type
                | `Affiliation <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/affiliation.html>`_
   :instructions: Add all affiliations for the individual contributors to this research product version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _copyright_heading:

*********
copyright
*********

Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/copyright
   :value type: | embedded object of type
                | `Copyright <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/copyright.html>`_
   :instructions: Enter the copyright information of this research product version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _dataType_heading:

********
dataType
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/dataType
   :value type: | linked object array \(1-N\) of type
                | `SemanticDataType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/semanticDataType.html>`_
   :instructions: Add all semantic data types (raw, derived and/or simulated) provided in this dataset version.

`BACK TO TOP <DatasetVersion_>`_

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
   :instructions: Enter a description (or abstract) of this research product version. This value overrides the inherited value from the version-independent product.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/digitalIdentifier
   :value type: | linked object of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/DOI.html>`_, `GenericIdentifier <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/genericIdentifier.html>`_, `IdentifiersDotOrgID <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/IdentifiersDotOrgID.html>`_ or `RRID <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/RRID.html>`_
   :instructions: Add the globally unique and persistent digital identifier of this research product version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _documentation_heading:

*************
documentation
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/documentation
   :value type: | linked object of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/DOI.html>`_, `File <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/file.html>`_, `ISBN <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/ISBN.html>`_ or `WebResource <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/webResource.html>`_
   :instructions: Add the publication or file that acts as the documentation of this research product version. This value overrides the inherited value from the version-independent product.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _ethicsJurisdiction_heading:

******************
ethicsJurisdiction
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/ethicsJurisdiction
   :value type: | linked object of type
                | `SovereignState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/sovereignState.html>`_ or `SupranationalBody <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/supranationalBody.html>`_
   :instructions: Add the jurisdiction under which the ethics assessment of this dataset version was conducted.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _experimentalApproach_heading:

********************
experimentalApproach
********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/experimentalApproach
   :value type: | linked object array \(1-N\) of type
                | `ExperimentalApproach <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/experimentalApproach.html>`_
   :instructions: Add all experimental approaches which this dataset version has deployed.

`BACK TO TOP <DatasetVersion_>`_

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
   :instructions: Enter a descriptive full name (or title) for this research product version. This value overrides the inherited value from the version-independent product.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _funding_heading:

*******
funding
*******

Money provided by a legal person for a particular purpose.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/funding
   :value type: | linked object array \(1-N\) of type
                | `Funding <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/funding.html>`_
   :instructions: Add all funding information of this research product version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _homepage_heading:

********
homepage
********

Main website of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/homepage
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this research product version. This value overrides the inherited value from the version-independent product.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _howToCite_heading:

*********
howToCite
*********

Preferred format for citing a particular object or legal person.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/howToCite
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter the preferred citation text for this research product version. Leave blank if citation text can be extracted from the assigned digital identifier.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _inputData_heading:

*********
inputData
*********

Data that is put into a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/inputData
   :value type: | linked object array \(1-N\) of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/DOI.html>`_, `File <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/file.html>`_, `FileBundle <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/fileBundle.html>`_, `WebResource <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/webResource.html>`_, `AnatomicalAtlas <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/anatomicalAtlas.html>`_, `AnatomicalAtlasVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/anatomicalAtlasVersion.html>`_, `CommonCoordinateFramework <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/commonCoordinateFramework.html>`_ or `CommonCoordinateFrameworkVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/commonCoordinateFrameworkVersion.html>`_
   :instructions: Add the data that was used as input for this dataset version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _isPrecededBy_heading:

************
isPrecededBy
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/isPrecededBy
   :value type: | linked object of type
                | `DatasetVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/datasetVersion.html>`_
   :instructions: Add the dataset version preceding this dataset version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _isVariantOf_heading:

***********
isVariantOf
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/isVariantOf
   :value type: | linked object array \(1-N\) of type
                | `DatasetVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/datasetVersion.html>`_
   :instructions: Add all dataset versions that can be used alternatively to this dataset version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _isVersionOf_heading:

***********
isVersionOf
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/isVersionOf
   :value type: | linked object of type
                | `Dataset <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/dataset.html>`_
   :instructions: Add the version-independent information about this dataset.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _keyword_heading:

*******
keyword
*******

Significant word or concept that are representative of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/keyword
   :value type: | linked object array \(1-N\) of type
                | `AccessChannel <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/accessChannel.html>`_, `AccessEligibilityType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/accessEligibilityType.html>`_, `AccessForm <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/accessForm.html>`_, `AccessProcessType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/accessProcessType.html>`_, `ActionStatusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/actionStatusType.html>`_, `AgeCategory <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/ageCategory.html>`_, `AgeReference <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/ageReference.html>`_, `AnalysisTechnique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/analysisTechnique.html>`_, `AnatomicalAxesOrientation <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/anatomicalAxesOrientation.html>`_, `AnatomicalCavity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/anatomicalCavity.html>`_, `AnatomicalIdentificationType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/anatomicalIdentificationType.html>`_, `AnatomicalPlane <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/anatomicalPlane.html>`_, `AnnotationCriteriaType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/annotationCriteriaType.html>`_, `AnnotationType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/annotationType.html>`_, `AtlasType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/atlasType.html>`_, `AuditoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/auditoryStimulusType.html>`_, `BiologicalOrder <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/biologicalOrder.html>`_, `BiologicalProcess <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/biologicalProcess.html>`_, `BiologicalSex <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/biologicalSex.html>`_, `BreedingType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/breedingType.html>`_, `CellCultureType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/cellCultureType.html>`_, `CellType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/cellType.html>`_, `ChemicalMixtureType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/chemicalMixtureType.html>`_, `Colormap <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/colormap.html>`_, `CommunicationInterfaceType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/communicationInterfaceType.html>`_, `CommunicationProtocol <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/communicationProtocol.html>`_, `ContributionType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/contributionType.html>`_, `CranialWindowConstructionType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/cranialWindowConstructionType.html>`_, `CranialWindowReinforcementType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/cranialWindowReinforcementType.html>`_, `CriteriaQualityType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/criteriaQualityType.html>`_, `DataType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/dataType.html>`_, `DependencyImpact <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/dependencyImpact.html>`_, `DeploymentEnvironmentType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/deploymentEnvironmentType.html>`_, `DeviceMountingType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/deviceMountingType.html>`_, `DeviceType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/deviceType.html>`_, `DifferenceMeasure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/differenceMeasure.html>`_, `Disease <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/disease.html>`_, `DiseaseModel <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/diseaseModel.html>`_, `EducationalLevel <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/educationalLevel.html>`_, `ElectricalStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/electricalStimulusType.html>`_, `ExperimentalApproach <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/experimentalApproach.html>`_, `ExternalBodyRegion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/externalBodyRegion.html>`_, `FileBundleGrouping <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/fileBundleGrouping.html>`_, `FileRepositoryType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/fileRepositoryType.html>`_, `FileUsageRole <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/fileUsageRole.html>`_, `GeneticStrainType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/geneticStrainType.html>`_, `GustatoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/gustatoryStimulusType.html>`_, `Handedness <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/handedness.html>`_, `Language <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/language.html>`_, `Laterality <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/laterality.html>`_, `LearningResourceType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/learningResourceType.html>`_, `MRIFatSuppressionTechnique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/MRIFatSuppressionTechnique.html>`_, `MRIParallelAcquisitionTechnique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/MRIParallelAcquisitionTechnique.html>`_, `MRIPulseSequence <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/MRIPulseSequence.html>`_, `MRISpoilingTechnique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/MRISpoilingTechnique.html>`_, `MRIWeighting <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/MRIWeighting.html>`_, `MeasuredQuantity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/measuredQuantity.html>`_, `MeasuredSignalType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/measuredSignalType.html>`_, `MetaDataModelType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/metaDataModelType.html>`_, `ModelAbstractionLevel <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/modelAbstractionLevel.html>`_, `ModelScope <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/modelScope.html>`_, `ModificationConsentRequirement <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/modificationConsentRequirement.html>`_, `ModificationConstraint <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/modificationConstraint.html>`_, `ModificationForm <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/modificationForm.html>`_, `ModificationScope <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/modificationScope.html>`_, `MolecularEntity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/molecularEntity.html>`_, `MuscularStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/muscularStructure.html>`_, `NervousSystemStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/nervousSystemStructure.html>`_, `OlfactoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/olfactoryStimulusType.html>`_, `OperatingDevice <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/operatingDevice.html>`_, `OperatingSystem <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/operatingSystem.html>`_, `OperationalApproach <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/operationalApproach.html>`_, `OpticalStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/opticalStimulusType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organ.html>`_, `OrganSystemStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organSystemStructure.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organismSubstance.html>`_, `OrganismSystem <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organismSystem.html>`_, `OrganizationType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organizationType.html>`_, `PatchClampVariation <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/patchClampVariation.html>`_, `PaymentModelType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/paymentModelType.html>`_, `PreparationType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/preparationType.html>`_, `ProgrammingLanguage <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/programmingLanguage.html>`_, `ProjectType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/projectType.html>`_, `PublicationStatus <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/publicationStatus.html>`_, `PulseShape <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/pulseShape.html>`_, `QualitativeOverlap <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/qualitativeOverlap.html>`_, `SemanticDataType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/semanticDataType.html>`_, `SetupType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/setupType.html>`_, `SignalDirectionality <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/signalDirectionality.html>`_, `SkeletalStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/skeletalStructure.html>`_, `SoftwareApplicationCategory <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/softwareApplicationCategory.html>`_, `SoftwareFeature <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/softwareFeature.html>`_, `SovereignState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/sovereignState.html>`_, `SpatialEncoding <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/spatialEncoding.html>`_, `Species <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/species.html>`_, `StimulationApproach <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/stimulationApproach.html>`_, `StimulationTechnique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/stimulationTechnique.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/subcellularEntity.html>`_, `SubjectAttribute <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/subjectAttribute.html>`_, `SupranationalBody <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/supranationalBody.html>`_, `TactileStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/tactileStimulusType.html>`_, `Technique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/technique.html>`_, `TermSuggestion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/termSuggestion.html>`_, `Terminology <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/terminology.html>`_, `TissueSampleAttribute <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/tissueSampleAttribute.html>`_, `TissueSampleType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/tissueSampleType.html>`_, `TissueStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/tissueStructure.html>`_, `TypeOfUncertainty <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/typeOfUncertainty.html>`_, `UnitOfMeasurement <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/unitOfMeasurement.html>`_, `VascularStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/vascularStructure.html>`_, `VisualStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/visualStimulusType.html>`_ or `WeightType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/weightType.html>`_
   :instructions: Add all relevant keywords to this research product version either by adding controlled terms or by suggesting new terms. This value overrides the inherited value from the version-independent product.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _preparationType_heading:

***************
preparationType
***************

Distinct class of actions or processes that make something ready for use or service.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/preparationType
   :value type: | linked object array \(1-N\) of type
                | `PreparationType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/preparationType.html>`_
   :instructions: Add all preparation types used in this dataset version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _protocol_heading:

********
protocol
********

Plan that describes the process of a scientific or medical experiment, treatment, or procedure.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/protocol
   :value type: | linked object array \(1-N\) of type
                | `BehavioralProtocol <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/behavioralProtocol.html>`_ or `Protocol <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/protocol.html>`_
   :instructions: Add all protocols that were performed in this dataset version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _publicationStatus_heading:

*****************
publicationStatus
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/publicationStatus
   :value type: | linked object of type
                | `PublicationStatus <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/publicationStatus.html>`_
   :instructions: Add the relevant publication status indicating the current lifecycle state of the resource (published, embargoed, disposed, retracted, etc.).

`BACK TO TOP <DatasetVersion_>`_

------------

.. _relatedPublication_heading:

******************
relatedPublication
******************

Reference to something that was made available for the general public to see or buy.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/relatedPublication
   :value type: | linked object array \(1-N\) of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/DOI.html>`_, `GenericIdentifier <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/genericIdentifier.html>`_, `HANDLE <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/HANDLE.html>`_, `ISBN <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/ISBN.html>`_, `ISSN <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/ISSN.html>`_, `Book <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/publications/book.html>`_, `Chapter <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/publications/chapter.html>`_ or `ScholarlyArticle <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/publications/scholarlyArticle.html>`_
   :instructions: Add all further publications besides the documentation that provide the original context for the production of this research product version (e.g., an original research article that used or produced the data of this research product version). This value overrides the inherited value from the version-independent product.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _releaseDate_heading:

***********
releaseDate
***********

Fixed date on which a product is due to become or was made available for the general public to see or buy

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/releaseDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date (actual or intended) on which this research product version was first release, formatted as 'YYYY-MM-DD'.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _repository_heading:

**********
repository
**********

Place, room, or container where something is deposited or stored.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/repository
   :value type: | linked object of type
                | `FileRepository <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/fileRepository.html>`_
   :instructions: Add the file repository of this research product version.

`BACK TO TOP <DatasetVersion_>`_

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
   :instructions: Enter a short name (or alias) for this research product version that could be used as a shortened display title (e.g., for web services with too little space to display the full name). This value overrides the inherited value from the version-independent product.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _studiedSpecimen_heading:

***************
studiedSpecimen
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/studiedSpecimen
   :value type: | linked object array \(1-N\) of type
                | `Subject <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/subject.html>`_, `SubjectState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/subjectState.html>`_, `SubjectGroup <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/subjectGroup.html>`_, `SubjectGroupState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/subjectGroupState.html>`_, `TissueSample <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/tissueSample.html>`_, `TissueSampleState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/tissueSampleState.html>`_, `TissueSampleCollection <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/tissueSampleCollection.html>`_ or `TissueSampleCollectionState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/tissueSampleCollectionState.html>`_
   :instructions: Add all specimens, sets of specimen or states that were studied in this dataset.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _studyTarget_heading:

***********
studyTarget
***********

Structure or function that was targeted within a study.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/studyTarget
   :value type: | linked object array \(1-N\) of type
                | `AnatomicalCavity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/anatomicalCavity.html>`_, `AuditoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/auditoryStimulusType.html>`_, `BiologicalOrder <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/biologicalOrder.html>`_, `BiologicalSex <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/biologicalSex.html>`_, `BreedingType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/breedingType.html>`_, `CellCultureType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/cellCultureType.html>`_, `CellType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/cellType.html>`_, `DeviceType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/deviceType.html>`_, `Disease <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/disease.html>`_, `DiseaseModel <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/diseaseModel.html>`_, `ElectricalStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/electricalStimulusType.html>`_, `ExternalBodyRegion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/externalBodyRegion.html>`_, `GeneticStrainType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/geneticStrainType.html>`_, `GustatoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/gustatoryStimulusType.html>`_, `Handedness <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/handedness.html>`_, `MolecularEntity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/molecularEntity.html>`_, `MuscularStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/muscularStructure.html>`_, `NervousSystemStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/nervousSystemStructure.html>`_, `OlfactoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/olfactoryStimulusType.html>`_, `OpticalStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/opticalStimulusType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organ.html>`_, `OrganSystemStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organSystemStructure.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organismSubstance.html>`_, `OrganismSystem <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organismSystem.html>`_, `SkeletalStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/skeletalStructure.html>`_, `Species <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/species.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/subcellularEntity.html>`_, `TactileStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/tactileStimulusType.html>`_, `TermSuggestion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/termSuggestion.html>`_, `TissueSampleType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/tissueSampleType.html>`_, `TissueStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/tissueStructure.html>`_, `VascularStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/vascularStructure.html>`_, `VisualStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/visualStimulusType.html>`_, `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add all study targets of this dataset version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _supportChannel_heading:

**************
supportChannel
**************

Way of communication used to interact with users or customers.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/supportChannel
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter all channels through which a user can receive support for handling this research product version. This value overrides the inherited value from the version-independent product.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _technique_heading:

*********
technique
*********

Method of accomplishing a desired aim.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/technique
   :value type: | linked object array \(1-N\) of type
                | `AnalysisTechnique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/analysisTechnique.html>`_, `MRIFatSuppressionTechnique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/MRIFatSuppressionTechnique.html>`_, `MRIParallelAcquisitionTechnique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/MRIParallelAcquisitionTechnique.html>`_, `MRIPulseSequence <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/MRIPulseSequence.html>`_, `MRISpoilingTechnique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/MRISpoilingTechnique.html>`_, `MRIWeighting <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/MRIWeighting.html>`_, `SpatialEncoding <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/spatialEncoding.html>`_, `StimulationApproach <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/stimulationApproach.html>`_, `StimulationTechnique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/stimulationTechnique.html>`_ or `Technique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/technique.html>`_
   :instructions: Add all techniques that were used in this dataset version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _usageCondition_heading:

**************
usageCondition
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/usageCondition
   :value type: | linked object array \(1-N\) of type
                | `License <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/license.html>`_ or `UsageAgreement <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/usageAgreement.html>`_
   :instructions: Add all licenses and available data usage agreements applicable to this product version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _versionIdentifier_heading:

*****************
versionIdentifier
*****************

Term or code used to identify the version of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/versionIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the version identifier of this research product version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _versionSpecification_heading:

********************
versionSpecification
********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/versionSpecification
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short description (or summary) of the novelties/peculiarities of this research product version in comparison to its preceding versions. If this research product version is the first version, you can enter the following disclaimer 'This is the first version of this research product'.

`BACK TO TOP <DatasetVersion_>`_

------------

