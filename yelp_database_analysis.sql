By: Sophia Braddock
Date: May-1-2018

Data Scientist Role Play: Profiling and Analyzing the Yelp Dataset Coursera Worksheet

This is a 2-part assignment. In the first part, you are asked a series of questions that
will help you profile and understand the data just like a data scientist would. For this
first part of the assignment, you will be assessed both on the correctness of your
findings, as well as the code you used to arrive at your answer. You will be graded on
how easy your code is to read, so remember to use proper formatting and comments where
necessary.

In the second part of the assignment, you are asked to come up with your own inferences
and analysis of the data for a particular research question you want to answer. You will be
required to prepare the dataset for the analysis you choose to do. As with the first part,
you will be graded, in part, on how easy your code is to read, so use proper formatting
and comments to illustrate and communicate your intent as required.

For both parts of this assignment, use this "worksheet." It provides all the questions
you are being asked, and your job will be to transfer your answers and SQL coding where
indicated into this worksheet so that your peers can review your work. You should be able
to use any Text Editor (Windows Notepad, Apple TextEdit, Notepad ++, Sublime Text, etc.)
to copy and paste your answers. If you are going to use Word or some other page layout
application, just be careful to make sure your answers and code are lined appropriately.
In this case, you may want to save as a PDF to ensure your formatting remains intact
for you reviewer.



Part 1: Yelp Dataset Profiling and Understanding

1. Profile the data by finding the total number of records for each of the tables below:

		SELECT COUNT(*)
		FROM table

	i. 		Attribute table = 10000
	ii. 	Business table = 10000
	iii. 	Category table = 10000
	iv. 	Checkin table = 10000
	v. 		elite_years table = 10000
	vi. 	friend table = 10000
	vii. 	hours table = 10000
	viii. 	photo table = 10000
	ix. 	review table = 10000
	x. 		tip table = 10000
	xi. 	user table = 10000



2. Find the total number of distinct records for each of the keys listed below:

		SELECT COUNT(DISTINCT(key))
		FROM table

	i. 		Business = id: 10000
	ii. 	Hours = business_id: 1562
	iii. 	Category = business_id: 2643
	iv. 	Attribute = business_id: 1115
	v. 		Review = id:10000, business_id: 8090, user_id: 9581
	vi. 	Checkin = business_id: 493
	vii. 	Photo = id: 10000, business_id: 6493
	viii. 	Tip = user_id: 537, business_id: 3979
	ix. 	User = id: 10000
	x. 		Friend = user_id: 11
	xi. 	Elite_years = user_id: 2780



3. Are there any columns with null values in the Users table? Indicate "yes," or "no."

	Answer: "no"


	SQL code used to arrive at answer:

		SELECT COUNT(*)
		FROM user
		WHERE id IS NULL OR
		  name IS NULL OR
		  review_count IS NULL OR
		  yelping_since IS NULL OR
		  useful IS NULL OR
		  funny IS NULL OR
		  cool IS NULL OR
		  fans IS NULL OR
		  average_stars IS NULL OR
		  compliment_hot IS NULL OR
		  compliment_more IS NULL OR
		  compliment_profile IS NULL OR
		  compliment_cute IS NULL OR
		  compliment_list IS NULL OR
		  compliment_note IS NULL OR
		  compliment_plain IS NULL OR
		  compliment_cool IS NULL OR
		  compliment_funny IS NULL OR
		  compliment_writer IS NULL OR
		  compliment_photos IS NULL



4. Find the minimum, maximum, and average value for the following fields:

		SELECT AVG(column)
		FROM table

	i. Table: Review, Column: Stars

		min: 1		max: 5		avg: 3.7082


	ii. Table: Business, Column: Stars

		min: 1 		max: 5		avg: 3.6549


	iii. Table: Tip, Column: Likes

		min: 0		max: 2		avg: 0.0144


	iv. Table: Checkin, Column: Count

		min: 1		max: 53		avg: 1.9414


	v. Table: User, Column: Review_count

		min: 0		max: 2000		avg: 24.2995



