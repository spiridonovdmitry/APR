CREATE USER search WITH PASSWORD '7778';
CREATE DATABASE searcheng WITH OWNER = 'postgres' ENCODING = 'UTF8';

CREATE TABLE "posts" (
  "id" serial PRIMARY KEY,
  "rubrics" VARCHAR(32) ARRAY[3] NOT NULL,
  "text" TEXT DEFAULT '',
  "created_date" TIMESTAMP NOT NULL);