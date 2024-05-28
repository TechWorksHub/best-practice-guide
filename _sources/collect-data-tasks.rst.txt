How do I collect data for my AI/ML project: Task List
========================================================


:ref:`How do I collect data for my AI/ML project?`
--------------------------------------------------

.. _Collecting your Data Set:

:ref:`Collecting your Data Set<How do I collect data for my AI/ML project?>`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Defining the Plan
#################

The first step in creating our AI application is to create and (with caveats)
implement a plan to collect a dataset to drive your AI application. The plan
will include:

* What data you are going to collect
* Where/whom you are going to collect it from
* How you are going to do this

The best way to initially approach this is to approach it as you would any novel
software problem: do not reinvent the wheel and never build anything yourself
that you could fairly appropriate from somebody else. There are many free
datasets for a wide range of problems publicly available. Observe what types of
data others who are solving problems similar to you have collected, and what you
can learn about the datasets they used. It may be appropriate in the first
instance, and if a suitable dataset exists, to initially use a public dataset
and iterate. If you do use other datasets, do make sure you respect the licenses
that may come with them.

In most business cases, you will at some point end up collecting your own data.
Even if you don’t, it is important to be aware of what kind of data is desirable
for AI and machine learning, and what kind of data is not. When looking at
potential data, some key criteria to consider are:

* Accuracy

  * Does the data accurately measure a quantity you are interested in?
  * Not all data can be trusted. Data from questioning human participants
    for example, can be inaccurate and contradictory. 

* Completeness

  * Does the dataset represent a complete view of all data points of interest?
  * Does it have more data about some quantities than others? Should it?
  
    * Your models cannot learn from examples that are not in the data

* Relevance

  * To what extent is the collected data relevant to the measure of interest?
  * Including data that is only weakly relevant may cause more problems than it
    solves

* Missingness

  * Are there missing values in the data?
  * Distinct from completeness. Completeness is about overall coverage,
    missingness is about which bits of your collected data are not present. 

* Timeliness

  * Is the data still relevant now?

* Subjectivity

  * AI methods are fundamentally quantitative, and deal best with quantitative
    data
  
* Attainability

  * Can the data be realistically obtained (and in the quantities required)?

* Standardization

  * Is the data collectable/attainable in a standardized format amenable to 
    computation

What data you intend to collect is likely to be very tightly tied to where you
collect your data. The best source of data is usually the source that gives the
best data by the criteria we list above. This is not always the only
consideration though, it is also wise to consider:

* Licensing. This applies both if you’re using an existing dataset licensed by
  a third party (even a free one), or if your data might contain licensed work.
  As an example of the latter building a dataset of artwork may require you to
  consider the licenses of those artworks.
* Personal Data: classes of data (e.g., personal data) must be treated
  specially. More on this at the bottom of this section
* Special Cases: Depending on the data and end goal, you may be required to take
  additional steps in data collection. For example, data collected by
  experimenting on animals is likely to require extra licenses and oversight.

Implementing the Plan
#####################

We discussed supervised and unsupervised learning in the
:ref:`Establish Goals and KPIs<Establish Goals and KPIs>` section. If you are
dealing with a supervised learning problem (as is likely), the largest concern
of data collection is how the data can be labeled. In a supervised learning
application, we want to learn to predict some quantity from our data. To do
that, we need examples which match our data and that quantity together. For
example if we want an AI application that detects spam, we need to collect as
data a set of emails, and divide them up into two categories - spam or not.

Fundamentally, you have two choices of how to do this. Firstly, you can contrive
a way to achieve this automatically. If you are predicting how sales from your
website occur based on how people engage with it, it might be a fairly simple
affair for you to match these two bits of information up. Otherwise, if you can
not contrive a way to do otherwise, the data must be labeled manually, by hand.
For example, in a dataset of pictures of animals, the only way to effectively
know what animal is present in the picture is to get a human to decide. In
general, we wish to avoid this - for the purposes of this type of task, humans
are expensive, prone to error and hard to scale.

