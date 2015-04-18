-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2015-04-06 01:03:35.811




-- tables
-- Table record
DROP TABLE IF EXISTS record;

CREATE TABLE IF NOT EXISTS record (
	id int auto_increment,
    record int    NOT NULL ,
    totalCount int    NOT NULL ,
    times int    NOT NULL ,
    user varchar(255)    NOT NULL ,
    CONSTRAINT id_pk PRIMARY KEY (id)
);

-- Table word
DROP TABLE IF EXISTS word;

CREATE TABLE IF NOT EXISTS word (
	id int auto_increment,
    w varchar(255)    NOT NULL ,
    t varchar(255)    NOT NULL ,
    CONSTRAINT id_pk PRIMARY KEY (id)
);






-- End of file.

