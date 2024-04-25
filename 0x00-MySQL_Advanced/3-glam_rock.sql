-- Old school band
-- Lists all bands with Glam rock as their style,
-- ranked by their longevity
-- Column names must be: band_name & lifespan

SELECT 
    band_name, 
    IF(split IS NULL OR split = 0, 2022 - formed, split - formed) AS lifespan
FROM 
    metal_bands
WHERE 
    style = 'Glam rock'
ORDER BY 
    lifespan DESC;
