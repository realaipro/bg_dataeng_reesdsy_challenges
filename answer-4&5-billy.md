## Part B

The marketing Team at Bookly introduced A/B Testing on their blog - each blog post will show a given registration popup from a set of pre-configured popups.
The raw dataset in [dataset.tsv](data/dataset.tsv) offers a table with various content properties and the conversion rates for each combination of blog post and registration popup.

### Question 4

What is the major contributor to user registrations? In other words, what is the most relevant factor that contributes the most to convert user views into user registrations?

_Describe in detail all the steps you take to perform the analysis, provide code snippets, relevant data transformations and results._

# Answer 

As the views and registrations are in different amounts, and the data available is the totals. I calculated the average value of the conversion from views to registrations, and sorted by the highest converting.  Additionally I created a sheet putting together the conversion rates of everything added together.

The learning/teaching content has a high influence on the conversion factor.

To run the code
```
python3 -m venv venv
source venv/bin/activate
pip3 install pandas
python3 qu4_data.py
```

### Question 5

Explore the dataset. What other insights can be extracted?

_Describe in detail all the steps you take to perform the analysis, provide code snippets, relevant data transformations and results._

I noticed that foreign language content is very good, sometimes providing 100% conversion rate and is providing registrations that potentially would not have occured without the localisation.  Additionally, I noticed a large number of views of 21 with 21 conversion - I would extrapolate from the unlikeliness of this, that the dataset is synthentic (made up for the question) - however in a production system, I would have evaluated there may be an issue to diagnose in the pipeline.
