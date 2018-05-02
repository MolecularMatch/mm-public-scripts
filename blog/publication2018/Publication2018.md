## MolecularMatch Publications 2018 Update

Publication search has expanded in importance in recent years at MM due to our in-house curation requirements and necessity to assert all recommendations with literature evidence. Our main goals with our search engines is to allow the user to enter a very wide variety of terms related to a case, and for us to surface the most relevant results in the top 10.

Evidence grading: https://api.molecularmatch.com/#tieringTemplate

Continually updated, scored and sorted, and cited for you to easily incorporate into your products.

- [API Publication Search](https://api.molecularmatch.com/#publications)
- [API Assertions Search](https://api.molecularmatch.com/#assertions)
- [Publications.MolecularMatch.com](https://publications.molecularmatch.com)
- [Assertions.MolecularMatch.com](https://assertions.molecularmatch.com)

MolecularMatch indexes clinically relevant publications in several ways:

1. Weekly acquisition from PubMed for certain journals (see bottom)
2. Mutation based acquisition from PubMed for journals outside of list
3. Conference Meeting Abstracts (ASCO, AACR)
4. Medical curator findings
5. NCCN Guideline cited publications
6. Custom additions of pubs we were missing by users of our pathology software

Aggregating a large number of publications (450,000!) is only half the battle. To ensure relevancy to patient cases, a great deal of further technology automation and human curation is required.

---------

### Scoring System Explained

Our Publications, like Trials, Drugs and Assertions, are accessed through our search endpoints, and returned sorted based on a highly advanced scoring system. Through extensive testing with M.D. and Ph.D. oversight, we've settled on a publication search engine that is most likely to have results relevant to your case in the top 10.

Scores are made up of a combination of intrinsic and extrinsic values. Intrinsic score comes automatically on the target. The extrinsic is calculated in at search time based on your input.

The intrinsic score on a publication has several factors:

1. Journal Impact Factor
2. Number of citations
3. Number of assertions within MM where curators added this publication
4. Number of evidence items in CIViC referencing this publication
5. Publication Types (scores adjust up or down)

The extrinsic score of publications is calculated when matching your search criteria to information on the abstract. For example, terms matched in the title are given more score than terms found lower in the abstract, like in the methods.

##### Publication Types and their score adjustments

Publications get automatically, or manually, assigned a type. This type influences the intrinsic score.

- In patients  **25 points**
- Clinical Trial  25
- Expert Reviewed Recommendation Paper  15
- Case Study  3
- Practice Guideline  2
- Consensus Development Conference  2
- Rationale and design  -5
- mouse model  -5
- Webcasts  -5
- Editorial  -5
- Cell-line  -10
- In-vitro  -10
- Quality of Life  -10
- Comment  -10
- Letter  -10
- Historical Article  -10
- Biography  -10
- Patient Education Handout  -10
- Video-Audio Media  -10
- Classical Article  -10
- Observational Study  -10
- Drosophila  -10
- Method paper  -20
- Retracted Publication  -50

---------

Journals automatically imported (as of April 2018):

- Advances in cancer research
- American Society of Clinical Oncology educational book / ASCO. American Society of Clinical Oncology. Meeting
- American journal of cancer research
- American journal of clinical oncology
- Annals of oncology : official journal of the European Society for Medical Oncology / ESMO
- Annals of surgical oncology
- BMC cancer
- Biochemical pharmacology
- Blood
- Blood cancer journal
- Breast cancer research and treatment
- Cancer
- Cancer biology & therapy
- Cancer cell
- Cancer discovery
- Cancer genetics
- Cancer immunology, immunotherapy : CII
- Cancer letters
- Cancer research
- Cancer science
- Cancers
- Carcinogenesis
- Case reports in oncology
- Cell growth & differentiation : the molecular biology journal of the American Association for Cancer Research
- Cell reports
- Cell stem cell
- Cellular immunology
- Cellular oncology : the official journal of the International Society for Cellular Oncology
- Clinical breast cancer
- Clinical cancer research : an official journal of the American Association for Cancer Research
- Clinical lymphoma, myeloma & leukemia
- Critical reviews in oncology/hematology
- Current cancer drug targets
- European journal of cancer (Oxford, England : 1990)
- Frontiers in oncology
- Gastric cancer : official journal of the International Gastric Cancer Association and the Japanese Gastric Cancer Association
- Genes & cancer
- ISRN oncology
- International journal of clinical oncology
- International journal of radiation oncology, biology, physics
- JAMA
- JAMA oncology
- Journal of cancer research and clinical oncology
- Journal of clinical oncology : official journal of the American Society of Clinical Oncology
- Journal of hematology & oncology
- Journal of neuro-oncology
- Journal of oncology
- Journal of the National Cancer Institute
- Journal of the National Comprehensive Cancer Network : JNCCN
- Journal of thoracic oncology : official publication of the International Association for the Study of Lung Cancer
- Lancet (London, England)
- Leukemia
- Leukemia & lymphoma
- Leukemia research
- Leukemia research reports
- Lung cancer (Amsterdam, Netherlands)
- Molecular & cellular proteomics : MCP
- Molecular and clinical oncology
- Molecular cancer
- Molecular cancer research : MCR
- Molecular cancer therapeutics
- Molecular cell
- Molecular cell biology research communications : MCBRC
- Molecular oncology
- Nature cell biology
- Nature clinical practice. Oncology
- Nature reviews. Cancer
- Nature reviews. Clinical oncology
- Nature reviews. Molecular cell biology
- Neuro-oncology
- Oncogene
- Oncology
- Oncology (Williston Park, N.Y.)
- Oncology letters
- Oncotarget
- Pathology oncology research : POR
- Pediatric blood & cancer
- Science (New York, N.Y.)
- Science signaling
- Science translational medicine
- The Lancet. Oncology
- The New England journal of medicine
