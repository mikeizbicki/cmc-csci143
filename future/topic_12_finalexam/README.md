# Final Exam

Oral, 1 on 1 exam in my office at the scheduled time.
1. Everyone can signup at: <https://docs.google.com/spreadsheets/d/1axeCxjA8i8koFtmPWlzSbos108D8XAtXbGEkiU63E30/edit#gid=0>
1. Goal is to prepare you for interview situations
1. Combination of a SQL interview and System Design interview

The database schema:
1. For graduating students:
    1. I will provide you the schema at the start of the exam
    1. It will be based on the `twitter_normalized` database
    1. You can find examples in the previous final exams and the review pdfs
1. For non-graduating students:
    1. You will provide the schema based on your final project
    1. This will be the only difference in the exam

I will ask three SQL questions:
1. One without a JOIN
1. One with a JOIN (possibly more than 1 table)
1. One with a full text search (possibly with a JOIN)
1. I'm planning for ~10 minutes/question = 30 minutes in total

Grading:
1. Exam is out of 64 points
1. You get 4 points for free :)
1. Each question will be worth 20 points:
    1. 4 points for providing reasonable SQL
    1. 8 points for explaining how to make the SQL query fast
        1. You will provide any needed indexes
            1. Correct syntax is much less important than the right idea
        1. Then describe what you expect the EXPLAIN query plan would look like
            1. why it's fast
            1. why it can't be made faster (if applicable)
        1. I might ask some minor followup questions here to help you get more points
    1. 8 points for detailed followup questions:   
        1. You should be prepared to draw any of the figures from the required reading
        1. **Anything in the reading is fair game for the exam**
        1. Examples of things you should know that we did not cover in class in detail:
            1. CLUSTER command
            1. ANALYZE command
            1. partial indexes with WHERE clause
            1. using ASC/DESC in multicolumn indexes
            1. covering indexes with and without the INCLUDE clause
            1. xid wraparound problem
1. I will tell you your grade immediately after the final is over

    **Note:**
    I am extending the due date for the `twitter-postgres-indexes` assignment for all students until Tuesday, April 30.

    1. I recommend graduating students still finish before Sunday April 21 so that:
        1. I can give you your final grade during the oral exam.
        1. You can be done with the course early.

    1. The extension will give you all a bit more flexibility, however, in scheduling your time for your last few days as a student.
