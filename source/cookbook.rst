.. header:: TechNES AI Best Practices Group: 

Executive Summary
=============================

Artificial Intelligence (AI) and Machine Learning (ML) technologies are key to
many modern engineering projects due to their ability to solve many problems
that are difficult or impossible with other methods. While most engineers will
find themselves enjoying a significant overlap between these techniques and
their existing skill set, they are also liable to find that AI and Machine
Learning is its own field with its own unique demands and (often hidden)
pitfalls. While there are many resources available for self teaching, it is
generally assumed the practitioner is either an absolute beginner to
engineering, or already a seasoned expert in AI and ML. In this document, we
provide a practical guide to AI and Machine learning for  electronic systems
engineers who already have a strong base of knowledge in electronic systems but
no specialized expertise. This guide will be practice focused, with the goal of
helping engineers to make good decisions and avoid problems. The guide will
cover, among many others areas:

* Preliminary problem assessment
* Data collection
* Pipelining
* Testing and Validation
* Privacy and Security
* Ethical and Legal considerations



Target Audience
===============
The target audience for this guide is electronic systems engineers with little
to no specific expertise in AI and Machine Learning techniques. It will be
assumed, because of this background, that readers will have a base level of
competence in programming and mathematics, though the guide will err on the side
of caution in respect of assumed knowledge. We may, for example, assume our
reader has knowledge of concepts in basic calculus, but are unlikely to assume
that they are able to remember any specific formula. We are also assuming that
the primary interest in practically deploying these techniques rather than
understanding the theory and context of their development. For readers
interested in a more theoretical treatment, we list several texts in the
resources section appropriate to a range of different levels of background
knowledge.

Using this Guide
================
This guide provides a preamble discussing the key issues in each section,
followed by a questionnaire for each section dictating, for each AI risk and
privacy level, key steps to take. Where AI and Privacy levels are both
specified, you must fulfill this requirement if you meet either of these
specifications. 

In terms of structure, this guide specifies several different categories of
requirements. Creating an effective AI project is an iterative process, and it
is not intended that the ordering of the requirements specifies a strong order
in which to tackle the requirements, beyond the obvious (e.g. we must collect
the data before we can do anything with it). The only exception to this is the
Preliminary Assessment that forms the first step of any project, and establishes
the AI and Privacy risk levels discussed below. 

AI Risk Levels
--------------
One of the key concepts leveraged in this guide in order to provide an
appropriate level of risk management to AI is the classification of different AI
applications into different risk categories. This framework strongly mimics the
approach proposed in the upcoming EU Artificial Intelligence act, and defines
four categories of risk for AI:

* Unacceptable risk. Applications that are a clear threat to the safety,
  livelihoods or rights of people.
* High risk. Applications that are critical to the safety or wellbeing of
  people, that require special mitigations to adequately cover the risks they
  pose 
* Limited risk. Applications with lower impacts to safety or wellbeing, but
  which still require some level of mitigation 
* Minimal or no risk. Applications with minimal to zero risk. 
* We define these terms in more detail, with examples, in the appendix.

The framework this guide provides dictates different requirements according to
each category.

Privacy Risk Levels
-------------------
The other key concepts used in this guide are privacy and security requirements.
As data driven methods, AI and Machine Learning algorithms have the potential to
pose significant risks in these areas. We define three levels of privacy and
security requirements:

* High risk. Applications that deal with personal data that may pose a risk to
  the safety or wellbeing of people
* Limited risk. Applications that deal with personal data with lower impacts to
  safety or wellbeing, but which still require some level of mitigation 
* Minimal or no risk. Applications that either do not deal with personal data,
  or do so with minimal to zero risk. 


Preliminary Assessment
======================
In order to usefully realize the content of this guide, the AI and Privacy risks
that the project poses need to be defined. To do this, we need to undertake
several preliminary steps to define the project.

The very first step is to establish that AI and Machine Learning algorithms are
an effective and suitable approach to the proposed problem. The goals of the
project should be reviewed in the context of what AI and Machine Learning
algorithms can achieve, and compared to other (non AI) approaches. Simpler
approaches may lead to comparable or better results, without the overhead of
managing an AI and Machine Learning project. 

The next step is to scope out the goals and requirements of the proposed product
in the context of the business constraints it is subject to. Given the
challenges of validating AI approaches, it is imperative to define clear,
specific goals for the project. When the goals and requirements of the proposed
project have been established, well defined metrics of what success in achieving
these goals will look like need to be created. 

Once these goals and metrics are defined, it is then appropriate to undertake a
risk assessment of the project. This risk assessment should, without exception,
inform a fair assessment of the AI risk and privacy risk category that the
proposed projects outcomes fall into.


+--------------------+----------+-----------+--------------+----------+
|    Requirement     | Evidence |  AI Risk  | Privacy Risk | Complete |
+====================+==========+===========+==============+==========+
| Assess alternative | -        | Mandatory | Mandatory    | -        |
| approaches         |          |           |              |          |
+--------------------+----------+-----------+--------------+----------+
| Risk Assessment    | -        | Mandatory | Mandatory    | -        |
+--------------------+----------+-----------+--------------+----------+
| Risk Categories    | -        | Mandatory | Mandatory    | -        |
+--------------------+----------+-----------+--------------+----------+