5. List the cities with the most reviews in descending order:

	SQL code used to arrive at answer:

		SELECT city,
			   SUM(review_count) AS reviews
		FROM business
		GROUP BY city
		ORDER BY reviews DESC

	Copy and Paste the Result Below:

		+-----------------+---------+
		| city            | reviews |
		+-----------------+---------+
		| Las Vegas       |   82854 |
		| Phoenix         |   34503 |
		| Toronto         |   24113 |
		| Scottsdale      |   20614 |
		| Charlotte       |   12523 |
		| Henderson       |   10871 |
		| Tempe           |   10504 |
		| Pittsburgh      |    9798 |
		| Montréal        |    9448 |
		| Chandler        |    8112 |
		| Mesa            |    6875 |
		| Gilbert         |    6380 |
		| Cleveland       |    5593 |
		| Madison         |    5265 |
		| Glendale        |    4406 |
		| Mississauga     |    3814 |
		| Edinburgh       |    2792 |
		| Peoria          |    2624 |
		| North Las Vegas |    2438 |
		| Markham         |    2352 |
		| Champaign       |    2029 |
		| Stuttgart       |    1849 |
		| Surprise        |    1520 |
		| Lakewood        |    1465 |
		| Goodyear        |    1155 |
		+-----------------+---------+


6. Find the distribution of star ratings to the business in the following cities:

	i. Avon

		SQL code used to arrive at answer:

			SELECT stars,
				   SUM(review_count) AS count
			FROM business
			WHERE city == 'Avon'
			GROUP BY stars


		Copy and Paste the Resulting Table Below (2 columns - star rating and count):

			+-------+-------+
			| stars | count |
			+-------+-------+
			|   1.5 |    10 |
			|   2.5 |     6 |
			|   3.5 |    88 |
			|   4.0 |    21 |
			|   4.5 |    31 |
			|   5.0 |     3 |
			+-------+-------+


	ii. Beachwood

		SQL code used to arrive at answer:

			SELECT stars,
				   SUM(review_count) AS count
			FROM business
			WHERE city == 'Beachwood'
			GROUP BY stars

		Copy and Paste the Resulting Table Below (2 columns - star rating and count):

			+-------+-------+
			| stars | count |
			+-------+-------+
			|   2.0 |     8 |
			|   2.5 |     3 |
			|   3.0 |    11 |
			|   3.5 |     6 |
			|   4.0 |    69 |
			|   4.5 |    17 |
			|   5.0 |    23 |
			+-------+-------+


7. Find the top 3 users based on their total number of reviews:

	SQL code used to arrive at answer:

		SELECT id,
			   name,
			   review_count
		FROM user
		ORDER BY review_count DESC
		LIMIT 3

	Copy and Paste the Result Below:

		+------------------------+--------+--------------+
		| id                     | name   | review_count |
		+------------------------+--------+--------------+
		| -G7Zkl1wIWBBmD0KRy_sCw | Gerald |         2000 |
		| -3s52C4zL_DHRK0ULG6qtg | Sara   |         1629 |
		| -8lbUNlXVSoXqaRRiHiSNg | Yuri   |         1339 |
		+------------------------+--------+--------------+

