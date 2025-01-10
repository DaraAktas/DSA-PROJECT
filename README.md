# DSA-PROJECT
## Description
Sabanci University DSA210 Introduction to Data Science Course Fall 2024-2025 Term Project. This project will be an analysis on relation between my own bitaksi usage and academic schedule.
Final Report: 

## Table of Contents
**[Motivation](#motivation)**  

**[Research question](#research-question)**  

**[Data Source](#data-source)**  

**[Tools](#tools)**  

**[Data Analysis](#data-analysis)**

**[Findings](#findings)**

**[Limitations](#limitations)**  

**[Future Work](#future-work)**  

## Motivation
While planning my project, I realized that I could explore a pattern between my transportation and my academic schedule. As BiTaksi is one of my primary method of transportation, I decided to focus on analyzing its usage. The motivation behind this analysis is to show if my taxi usage is influenced by my lecture times, workload,,exams and overall schedule. By examining trends such as the time of the rides, frequency during specific weeks, and peak usage periods, I aim to show if there is any relation between my taxi usage and University chedule

## Research question
Is there a relationship between my BiTaksi usage and my academic schedule, such as lecture times, workload, and exam periods?

## Data Source
I have gathered my data from two main sources:
 - BiTaksi Usage Data: I contacted bitaxi consumer services and got my ride history in csv format. This data contains information about the date, time, and cost of my rides, along with pickup and drop-off locations.
 - Academic Schedule: My academic schedule was extracted from my university's course management system. It includes the course name, time slots, and location of my lectures.I preprocessed the raw data into a json file

## Tools

 - **[Jupyter Notebook](https://jupyter.org/):** I will use jupyter for coding notebook and processing.  
 - **[Pandas](https://pandas.pydata.org/):** I will use pandas libraries for data cleaning, filtering, and structuring.  
 - **[Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/):** I will use this two for data visualisation in python.  
 - **[Numpy](https://numpy.org/):** I will use numpy for mathematical operations.  

## Data Analysis 

The analysis will proceed through the following stages to investigate the relationship between my BiTaksi usage and my academic schedule:

### 1. Data Collection
**BiTaksi Data:**
 - Ride History: Exported from BiTaksi customer services as .csv file, including: date and time of rides, pickup and drop-off locations, total cost for each ride.
**Academic Schedule Data:**
 - Course Schedule: Extracted from my university’s course management system and preprocessed into a .json file. Includes: course names, time slots (start and end times), lecture locations, key dates for exams and deadlines.
### 2. Data Cleaning
 - Removed incomplete or erroneous entries (e.g., missing location data or costs marked as zero).
### 3. Exploratory Data Analysis (EDA) 
**Objective:** Determine the relationship between ride timings and lecture schedules.
 - Analysing the frequency of rides by days to identify peak usage days.
 - Examining  hours to determine the most common times for rides.
 - Considering usage around exams.

## Findings
###	1.Frequent Destinations
 - The most common destinations are “Orta Mah., Üniversite Cad., Tuzla” , which is the location of my University.
###	2.Activity Peaks
 - Travel activity is highest on Wednesday and Saturday, while Sunday shows lower usage; week days are more active.
###	3.Time Alignment
 - Taxi usage aligns closely with academic schedules, particularly in the afternoon (1 PM–3 PM), reflecting a strong time correlation.
###	4.Class vs. Taxi Usage
 - Class activities are mostly in the morning and early afternoon, while taxi usage spans a broader range, including evenings.
###	5.Key Location Impact
 - “Orta Mah., Cengizhan Cad., Tuzla” is a significant location, contributing a large share of overall trips.


## Limitations

## Future work
