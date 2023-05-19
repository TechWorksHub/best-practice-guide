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
helping engineers to make good decisions and avoid problems. 

The guide will cover, in order:

* Should I AI?
* Defining the Project
* Collecting Data
* Training your AI Application
* Deploying your AI Application
* Testing your AI Application



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
This guide is laid out as a series of steps taking you from conceptualizing your
AI application through to deploying it in the real world. These steps are broken
into sections, and set out in the order they should be initially considered.
It’s strongly suggested you don’t “skip ahead” to later steps from earlier ones.
However, it is expected reviewing later sections may prompt you to reevaluate
previous decisions and return to earlier steps.

Each step discusses a problem to be solved, what needs to be done to solve it,
and what evidence needs to be provided to support this. The steps are enumerated
in a table available in each section, to be filled in as the steps are worked
through. The table lists 3 columns. The first lists the name of the requirement.
The second is for recording the evidence supporting the fulfillment of the
requirement, and the third is a checkbox to note when the requirement has been
completed. An example table with the first requirement filled out is below:

+-----------------------+------------------------------------------+----------+
| Requirement           | Evidence                                 | Complete |
+=======================+==========================================+==========+
| Example requirement 1 | Example Risk Assessment.pdf,             | Yes      |
|                       | Example document.pdf                     |          |
+-----------------------+------------------------------------------+----------+
| Example requirement 2 | -                                        | -        |
+-----------------------+------------------------------------------+----------+
| ...                   | -                                        | -        |
+-----------------------+------------------------------------------+----------+


Not every part of every step will need to be fulfilled for every application.
Some applications may pose their own classes of problems that will need to be
dealt with separately. We discuss these below.

Application Specific Requirements
---------------------------------

AI Risk
++++++++

Direct regulation of AI in the EU is tending to a risk based approach examining
the harm of AI applications to people. Applications are classified into risk
categories, and those that pose a high risk are to be subject to more stringent
requirements. These categories are currently:

* Unacceptable risk. Applications that are a clear threat to the safety,
  livelihoods or rights of people.
* High risk. Applications that are critical to the safety or wellbeing of
  people, that require special mitigations to adequately cover the risks they
  pose 
* Limited risk. Applications with lower impacts to safety or wellbeing, but
  which still require some level of mitigation 
* Minimal or no risk. Applications with minimal to zero risk. 

Providing guidance on any upcoming or current legislation is out of the scope of
this guide. However, this categorization of the risk that AI applications pose
is a useful tool for discussing best engineering practices. These risk levels
will recur in this guide, and we will refer to them as AI Risk. 

Data Protection
+++++++++++++++

AI models are data driven. This leaves them significantly subject to data
protection regulation, especially GDPR. According to GDPR, if you process data,
you have to do so according to seven protection and accountability principles:

* Lawfulness, fairness and transparency — Processing must be lawful, fair, and
  transparent to the data subject.
* Purpose limitation — You must process data for the legitimate purposes
  specified explicitly to the data subject when you collected it.
* Data minimization — You should collect and process only as much data as
  absolutely necessary for the purposes specified.
* Accuracy — You must keep personal data accurate and up to date.
* Storage limitation — You may only store personally identifying data for as
  long as necessary for the specified purpose.
* Integrity and confidentiality — Processing must be done in such a way as to
  ensure appropriate security, integrity, and confidentiality (e.g. by using
  encryption).
* Accountability — The data controller is responsible for being able to
  demonstrate GDPR compliance with all of these principles.

There are also certain categories of data that must be given special
consideration. Providing guidance on legislation remains out of the scope of
this guide. However, once again, the ideas put forward in GDPR are important in
framing the discussion of best engineering practices, and will recur in this
guide.

Safety, Security and Robustness
+++++++++++++++++++++++++++++++

A core requirement of any system is that it functions correctly, both in
conditions of normal use, as well as conditions of misuse (intentional or
otherwise), or other adverse conditions. An AI system should be:

* Safe: either functioning correctly or failing safely in all conditions
* Secure: resilient against misuse or abuse (intentionally or otherwise), and
* Robust: ensuring functionality in as wide a range of conditions as possible