Other than this, the process of how you will collect your data is simply the
practical realization of what you have set out in the previous steps. Your focus
here is making the process as simple and replicable as possible. As a general
rule, the more automated the process can be, the better. Automated collection
processes scale better, and involving human factors in the collection process is
usually an excellent way to introduce an extra set of errors. Automated data
collection is not possible in every application though. If you do have to have
people involved in your data collection process, try and work as hard as you can
to maximize the consistency of the process for them.

It is worth saying that regardless of the initial choices you make, it is likely
you will revisit this step as you follow the other instructions and find out
what works for you and what does not. This is perfectly fine, and it is much
better initially to pick a dataset, make a start, and iterate, rather than
trying to get it perfect the first time.

The criteria to complete this step are:

* To create and implement (with exceptions, see below) a Data Collection Plan.
  This is a plan that details:

  * What data you are going to collect
  * Where/who you are going to collect it from
  * How you are going to collect the data
  * Any extra considerations

What data you are going to collect should include a data blueprint, a sample of
exactly what you think the data you are going to collect should look like. The
where/who should include specific populations you can feasibly target. The How
should be a plan of action to collect the data from the first step from the
groups you defined in the second step including, where required, a plan for how
the data is to be labeled.

If your AI application is in the high AI Risk category, or you are dealing with
personal data, some special considerations exist. Create this plan, but do not
implement it until you have worked through the following:

For high AI Risk applications:

* You will be required to provide adequate documentation around data collection,
  and log all data collection activity. You will also be required to have human
  oversight over the data collection process. Make sure you visit the
  Documentation and Logging section of the guide that covers these areas before
  collecting any data
* You have a duty to make sure the data you collect is of a high quality to
  minimize discriminatory outcomes. Make sure you visit the Data Exploration and
  Biases section of the guide before collecting data.

For AI applications dealing with personal data:

* You must collect data according to GDPR regulation. This topic is expanded on
  in our Appendix on GDPR.

Examples
###########

In this example, we work through the case of an oncologist looking to create an
AI application to help other physicians detect the presence of tumors in a chest
x-ray. There is an `example data set creation document<dataset_creation>`,
and a description below:

The data I, as our imaginary oncologist, will need for my application is a set
of chest x-rays, and whether they contain cancer or not.

+--------------+----------------+
| Data         | classification |
+==============+================+
| x-ray0.png   | cancerous      |
+--------------+----------------+
| x-ray1.png   | non-cancerous  |
+--------------+----------------+
| x-ray2.png   | cancerous      |
+--------------+----------------+
| ...          | ...            |
+--------------+----------------+

In respect to where I can find the data, a starting point is obviously the data
that I can collect from my own patients. I may be able to get data from other
patients from people in my professional network, or simply search online (there
are several publicly available datasets on this particular topic).

In respect of how I can go about collecting (and labeling) my data. I can get
chest X-rays from the sources described above. To label them, I can use my own
expert knowledge, and/or ask other physicians to also contribute to corroborate. 

In respect of extra considerations: I am working with personal health data. I’d
likely need to obtain consent from the patients, must respect GDP, and may have
additional requirements to fulfill in respect of my medical license, or an
ethics board to satisfy. It’s likely that this application would also fall into
a high AI Risk category, and be subject to extra requirements. 



.. _Version Control, CI/CD for Data:

:ref:`Version Control, CI/CD for Data<How do I collect data for my AI/ML project?>`
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Any electronic systems engineer should be familiar with version control. These
ideas are just as important in developing AI applications as any other software
product. In this step we explore:

* Version control systems for all data collection code
* Version control systems for all data collected

Our reasons for developing version control for data collection code are the same
as they would be for any other software project. We have similar requirements of
the datasets we collect with this code. Just like our code, our data is not
something we can consider static. Not only is it possible we will collect more,
but our existing data may be reorganized, fixed, or updated.

Version control for code is very well established, with a range of standard free
tools (e.g. Git, Mercurial, Subversion) available. Version control of data
requires a little more work. The standard tools used for code control are only
appropriate for a (relatively) small number of small files, tracking a
relatively small number of changes. Many datasets will not meet these criteria.
In these cases we can either extend existing version control with “large file”
control, or with an entirely separate data version control system. Free and Open
Source examples of the above are Git LFS and Data Version Control respectively.

To complete this section, you must:

* Set up a version control system for your code and data

