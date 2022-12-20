The Customer Support team spends considerable time scanning through customer reviews and comments in order to filter out illegitimate ones. Multiple factors can contribute to label comments as authentic or not:

- Comment is made by a registered user vs. anonymous;
- Level of user activity (eg: number of past reviews and comments);
- Content of the comment (eg: unauthorized advertising)
- ...

In order to automate the filtering process, design a conceptual, real-time, decision support system that takes data as input (user properties, user actions, content, etc) and automatically labels comments as legitimate/illegitimate for the Customer Support Team to quickly flag and remove the unwanted.

_Describe the different components of the architecture, tools involved and compare possible approaches._
# Answer
## Description of solution

In addition to the factors mentioned above, I would also consider:

- Source IP address of User
- Email domain of User
- Time of Day
- Use word list developed by customer service team (of likely spam messages)
- Does the review contain a website address 
- Use the count of words, especially looking for repeated phrases
- Check for mention of book title or author in post
- Number of common words across posts, and multiple posts in a short time.
- Monitor activity level per each book title 

## Approach a - Use machine learning. 

Collect the data for all successful and banned reviews in the past.  Identify the reason that each review was banned.  Collect the metadata and normalise it (convert the IP to general location, and post time to general time of day), get the sentiment analysis result.  Train a model to predict if a review will be banned, use this to flag up the most likely to be banned to customer support.

The model could be queried by batch collecting new review text and metadata from an API every so often, including its' review_id value.  The response from the API could be the proposed label matched with the review_id.

## Approach b - Decision support system:
 
Review is put in the database, with a flag of 'unreviewed'.
Web hook is hit, which collects all reviews which are unreviewed.
Gathers information on the User account, Number of Posts in the last 12 hours, Number of common words per posts.
Each of the factors above have a set of values which provide a 'risk score' (e.g. fewer historic posts are more common for spammers), the risk scores are added up, and the list is shown to the customer support team in order of highest risk first.

This could be shown in a simple dedicated web-app or integrated into the existing customer support tool platform.