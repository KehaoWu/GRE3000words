-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2015-04-06 01:03:35.811




-- tables
-- Table record
CREATE TABLE record (
    record int    NOT NULL ,
    totalCount int    NOT NULL ,
    CONSTRAINT record_pk PRIMARY KEY (record)
);

-- Table word
CREATE TABLE word (
    w varchar(255)    NOT NULL ,
    t varchar(255)    NOT NULL ,
    CONSTRAINT word_pk PRIMARY KEY (w)
);






-- End of file.