While the need to meet these challenges is not unique to AI systems, AI systems
bring several unique problems to each of these areas. For example:

* Safety is a continual challenge in AI systems that are fundamentally
  statistical. Guaranteeing safe behavior in the wide range of situations an
  automotive AI may encounter, for example, remains a continuous challenge. 
* AI models present unique attack surfaces that must be secured. For example,
  in many situations, models will leak information about the data that they were
  trained on.
* Similarly, AI models struggle to robustly deal with novel data outside of
  their training set. This can both cause problems in normal use, and be
  exploited by attackers.

Safety, security and robustness will be important ideas throughout this document.

Transparency and Explainability
+++++++++++++++++++++++++++++++

Another core requirement of any system is that we can understand how it
functions. This imperative should be familiar to any electronic systems
engineer, through the value of clear code and documentation. We use two terms to
describe these requirements:

* Transparency: the communication of appropriate information about an AI system
  to relevant people (for example, information on how, when, and for which
  purposes an AI system is being used), and
* Explainability: the extent to which it is possible for relevant parties to
  access, interpret and understand the decision-making processes of an AI system

Many AI systems are uniquely troublesome in these respects. Many common methods,
such as Neural Networks are effectively “black boxes”. These methods provide a
solution, but through a means that is ultimately not human interpretable. 

Fairness
++++++++
Fairness is another core requirement of any system, especially in light of the
above ideas of transparency and explainability. By fairness, we mean a system
that:

Does not undermine the legal rights of individuals or organizations,
discriminate unfairly against individuals or create unfair market outcomes. 

Fairness is a challenge in AI systems that learn from data. The decisions these
systems make are a reflection of the patterns in the data they are trained on.
If the data is biased, the systems trained on them will also be biased. This has
been proven expensively and at length in the real world, for example through
attempts at creating criminal justice AI or hiring AI.

Accountability and Governance
+++++++++++++++++++++++++++++
Any system that has the potential to cause harm requires oversight. Any AI
system will therefore require systems of:

* Governance, a framework for managing the development, deployment and operation
  of AI
* Accountability, clear lines of responsibility for all aspects of the AI
  applications

The full scope of requirements is unlikely to be fully addressed by engineering.
Nonetheless, these principles are important in the greater context of the AI
application, and will be an important part of development. 

Contestability and Redress
++++++++++++++++++++++++++
Any system that has the potential to cause harm also requires ways for this harm
to be recognised and reversed. Any AI system will therefore require systems of:

* Contestability, those who may be adversely affected must have a route to
  contest decisions or outcomes
* Redress, there must be a system in place to assess these concerns, and redress
  the affected party when necessary

The full scope of requirements is unlikely to be fully addressed by engineering.
Nonetheless, these principles are important in the greater context of the AI
application, and will be an important part of development.


Should I AI?
======================
Developing an AI application can present significant challenges. Collection of
data is burdensome. Testing and validation are problematic. As seen in the
previous section, many applications of AI will come with special requirements
that can be a challenge in themselves. To address this, the very first step in
this guide is to be able answer the following: should I use AI to solve my
problem? This greater question is broken down into 3 sub questions to be
completed.

+------------------------------+----------+----------+
| Requirement                  | Evidence | Complete |
+==============================+==========+==========+
| Evaluate engineering case    | -        |          |
+------------------------------+----------+----------+
| Initial AI Risk Assessment   | -        |          |
+------------------------------+----------+----------+
| Initial Data Risk Assessment | -        |          |
+------------------------------+----------+----------+

Defining the Project
======================
The next step is to scope out the goals and requirements of the proposed product
in the context of the constraints it is subject to. There are two steps here.
Firstly, defining a clear set of goals and metrics for success. Secondly,
undertaking a more complete risk assessment of the project, including a full
assessment of the AI risk of the project, and any risks around the data likely
to be required. 

+------------------------------+----------+----------+
| Requirement                  | Evidence | Complete |
+==============================+==========+==========+
| Establish Goals              | -        |          |
+------------------------------+----------+----------+
| Risk Assessment              | -        |          |
+------------------------------+----------+----------+