8. Does posting more reviews correlate with more fans?

		Yes. The amount of time that they have been using Yelp is also a factor. The longer they
		have had a Yelp account and the more reviews the Yelper post will give a higher fan count.

	Please explain your findings and interpretation of the results:

		SELECT id,
			   name,
			   review_count,
			   fans,
			   yelping_since
		FROM user
		ORDER BY fans DESC

		+------------------------+-----------+--------------+------+---------------------+
		| id                     | name      | review_count | fans | yelping_since       |
		+------------------------+-----------+--------------+------+---------------------+
		| -9I98YbNQnLdAmcYfb324Q | Amy       |          609 |  503 | 2007-07-19 00:00:00 |
		| -8EnCioUmDygAbsYZmTeRQ | Mimi      |          968 |  497 | 2011-03-30 00:00:00 |
		| -2vR0DIsmQ6WfcSzKWigw  | Harald    |         1153 |  311 | 2012-11-27 00:00:00 |
		| -G7Zkl1wIWBBmD0KRy_sCw | Gerald    |         2000 |  253 | 2012-12-16 00:00:00 |
		| -0IiMAZI2SsQ7VmyzJjokQ | Christine |          930 |  173 | 2009-07-08 00:00:00 |
		| -g3XIcCb2b-BD0QBCcq2Sw | Lisa      |          813 |  159 | 2009-10-05 00:00:00 |
		| -9bbDysuiWeo2VShFJJtcw | Cat       |          377 |  133 | 2009-02-05 00:00:00 |
		| -FZBTkAZEXoP7CYvRV2ZwQ | William   |         1215 |  126 | 2015-02-19 00:00:00 |
		| -9da1xk7zgnnfO1uTVYGkA | Fran      |          862 |  124 | 2012-04-05 00:00:00 |
		| -lh59ko3dxChBSZ9U7LfUw | Lissa     |          834 |  120 | 2007-08-14 00:00:00 |
		| -B-QEUESGWHPE_889WJaeg | Mark      |          861 |  115 | 2009-05-31 00:00:00 |
		| -DmqnhW4Omr3YhmnigaqHg | Tiffany   |          408 |  111 | 2008-10-28 00:00:00 |
		| -cv9PPT7IHux7XUc9dOpkg | bernice   |          255 |  105 | 2007-08-29 00:00:00 |
		| -DFCC64NXgqrxlO8aLU5rg | Roanna    |         1039 |  104 | 2006-03-28 00:00:00 |
		| -IgKkE8JvYNWeGu8ze4P8Q | Angela    |          694 |  101 | 2010-10-01 00:00:00 |
		| -K2Tcgh2EKX6e6HqqIrBIQ | .Hon      |         1246 |  101 | 2006-07-19 00:00:00 |
		| -4viTt9UC44lWCFJwleMNQ | Ben       |          307 |   96 | 2007-03-10 00:00:00 |
		| -3i9bhfvrM3F1wsC9XIB8g | Linda     |          584 |   89 | 2005-08-07 00:00:00 |
		| -kLVfaJytOJY2-QdQoCcNQ | Christina |          842 |   85 | 2012-10-08 00:00:00 |
		| -ePh4Prox7ZXnEBNGKyUEA | Jessica   |          220 |   84 | 2009-01-12 00:00:00 |
		| -4BEUkLvHQntN6qPfKJP2w | Greg      |          408 |   81 | 2008-02-16 00:00:00 |
		| -C-l8EHSLXtZZVfUAUhsPA | Nieves    |          178 |   80 | 2013-07-08 00:00:00 |
		| -dw8f7FLaUmWR7bfJ_Yf0w | Sui       |          754 |   78 | 2009-09-07 00:00:00 |
		| -8lbUNlXVSoXqaRRiHiSNg | Yuri      |         1339 |   76 | 2008-01-03 00:00:00 |
		| -0zEEaDFIjABtPQni0XlHA | Nicole    |          161 |   73 | 2009-04-30 00:00:00 |
		+------------------------+-----------+--------------+------+---------------------+



9. Are there more reviews with the word "love" or with the word "hate" in them?

	Answer: love has 1780, while hate only has 232


	SQL code used to arrive at answer:

		SELECT COUNT(*)									SELECT COUNT(*)
		FROM review										FROM review
		WHERE text LIKE "%love%"						WHERE text LIKE "%hate%"

		= 1780											= 232

10. Find the top 10 users with the most fans:

	SQL code used to arrive at answer:

		SELECT id,
			   name,
			   fans
		FROM user
		ORDER BY fans DESC
		LIMIT 10


	Copy and Paste the Result Below:

		+------------------------+-----------+------+
		| id                     | name      | fans |
		+------------------------+-----------+------+
		| -9I98YbNQnLdAmcYfb324Q | Amy       |  503 |
		| -8EnCioUmDygAbsYZmTeRQ | Mimi      |  497 |
		| -2vR0DIsmQ6WfcSzKWigw  | Harald    |  311 |
		| -G7Zkl1wIWBBmD0KRy_sCw | Gerald    |  253 |
		| -0IiMAZI2SsQ7VmyzJjokQ | Christine |  173 |
		| -g3XIcCb2b-BD0QBCcq2Sw | Lisa      |  159 |
		| -9bbDysuiWeo2VShFJJtcw | Cat       |  133 |
		| -FZBTkAZEXoP7CYvRV2ZwQ | William   |  126 |
		| -9da1xk7zgnnfO1uTVYGkA | Fran      |  124 |
		| -lh59ko3dxChBSZ9U7LfUw | Lissa     |  120 |
		+------------------------+-----------+------+


