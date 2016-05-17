import logging
import os
import json
from errno import errorcode

import mysql.connector


class DataBaseHandler(object):

    def __init__(self):
        self.db = None

        with open(os.path.join(os.getcwd(), "config.json")) as config_file:
            self.config = json.load(config_file)

        try:
            # Instantiate connection object and connect to MySQL database
            self.db = mysql.connector.connect(host=self.config["host"], user=self.config["user"],
                                              password=self.config["password"], database=self.config["db"])

            # Instantiate cursor object
            self.cursor = self.db.cursor(dictionary=True)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.error("Wrong user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
            else:
                logging.error(err)

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.db:
            self.db.close()

    def view(self):
        if self.db is not None:
            try:
                blogs_list = []
                self.cursor.execute("select id, title from blogs")
                for blog in self.cursor:
                    blogs_list.append(blog)
                return blogs_list
            except:
                logging.Error("Error while selecting all blogs")

    def create(self, blog):
        try:
            add_blog = "insert into blogs (title, text, publisher_name, created_date, updated_date) " \
                  "values (%s, %s, %s, NOW(), NOW())"

            blog_data = (blog["title"], blog["text"], blog["publisher_name"])
            # insert into blogs
            self.cursor.execute(add_blog, blog_data)
            self.db.commit()
        except:
            logging.error("Error while inserting blog")

        return True

    def edit(self, id, blog):
        try:
            update_blog = "update blogs set title = '%s', text = '%s', publisher_name = '%s', " \
                          "updated_date = NOW() where id = %d" % (blog["title"], blog["text"], blog["publisher_name"], id)

            #update blogs
            self.cursor.execute(update_blog)
            self.db.commit()
        except:
            logging.error("Error while updating blog")
        return True

    def delete(self, id):
        try:
            delete_blog = "delete from blogs where id = %d" % id

            #update blogs
            self.cursor.execute(delete_blog)
            self.db.commit()
        except:
            logging.error("Error while updating blog")
        return True