Collecting Data
===============
One of the requirements of any AI application is that it is data driven. This
usually means that you will need to collect some data, or at the very least to
process some. It’s very important to get this right, as the strength of the data
will have a strong effect on the efficacy of training and deploying our AI
application. Our primary challenges are:

* Making sure the data we’re collecting contains the information we’re
  interested in
* Making sure our data is in a form easily understood by potential AI algorithms
* Making sure our infrastructure and collection process is robust


+-----------------------------------------+----------+----------+
| Requirement                             | Evidence | Complete |
+=========================================+==========+==========+
| Create a Target Dataset                 | -        |          |
+-----------------------------------------+----------+----------+
| Eatsblish a Data Quantization Process   | -        |          |
+-----------------------------------------+----------+----------+
| Automate Data Quality Checking          | -        |          |
+-----------------------------------------+----------+----------+
| Create a Data Collection Process        | -        |          |
+-----------------------------------------+----------+----------+
| Automate Data Cleaning                  | -        |          |
+-----------------------------------------+----------+----------+
| Data Biases and Discrimination Analysis | -        |          |
+-----------------------------------------+----------+----------+
| Data Anonymization                      | -        |          |
+-----------------------------------------+----------+----------+
| Data Transmission Safety                | -        |          |
+-----------------------------------------+----------+----------+
| Data Security                           | -        |          |
+-----------------------------------------+----------+----------+

Training your AI Application
============================

Our next step is to train our AI application on the data collected in the last
step. This step is about three things:

* Establishing which AI approach we’re going to use
* Engineering a pipeline to train our approach in the best possible way
* Checking this training results in an AI algorithm that does all the things it
  should, and none of the things it shouldn’t

+------------------------+----------+----------+
| Requirement            | Evidence | Complete |
+========================+==========+==========+
| Training Requirement 1 | -        |          |
+------------------------+----------+----------+
| Training Requirement 2 | -        |          |
+------------------------+----------+----------+
| Training Requirement 3 | -        |          |
+------------------------+----------+----------+
| ...                    | -        |          |
+------------------------+----------+----------+

Deploying your AI Application
=============================

Testing your AI Application
===========================

Task list
=========

Should I AI?
------------

Evaluate Engineering Case
+++++++++++++++++++++++++

AI is a powerful tool in many applications, but it may not be immediately
appropriate for the problem you are trying to solve. This step requires the
enumeration and assessment of available alternative approaches to solving the
problem.

In this step, you should consider at least the following:

* Is it possible to solve the problem without using a data driven approach?

  * What are the benefits and consequences of doing this?

* Is it possible to solve the problem using a data driven approach without
  learning? What are the benefits and consequences of doing this?

  * For example, clickthrough rate is likely to be a very good way of ranking
    the effectiveness of an advert. A fairly effective spam filter may be to
    simply block a list of domains known for producing spam.

To complete this step, at least both of these questions should be answered.

Assess AI Risk
++++++++++++++
In the Using This Guide section, we defined AI risk in several categories:
Unacceptable, High, Limited, and Minimal. An important question to answer at
this early stage is whether your application is likely to fall into the
Unacceptable category. These are applications that are a clear threat to the
safety, livelihoods or rights of people. Examples include:

* AI systems using subliminal techniques, or manipulative or deceptive
  techniques to distort behavior
* AI systems exploiting vulnerabilities of individuals or specific groups
* Biometric categorization systems based on sensitive attributes or
  characteristics
* AI systems used for social scoring or evaluating trustworthiness
* AI systems used for risk assessments predicting criminal or administrative
  offenses
* AI systems creating or expanding facial recognition databases through
  untargeted scraping
* AI systems inferring emotions in law enforcement, border management, the 
  workplace, and education

At this stage, you may not have fully fleshed out the scope of your application.
Nonetheless, this initial assessment is important to pre-empt these risks. If
your application falls into this category, it may not be appropriate to develop.
To complete this step, a categorisation of the proposed project into
unacceptable or not should be created, along with a justification.  

Assess Data Risk
++++++++++++++++
In the Using this Guide section, discussed how data protection principles fall
into best practices. In this section, we evaluate the practicality of collecting
the type of data we’re likely to be required for our project in the light of
these principles. 