11. Is there a strong correlation between having a high number of fans and being listed
	as "useful" or "funny?"

		Yes, see table.

	SQL code used to arrive at answer:

		SELECT name,
			   fans,
			   useful,
			   funny,
			   review_count,
			   yelping_since
		FROM user
		ORDER BY fans DESC

	Copy and Paste the Result Below:

		+-----------+------+--------+--------+--------------+---------------------+
		| name      | fans | useful |  funny | review_count | yelping_since       |
		+-----------+------+--------+--------+--------------+---------------------+
		| Amy       |  503 |   3226 |   2554 |          609 | 2007-07-19 00:00:00 |
		| Mimi      |  497 |    257 |    138 |          968 | 2011-03-30 00:00:00 |
		| Harald    |  311 | 122921 | 122419 |         1153 | 2012-11-27 00:00:00 |
		| Gerald    |  253 |  17524 |   2324 |         2000 | 2012-12-16 00:00:00 |
		| Christine |  173 |   4834 |   6646 |          930 | 2009-07-08 00:00:00 |
		| Lisa      |  159 |     48 |     13 |          813 | 2009-10-05 00:00:00 |
		| Cat       |  133 |   1062 |    672 |          377 | 2009-02-05 00:00:00 |
		| William   |  126 |   9363 |   9361 |         1215 | 2015-02-19 00:00:00 |
		| Fran      |  124 |   9851 |   7606 |          862 | 2012-04-05 00:00:00 |
		| Lissa     |  120 |    455 |    150 |          834 | 2007-08-14 00:00:00 |
		| Mark      |  115 |   4008 |    570 |          861 | 2009-05-31 00:00:00 |
		| Tiffany   |  111 |   1366 |    984 |          408 | 2008-10-28 00:00:00 |
		| bernice   |  105 |    120 |    112 |          255 | 2007-08-29 00:00:00 |
		| Roanna    |  104 |   2995 |   1188 |         1039 | 2006-03-28 00:00:00 |
		| Angela    |  101 |    158 |    164 |          694 | 2010-10-01 00:00:00 |
		| .Hon      |  101 |   7850 |   5851 |         1246 | 2006-07-19 00:00:00 |
		| Ben       |   96 |   1180 |   1155 |          307 | 2007-03-10 00:00:00 |
		| Linda     |   89 |   3177 |   2736 |          584 | 2005-08-07 00:00:00 |
		| Christina |   85 |    158 |     34 |          842 | 2012-10-08 00:00:00 |
		| Jessica   |   84 |   2161 |   2091 |          220 | 2009-01-12 00:00:00 |
		| Greg      |   81 |    820 |    753 |          408 | 2008-02-16 00:00:00 |
		| Nieves    |   80 |   1091 |    774 |          178 | 2013-07-08 00:00:00 |
		| Sui       |   78 |      9 |     18 |          754 | 2009-09-07 00:00:00 |
		| Yuri      |   76 |   1166 |    220 |         1339 | 2008-01-03 00:00:00 |
		| Nicole    |   73 |     13 |     10 |          161 | 2009-04-30 00:00:00 |
		+-----------+------+--------+--------+--------------+---------------------+


	Please explain your findings and interpretation of the results:

	Row 3 - Harald - has exponential amount of 'useful' and 'funny' in comparison to the other Yelpers. Row 3 seems to be
  an abnormality. Disregarding the outlier the results are pretty consistent
  that more fans are a result of more time on Yelp and more reviews. The amount of 'useful' and 'funny'
  does seem to help newer Yelpers gain more fans. Further analysis:

  --If:
  --0% - 25% - Low relationship
  --26% - 75% - Medium relationship
  --76% - 100% - Strong relationship

  	--:(2 Part Query)
  	--PART-1 --
  	SELECT MAX(norm_useful) as max_use,MAX(norm_funny) as max_fun,
  	AVG(norm_funny),AVG(norm_useful),MIN(norm_funny),MIN(norm_useful)
  	from (SELECT fans,useful/fans as norm_useful,
        	funny/fans as norm_funny, useful,funny
        	from user)

  	--PART-2
  	select uf_corr,count(uf_corr)
  	from (select CASE
  	WHEN (fans < 125)  AND  (useful > 1308 OR funny > 1178) THEN 'LOW'
  	WHEN (fans < 125)  AND  ((useful > 436 AND useful < 1308) OR (funny > 393 AND funny > 1178)) THEN 'MEDIUM'
  	WHEN (fans < 125) AND (useful < 436 OR funny < 393) THEN 'STRONG'
  	WHEN (fans > 125 AND fans < 375)  AND  (useful > 1308 OR funny > 1178) THEN 'MEDIUM'
  	WHEN (fans > 125 AND fans < 375)  AND  ((useful > 436 AND useful < 1308) OR (funny > 393 AND funny > 436)) THEN 'STRONG'
  	WHEN (fans > 125 AND fans < 375) AND (useful < 436 OR funny < 393) THEN 'MEDIUM'
  	WHEN (fans > 375)  AND  (useful > 1308 OR funny > 1178) THEN 'STRONG'
  	WHEN (fans > 375)  AND  ((useful > 436 AND useful < 1308) OR (funny > 393 AND funny > 1178)) THEN 'MEDIUM'
  	WHEN (fans > 375) AND (useful < 436 OR funny < 393) THEN 'LOW'
  	END as uf_corr
  	from user)
  	group by uf_corr


  +---------+----------------+
  | uf_corr | count(uf_corr) |
  +---------+----------------+
  | LOW     |             32 |
  | MEDIUM  |             47 |
  | STRONG  |           9921 |
  +---------+----------------+


