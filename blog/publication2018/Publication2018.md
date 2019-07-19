## MolecularMatch Publications 2019 Update

Publication search has expanded in importance in recent years at MM due to our in-house curation requirements and necessity to assert all recommendations with [literature evidence](https://api.molecularmatch.com/#aboutCompliance).

Our guiding philosophy of our search engines is to allow the user to enter a very wide variety of terms related to a case, and we surface the most relevant results in the top 10.

Publications are continually updated, scored, sorted, and MLA cited for you to easily incorporate into your products.

- [API Publication Search](https://api.molecularmatch.com/#publications)
- [API Assertions Search](https://api.molecularmatch.com/#assertions)
- [Publications.MolecularMatch.com](https://publications.molecularmatch.com)
- [Assertions.MolecularMatch.com](https://assertions.molecularmatch.com)

MolecularMatch indexes clinically relevant publications in several ways:

1. Weekly acquisition from PubMed from our cancer-related journals list
2. Mutation based acquisition from PubMed for journals outside of our list
3. Conference Meeting Abstracts (ASCO, AACR, ESMO)
4. Medical curator findings (in-house research)
5. NCCN Guideline cited publications
6. Custom additions of publications by users of our pathology software

Aggregating a large number of publications (850,000!) is only half the battle. To ensure relevancy to patient cases, a great deal of further technology automation and human curation is required.

---------

### Scoring System Explained

Our Publications, like Trials, Drugs and Assertions, are accessed through our search endpoints, and returned sorted based on a highly advanced scoring system. Through extensive testing with M.D. and Ph.D. oversight, we've settled on a publication search engine that is most likely to have results relevant to your case in the top 10. For clinical uses, this a big improvement over other search engines like Google Scholar and Web of Science.

Scores are made up of a combination of intrinsic and extrinsic values. Intrinsic score comes automatically on the target. The extrinsic is calculated in at search time based on your input.

The intrinsic score on a publication has several factors:

1. Journal Impact Factor
2. Number of citations (PubMed Central citation count)
3. Number of assertions within MM where curators added this publication
4. Number (and quality) of evidence items in CIViCdb.org referencing this publication
5. Publication Types (scores adjust up or down)
6. Trial Types (scores adjust up or down)

The extrinsic score of publications is calculated when matching your search criteria to information on the abstract. For example, terms matched in the title are given more score than terms found lower in the abstract, like in the methods.

#### Publication Types and Trial Types for score adjustments

Publications get automatically, or manually, assigned types. Types influences the intrinsic score.

The highest scoring publications will be those of clinical utility. That is if they correspond to clinical trials (higher phases scoring higher), interventional treatments, practice guidelines, case studies, consensuses, etc. And lower scoring publications that have to do with animal models, cell-line, observational research only, etc.

Publication ranking has been validated through hundreds of test suites. Test suites are basically patient cases (gene + condition), and we use them to check and adjust the ranking of publications so that the most relevant come up first.

---------

### Journals

We will acquire any publication from any journal if it is relevant to cancer conditions and mutations that we index. Though some journals are automatically imported.

Journals automatically imported (as of July 2019):

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
- British journal of cancer
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
- Cell biochemistry and biophysics
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
- European urology
- Frontiers in oncology
- Gastric cancer : official journal of the International Gastric Cancer Association and the Japanese Gastric Cancer Association
- Genes & cancer
- Haematologica
- Human pathology
- ISRN oncology
- International journal of clinical oncology
- International journal of radiation oncology, biology, physics
- JAMA
- JAMA oncology
- Journal of Cancer
- Journal of cancer research and clinical oncology
- Journal of clinical oncology : official journal of the American Society of Clinical Oncology
- Journal of hematology & oncology
- Journal of neuro-oncology
- Journal of oncology
- Journal of the National Cancer Institute
- Journal of the National Comprehensive Cancer Network : JNCCN
- Journal of thoracic oncology : official publication of the International Association for the Study of Lung Cancer
- Journal of translational medicine
- Lancet (London, England)
- Leukemia
- Leukemia & lymphoma
- Leukemia research
- Leukemia research reports
- Lung cancer (Amsterdam, Netherlands)
- Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc
- Molecular & cellular proteomics : MCP
- Molecular and clinical oncology
- Molecular cancer
- Molecular cancer research : MCR
- Molecular cancer therapeutics
- Molecular carcinogenesis
- Molecular cell
- Molecular cell biology research communications : MCBRC
- Molecular oncology
- Nature cell biology
- Nature clinical practice. Oncology
- Nature communications
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
- PloS one
- Science (New York, N.Y.)
- Science signaling
- Science translational medicine
- Scientific reports
- The Journal of molecular diagnostics : JMD
- The Lancet. Oncology
- The New England journal of medicine
- Tumour biology : the journal of the International Society for Oncodevelopmental Biology and Medicine
- Urologic oncology
