#################################
Terminologies: DeviceType library
#################################

Related schema specification: `DeviceType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/deviceType.html>`_

------------

------------

CTscanner
---------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/CTscanner
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: A 'CT scanner' is an x-ray machine that creates and combines serial two-dimensional x-ray images (sections) with the aid of a computer to generate cross-sectional views and/or three-dimensional images of internal body structures (e.g., bones, blood vessels or soft tissues).
   :name: CT scanner

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIBodyCoil
-----------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/MRIBodyCoil
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: Type of volume coil optimized for uniform radiofrequency transmission and/or reception across large anatomical regions, typically encompassing the torso or entire body.
   :description: Body coils are integrated volume coils typically built into the bore of an MRI scanner to provide homogeneous B1 field distribution across extensive anatomical areas. They are often used as transmit or transmit/receive coils for imaging the torso and whole body, and frequently serve as the system's default transmit coil when combined with local receive arrays. Their large geometry ensures consistent excitation and reception, enabling high-quality imaging across diverse body regions and supporting calibration or reference functions in multi-coil setups.
   :name: MRI body coil

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIExtremityCoil
----------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/MRIExtremityCoil
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: Type of volume coil optimized for imaging peripheral anatomical regions such as the arms, legs, wrists, ankles, or knees; in rare cases, extremity coils may adopt a surface-coil design when full enclosure of the anatomy is impractical.
   :description: Extremity coils are specialized radiofrequency volume coils designed to provide high signal-to-noise ratio and uniform excitation when imaging smaller body parts like the limbs. They typically use cylindrical or contoured geometries that enclose the target region but can also appear as surface-coil variants for joints or areas where full coverage is not feasible. Extremity coils are widely used in musculoskeletal and vascular MRI, offering focused, high-resolution imaging of localized peripheral structures.
   :name: MRI extremity coil

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIHeadCoil
-----------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/MRIHeadCoil
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: Type of volume coil optimized for radiofrequency transmission and/or reception over the head and brain, providing homogeneous B1 field coverage within the cranial region.
   :description: Head coils are dedicated radiofrequency (RF) volume coils designed to image the brain and cranial structures. They typically use birdcage or quadrature configurations to achieve uniform excitation and reception across the entire head. Head coils can operate as transmit/receive or receive-only systems depending on the scanner design. High-channel phased-array head coils are increasingly common, improving signal-to-noise ratio (SNR) and parallel-imaging capabilities. In some advanced configurations, open or partial head coils are employed for interventional or functional MRI studies, where full enclosure is not required.
   :name: MRI head coil

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIInsertGradientCoil
---------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/MRIInsertGradientCoil
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: A secondary gradient coil assembly placed inside the main magnetic resonance imaging (MRI) bore to generate high-performance spatially varying magnetic fields over a restricted imaging region.
   :description: An MRI insert gradient coil is installed within the bore of an existing MRI system as an auxiliary gradient subsystem. It operates in conjunction with the MRI system gradient coil to provide enhanced gradient strength and slew rates within a limited field of view. This localized performance supports high-resolution and rapid imaging applications. Insert gradient coils are commonly used in head, extremity, and research-oriented configurations. Such coils are typically non-integrated and mounted in a form-stable, non-conformable manner to ensure mechanical and electromagnetic stability.
   :name: MRI insert gradient coil

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIMulti-coilArray
------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/MRIMulti-coilArray
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: Type of radiofrequency coil composed of multiple coordinated elements optimized for transmit and/or receive operation over an extended field of view; phased-array coils are a specialized subclass focused on parallel signal reception.
   :description: Multi-coil arrays consist of several individual RF elements that work together to improve signal quality, coverage, and control of the B₁ field. Depending on their configuration, they may operate as transmit, receive, or transmit-receive systems, enabling techniques such as RF shimming, parallel transmission, and parallel imaging. These arrays can be designed with volume-type geometries that enclose the anatomy or surface-type arrangements that conform to the body's contour. Phased-array coils represent a subset of multi-coil arrays specialized for independent receive channels used in parallel acquisition.
   :name: MRI multi-coil array

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIRFMulti-arrayCoil
--------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/MRIRFMulti-arrayCoil
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: A multi-element radiofrequency (RF) coil system in which independent channels are used for parallel signal transmission and/or reception and enhanced spatial encoding in magnetic resonance imaging (MRI).
   :description: An MRI RF multi-array coil consists of multiple RF coil elements arranged around the region of interest to acquire localized signals in parallel. Each element operates independently, enabling spatially distributed signal detection and improved signal-to-noise ratio. Multi-coil arrays enhance coverage and allow control of the B₁ field through techniques such as RF shimming, parallel transmission, and parallel imaging. Depending on their configuration, they may operate in transmit, receive, or transmit-receive modes, although most clinical systems use them primarily for reception in combination with an MRI RF volume coil for transmission. These coils may be implemented in volume-type geometries that enclose the anatomy or in surface-type arrangements that are form-stable or conformable.
   :name: MRI RF multi-array coil

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIRFSurfaceCoil
----------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/MRIRFSurfaceCoil
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: A localized radiofrequency (RF) coil designed to transmit and/or receive magnetic resonance imaging (MRI) signals from a limited region near the body surface.
   :description: An MRI RF surface coil is positioned directly adjacent to the region of interest to maximize local signal sensitivity. Its sensitivity decreases rapidly with distance, making it primarily suitable for imaging superficial anatomical regions. In most clinical configurations, it is used in combination with an MRI RF volume coil for transmission and operates mainly in receive mode. In specialized or legacy systems, it may also be configured for both transmission and reception. MRI RF surface coils are typically mounted in a non-integrated manner and may be either conformable or form-stable, depending on their mechanical design and intended application.
   :name: MRI RF surface coil

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIRFVolumeCoil
---------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/MRIRFVolumeCoil
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: An radiofrequency (RF) coil that surrounds the imaging region to provide relatively uniform RF excitation and/or signal reception over a large volume in magnetic resonance imaging (MRI).
   :description: An MRI RF volume coil encloses the region of interest within its conductive structure to generate spatially homogeneous RF fields. Its primary design goal is uniform excitation and consistent signal sensitivity across the imaging volume. In most clinical systems, it is used primarily for transmission and operates in combination with surface coils or multi-array coils for reception. In some configurations, it may also function in transmit–receive mode, particularly in specialized or legacy systems. MRI RF volume coils are typically integrated into the scanner or mounted in a form-stable, non-conformable configuration to maintain geometric and electromagnetic stability.
   :name: MRI RF volume coil

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIShimCoil
-----------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/MRIShimCoil
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: An electromagnetic coil system used to generate corrective magnetic fields that improve static magnetic field (B₀) homogeneity in magnetic resonance imaging (MRI).
   :description: An MRI shim coil produces small, adjustable magnetic field components within the imaging volume to compensate for spatial inhomogeneities of the main magnetic field. These corrective fields improve spectral resolution, signal stability, and overall image quality. In modern systems, shim coils are actively controlled and adjusted during system calibration and examination setup. Shimming parameters may be optimized globally or locally depending on the imaging protocol. Such coils are typically integrated into the scanner structure and operate continuously or intermittently as required by system design.
   :name: MRI shim coil

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRISurfaceCoil
--------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/MRISurfaceCoil
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: Type of radiofrequency coil optimized for localized signal reception from tissue near the coil surface, providing high sensitivity over a small field of view.
   :description: Surface coils are small radiofrequency coils placed directly adjacent to the region of interest to capture strong signals from nearby tissues with high spatial resolution. Their sensitivity decreases rapidly with distance, making them ideal for imaging superficial structures such as the spine, joints, or breast. Surface coils are typically receive-only and operate in combination with a separate transmit coil, often the body coil. They can also serve as building blocks in multi-coil or phased-array configurations, extending coverage while maintaining local sensitivity.
   :name: MRI surface coil

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRISystemGradientCoil
---------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/MRISystemGradientCoil
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: The primary gradient coil assembly integrated into a magnetic resonance imaging (MRI) system for generating spatially varying magnetic fields used in image encoding.
   :description: An MRI system gradient coil is permanently integrated into the scanner structure and forms the main source of spatially varying magnetic fields for imaging. It generates rapidly switching magnetic field gradients along three orthogonal axes to enable spatial localization of the MRI signal. The design prioritizes whole-volume coverage, thermal stability, and mechanical robustness. In most systems, it operates continuously during image acquisition in coordination with the main magnet and radiofrequency (RF) subsystems. MRI system gradient coils are typically integrated and mounted in a form-stable, non-conformable configuration to maintain geometric and electromagnetic stability.
   :name: MRI system gradient coil

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIVolumeCoil
-------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/MRIVolumeCoil
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: Type of radiofrequency coil optimized for uniform transmit and/or receive coverage across a defined enclosed volume of anatomy.
   :description: Volume coils are radiofrequency coils that fully or partially enclose the anatomy to produce a homogeneous B₁ field within a specified region, such as the head, torso, or extremities. They are used for both transmission and reception of MR signals and are commonly built in birdcage or quadrature configurations. Volume coils provide uniform excitation and reception, making them suitable for general-purpose imaging or as transmit coils in combination with local receive arrays. Their subtypes include body, head, and extremity coils, which differ mainly by size and anatomical coverage.
   :name: MRI volume coil

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIscanner
----------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/MRIscanner
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: An 'MRI scanner' is a machine that uses strong magnetic fields, magnetic field gradients, and radio waves to generate static or time-resolved three-dimensional images of the anatomy and physiological processes of the body.
   :interlexIdentifier: http://uri.interlex.org/base/ilx_0106463
   :name: MRI scanner
   :preferredOntologyIdentifier: http://uri.neuinfo.org/nif/nifstd/birnlex_2100

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