Data Collection
===============
Establishing a data collection pipeline is an iterative process that requires
careful consideration of factors that may impact data quality and introduce
sampling biases. It's important to explore the data to identify interesting
patterns and problems early on, but this must be done carefully to avoid
introducing biases. The risk level and privacy requirements of the AI
application may dictateadditional steps, including a risk assessment,
appropriate mitigation strategies, and screening data for biases.


+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Requirement                                                       | Evidence | Risk Requirement | Privacy Requirement | Complete |
+===================================================================+==========+==================+=====================+==========+
| Establish the goals that the data collection process is achieving | -        | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Select target data                                                | -        | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Target data quality analysis                                      | -        | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Establish data quantization process                               | -        | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Create data quality checks                                        | -        | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Create data collection process                                    | -        | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Create data pre-processing pipeline                               |          | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Establish infrastructure for storing raw data                     |          | High             | None                |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Data biases and discrimination analysis                           |          | High             | None                |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Data collection harm risk assessment                              |          | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Data collection harm risk mitigation strategy                     |          | High             | Moderate            |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Data is anonymised                                                |          | High             | High                |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Data transmitted during the collection process must be encrypted  |          | High             | High                |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Data must be secured after collection                             |          | High             | High                |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+

Requirements
------------

Creating target dataset
+++++++++++++++++++++++
The first step of the preliminary assessment was to create an overarching goal
and corresponding set of tangible, measurable outcomes. In data collection, our
first step is to establish the data that we need to achieve these goals. To do
this, we need to understand what good data is in the context of our desired
outcomes, and to temper this with what is realistically achievable.

Good data is, first and foremost, the data that leads us to our desired
outcomes. Important considerations are:

* Accuracy
    * Does the data accurately measure the quantity of interest?
* Completeness
    * Does the dataset represent a complete view of all data points of interest?
    * Does it have more data about some quantities than others? Should it?
* Relevance
    * To what extent is the collected data relevant to the measure of interest?
* Missingness
    * Are there missing values in the data?
* Timeliness
    * Is the data still relevant now?
* Subjectivity
    * AI methods are fundamentally quantitative, and deal best with quantitative data
* Attainability
    * Is it realistic to obtain the data in the quantities required?
* Standardization
    * Is the data collectable/attainable in a standardized format amenable to computation


It’s unlikely that we will be able to establish a perfect dataset, and the
quality of the collected data will significantly affect subsequent steps that
consume it. The purpose of this step is therefore to establish both what a
realistic and useful set of data to collect, and to inventory the limitations of
this same data to anticipate later risks and problems. For example, missing
data, depending on how that missingness manifests, might be either a non-issue
or a serious problem. If it manifests as a problem, an appropriate mitigation
might be data imputation.

To complete the outcome of this step, fill out the following questionnaire.

Create automated data quality checks
++++++++++++++++++++++++++++++++++++

In the Create Target Dataset step, we established a measure of the potential
limitations of our dataset. In this step, we establish a process for monitoring
the level that these problems manifest in our data. 

This should be achieved algorithmically in almost all instances. Where this is
not possible, it is imperative that any decision making process is recorded as
clearly as possible, with any persons involved in the process recorded. 

The output of this step is a document detailing how each of the limitations
identified in the previous step can be automatically monitored in collected
data. 
Create data collection process
Having established the target data, the next major step is to establish a
process by which the data can be collected. 

Before considering the details of how to achieve this, an important preliminary
step is to consider where the data is going to be stored. In all applications,
it is an extremely good idea to store raw data forever. For high AI risk
applications, storing (and keeping) the raw data should be considered mandatory. 

This step is likely to end up revealing additional limitations in the dataset.

Establish data storage
++++++++++++++++++++++
Create data pre-processing pipeline
Raw data will almost universally require pre-processing before integration into
any AI pipeline.

This should be achieved algorithmically in almost all instances. Where this is
not possible, it is imperative that any decision making process is recorded as
clearly as possible, with any persons involved in the process recorded. 
Data biases and discrimination analysis
In high AI risk applications, biases in the training dataset may cascade into
discriminative or other harmful outcomes for the project as a whole. 

It is not usually feasible to remove all biases from a dataset. Indeed, even
removing direct references to characteristics may not be enough to remove biases
associated with them. For example, a hiring AI trained on gender-biased data
will continue to be gender-biased even when direct references to gender are
removed, by identifying proxy identifiers (e.g. female-only colleges)[].

This step is about identifying and cataloging potential biases in the data.
Some of the biases identified may be able to be (and should be) mitigated at
this early stage. Others may not be feasible to tackle until later steps. 
Data collection ethics
In some applications, especially those involving human factors, the data
collection process may have the potential to cause harm. The nature of
collecting health data by assessing volunteers, for example, may come with risks
to their wellbeing. 