At this early stage, it’s unlikely that the full scope of the dataset required
will have been set out. Nonetheless, it is important to get a good understanding
of whether collecting the data required for the proposed project is likely to be
practicable. The questions that need to be answered in this step are:

* What personal data am I likely to need to collect for my application?
* What restrictions might there be on collecting this data?

To complete this step, provide answers to the two above questions.


Defining the Project
--------------------

Establish goals
+++++++++++++++

Risk Assessment
+++++++++++++++

Collecting Data
---------------

Create a Target Dataset
+++++++++++++++++++++++
The first step of the preliminary assessment was to create an overarching goal and corresponding set of tangible, measurable outcomes. In data collection, our first step is to establish the data that we need to achieve these goals. To do this, we need to understand what good data is in the context of our desired outcomes, and to temper this with what is realistically achievable.

Good data is, first and foremost, the data that leads us to our desired outcomes. Important considerations are:

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

  * AI methods are fundamentally quantitative, and deal best with quantitative
    data

* Attainability

  * Is it realistic to obtain the data in the quantities required?

* Standardization

  * Is the data collectable/attainable in a standardized format amenable to
    computation


It’s unlikely that we will be able to establish a perfect dataset, and the
quality of the collected data will significantly affect subsequent steps that
consume it. The purpose of this step is therefore to establish both what a
realistic and useful set of data to collect, and to inventory the limitations of
this same data to anticipate later risks and problems. For example, missing
data, depending on how that missingness manifests, might be either a non-issue
or a serious problem. If it manifests as a problem, an appropriate mitigation
might be data imputation.

Establish a data quantization process
+++++++++++++++++++++++++++++++++++++

In many instances, dealing with data involving some measure of subjectivity is
unavoidable. To avoid problems using such data in what are fundamentally
quantitative algorithms, it is important to establish a clear process for
converting this subjective data to quantitative measurement.

It is strongly preferable to do this quantisation algorithmically. Where this is
not possible, it is imperative that any decision making process is recorded as
clearly as possible, with any persons involved in the process recorded. 

The output of this step is a document listing all processes used to quantize
data.

Automate Data Quality Checking
++++++++++++++++++++++++++++++

In the Crate Target Dataset step, we established a measure of the potential
limitations of our dataset. In this step, we establish a process for monitoring
the level that these problems manifest in our data. 

This should be achieved algorithmically in almost all instances. Where this is
not possible, it is imperative that any decision making process is recorded as
clearly as possible, with any persons involved in the process recorded. 

The output of this step is a document detailing how each of the limitations
identified in the previous step can be automatically monitored in collected
data.

Create a Data Collection Process
++++++++++++++++++++++++++++++++

Having established the target data, the next major step is to establish a
process by which the data can be collected. 

Before considering the details of how to achieve this, an important preliminary
step is to consider where the data is going to be stored. In all applications,
it is an extremely good idea to store raw data forever. For high AI risk
applications, storing (and keeping) the raw data should be considered mandatory. 

This step is likely to end up revealing additional limitations in the dataset.
Record them.

Automate Data Cleaning
++++++++++++++++++++++

Raw data will almost universally require pre-processing before integration into
any AI pipeline.

This should be achieved algorithmically in almost all instances. Where this is
not possible, it is imperative that any decision making process is recorded as
clearly as possible, with any persons involved in the process recorded.

Data Biases and Discrimination Analysis
+++++++++++++++++++++++++++++++++++++++
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

Data Anonymization
++++++++++++++++++

All collected data should be stripped of personal identifying information.

This can be more challenging than it may first appear. It is not always
sufficient to remove directly identifiable data. Classically, 87% of the US
population can be uniquely identified by zip code, gender and date of birth.
Fully mitigating this issue may require steps to be taken further down the line. 

This step requires data to be stripped of all directly identifying personal
information, and a risk assessment of non-directly identifying data. 

Data Transmission Safety
++++++++++++++++++++++++
All data collected should be fully encrypted from the point of collection to the
point of storage.

Data Security
+++++++++++++
Data must be fully secured after collection. Data should be secured by an access
control system. Data should only be accessible to those that need it. 