Useful and funny reviews do strongly correlate to number of fans.


Part 2: Inferences and Analysis

1. Pick one city and category of your choice and group the businesses in that city or category by their overall star rating. Compare the businesses with 2-3 stars to the businesses with 4-5 stars and answer the following questions. Include your code.

i. Do the two groups you chose to analyze have a different distribution of hours?

Yes, the two groups have different hours of operation.

ii. Do the two groups you chose to analyze have a different number of reviews?

Yes, the two groups have different review counts

iii. Are you able to infer anything from the location data provided between these two groups? Explain.

From the location data provided we see that these businesses are located in different zip codes.
Based on that if a restaurant is located in a specific area code it has higher ratings compared to another area code.

	SQL code used for analysis:

  		SELECT B.name,
  			   B.review_count,
  			   H.hours,
  			   postal_code,
  			   CASE
  				  WHEN hours LIKE "%monday%" THEN 1
  				  WHEN hours LIKE "%tuesday%" THEN 2
  				  WHEN hours LIKE "%wednesday%" THEN 3
  				  WHEN hours LIKE "%thursday%" THEN 4
  				  WHEN hours LIKE "%friday%" THEN 5
  				  WHEN hours LIKE "%saturday%" THEN 6
  				      WHEN hours LIKE "%sunday%" THEN 7
  			   END AS ord,
  			   CASE
  				  WHEN B.stars BETWEEN 2 AND 3 THEN '2-3 stars'
  				  WHEN B.stars BETWEEN 4 AND 5 THEN '4-5 stars'
  			   END AS star_rating
  		FROM business B INNER JOIN hours H
  		ON B.id = H.business_id
  		INNER JOIN category C
  		ON C.business_id = B.id
  		WHERE (B.city == 'Las Vegas'
  		AND
  		C.category LIKE 'Restaurants')
  		AND
  		(B.stars BETWEEN 2 AND 3
  		OR
  		B.stars BETWEEN 4 AND 5)
  		GROUP BY stars,ord
  		ORDER BY ord,star_rating ASC



