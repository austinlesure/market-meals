LOAD DATA LOCAL INFILE 'C:/Users/Marianne Goldin/Documents/GitHub/market-meals/mysql-db/importdata/farmer.tsv' 
INTO TABLE farmer 
LINES TERMINATED BY '\n'; 

LOAD DATA LOCAL INFILE 'C:/Users/Marianne Goldin/Documents/GitHub/market-meals/mysql-db/importdata/market.tsv' 
INTO TABLE market
LINES TERMINATED BY '\n'; 

LOAD DATA LOCAL INFILE 'C:/Users/Marianne Goldin/Documents/GitHub/market-meals/mysql-db/importdata/marketday.tsv' 
INTO TABLE marketday
LINES TERMINATED BY '\n'; 

LOAD DATA LOCAL INFILE 'C:/Users/Marianne Goldin/Documents/GitHub/market-meals/mysql-db/importdata/prodcat.tsv' 
INTO TABLE prodcat
LINES TERMINATED BY '\n'; 

LOAD DATA LOCAL INFILE 'C:/Users/Marianne Goldin/Documents/GitHub/market-meals/mysql-db/importdata/product.tsv' 
INTO TABLE product
LINES TERMINATED BY '\n'; 

LOAD DATA LOCAL INFILE 'C:/Users/Marianne Goldin/Documents/GitHub/market-meals/mysql-db/importdata/recipe.tsv' 
INTO TABLE recipe
LINES TERMINATED BY '\n'; 

LOAD DATA LOCAL INFILE 'C:/Users/Marianne Goldin/Documents/GitHub/market-meals/mysql-db/importdata/recipeproduct.tsv' 
INTO TABLE recipeproduct
LINES TERMINATED BY '\n'; 