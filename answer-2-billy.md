### Question 2

The Marketing Team at Bookly wants to merge and analyze all the data that is being collected by the different products in order to extract useful business insights of various kinds.
Examples of such analytics include (but are not restricted to):

- List all-time top rated books and trending ones;
- Measure user sign-up rate over certain periods (weekly, quarterly, etc);
- Show the total number of real-time (current) page views for any given book description page (product page);
- ...

Design a conceptual data pipeline to drive and aggregate data from all the different sources to ultimately be accessible by a user-friendly data exploration/dashboarding tool of your choice. Feel free to pick any technology available (e.g. open source, cloud providers, etc.).

_Describe the different components of the architecture, tools involved and compare possible approaches._
# Answer

## Description of business process
As each of the systems have databases, I would work with the marketing team to identify their questions of the data to confirm which tables and conntent from the individual databases would need to go into an ETL pipeline. The ETL would be made of Python and SQL code which is able to conduct the pipeline, compared to using cloud tools which have visual pipeline.

Application DBs <--> Python Code/Serverless <---> BI Database <---> Tableau <---> Marketting Team

The results would be stored in a dedicated database used for business intelligence insights.  The database would hold the complete history of the book titles and ratings, plus the rest of the relevant data from the app DBs in full.  

I would have serverless computer systems which use SQL queries which ran at sensible scheduled intervals (e.g. every 3 hours) to collect only the delta/updated information from the databases (ideally using a mirror database if available, to remove load from application databases).  

I would propose using Tableau to visualise the insights, as the views can be pre-prepared by the data engineer. 

Trending updates would be found by collecting the average ratings within only a certain timeframe, where the minimum number of ratings are above X in that time period - to be advised by marketting.

User sign-up rates would be pre calculated into daily totals, with columns representing the allocated week/quarter/year, and when viewed in tableau the daily sign ups would be summed together.