2.	Group business based on the ones that are open and the ones that are closed. What
	differences can you find between the ones that are still open and the ones that are
	closed? List at least two differences and the SQL code you used to arrive at your
	answer.

	i. 	Difference 1:

		The businesses that are open tend to have more reviews than ones that
		are closed on average.

			Open:   AVG(review_count) = 31.757
			Closed: AVG(review_count0 = 23.198


	ii.	Difference 2:

		The average star rating is higher for businesses that are open than
		businesses that are closed.

			Open:   AVG(stars) = 3.679
			Closed: AVG(stars) = 3.520


	SQL code used for analysis:

		SELECT COUNT(DISTINCT(id)),
			   AVG(review_count),
			   SUM(review_count),
			   AVG(stars),
			   is_open
		FROM business
		GROUP BY is_open



    3. For this last part of your analysis, you are going to choose the type of analysis you want to conduct on the Yelp dataset and are going to prepare the data for analysis.

    Ideas for analysis include: Parsing out keywords and business attributes for analysis, clustering businesses to find commonalities or anomalies between them, predicting the overall star rating for a business, predicting the number of fans a user will have.

    i. Indicate the type of analysis you chose to do:

    Predicting the Star Rating of a business              

    ii. Write 1-2 brief paragraphs on the type of data you will need for your analysis and why you chose that data:

    The data required for predicting star rating for a business includes the City, Area where the business is located, any previous ratings available for the business, number of checkins by users in the previous month, any amineties that the business has to offer. Number of votes for the business bu users.

    iii. Output of your finished dataset:
    -----+-------------------+------------------+-------------------------+-------+--------------+--------------+
  | name                                      | city              | neighborhood     | address                 | stars | review_count | SUM(c.count) |
  +-------------------------------------------+-------------------+------------------+-------------------------+-------+--------------+--------------+
  | Cracker Barrel Old Country Store          | Sheffield Village |                  | 5205 Detroit Rd         |   3.5 |           27 |          161 |
  | Courtyard Cleveland Willoughby            | Willoughby        |                  | 35103 Maplegrove Rd     |   3.0 |           11 |           95 |
  | LongHorn Steakhouse                       | Mentor            |                  | 9557 Mentor Ave         |   3.5 |           21 |           95 |
  | John Christ Winery                        | Avon Lake         |                  | 32421 Walker Rd         |   3.0 |           27 |           64 |
  | Chagrin Valley Little Theatre             | Chagrin Falls     |                  | 40 River St             |   4.5 |            4 |           54 |
  | Rite Aid                                  | Cleveland         | Detroit-Shoreway | 6512 Franklin Blvd      |   2.0 |            6 |           46 |
  | Highland Square Tavern                    | Cleveland         | Edgewater        | 11634 Madison Ave       |   2.5 |            3 |           38 |
  | Panda Chinese Restaurant                  | Willoughby        |                  | 35535 Euclid Ave        |   3.5 |           16 |           31 |
  | Atlas Cinemas                             | Mentor            |                  | 9555 Diamond Centre Dr  |   3.0 |            8 |           29 |
  | Pizza Cutter                              | Avon Lake         |                  | 33501 Lake Rd, Ste K    |   4.0 |           11 |           28 |
  | Spudnut Shop Donuts                       | Mentor            |                  | 6930 Center St          |   4.5 |           21 |           26 |
  | CVS Pharmacy                              | Willoughby        |                  | 6005 Som Center Rd      |   3.0 |            6 |           25 |
  | Chapman's Food Mart                       | Lorain            |                  | 2875 G St               |   4.0 |            5 |           24 |
  | Davitino's Restaurant                     | Mentor            |                  | 8820 Mentor Ave Town Sq |   3.0 |           19 |           21 |
  | Burger King                               | Mentor            |                  | 5725 Heisley Rd         |   1.0 |            4 |           15 |
  | Stella's Pizza & Italian Restaurant       | Avon Lake         |                  | 445 Avon Belden Rd      |   2.0 |           16 |           15 |
  | Red Wagon Farm                            | Columbia Station  |                  | 16081 E River Rd        |   3.5 |           13 |           14 |
  | Manakiki Golf Course-Cleveland Metroparks | Willoughby        |                  | 35501 Eddy Rd           |   3.5 |            5 |           13 |
  | Dairy Queen                               | Chesterland       |                  | 8423 Mayfield Rd        |   4.5 |            3 |           11 |
  | Berkshire Hills Golf Course               | Chesterland       |                  | 9760 Mayfield Rd        |   3.0 |            7 |           10 |
  | Brownie's Market                          | Sheffield Lake    |                  | 5260 E Lake Rd          |   4.0 |            4 |            9 |
  | Days Inn Willoughby/Cleveland             | Willoughby        |                  | 4145 State Route 306    |   1.0 |           12 |            7 |
  | The Inn of Chagrin Falls                  | Chagrin Falls     |                  | 87 West St              |   4.0 |            3 |            6 |
  | Galleria Gowns                            | Highland Heights  |                  | 783B Alpha Plz          |   4.5 |           16 |            5 |
  | Wah Sun                                   | Chesterland       |                  | 12550 Chillicothe Rd    |   3.5 |            9 |            4 |
  +-------------------------------------------+-------------------+------------------+-------------------------+-------+--------------+--------------+
  (Output limit exceeded, 25 of 10000 total rows shown)



    iv. Provide the SQL code you used to create your final dataset:

    SELECT b.name ,b.city,b.neighborhood,b.address,b.stars,b.review_count,SUM(c.count)

    FROM business b LEFT JOIN checkin c

    ON b.id=c.business_id

    LEFT JOIN attribute a

    ON b.id = a.business_id

    GROUP BY b.name ,b.city,b.neighborhood,b.address,b.stars

    ORDER BY SUM(c.count) DESC
