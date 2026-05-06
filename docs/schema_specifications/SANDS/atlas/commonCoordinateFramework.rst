#########################
CommonCoordinateFramework
#########################

:Semantic name: https://openminds.om-i.org/types/CommonCoordinateFramework

:Display as: Common coordinate framework


For this schema openMINDS provides a `library of instances <https://openminds-documentation.readthedocs.io/en/latest/instance_libraries/commonCoordinateFrameworks.html>`_.

------------

------------

Properties
##########

:Required: `contribution <contribution_heading_>`_, `description <description_heading_>`_, `fullName <fullName_heading_>`_, `howToCite <howToCite_heading_>`_, `shortName <shortName_heading_>`_, `usedTaxon <usedTaxon_heading_>`_
:Optional: `abbreviation <abbreviation_heading_>`_, `contributorAffiliation <contributorAffiliation_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `documentation <documentation_heading_>`_, `homepage <homepage_heading_>`_, `keyword <keyword_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_, `relatedPublication <relatedPublication_heading_>`_, `supportChannel <supportChannel_heading_>`_

------------

.. _abbreviation_heading:

************
abbreviation
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/abbreviation
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the official abbreviation of this common coordinate framework.

`BACK TO TOP <CommonCoordinateFramework_>`_

------------

.. _contribution_heading:

************
contribution
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contribution
   :value type: | embedded object array \(1-N\) of type
                | `Contribution <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/contribution.html>`_
   :instructions: Add all individual, organisational, or consortial contributions to this research product. Inherited by all product versions unless overridden at the version level.

`BACK TO TOP <CommonCoordinateFramework_>`_

------------

.. _contributorAffiliation_heading:

**********************
contributorAffiliation
**********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contributorAffiliation
   :value type: | embedded object array \(1-N\) of type
                | `Affiliation <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/affiliation.html>`_
   :instructions: Add all affiliations for the individual contributors to this research product. Inherited by all product versions unless overridden at the version level.

`BACK TO TOP <CommonCoordinateFramework_>`_

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
   :instructions: Enter a description (or abstract) of this research product. Inherited by all product versions unless overridden at the version level.

`BACK TO TOP <CommonCoordinateFramework_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/digitalIdentifier
   :value type: | linked object of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/DOI.html>`_, `ISBN <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/ISBN.html>`_ or `RRID <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/RRID.html>`_
   :instructions: Add the globally unique and persistent digital identifier of this research product. Note that this digital identifier will be used to reference all attached research product versions.

`BACK TO TOP <CommonCoordinateFramework_>`_

------------

.. _documentation_heading:

*************
documentation
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/documentation
   :value type: | linked object of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/DOI.html>`_, `File <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/file.html>`_, `ISBN <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/ISBN.html>`_ or `WebResource <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/webResource.html>`_
   :instructions: Add the publication or file that acts as the documentation of this research product. Inherited by all product versions unless overridden at the version level.

`BACK TO TOP <CommonCoordinateFramework_>`_

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
   :instructions: Enter a descriptive full name (or title) for this research product. Inherited by all product versions unless overridden at the version level.

`BACK TO TOP <CommonCoordinateFramework_>`_

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
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this research product. Inherited by all product versions unless overridden at the version level.

`BACK TO TOP <CommonCoordinateFramework_>`_

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
   :instructions: Enter the preferred citation text for this research product. Leave blank if citation text can be extracted from the assigned digital identifier.

`BACK TO TOP <CommonCoordinateFramework_>`_

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
   :instructions: Add all relevant keywords to this research product either by adding controlled terms or by suggesting new terms. Inherited by all product versions unless overridden at the version level.

`BACK TO TOP <CommonCoordinateFramework_>`_

------------

.. _ontologyIdentifier_heading:

******************
ontologyIdentifier
******************

Term or code used to identify something or someone registered within a particular ontology.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/ontologyIdentifier
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this common coordinate framework.

`BACK TO TOP <CommonCoordinateFramework_>`_

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
   :instructions: Add all further publications besides the documentation that provide the original context for the production of this research product (e.g., an original research article that used or produced the data of this research product). Inherited by all product versions unless overridden at the version level.

`BACK TO TOP <CommonCoordinateFramework_>`_

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
   :instructions: Enter a short name (or alias) for this research product that could be used as a shortened display title (e.g., for web services with too little space to display the full name). Inherited by all product versions unless overridden at the version level.

`BACK TO TOP <CommonCoordinateFramework_>`_

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
   :instructions: Enter all channels through which a user can receive support for handling this research product. Inherited by all product versions unless overridden at the version level.

`BACK TO TOP <CommonCoordinateFramework_>`_

------------

.. _usedTaxon_heading:

*********
usedTaxon
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/usedTaxon
   :value type: | linked object of type
                | `BiologicalOrder <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/biologicalOrder.html>`_ or `Species <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/species.html>`_
   :instructions: Add the taxon (e.g., species) that was used for the creation of this common coordinate framework.

`BACK TO TOP <CommonCoordinateFramework_>`_

------------