closedBoreMRIScanner
--------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/closedBoreMRIScanner
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: 'Closed-bore MRI scanners' are high-field scanners which feature a magnet surrounding the patient creating a capsule-like space (standard or wide) where the patient lies on.
   :name: closed-bore MRI scanner

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

electronicAmplifier
-------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/electronicAmplifier
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: An 'electronic amplifier' is a device that increases the power (voltage or current) of a time-varying signal.
   :interlexIdentifier: http://uri.interlex.org/base/ilx_0100567
   :name: electronic amplifier
   :preferredOntologyIdentifier: http://uri.neuinfo.org/nif/nifstd/nlx_27076

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

microscope
----------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/microscope
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: A 'microscope' is an instrument used to obtain a magnified image of small objects and reveal details of structures not otherwise distinguishable.
   :interlexIdentifier: http://uri.interlex.org/base/ilx_0106921
   :name: microscope
   :preferredOntologyIdentifier: http://uri.neuinfo.org/nif/nifstd/birnlex_2106

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

microtome
---------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/microtome
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: A 'microtome' is a mechanical instrument with a steel, glass or diamond blade used to cut (typically) biological specimens into very thin segments for further treatment and ultimately microscopic or histologic examination.
   :interlexIdentifier: http://uri.interlex.org/base/ilx_0106925
   :name: microtome
   :preferredOntologyIdentifier: http://purl.obolibrary.org/obo/OBI_0400168

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

openBoreMRIScanner
------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/openBoreMRIScanner
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: 'Open-bore MRI scanners' are low-field scanners which have a magnetic top and bottom, but are otherwise open, increasing patient's comfort and unobstructed view of the scanning area.
   :name: open-bore MRI scanner

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

standardBoreMRIScanner
----------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/standardBoreMRIScanner
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: A 'standard-bore MRI scanner' is a closed high-field scanner which features a magnet surrounding the patient creating a capsule-like space where the patient lies on.
   :name: standard-bore MRI scanner

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

vibratingMicrotome
------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/vibratingMicrotome
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: A 'vibrating microtome' is an mechanical instrument with a vibrating steel blade used to cut (typically) biological specimens into thin segments for further treatment and ultimately microscopic or histologic examination.
   :interlexIdentifier: http://uri.interlex.org/base/ilx_0780522
   :name: vibrating microtome

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

wideBoreMRIScanner
------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/deviceType/wideBoreMRIScanner
   :@type: https://openminds.om-i.org/types/DeviceType
   :definition: A 'wide-bore MRI scanner' is a closed high-field scanner which features a widened bore compared to the standard-bore MRI scanner.
   :name: wide-bore MRI scanner

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