Examples
###########

.. _Documentation:

:ref:`Documentation<How do I collect data for my AI/ML project?>`
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Another task that any electronic systems engineer should be familiar with is
documentation. As with version control, good documentation is just as important,
or perhaps even more so, as any other software development project. In this step
we will explore:

* Documentation for the code and;
* Documentation for data

Compared to many software engineering projects, AI projects can often suffer
from large variances in behavior due to the stochastic nature of the algorithms
involved. A consequence of this is that it is imperative to maintain clear
documentation. We must be able to clearly distinguish between acceptable
variances in behavior due to irreducible randomness in our processes, and
unacceptable variances in behavior due to mistakes.

Documentation should follow standard best practices. This is quite a large topic
that has been extensively covered elsewhere
(e.g. `Write The Docs <https://www.writethedocs.org/guide/>`_), that we won’t
repeat in this guide. Instead, we devote this section to discussing the
additional considerations required for documentation of data. Documentation for
data serves not just a similar function to documentation for code in terms of
bringing clarity and transparency to what has been done, but it also has a
strong role in ensuring reproducibility. In many cases, and especially when
dealing with challenging data (such as data involving human factors), how you
went about collecting this data is just as important as what you ultimately
collected. Ultimately, we suggest that documentation for data should consider
the following three things:

**What you collected**. A good description should (if reasonable) include a way
of positively identifying what was collected, where it was collected from, and
when.

**How you collected it**. A good description should both include a succinct high
level description of what was done, and include enough detail to allow a full
replication. Especially for complicated data collection paradigms, the devil is
often in the details. Seemingly unimportant details can become important later. 

**Why you did it this way**. Should both rationalize the process you took and,
crucially, why you did this instead of other things. This gives important
contextual hints to anyone trying to replicate your results that may be absent
from a pure “how” description, and can help them avoid any problems you
encountered in the process.

To achieve this we suggest that:

* Each piece of data comes with metadata, describing what it is

* Each group of data should be accompanied by a short document describing how
  and why it was collected.

This may sound like a significant overhead but, especially if your data is being
collected digitally, the burden is not especially high. Populating metadata can
often be significantly automated, and written documentation may overlap
significantly with the existence and documentation of relevant code. For
example, consider a dataset of images collected by a web scraper. It would be
very easy to include a hash to positively identify what was collected, the web
location it was collected from, and at what time during the scraping process. In
respect of how this data was collected, the code for the webscraper itself
provides a strong description of this. Even in respect of why it was done this
way, the documentation for this code provides a significant amount of context. 


High AI Risk applications:

* For high AI risk applications, documentation is no longer an internally driven
  process to improve productivity, but a (likely mandated) part of the
  requirement to demonstrate traceability and auditability of the software
  
* High risk AI Applications must have human oversight. Automated documentation of
  data collection will require a level of human oversight and validation.


The criteria to complete this step are:

* Creating documentation for all code written to this point, and standards for
  future code

* Creating documentation for any data collected to this point, and a process for
  documenting future data

Examples
###########

.. _Logging:

:ref:`Logging<How do I collect data for my AI/ML project?>`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Logging is a core requirement of the software development process. It must be
accepted that software will break or not fulfill its function correctly, and
when it does we need to be able to diagnose those faults effectively.
Furthermore, software is rarely static, and in order to change it we must
understand how it works. Finally, in many cases we may wish (or be required) to
audit and review our software, and logging is an important part of this. In this
step, we will explore:

* How to create a logging process for out data collection

When creating a logging process, the first question is always “What should we
log?”. The best place to start with this is to instead start with the question
“what questions do we want to answer about our software?”. Obviously, the answer
to this will depend on the specifics of our data collection, but some recurring
questions you will often need to answer are:

* Where did I get this piece of data?
* When did I get this piece of data?
* What was the state of my collection program when I collected this data?
* Was collecting this piece of data successful?
* Why was collecting this piece of data unsuccessful?

For high AI Risk applications:

* For high AI risk applications, logging is no longer optional. Logging of all
  actions relevant to proving compliance with the EU AI Act (see appendix) must
  be undertaken.

The criteria to complete this step are:

* Creating a logging process for all data collection code

