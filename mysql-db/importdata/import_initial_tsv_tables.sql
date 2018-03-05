LOAD DATA LOCAL INFILE 'C:/Users/Marianne Goldin/Documents/GitHub/market-meals/mysql-db/importdata/farmer.tsv' INTO TABLE farmer FIELDS TERMINATED BY '\t';
LOAD DATA LOCAL INFILE 'C:/Users/Marianne Goldin/Documents/GitHub/market-meals/mysql-db/importdata/market.tsv' INTO TABLE market FIELDS TERMINATED BY '\t';
LOAD DATA LOCAL INFILE 'C:/Users/Marianne Goldin/Documents/GitHub/market-meals/mysql-db/importdata/marketday.tsv' INTO TABLE marketday FIELDS TERMINATED BY '\t';
LOAD DATA LOCAL INFILE 'C:/Users/Marianne Goldin/Documents/GitHub/market-meals/mysql-db/importdata/prodcat.tsv' INTO TABLE prodcat FIELDS TERMINATED BY '\t';
LOAD DATA LOCAL INFILE 'C:/Users/Marianne Goldin/Documents/GitHub/market-meals/mysql-db/importdata/product.tsv' INTO TABLE product FIELDS TERMINATED BY '\t';
LOAD DATA LOCAL INFILE 'C:/Users/Marianne Goldin/Documents/GitHub/market-meals/mysql-db/importdata/recipe.tsv' INTO TABLE recipe FIELDS TERMINATED BY '\t';