These potential problems should be cataloged and risk assessed.

Data is anonymised
++++++++++++++++++
All collected data should be stripped of personal identifying information.

This can be more challenging than it may first appear. It is not always
sufficient to remove directly identifiable data. Classically, 87% of the US
population can be uniquely identified by zip code, gender and date of birth.
Fully mitigating this issue may require steps to be taken further down the line. 

This step requires data to be stripped of all directly identifying personal
information, and a risk assessment of non-directly identifying data. 

Data transmitted during the collection process must be encrypted
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
All data collected should be fully encrypted from the point of collection to
the point of storage.

Data must be secured after collection
+++++++++++++++++++++++++++++++++++++
Data must be fully secured after collection. Data should be secured by an
access control system. Data should only be accessible to those that need it. 



Pipelining
===============

Pipelining is the process of creating a set of sequential steps that orchestrate
the flow of data, all the way from the extraction of the raw data to the final
output of the model. This section covers the practical aspects of designing and
maintaining such a construct.

Designing a pipeline is fundamentally a software engineering problem, and
typical software engineering best practices are all appropriate here. Data
pipelines should be version controlled, different concurrent versions of the
code should be siloed into different branches with appropriate restrictions on
who can change them, and updates to the pipeline should be peer reviewed.
Testing is also very important, so much so that it has its own later section in
this guide dedicated to it. 

In a similar vein, maintaining comprehensive documentation and logging are a
significant part of creating and maintaining an AI pipeline. This is especially
important in AI and Machine Learning projects that have any significant AI risk
or privacy risks, which might be called to account for the processes that go
into their decision making.

Hardware considerations are also a significant part of pipelining, especially
for projects at a large scale. Data pipelines may significantly expand any
storage requirements for raw data, prompting decisions about data storage at
scale. Larger projects may make it desirable or necessary to orchestrate data
pipelining across multiple machines. This requires these machines to be sourced,
and prompts the question of how this orchestration is going to happen. 

One often desirable decision is to have some, or all, data pipelining to happen
in the cloud. While this can be advantageous, transferring data and compute
outside of your direct custody can be problematic. Additional steps will need to
be taken for pipelines that advantage cloud computing, especially those with
high AI or, especially, privacy risks.

+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Requirement                                                       | Evidence | Risk Requirement | Privacy Requirement | Complete |
+===================================================================+==========+==================+=====================+==========+
| Establish version control system                                  | -        | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Separate project into branches                                    | -        | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Define permissions on version control structure                   | -        | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Establish peer review process                                     | -        | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Establish documentation process                                   | -        | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Establish logging process                                         | -        | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Create data pre-processing pipeline                               |          | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Define data storage requirements                                  |          | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Establish distributed computing requirements                      |          | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Cloud data harm risk mitigation strategy                          |          | Mandatory        | Mandatory           |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Data is anonymised                                                |          | High             | High                |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Data transmitted during the collection process must be encrypted  |          | High             | High                |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+
| Data must be secured after collection                             |          | High             | High                |          |
+-------------------------------------------------------------------+----------+------------------+---------------------+----------+


Testing
===============

Testing AI and Machine Learning algorithms is the process of designing an
automated set of tests to make sure our algorithms are behaving correctly. The
process is extremely similar to testing in software engineering. In this
section, we describe how to test these algorithms covering, in turn, general
software testing principles, and the special considerations of AI and Machine
Learning Algorithms. 

AI and Machine Learning has no exemption from normal software engineering best
practices. Testing should be fully automated. We should have unit tests for
individual units of functionality, integration tests of how these fit together,
and system tests of wider functionality. There should be a suite of regression
tests to ensure that new additions and changes don’t introduce regressions of
bugs in performance in the existing code. Tests should be clearly written and
documented and have well defined pass and failure conditions.

It is important to understand when designing these tests that performance on
the data the algorithms have been trained on (training data), does not reflect
performance in general. Algorithms specialize to their training data, and will
perform better on this data than they will in general. To mitigate this, it is
sufficient to have testing split the data into sets, and ensure that training
and testing occur separately. Two sets is often sufficient, but sometimes
additional splits will be needed. In the cases in which we wish to tune the
hyperparameters of an algorithm, for example, we will need a further split
(often called a validation set in this case) to evaluate the performance of this
tuning. 

Unlike testing in many other software applications, the testing for AI and
Machine Learning algorithms often requires continuous attention, even in the
absence of changes to the software. Especially when human factors are involved,
it is not uncommon for data collected over time to observe patterns and concepts
drifting or changing. It’s important to understand the risk of this in any
project, and to monitor key performance indicators to track this. Without doing
this, it is difficult to be able to distinguish drops in performance and
failures in tests caused by this drift from real errors caused by mistakes.

For high AI risk or privacy risk applications, there are additional burdens in
testing in order to fulfill the requirements dictated. High AI risk applications
must demonstrate how threats to wellbeing and safety are mitigated. High privacy
risk applications must similarly test for appropriate classes of privacy
violations. 