.. _Data Exploration:

:ref:`Data Exploration<How do I collect data for my AI/ML project?>`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This step is separated from the Data Cleaning step for clarity, but in reality
these two steps are likely to be quite closely linked together. In this step we
will look at the process of exploring the data we collect.

In our steps so far we have designed an AI application, designed a dataset we
think will achieve our goals, and have taken the initial steps to ensure that
there is a robust coding framework around this. Before going any further, we
need to take a look at the data we have collected and try and understand it’s
key characteristics, strengths, and weaknesses of the data to establish:

* An understanding of the the key characteristics, strengths, and weaknesses of the data
* What patterns and relationships exist in the data
* Whether it is likely to be useful for the purpose we intended
* What further data collection should fix, and what it should do more of

We discussed previously in the guide that you may wish to return to earlier
steps, and this data exploration step is one of the steps which is likely to
encourage this. While this initial examination obviously can not understand the
end result of our full AI pipeline ahead of time, we can build up an
understanding of our data. It’s likely that, especially for the first time, our
data may not be exactly as we had hoped it would be. 

Our data exploration process is about trying to digest information about our
dataset. The methods we use to do this are very fundamental, intuitive ideas:

* Looking directly at the data and subsets thereof
* Trying to understand the data in an intuitive visual way
* Trying to understand the data through summaries and heuristics

The best approach for this will vary, but standard approaches for these are:

* Tabular reports
* Data Visualization
* Data Profiling

**Tabular reports.** Forming tabular reports is a very simple way to look at our
data directly. This is simply structuring our data set in a row/column format.
There are no hard rules about how we might want to do this. We could look at
subsets of the data, look at ordered columns, or anything else. Just looking at
the raw data can often be very useful. We can check our intuitions about the
data, identify potential patterns, and notice errors that may be hard to
identify other ways.

**Data Visualization.** Directly examining data is useful in a way that should
not be discarded. However, most of us will find it more useful to process data
visually. There are a very large number of ways to do this. Edward Tuft lists a
series of key ideas that are often cited for this:

* show the data
* induce the viewer to think about the substance rather than about methodology,
  graphic design, the technology of graphic production, or something else
* avoid distorting what the data has to say
* present many numbers in a small space
* make large data sets coherent
* encourage the eye to compare different pieces of data
* reveal the data at several levels of detail, from a broad overview to the fine
  structure
* serve a reasonably clear purpose: description, exploration, tabulation, or
  decoration
* be closely integrated with the statistical and verbal descriptions of a data
  set.

Good visualizations are often as much of an art as a science. As with many
things for which this is the case, the best initial approaches are as follows:

* Start from the basics, the simple tools that everyone else uses (line plot,
  scatter graphs, heatmaps)
* Unashamedly appropriate good ideas from other people doing similar things
* Explore your own ideas to find out works for you and what does not


**Data Profiling.** Data profiling tries to capture yet another approach to
understanding our data, this time through the use of summarizations and
statistics about our data. 

* What groupings (or clusters) within in our data
* Averages (mean, median, etc.)
* Spreads (standard deviation, quartiles, etc.)

As part of this we might want to explore how different bits of our data relate
to each other. For example:

* Comparing different data
* Correlating different data

Alongside these broad techniques, we might also choose to do a detailed
“drilldown” into our data and run a more detailed analysis of some parts. We
might look at some more advanced statistics or visualizations of these subsets,
or even perform a small scale trial run of some AI approaches we are considering
later. 

To criteria to complete this step is to:

* Create a data exploration process
* Create a data exploration report


.. _Data Cleaning:

:ref:`Data Cleaning<How do I collect data for my AI/ML project?>`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The raw data that is collected through our data collection process is not
necessarily the best data to use in training our algorithm. Some parts of our
data might be poor quality for one reason or another. Following our previous
examples, we should look for:

* Accuracy
* Completeness
* Relevance
* Missingness
* Timeliness
* Subjectivity
* Attainability
* Standardization

Hopefully, the data analysis we discussed in the previous step will have
uncovered many of these issues already. If there are any issues with the data
quality you have not explored, so far, this is the step to do them (using the
techniques in the last section).

