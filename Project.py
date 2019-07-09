#!/usr/bin/env python3

import psycopg2

DBNAME = 'news'

question1 = "What are the most popular three articles of all time?\n"

query1 = """
        SELECT title, count(*) AS numb_of_views\
        FROM articles, log\
        WHERE log.path = '/article/' || articles.slug\
        GROUP BY articles.title\
        ORDER BY numb_of_views DESC LIMIT 3;
        """

question2 = "Who are the most popular authors from all time?\n"

query2 = """
        SELECT authors.name, count(*) AS numb_of_views\
        FROM articles\
        JOIN authors\
        ON articles.author = authors.id\
        JOIN log\
        ON log.path = '/article/' || articles.slug\
        GROUP BY authors.name\
        ORDER BY numb_of_views DESC;
        """

question3 = "On which days did more than 1% of requests lead to errors?\n"

query3 = """
        SELECT * FROM\
        (SELECT var1.date, round(100.0 * error/logcounter, 2) AS percentage\
        FROM(SELECT time::date AS DATE,\
        count(*) as logcounter FROM log GROUP BY DATE) AS var1\
        JOIN (SELECT to_char(time, 'MON DD, YYYY') AS DATE,\
        count(*) as error FROM log\
        WHERE status != '200 OK' GROUP BY DATE) AS var2\
        ON var1.date = var2.date) AS var3 WHERE percentage > 1.0;
        """


def connect(query):
    """ Connect to database """
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def popular_articles(query):
	""" Query through the database """
    result = connect(query)
    print(question1)
    for i in result:
        print("* " + str(i[0]) + " --- " + str(i[1]) + " views.")
    print("")


def popular_authors(query):
    """ Query through the database """
    result = connect(query)
    print(question2)
    for i in result:
        print("* " + str(i[0]) + " --- " + str(i[1]) + " views.")
    print("")


def more_errors_day(query):
    """ Query through the database """
    result = connect(query)
    print(question3)
    for i in result:
        print(str(i[0]) + " --- " + str(i[1]) + "%" + " errors.")
    print("")

if __name__ == '__main__':
    popular_articles(query1)
    popular_authors(query2)
    more_errors_day(query3)