As with visualizing the data, the best way to clean it will depend on your
problem and precisely what it is you’re trying to do with it. However, there are
some common problems for which there are well established solutions:


**Basic Cleaning.** Not all data collection processes perform ideally.
Particularly, if many data sources are aggregated together, it’s very possible
to see errors such as duplicated data points, or inconsistent labels (“eleven”
vs 11, for example). The following is a list of these common errors, and what
can be done about each:

* Formatting

  * Convert all labels to one format or representation. For example, all numbers
    as digits, or all dates as DD/MM/YY.

* Data duplication

  * Check for duplicate entries and remove them. 

* Structural issues

  * Not all data sources may have collected the same data. Choose which ones to
    keep 

* Irrelevant data

  * Remove if if you are not going to use it

* Errors

  * Fix or remove any data points with errors (e.g. spelling mistakes from user
    input)

This is not an exhaustive list, but you should at the minimum consider each of
these in your data cleaning.

**Missing/corrupt data.** A very common problem is for some parts of the data to
be missing. For many AI techniques we might want to apply later, this is an
issue. The ideal thing to do about this problem is to collect a fresh set of
data with less (or ideally zero) parts missing. Obviously, this is not always
practical. If we can not do this, then we essentially have two solutions:

* Cut all entries with missing data points out
* Use an AI technique that is robust to the missing data
* Impute our data, filling in estimates of the missing values

We won’t cover the techniques for any of these in detail, for which there are a
wealth of resources elsewhere (imputation), but we note that the extent to which
any of these strategies is plausible depends on how the missingness in our data
has come about. There are three ways the data might be missing:

* Missing totally at random (MCAR) - the data is missing completely randomly
  with no pattern at all
* Missing random (MAR) - the data is missing randomly, but in a way that is
  explained by the data you are using to predict things
* Missing not at random (MNAR) - the data is missing in a way that is not
  explained by the data you are using to predict things

As an example of the first, might be some bits of our data being deleted
randomly by a bad sensor. An example of the last would be a survey about
depression - participants with severe depression are more likely to refuse to
complete the survey about depression severity. An example of the second is a
little more tricky. Consider a dataset of blood pressure, containing both a
group of old participants and young participants. Clearly, data won’t be missing
entirely at random because older participants are more likely to have their
blood pressure measured. However, as long as this is the only difference between
the two groups, this is not usually a problem. We can e.g. treat them
separately.

The distinction between these can be a bit subtle, but the headline from this is
as follows: When data is missing either completely randomly (MCAR), or for a
reason we fully understand and can measure (MAR), this is fine. We can use data
imputation, or (for some AI models) adapt our model to this situation. When data
is missing for a reason we do not understand and/or can not measure (MNAR), we
(typically) can not do either and this is not. If you find yourself in this
case, typically you need to reformulate the problem. For example, accounting for
the fact that the data point is missing as a point of data in itself. 


**Removing Outliers.** Removing outliers is technically simple - there are a
range of techniques to do this that we will not re-cover here. The reason we
have included this short section is to cover when you should consider removing
outliers and when you should not.


Shortly, outliers are data points too. It can be tempting to remove them if they
are, for example, making large contributions to an average that you feel is
skewing your measure of interest. However, doing this without a valid reason
causes problems. Especially, removing data points because they do not agree with
your expectations will ultimately lead you to believe them to be true even when
they are not true. 


The valid reasons to remove an outlier data point are:

* You believe that it is a measurement error

  * It is an outlier because the process user to measure is in error

* You believe it is a data entry or processing error

  * It is an outlier because the way it has been entered into storage or processed is in error

* You believe that your sampling process is incorrect

  * It is an outlier because the way the data point has been chosen over others is in error


A datapoint is a measurement error if the process used to measure it has
measured it incorrectly. 


To complete this step:

* Clean your data and establish a cleaning process


.. _Validation and Testing:

:ref:`Validation and Testing<How do I collect data for my AI/ML project?>`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

We established a good idea of what qualities our data has (and does not have)
from our previous steps. Unfortunately, if and when we collect more of this
data, we have no guarantee that things are going to stay the same. Similarly, we
want to be sure that in the process of storing and moving the data around, we
are not introducing new errors. We therefore want to set up an automated
monitoring and testing process to look at the data as we collect it. 


Very broadly, we hope with this validation and testing process to be checking
two things:

* Does my data look like I expect it to?
* Is my data remaining of a high quality?
* Or at least, is it broken in all the ways I expect it to be and none of the
  ones I do not


The way we go about this is with a tool that should be familiar to any software
engineer: writing tests. The criteria for these tests may have to be a little
different from usual. Our data collection process is ultimately stochastic, and
so a lot of our tests will have to be stochastic too. Examples include:

* Checking if data falls within the min-max ranges of that data element (based
  on all previous data registered),
* Defining several validation rules, and display data units violate these
  validation rules.
* Analysis of data sets, i.e., examining gaps in data, missing values, existing
  trends, and so forth

To complete this step:

* Create a validation process.


.. _Data Storage and Access:

:ref:`Data Storage and Access<How do I collect data for my AI/ML project?>`
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Having collected this data, we need to think about how it is going to be stored
and accessed. The solution to this will vary significantly depending on the
scale of the operations we are dealing with. Small, lightweight projects might
be adequately managed in a spreadsheet, big ones might require a large data
warehousing system integrating multiple sources of data.


This section is not intended to be a reintroduction to the technical details of 
data storage and management, but a review of the problems and considerations around using them in these types of workflows.

**Structured vs unstructured storage.** When collecting your data, you have the
option of storing it in an unstructured form (e.g. in a raw data format), or
storing it in a structured format (e.g. a database). 


While you are ultimately very likely to need your data to be in a structured
format at some point for your analysis, it is not always advantageous to store
it in this format. 

* On one hand, storing data in a structured format decreases the flexibility you
  have to store that data, and requires you to commit ahead of time to a data
  model that involves that format that you choose. 

* On the other hand, if you can pre-specify a structure for your data, it will
  significantly reduce the amount of time and effort we need to spend
  structuring it later.


The tradeoff between these two will depend on your application. General
considerations are:

* How much does storing raw data cost me, versus structuring it?
* How much effort will it be to convert raw data into the structured format I
  will need later, if I don’t do it on collection?
* What is the realistic opportunity cost for forcing my data collection into a
  structured format, versus unstructured collection?

**Data validation & multiple data sources.** The data collection process is
rarely perfect, and these problems are often compounded when data is collected
from multiple sources, and integrated together later on for analysis. This is
one of the causes of many problems that we discussed in the data cleaning
section:

* Formatting

  * Convert all labels to one format or representation. For example, all numbers as digits, or all dates as DD/MM/YY. 

* Data duplication

  * Check for duplicate entries and remove them. 

* Structural issues

  * Not all data sources may have collected the same data. Choose which ones to keep

* Irrelevant data

  * Remove if you are not going to use it

* Errors

  * Fix or remove any data points with errors (e.g. spelling mistakes from user input)


While you should continue to deal with these issues as part of your data
cleaning, you should also solve as many of them as you can as part of your data
management process. For example, applying a universal enforcement that all
numbers should be entered into the system as digits. 

**Cloud vs Local.** It can often be very attractive to pay for someone else to
store data with a cloud service. We will not cover the general merits of cloud
vs local storage here, which we assume are already known.

The main additional considerations in the contexts of AI and machine workloads
are what you are doing to do with the data you have stored. Training is an
access intensive process, and how you intend to get the data from wherever it is
stored to the computing power doing the storage has a strong impact on
performance. 

Shortly, whichever of local vs cloud computing you intend to use for training
your model, you should consider how this is going to translate into storage.

**Performance Requirements.** Not all storage is created equal. The target
audience of this guide should be well aware that there are a range of physical
solutions from magnetic tapes to SSDs for storing and retrieving data that
tradeoff cost and performance, with similar cost models for cloud storage
systems.

For AI systems, it is worth considering that data that is going to be used
directly for training will need to be accessed quickly and repeatedly during the
process. In many cases making an investment in high performance storage may
speed up the process significantly. However, not all applications will be like
this, and not all data will directly be part of the training process. Raw
unstructured data, infrequently accessed, for example, may be a prime candidate
for lower performance storage. 

To complete this step:

* Establish your data storage strategy